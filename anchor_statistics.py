import logging
import multiprocessing
import os
import time
import re
from argparse import ArgumentParser
from bz2 import BZ2File
from multiprocessing.context import Process
from queue import Empty
from threading import Thread
from xml.sax import parse

from elasticsearch import Elasticsearch, NotFoundError, ElasticsearchException
from elasticsearch.helpers import parallel_bulk

from nlp import NLP, TownProvider, GeoProvider, Cache, NameProvider
from reader import WikiReader

INDEX = "vi_index_to2"


# TODO: offline statistiky vyskytov entit


logging.getLogger().setLevel(logging.WARN)

mapping = {
    "mappings": {
        "properties": {
            "page_to": {
                "type": "keyword"
            },
            "page_to_entity": {
                "type": "keyword"
            },
            "anchors": {
                "properties": {
                    "anchor_text": {
                        "type": "text",
                        "term_vector": "with_positions"
                    },
                    "page_from": {
                        "type": "keyword"
                    },
                    # "entities": {
                    #     "properties": {
                    #         "text": {
                    #             "type": "keyword"
                    #         },
                    #         "start": {
                    #             "type": "short"
                    #         },
                    #         "end": {
                    #             "type": "short"
                    #         },
                    #         "label": {
                    #             "type": "keyword"
                    #         }
                    #     }
                    # }
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
    for match in re.finditer(pattern="\[\[(.*?)\]\]", string=source):
        yield match.group(1)


class ArticleProcessor:

    def __init__(self, provider, output) -> None:
        super().__init__()
        self.output = output
        self.provider = provider

    def __call__(self):
        for page_title, source in self.provider:
            for anchor in get_anchors(source=source):
                anchor = anchor.split("|")
                link_to = anchor[0]
                anchor_text = anchor[1] if len(anchor) == 2 else link_to
                self.output({
                    "page_from": page_title,
                    "page_to": link_to,
                    "anchor_text": anchor_text
                })


class ESWriter:

    def __init__(self, iterator) -> None:
        super().__init__()
        self.iterator = iterator
        self.esx = Elasticsearch()

    def __call__(self):
        try:
            for success, info in parallel_bulk(client=self.esx, actions=self.preprocess(read_from_queue(output_queue)),
                                               chunk_size=250, request_timeout=60):
                if not success:
                    print("Insert failed: ", info)
        except ElasticsearchException:
            print("NEVYDALO :(")
            self.__call__()

    def preprocess(self, iterator):
        for i in iterator:
            yield self.create_action(**i)

    @staticmethod
    def create_action(page_to, page_to_entity, anchors):
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
                        "anchor": anchors
                    }
                },
                "upsert": {
                    "page_to": page_to,
                    "anchors": anchors,
                    "page_to_entity": page_to_entity
                }
            }
        }


class Aggregator:

    def __init__(self, provider, output) -> None:
        super().__init__()
        self.provider = provider
        self.output = output
        self.nlp = NLP(NameProvider("/home/martin/Dokumenty/skola/vi/gn_csv/mena.csv"),
                       TownProvider("/home/martin/Dokumenty/skola/vi/gn_csv/GNKU.csv"),
                       GeoProvider("/home/martin/Dokumenty/skola/vi/gn_csv/geograficky_nazov.csv"))
        self.cache = Cache(100000, output)

    def __call__(self):
        for i in self.provider:
            if i["page_to"] not in self.cache:
                self.cache[i["page_to"]] = {
                    "page_to": i["page_to"],
                    "page_to_entity": self.nlp[i["page_to"]],
                    "anchors": []
                }
            self.cache[i["page_to"]]["anchors"].append({"page_from": i["page_from"], "anchor_text": i["anchor_text"]})
        for i in self.cache:
            self.output(i)


def display():
    while not shutdown:
        logging.warning("Queue sizes: articles={0} anchors={1} output={2}. Read: {3}".format(
            article_queue.qsize(),
            anchor_queue.qsize(),
            output_queue.qsize(),
            reader.status_count))
        time.sleep(1)


def read_from_queue(queue):
    while not shutdown or not queue.empty():
        try:
            yield queue.get(timeout=1)
        except EOFError:
            continue
        except Empty:
            continue


def process_article():
    ArticleProcessor(read_from_queue(article_queue), anchor_queue.put)()


if __name__ == "__main__":
    shutdown = False
    parser = ArgumentParser()
    parser.add_argument("wiki", help="wiki dump file .xml.bz2")
    # parser.add_argument("out", help="final file .txt")
    args = parser.parse_args()
    logging.debug("subor: " + args.wiki)
    wiki = BZ2File(args.wiki)
    logging.debug("nacitane")
    # out_file = open(os.path.join(args.out), "w+")

    manager = multiprocessing.Manager()
    output_queue = manager.Queue(maxsize=2000)
    article_queue = manager.Queue(maxsize=2000)
    anchor_queue = manager.Queue(maxsize=2000)

    reader = WikiReader(lambda ns: ns == 0, article_queue.put)

    status = Thread(target=display, args=())
    status.start()

    processes = []
    for _ in range(2):
        process = Process(target=process_article)
        process.start()
        processes.append(process)
    # for _ in range(14):
    #     process = Process(target=write_out)
    #     process.start()
    aggregators = []
    for _ in range(13):
        aggregator = Aggregator(provider=read_from_queue(anchor_queue), output=output_queue.put)
        agg_thread = Process(target=aggregator)
        agg_thread.start()
        aggregators.append(agg_thread)
    writer = ESWriter(output_queue)
    write_thread = Thread(target=writer)
    write_thread.start()
    parse(wiki, reader)
    shutdown = True
    for process in processes:
        process.join()
    for process in aggregators:
        process.join()
    write_thread.join()
    status.join()
