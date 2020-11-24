import unittest
from unittest import TestCase

from anchor_statistics import get_anchors, process_anchor

text = '''

{{Infobox Programovací jazyk
| Logo = Python logo and wordmark.svg
| Názov = Python
| Dátum vzniku = Február 1989
| Druh = objektový
| Interpretovaný = áno
| Typová kontrola = stredná
| Tvorca = [[Guido van Rossum]]
| Prípony = .py, .pyc, .pyd
| Dialekty = [[Jython]], [[Iron Python]]
| Použitie = Všetky platformy
}}

[[Súbor:Python script.svg|right|thumb|Ukážka kódu v Pythone]]

Python je [[Interpreter (programovanie)|interpretovaný]], interaktívny [[programovací jazyk]], ktorý vytvoril [[Guido van Rossum]], pôvodne ako skriptovací jazyk pre [[Amoeba OS]] schopný [[Systémové volanie|systémových volaní]]. Python je často porovnávaný s jazykmi [[Tcl]], [[Perl]], [[Scheme]], [[Java (programovací jazyk)|Java]] a [[Ruby (programovací jazyk)|Ruby]]. Python je vyvíjaný ako [[open source]] projekt, a je v súčasnosti pri verzii 3.8.3.

== Charakteristika ==
Python je multi-paradigmový jazyk podobne ako [[Perl]], na rozdiel od [[Smalltalk]]u alebo [[Haskell]]u. To znamená, že namiesto toho aby nútil programátora používať určitý štýl programovania, umožňuje použivanie viacerých. Python podporuje objektovo orientované, štruktúrované aj funkcionálne programovanie. Je to dynamicky typový jazyk, podporuje veľké množstvo vysokoúrovňových dátových typov a na správu pamäte používa garbage collection.

Aj keď sa Python často označuje ako "skriptovací jazyk", používa sa na vývoj mnohých veľkých softvérových projektov ako sú aplikačný server [[Zope]] a systémy na zdieľanie súborov [[Mnet]] a [[BitTorrent]]. Tak isto ho široko využíva [[Google]]. Zástanci Pythónu ho radšej volajú vysokoúrovňovým dynamickým programovacím jazykom, lebo pojem "skriptovací jazyk" sa asociuje s jazykmi, ktoré sa používajú len na jednoduché shell skripty alebo s jazykmi ako [[JavaScript]]: jednoduchšími a na väčšinu účelov menej spôsobilými ako "skutočné" programovacie jazyky ako Python.

Ďalšou dôležitou vlastnosťou Pythonu je to, že sa dá jednoducho rozširovať. Nové zabudované moduly môžu byť jednoducho napísané v [[C (programovací jazyk)|C]] alebo [[C Plus Plus|C++]]. Python tiež môže byť použitý ako rozširovací jazyk pre existujúce moduly a aplikácie, ktoré potrebujú programovateľné rozhranie.

Aj keď návrhár Pythonu je trochu nepriateľský k funkcionálnemu programovaniu a k tradícii Lispu, sú tu viditeľné paralely medzi filozofiou Pythonu a filozofiou minimalistických jazykov Lispovej rodiny ako sú [[Scheme]]. Kvôli tomu veľa bývalých programátorov v [[Lisp]]e považujú Python za príťažlivý {{bez citácie}}.

Názov jazyka vôbec nevznikol z názvu druhu hada. Autor nazval jazyk podľa populárneho britského satirického seriálu [[Monty Python’s Flying Circus]]. Ale napriek tomu sa názov jazyka často asociuje práve s hadom a nie so seriálom.

== Dátové typy a štruktúry ==
Python podporuje základné dátové typy, ako celé čísla a čísla s pohyblivou desatinnou čiarkou, ale podporuje aj celé čísla neobmedzenej dĺžky a komplexné čísla.

Taktiež podporuje bežné operácie s reťazcami s jednou výnimkou: reťazce sú v Pythone nemenným typom, takže operácie, ktoré by inak menili reťazec (napríklad zámena znakov), namiesto toho vracajú nový reťazec.

V Pythone premenné nemajú typ, majú iba hodnoty. Teda Python je dynamicky typový jazyk na rozdiel od [[Java (programovací jazyk)|Java]] a [[C (programovací jazyk)|C]]. Všetky hodnoty sa odovzdávajú odkazom a nie hodnotou.

Medzi dynamicky typovými jazykmi má Python stredne prísnu typovú kontrolu. Implicitné konverzie sú definované pre číselné typy, takže môžeme napríklad vynásobiť komplexné číslo celým bez explicitného pretypovania. Ale nie je tu implicitná konverzia medzi číslami a reťazcami.

=== Kolekcie ===
Jedným z fundamentálnych aspektov Pythonu je koncept kolekčných (alebo kontajnerových) typov. Vo všeobecnosti kolekcia je objekt, ktorý obsahuje iné objekty tak, že k nim môžeme pristupovať pomocou indexov alebo kľúčov. Kolekcie majú dve základné formy: mapované typy a sekvenčné typy.

Mapované typy sú nezoradené premenné typy implementované v podobe asociatívneho poľa, ktoré mapuje množinu objektov alebo kľúčov na elementy v množine hodnôt podobne ako matematické funkcie.

Iným typom kolekcií sú zoradené postupnosti — sekvenčné typy, ktoré reprezentujú zoznamy, tuple a reťazce. Všetky sekvenčné typy sú indexované pozične (od 0 po dĺžku – 1) a všetky okrem reťazcov môžu obsahovať objekty ľubovoľného typu (reťazce môžu obsahovať iba znaky, ktoré sú v Pythone reprezentované ako jednoznakové reťazce). Reťazce a tuple sú nemenné, zatiaľ čo zoznamy sú premenné, teda môžeme pridávať, odoberať alebo meniť elementy.

Python tak isto poskytuje rozsiahle možnosti manipulácie s kolekciami ako je zabudovaný operátor na kontrolu, či kolekcia obsahuje daný objekt, a jednoduchá iterácia pomocou "<code>for element in list</code>".

=== Objektový systém ===
Systém dátových typov Pythonu je dobre integrovaný so systémom tried. Zabudované dátové typy nie sú skutočnými triedami, ale triedy môžu od nich dediť. Takže je možné rozširovať reťazce, asociatívne polia alebo celé čísla.

Jazyk podporuje rozsiahlu introspekciu typov a tried. Typy môžeme prečítať a porovnávať, teda, ako v [[Smalltalk]]u, typy sú tiež objektmi. Atribúty objektu môžeme extrahovať ako asociatívne pole.

Operátory môžu byť v Pythone predefinované pomocou zadefinovania špeciálnej členskej funkcie, napríklad definovanie <code>__add__</code> v triede dovolí používať operátor <code>+</code> na inštancie triedy.

== Syntax ==
Python bol navrhovaný tak, aby bol dobre čitateľný. Má jednoduché vizuálne rozmiestnenie, často používa anglické kľúčové slová tam, kde iné jazyky používajú interpunkciu a má nápadne menej syntaktických konštrukcií ako mnohé iné štruktúrované jazyky ako [[C (programovací jazyk)|C]], [[Perl]] alebo [[Pascal]].

Napríklad Python má len dva tvary cyklov: <code>for</code>, ktorý prechádza elementmi zoznamu alebo iterátoru a <code>while</code>, ktorý sa opakuje, kým hodnota výrazu je true. Chýba mu komplexný <code>for</code> v štýle [[C (programovací jazyk)|C]] a <code>do</code>...<code>while</code>, aj keď sa samozrejme dajú ekvivalentne vyjadriť. Takisto má na vetvenie iba <code>if</code>...<code>elif</code>...<code>else</code> — žiadne <code>switch</code> alebo <code>goto</code> (goto bolo implementované ako vtip pre 1. apríl 2004 ako prídavný modul).

=== Syntaktická významnosť odsadenia ===
Jedným z nezvyčajných aspektov syntaxe Pythona je spôsob, akým sa určujú bloky v programe. Je to aspekt syntaxe Pythonu, o ktorom počuli aj programátori, ktorí inak nepoznajú Python, keďže je dosť unikátny medzi jazykmi rozšírenými v súčasnosti (iný jazyk zdieľajúci túto vlastnosť je [[Haskell]]).

V jazykoch, ktoré používajú blokovú štruktúru zdedenú po [[ALGOL]]e (vrátane [[Pascal]]u, [[C (programovací jazyk)|C]], [[Perl]]u a mnohých iných) bloky kódu sú oddelené pomocou zátvoriek alebo kľúčových slov ako <code>begin</code> a <code>end</code> v [[Pascal]]e. Avšak vo všetkých týchto jazykoch programátori obyčajne používajú odsadzovanie kódu v bloku od kraja, aby vizuálne oddelili blok od ostatného kódu.

Python na rozdiel od toho požičiava vlastnosť z málo známeho jazyka [[ABC (programovací jazyk)|ABC]] - namiesto interpunkcie alebo kľúčových slov používa samotné odsadzovanie na určenie bloku. Ozrejmí to krátky príklad. Tu je rekurzívna funkcia v [[C (programovací jazyk)|C]] a v Pythone, ktorá robí to isté — vypočíta [[faktoriál]] celého čísla.

''Faktoriál v C:''
<source lang="c">
 int factorial(int x) {
     if (x == 0) {
         return 1;
     } else {
         return x * factorial(x-1);
     }
 }
</source>

''Faktoriál v Pythone:''
<source lang="python">
 def factorial(x):
     if x == 0:
         return 1
     else:
         return x * factorial(x-1)
</source>

''Faktoriál v Pythone za použitia lambdy:''
<source lang="python">
factorial = lambda x: 1 if x==0 else x*factorial(x-1)
</source>

=== Dokumentačné reťazce ===
Reťazec umiestnený hneď za definíciou triedy alebo funkcie alebo na začiatku modulu sa stáva asociovaným dokumentačným reťazcom (tzv. docstring). Existujú nástroje na automatické vytváranie dokumentácie vo formáte [[HTML]] založenej na dokumentačných reťazcoch.

=== Funkcionálne programovanie ===
Ako už bolo spomenuté, ďalším kladom Pythonu je dostupnosť funkcionálneho štýlu programovania. Ako sa dá očakávať, umožňuje to oveľa priamočiarejšiu prácu so zoznamami a inými kolekciami. Jedna z takýchto konštrukcií je ''list comprehension'', prebratá z funkcionálneho jazyka [[Haskell]], ako je vidieť tu na výpočte prvých piatich mocnín čísla dva:

<source lang="python">
 numbers = [1, 2, 3, 4, 5]
 powers_of_two = [2**n for n in numbers]
</source>

Algoritmus [[quicksort]] môže byť tiež elegantne vyjadrený pomocou list comprehensions:

<source lang="python">
 def qsort(L):
     if L == []: return []
     return qsort([x for x in L[1:] if x< L[0] ]) + L[0:1] + \
         qsort([x for x in L[1:] if x>=L[0] ])
</source>

Keďže Python umožňuje odovzdávať funkcie ako argumenty, je možné vyjadriť aj ďalšie funkcionálne konštrukcie.

==== Lambda ====
Pomocou kľúčového slova <code>lambda</code> môžeme vytvárať malé anonymné funkcie. Bloky <code>lambda</code> v Pythone môžu obsahovať len jeden výraz a nemôžu obsahovať príkazy. Tu je funkcia, ktorá vracia súčet svojich dvoch argumentov: <source lang="python">lambda a, b: a+b</source>
==== Exec ====
Python umožňuje vykonanie kódu, ktorý je napr. obsahom premennej, pomocou funkcie <code>exec</code>. V zásade je tak možné spúšťať program, ktorý bude akoby meniť sám seba. 
Príklad: 
<source lang="python">
 premenna="""print "ahoj svet"; premenna="print 'tak ahoj';stale=False" """

 stale=True

 # keby sme nepoznali obsah premennej "premenna" mohli by sme sa domnievat, ze v dalsom riadku bude stale vykonavane to iste
 while stale: exec premenna

 """ Prebehnu vsak iba dva cykly a vypis bude:

 ahoj svet
 tak ahoj

  Co sa udialo? premenna "premenna" sa vykona prvykrat - cosi vypise a zmeni svoj obsah
  vykona sa druhykrat, ale druhykrat uz je jej obsahom zmena premennej "stale" na False
  (plus tlac ineho textu ako v prvom cykle) takze vykonanie tretikrat uz nebude  
 """
</source>

==== Generátory ====
Generátory v Pythone sú mechanizmom pre tzv. "lenivé vyhodnocovanie" funkcií, ktoré by inak vracali neúmerne veľké alebo výpočtovo náročné zoznamy.

Príklad:

<source lang="python">
 def generate_ints(N):
     for i in xrange(N):
         yield i
</source>

Teraz môžeme použiť generátor generate_ints:

<source lang="python">
 for i in generate_ints(N):
     print i
</source>

Definícia generátora vyzerá rovnako ako definícia funkcie, len namiesto kľúčového slova <code>return</code> je použité <code>yield</code>. Volanie generátora môžeme použiť namiesto zoznamu, alebo inej štruktúry, cez elementy ktorej chceme postupne prechádzať. Vždy, keď cyklus ''for'' v príklade potrebuje ďalší prvok, zavolá sa generátor, ktorý dá ďalší prvok.

=== Objektovo orientované programovanie ===
Python má rozsiahlu podporu pre objektovo orientované programovanie. Podporuje nielen polymorfizmus tried dediacich od tej istej triedy ako v staticky typových jazykoch, ale aj plný polymorfizmus pre všetky objekty. Všetko v Pythone je objekt vrátane tried, funkcií, čísel a modulov. Python tiež podporuje metatriedy – pokročilý nástroj na rozšírenie funkcionality tried. Samozrejme podporuje dedičnosť vrátane viacnásobnej dedičnosti. Má obmedzenú podporu pre súkromné premenné.

=== Spracovanie výnimiek ===
Python podporuje spracovanie výnimiek vo význame testovania chýb a iných výnimočných udalostí v programe. Takto je možné zachytiť aj výnimku spôsobenú syntaktickou chybou.

Výnimky dovoľujú stručnejšiu a spoľahlivejšiu kontrolu chýb ako iné spôsoby ohlasovania chýb alebo výnimočných udalostí. Výnimky nerobia kód neprehľadným ako testovanie vráteného kódu chyby v [[C (programovací jazyk)|C]] a môžu sa jednoducho šíriť volajúcimi funkciami, ak chyba musí byť ohlásená vyššej úrovni programu.

== Štandardná knižnica ==
Python má rozsiahlu štandardnú knižnicu, ktorá ho robí vhodným na veľa úloh. Moduly štandardnej knižnice môžu byť rozšírené vlastnými modulmi napísanými v [[C (programovací jazyk)|C]] alebo v Pythone. Štandardná knižnica je dobre prispôsobená písaniu aplikácií pracujúcich s Internetom, lebo podporuje množstvo štandardných formátov a protokolov (napríklad [[MIME]] a [[HTTP]]). Tak isto sú tam moduly pre vytváranie grafického užívateľského rozhrania, pripájanie sa k relačným databázam a manipulovanie s regulárnymi výrazmi.

Väčšia časť štandardnej knižnice je kompatibilná medzi platformami, teda programy môžu pracovať v UNIX, Windows, Macintosh a iných platformách bez zmeny.

== Ďalšie vlastnosti ==
Interpreter Pythonu tiež podporuje interaktívny režim, v ktorom výrazy môžu byť zadávané z terminálu a môžeme okamžite vidieť výsledok. Je to výhoda pre tých, ktorí sa učia jazyk, ale aj pre skúsených vývojárov: časti kódu môžu byť testované v interaktívnom režime pred tým, ako budú integrované do programu. Ineraktívny shell pre python [[ipython]], ktorý podporuje okrem iného aj code highlighting a automatické dopĺňanie výrazov, môže slúžiť priam ako náhrada systémového shellu. To môže byť užitočné zvlášť pre platformu Windows, ktorej štandardný shell je veľmi nepraktický. 

Python tak isto obsahuje vstavaný debugger, profiler a nástroje na testovanie (unit testing framework).

== Podporované platformy ==
Aj keď Python bol originálne programovaný pre platformu [[Amoeba OS]], táto verzia je „mŕtva“ (nie je udržiavaná). Najpopulárnejšie platformy, na ktorých pracuje Python, sú [[Linux (operačný systém)|Linux]], [[BSD]], [[Mac OS X]], [[Microsoft Windows]] a [[Java (programovací jazyk)|Java]] (Java verzia je kompletne oddelená implementácia). Mac GUI pre Python je spravované externým projektom nazývaným MacPython a bolo zahrnuté do Mac OS 10.3 „Panther“. Ďalšie podporované platformy sú:
* [[Mac Classic]]
* [[SPARC]] [[Solaris (operačný systém)|Solaris]]
* tak isto ďalšie [[Unix]]y, napr. [[Irix]]
* [[OS/2]]
* [[Amiga]]
* [[AROS]]
* [[AS/400]]
* [[BeOS]]
* [[Berkeley Software Distribution|BSD]]
* [[OS/390]]
* [[z/OS]]
* [[QNX]]
* [[VMS]]
* [[Psion]]
* [[RISC OS]] (predtým Acorn)
* [[VxWorks]]
* [[PlayStation 2]]
* [[Sharp Zaurus]]
* [[Windows CE]]/[[Pocket PC]]
* [[Palm OS]]
* [[S60]]
Ale väčšina knižníc pre Python je dostupná iba pre Linux, BSD, Mac OS X a Windows.

== Externé odkazy ==
* [http://www.python.org/ Domáca stránka projektu]
* [http://python.wraith.cz/ Odborné (cz) stránky o Pythonu]
* [http://www.py.cz/ www.py.cz PyCZ, „vše, co má alespoň něco společného s Pythonem“]
* [http://www.freenetpages.co.uk/hp/alan.gauld/czech/cztutintro.html učebnica programovania v pythone, česky + anglicky]
* [http://pydev.sf.net Rozšírenie PyDev do IDE Eclipse pre vývoj v Pythone]

{{Významné programovacie jazyky}}

[[Kategória:Programovacie jazyky]]
[[Kategória:Python]]


'''

