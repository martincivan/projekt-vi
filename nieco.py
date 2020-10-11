import json
import multiprocessing
import os
import time
from argparse import ArgumentParser
from bz2 import BZ2File
from multiprocessing.context import Process
from threading import Thread
from xml.sax import parse

from reader import WikiReader


def process_article():
    while not (shutdown and aq.empty()):

        page_title,source = aq.get()
        text = clean(source)

        doc = nlp(text)

        sents = []
        for s in doc.sents:
            if len(sents) > 0:
                # Fix some spacy sentence splitting errors by joining sentences if they don't end in a period
                if len(str(sents[-1]).strip()) and str(sents[-1]).strip()[-1] != ".":
                    sents[-1] += str(s)
                    continue
            sents.append(str(s))

        out_text = "\n".join(sents)
        fq.put(json.dumps({"page": page_title, "sentences":out_text}))

def write_out():
    while not (shutdown and fq.empty()):
        line = fq.get()
        out_file.write(line+"\n")


def display():
    while True:
        print("Queue sizes: aq={0} fq={1}. Read: {2}".format(
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

    manager = multiprocessing.Manager()
    fq = manager.Queue(maxsize=2000)
    aq = manager.Queue(maxsize=2000)

    wiki = BZ2File(args.wiki)
    out_file = open(os.path.join(args.out),"w+")

    reader = WikiReader(lambda ns: ns == 0, aq.put)

    status = Thread(target=display, args=())
    status.start()

    processes = []
    for _ in range(15):
        process = Process(target=process_article)
        process.start()

    write_thread = Thread(target=write_out)
    write_thread.start()

    parse(wiki, reader)
    shutdown = True