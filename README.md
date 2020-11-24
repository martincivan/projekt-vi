# Vyhľadávanie informácií - Wiki Anchor texty

## Zadanie
Anchor texty a štatistika k anchor textom. Document frequency, collection frequency (Python)

## Návod na použitie
Používať Python 3 - testované s 3.8
Nainštalované balíčky z `requirements.txt`
Na indexovanie je potrebné mať dostupný ElasticSearch 7.x na adrese `localhost:9200`

Naindexovanie a vytvorenie offline štatistík dát sa sputí skriptom `anchor_statistics.py` a 1. parameter je k wiki dumpu.

priklad: `python anchor_statistics.py /home/martin/fiit/vi/skwiki-latest-pages-articles.xml.bz2`

Dopyty sa vykonávajú skriptom `search.py`
Testy sa púšťajú skriptom `test.py`

## Popis dat
Na začiatok by som chcel použiť slovenskú wikipediu, po odladení projektu može byť použitý aj na anglickú. https://dumps.wikimedia.org/skwiki/latest/
Články sa nachádzajú v tabuľke pages-articles. Ide o XML súbor, ktorý obsahuje (okrem iného) nasledovné štruktúry: 
```xml
<page>
  <title>Main Page</title>
  <ns>0</ns>
  <id>2</id>
  <redirect title="Hlavná stránka" />
  <revision>
    <id>89777</id>
    <timestamp>2003-08-31T12:01:53Z</timestamp>
    <contributor>
      <username>Andre Engels</username>
      <id>2</id>
    </contributor>
    <model>wikitext</model>
    <format>text/x-wiki</format>
    <text bytes="30" xml:space="preserve">#REDIRECT [[Hlavná stránka]]</text>
    <sha1>gj4ij44roeqj42e06ryb2oj86hae6f8</sha1>
  </revision>
</page>
```

Element text obsahuje samotný text článku vo formáte wiki šablóny. Linka sa označuje dvojitými hranatými zátvorkami, anchor text je oddelený |. Napr. 
```
[[linka | anchor text]]
```

## Popis riešenia
Riešenie pozostáva z viacerých procesov a vlákien, ktoré sú pospájané pomocou správ (message queue).

Čítanie vstupného súboru pomocou SAX XML parsera prebieha v hlavnom vlákne a posiela jednotlivé články spolu s nadpisom do 1. queue - `article_queue`.

2 procesy čítajú `article_queue` a z článkov pomocou regulárneho výrazu vytiahnu jednotlivé anchor texty, ktoré vložia do 2. queue - `anchor_queue`.

Ďalších X (12) procesov číta `anchor_queue` a robí agregáciu podľa článku na ktorý odkazujú anchor linky. Pre každý článok taktiež vykonajú NLP analýzu menných entít.
Výstup uložia do 3. - výstupnej queue.

Tú číta jedno vlákno, ktoré skladá dopyty do ElasticSearch a počíta offline štatistiky entít.

Štruktúra dokumentu v ES indexe:

```json
{
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
            }
        }
    }       
}
```

príklad:
```json
{
  "_index" : "vi_index_to",
  "_type" : "_doc",
  "_id" : "Črmeľská dolina",
  "_source" : {
    "page_to" : "Črmeľská dolina",
    "anchors" : [
      {
        "page_from" : "Črmeľ",
        "anchor_text" : "Črmeľskú dolinu"
      }
    ],
    "page_to_entity" : "dolina"
  }
}
```

Offline štatistiky sa vytvoria do súboru `entity_counts<timestamp>.json`.

## NLP
Hľadanie entít funguje na princípe hľadania zhody v slovníkoch. 
Ako slovníky slúžia:
- zoznam krstných mien
- zoznam obcí z katastrálnej mapy
- zoznam ďaľších geografických názvov z katastrálnej mapy

Hľadanie prebieha najprv postupne pre úplnú zhodu, potom neskôr pre zhodu po jednotlivých slovách.
Mená sa hľadajú len pre 2-5 slovné spojenia.

Výsledky hľadania sa odkladajú do cache s maximálnou veľkosťou, ktorá po naplnení zahadzuje náhodné prvky.
