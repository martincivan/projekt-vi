from random import sample
from csv import DictReader


class Cache(dict):

    def __init__(self, max_size, delete_callback=lambda x: x) -> None:
        super().__init__()
        self.delete_callback = delete_callback
        self.max_size = max_size

    def __setitem__(self, k, v) -> None:
        if len(self.keys()) > self.max_size:
            for key in sample(list(self.keys()), k=10):
                self.delete_callback(self.pop(key))
        super().__setitem__(k, v)


class NLP:

    def __init__(self, *providers) -> None:
        super().__init__()
        self.providers = providers
        self.cache = Cache(100000)

    def __getitem__(self, item):
        item = item.lower()
        try:
            return self.cache[item]
        except KeyError:
            for provider in self.providers:
                value = provider[item]
                if value is not None:
                    self.cache[item] = value
                    return value
            items = item.split()
            for provider in self.providers:
                value = provider[items]
                if value is not None:
                    self.cache[item] = value
                    return value
            self.cache[item] = None
        return None


class TownProvider:

    def __init__(self, file) -> None:
        super().__init__()
        self.values = set()
        with open(file=file, encoding="windows-1250") as csvfile:
            reader = DictReader(csvfile, delimiter=";")
            for row in reader:
                self.values.add(row["NM5"].lower() + " " + row["NM4"].lower())
        self.label = "TOWN"

    def __getitem__(self, item):
        if isinstance(item, str):
            return self.label if self.stringcheck(item) else None
        if isinstance(item, list):
            return self.label if self.listcheck(item) else None
        return None

    def stringcheck(self, value):
        return value in self.values

    def listcheck(self, values):
        # for value in self.values:
        #     if any(v in value for v in values):
        #         return True
        return False


class GeoProvider:

    def __init__(self, file) -> None:
        super().__init__()
        self.values = {}
        with open(file=file, encoding="windows-1250") as csvfile:
            reader = DictReader(csvfile, delimiter=";")
            for row in reader:
                self.values[row["GEONAME"].lower()] = row["CAT"].lower()
        self.label = "TOWN"

    def __getitem__(self, item):
        if isinstance(item, str):
            return self.stringcheck(item)
        if isinstance(item, list):
            return self.listcheck(item)
        return None

    def stringcheck(self, value: str):
        try:
            return self.values[value]
        except KeyError:
            return None

    def listcheck(self, values: list):
        # for value in values:
        #     if value in self.values.keys():
        #         return self.values[value]
        return None


class NameProvider:
    def __init__(self, file) -> None:
        super().__init__()
        with open(file=file) as f:
            self.values = set(map(lambda s: s.strip('\n').lower(), f.readlines()))

    def __getitem__(self, item):
        if isinstance(item, str):
            return None
        if isinstance(item, list):
            return self.listcheck(item)
        return None

    def listcheck(self, values: list):
        if 1 < len(values) <= 4 and values[0] in self.values:
            return "PERSON"
        return None