anchors = [
    "Guido van Rossum",
    "Jython",
    "Iron Python",
    "Súbor:Python script.svg|right|thumb|Ukážka kódu v Pythone",
    "Interpreter (programovanie)|interpretovaný",
    "programovací jazyk",
    "Guido van Rossum",
    "Amoeba OS",
    "Systémové volanie|systémových volaní",
    "Tcl",
    "Perl",
    "Scheme",
    "Java (programovací jazyk)|Java",
    "Ruby (programovací jazyk)|Ruby",
    "open source",
    "Perl",
    "Smalltalk",
    "Haskell",
    "Zope",
    "Mnet",
    "BitTorrent",
    "Google",
    "JavaScript",
    "C (programovací jazyk)|C",
    "C Plus Plus|C++",
    "Scheme",
    "Lisp",
    "Monty Python’s Flying Circus",
    "Java (programovací jazyk)|Java",
    "C (programovací jazyk)|C",
    "Smalltalk",
    "C (programovací jazyk)|C",
    "Perl",
    "Pascal",
    "C (programovací jazyk)|C",
    "Haskell",
    "ALGOL",
    "Pascal",
    "C (programovací jazyk)|C",
    "Perl",
    "Pascal",
    "ABC (programovací jazyk)|ABC",
    "C (programovací jazyk)|C",
    "faktoriál",
    "HTML",
    "Haskell",
    "quicksort",
    "C (programovací jazyk)|C",
    "C (programovací jazyk)|C",
    "MIME",
    "HTTP",
    "ipython",
    "Amoeba OS",
    "Linux (operačný systém)|Linux",
    "BSD",
    "Mac OS X",
    "Microsoft Windows",
    "Java (programovací jazyk)|Java",
    "Mac Classic",
    "SPARC",
    "Solaris (operačný systém)|Solaris",
    "Unix",
    "Irix",
    "OS/2",
    "Amiga",
    "AROS",
    "AS/400",
    "BeOS",
    "Berkeley Software Distribution|BSD",
    "OS/390",
    "z/OS",
    "QNX",
    "VMS",
    "Psion",
    "RISC OS",
    "VxWorks",
    "PlayStation 2",
    "Sharp Zaurus",
    "Windows CE",
    "Pocket PC",
    "Palm OS",
    "S60",
    "Kategória:Programovacie jazyky",
    "Kategória:Python"
]


class TestAnchors(TestCase):

    def test_get_anchors(self):
        self.assertEqual(list(get_anchors(text)), anchors)

    def test_process_achor(self):
        self.assertEqual(process_anchor("Page to|Anchor text"), ("Anchor text", "Page to"))


if __name__ == '__main__':
    unittest.main()

# for anchor in get_anchors(text):
#     print(anchor)
