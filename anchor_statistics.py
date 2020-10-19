import logging
import multiprocessing
import os
import random
import time
from argparse import ArgumentParser
from bz2 import BZ2File
from multiprocessing.context import Process
from threading import Thread
from xml.sax import parse

from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch.helpers import parallel_bulk

from reader import WikiReader

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
    buffer = {}
    while not (shutdown and article_queue.empty()):
        logging.debug("processujem artikel")
        try:
            page_title, source = article_queue.get()
        except EOFError:
            continue
        logging.debug("mam titel: " + page_title)
        for anchor in get_anchors(source):
            anchor = anchor.split("|")
            link_to = anchor[0]
            anchor_text = anchor[1] if len(anchor) == 2 else link_to
            if link_to is not None and len(link_to) > 0:
                # fq.put()
                line = {"page_from": page_title, "anchor_text": anchor_text}
                page_to = link_to
                if page_to not in buffer.keys():
                    buffer[page_to] = []
                buffer[page_to].append(line)
                if len(buffer[page_to]) == 100:
                    output_queue.put(create_action(page_to, buffer.pop(page_to)))
                # if len(buffer) == 1000:

                if len(buffer) > 100000:
                    for key in random.sample(list(buffer.keys()), k=2000):
                        output_queue.put(create_action(key, buffer.pop(key)))
    for k in buffer.keys():
        output_queue.put(create_action(k, buffer[k]))


def create_action(page_to, line):
    return {
        "_index": INDEX,
        "_id": page_to,
        "_op_type": "update",
        "retry_on_conflict": 6,
        "_source": {
            "script": {
                "source": "ctx._source.anchors.addAll(params.anchor)",
                "lang": "painless",
                "params": {
                    "anchor": line
                }
            },
            "upsert": {
                "page_to": page_to,
                "anchors": line,
            }
        }
    }


def get_actions():
    while not (shutdown and output_queue.empty()):
        try:
            yield output_queue.get()
        except EOFError:
            continue


def write_out():
    esx = Elasticsearch()
    # bulk = []
    while not (shutdown and output_queue.empty()):
        for success, info in parallel_bulk(client=esx, actions=get_actions(), chunk_size=250, request_timeout=60):
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
            article_queue.qsize(),
            output_queue.qsize(),
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
    output_queue = manager.Queue(maxsize=2000)
    article_queue = manager.Queue(maxsize=2000)

    reader = WikiReader(lambda ns: ns == 0, article_queue.put)

    status = Thread(target=display, args=())
    status.start()

    processes = []
    for _ in range(8):
        process = Process(target=process_article)
        process.start()
        processes.append(process)
    # for _ in range(14):
    #     process = Process(target=write_out)
    #     process.start()

    write_thread = Thread(target=write_out)
    write_thread.start()
    parse(wiki, reader)
    shutdown = True
    for process in processes:
        process.join()
    write_thread.join()
    status.join()
