from xml.sax.handler import ContentHandler
import logging

logger = logging.getLogger(__name__)


class WikiReader(ContentHandler):
    def __init__(self, ns_filter, callback):
        super().__init__()

        self.filter = ns_filter

        self.stack = []
        self.text = None
        self.title = None
        self.namespace = None

        self.status_count = 0
        self.callback = callback

    def startElement(self, tag_name, attributes):
        if tag_name == "ns":
            self.namespace = None

        elif tag_name == "page":
            self.text = None
            self.title = None

        elif tag_name == "title":
            self.title = ""

        elif tag_name == "text":
            self.text = ""
        else:
            return

        self.stack.append(tag_name)

    def endElement(self, tag_name):
        if tag_name == self.stack[-1]:
            del self.stack[-1]

        if self.filter(self.namespace):
            if tag_name == "page" and self.text is not None and self.title is not None:
                self.status_count += 1
                self.callback((self.title, self.text))

    def characters(self, content):
        if len(self.stack) == 0:
            return

        if self.stack[-1] == "text":
            self.text += content

        if self.stack[-1] == "title":
            self.title += content

        if self.stack[-1] == "ns":
            self.ns = int(content)
