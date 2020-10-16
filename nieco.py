import json
import logging
import multiprocessing
import os
import time
from argparse import ArgumentParser
from bz2 import BZ2File
from multiprocessing.context import Process
from threading import Thread
from xml.sax import parse
from reader import WikiReader
from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch.helpers import parallel_bulk

INDEX = "vi_index_to"

logging.getLogger().setLevel(logging.WARN)

mapping = {
    "mappings": {
        "properties": {
            "page_to": {
                "type": "keyword"
            },
            "anchors": {
                "properties": {
                    "anchor_text": {
                        "type": "text"
                    },
                    "page_from": {
                        "type": "keyword"
                    }
                }
            }
        }
    }
}

es = Elasticsearch()
try:
    es.indices.delete(index=INDEX)
except NotFoundError:
    pass
es.indices.create(index=INDEX, body=mapping)


def get_anchors(source: str):
    begins = []
    results = []

    act_begin = False
    act_end = False
    for num, char in enumerate(source):
        if char == "[":
            if act_begin:
                begins.append(num + 1)
            act_begin = not act_begin
        else:
            act_begin = False
        if char == "]":
            if act_end:
                try:
                    results.append((begins.pop(), num - 1))
                except IndexError:
                    print(source)
                    print(begins)
            act_end = not act_end
        else:
            act_end = False
    for begin, end in results:
        yield source[begin:end]


def process_article():
    while not (shutdown and aq.empty()):
        logging.debug("processujem artikel")
        page_title, source = aq.get()
        logging.debug("mam titel: " + page_title)
        for anchor in get_anchors(source):
            anchor = anchor.split("|")
            link_to = anchor[0]
            anchor_text = anchor[1] if len(anchor) == 2 else link_to
            if link_to is not None:
                fq.put({"page_from": page_title, "anchor_text": anchor_text, "page_to": link_to})


def get_actions():
    while not (shutdown and fq.empty()):
        line = fq.get()
        page_to = line.pop("page_to")
        yield {
            "_index": INDEX,
            "_id": page_to,
            "_op_type": "update",
            "_source": {
                "script": {
                    "source": "ctx._source.anchors.add(params.anchor)",
                    "lang": "painless",
                    "params": {
                        "anchor": line
                    }
                },
                "upsert": {
                    "page_to": page_to,
                    "anchors": [line],
                }
            }
        }


def write_out():
    esx = Elasticsearch()
    # bulk = []
    while not (shutdown and fq.empty()):
        for success, info in parallel_bulk(client=esx, actions=get_actions(), thread_count=8):
            if not success:
                print("Insert failed: ", info)
    #     line = fq.get()
    #     esx.update(index=INDEX, id=line["page_to"], params={"retry_on_conflict": 6}, body={
    #         "script": {
    #             "source": "ctx._source.anchors.add(params.anchor)",
    #             "lang": "painless",
    #             "params": {
    #                 "anchor": line
    #             }
    #         },
    #         "upsert": {
    #             "page_to": line["page_to"],
    #             "anchors": [line],
    #         }
    #     })


def display():
    while not shutdown:
        logging.warning("Queue sizes: aq={0} fq={1}. Read: {2}".format(
            aq.qsize(),
            fq.qsize(),
            reader.status_count))
        time.sleep(1)


if __name__ == "__main__":
    shutdown = False
    parser = ArgumentParser()
    parser.add_argument("wiki", help="wiki dump file .xml.bz2")
    parser.add_argument("out", help="final file .txt")
    args = parser.parse_args()
    logging.debug("subor: " + args.wiki)
    wiki = BZ2File(args.wiki)
    logging.debug("nacitane")
    out_file = open(os.path.join(args.out), "w+")

    manager = multiprocessing.Manager()
    fq = manager.Queue(maxsize=2000)
    aq = manager.Queue(maxsize=2000)

    reader = WikiReader(lambda ns: ns == 0, aq.put)

    status = Thread(target=display, args=())
    status.start()

    processes = []
    for _ in range(2):
        process = Process(target=process_article)
        process.start()

    # for _ in range(14):
    #     process = Process(target=write_out)
    #     process.start()

    write_thread = Thread(target=write_out)
    write_thread.start()
    parse(wiki, reader)
    shutdown = True
