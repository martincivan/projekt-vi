from collections import Counter

from PyInquirer import prompt

from elasticsearch import Elasticsearch

INDEX = "vi_index_to2"

print("Wanchor!!!")

es = Elasticsearch()
es.index = INDEX
print(f'Index size: {es.count(body={"query": {"match_all": {}}})["count"]}')


def print_meta(es_result):
    print(f'Search took: {es_result["took"]}ms')
    print(f'Results count: {es_result["hits"]["total"]["value"]}')
    print("##########")
    return int(es_result["hits"]["total"]["value"])


def print_hits(hits):
    for hit in hits:
        print(f'{hit["_source"]["page_to"]} [{hit["_source"]["page_to_entity"]}]')
        c = Counter(f'    {a["anchor_text"]}: ({a["page_from"]})' for a in hit["_source"]["anchors"])
        for a in c:
            print(f'{a} [{c[a]}]')


def fulltext_search(off, size, q):
    return es.search({"query": {
        "query_string": {
            "query": q,
            "default_operator": "AND"
        }
    }, "size": size, "from": off})


def execute(get_input, request):
    offset = 0
    limit = 5
    query = get_input()
    es_result = request(off=offset, size=limit, q=query)
    total = print_meta(es_result=es_result)
    print_hits(hits=es_result["hits"]["hits"])
    offset = limit
    while offset < total and prompt([{"type": "list", "name": "type", "message": "Show more?",
                                      "choices": [{"name": "Yes", "value": True}, {"name": "No", "value": False}]}])[
        "type"]:
        es_result = request(off=offset, size=limit, q=query)
        print_hits(hits=es_result["hits"]["hits"])
        offset += limit


def select_entity():
    es_result = es.search({
        "size": 0,
        "aggs": {
            "entities": {
                "terms": {
                    "field": "page_to_entity",
                    "size": 500
                }
            }
        }
    })
    entities = [{"name": f'{i["key"]} [{i["doc_count"]}]', "value": i["key"]} for i in
                es_result["aggregations"]["entities"]["buckets"]]

    es_result = es.count({
        "query": {
            "bool": {
                "must_not": {
                    "exists": {
                        "field": "page_to_entity"
                    }
                }
            }
        }
    })

    entities.append({"name": f'none [{es_result["count"]}]', "value": "none"})
    return (
        prompt([{"type": "list", "name": "entity", "message": "Select entity filter", "choices": entities}])["entity"],
        input("Query: "))


def entity_search(off, size, q):
    if q[0] == "none":
        if q[1]:
            return es.search({"query": {
                "bool": {
                    "must": {
                        "query_string": {
                            "query": q[1],
                            "default_operator": "AND"
                        }
                    },
                    "must_not": {
                        "exists": {
                            "field": "page_to_entity"
                        }
                    }
                }
                ,
            }, "size": size, "from": off})
        else:
            return es.search({
                "query": {
                    "bool": {
                        "must_not":{
                            "exists": {
                                "field": "page_to_entity"
                            }
                        }
                    }
            }, "size": size, "from": off}, index=INDEX)
    else:
        if q[1]:
            return es.search({"query": {
                "bool": {
                    "must": {
                        "query_string": {
                            "query": q[1],
                            "default_operator": "AND"
                        }
                    },
                    "filter": {
                        "match": {
                            "page_to_entity": q[0]
                        }
                    }
                }
                ,
            }, "size": size, "from": off})
        else:
            return es.search({"query": {
                "match": {
                    "page_to_entity": q[0]
                }
            }, "size": size, "from": off})


while True:
    actions = [{"name": "General fulltext search", "value": lambda: execute(lambda: input("Query: "), fulltext_search)},
               {"name": "By entity type", "value": lambda: execute(select_entity, entity_search)},
               {"name": "Quit", "value": quit}]
    answers = prompt([{"type": "list", "name": "type", "message": "Select search type", "choices": actions}])
    answers["type"]()
