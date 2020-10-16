import logging

from regex import regex

text = '''{{Infobox Osobnosť
 | Meno               = Isaac Newton
 | Rodné meno         = 
 | Popis osoby        = anglický fyzik, matematik a filozof
 | Portrét            = GodfreyKneller-IsaacNewton-1689.jpg
 | Veľkosť portrétu   = 
 | Popis portrétu     = 
 | Dátum narodenia    = [[4. január]] [[1643]]
 | Miesto narodenia   = [[Woolsthorpe-by-Colsterworth]], [[Linc[[oln]]shire (grófstvo)|Lincolnshire]], [[Anglicko]]
 | Dátum úmrtia       = {{duv|1727|3|31|1643|1|4}}
 | Miesto úmrtia      = [[Londýn|Kensington]], [[Anglicko]]
 | Bydlisko           = 
 | Iné mená           = 
 | Štát pôsobenia     = 
 | Národnosť          = 
 | Štátna príslušnosť = 
 | Zamestnanie        = 
 | Známy vďaka        = 
 | Alma mater         = 
 | Profesia           = 
 | Aktívne roky       = <!-- [[1900]]{{--}}[[1900]] -->
 | Rodičia            = 
 | Príbuzní           = 
 | Súrodenci          = 
 | Manželka           = 
 | Partnerka          = 
 | Deti               = 
 | Podpis             = Isaac Newton signature.svg

 | Webstránka         = 
 | Poznámky           = 
 | Portál1            = Matematika
 | Portál2            = Fyzika
 | Portál3            = Astronómia
}}

Sir Isaac Newton, prezident [[Kráľovská spoločnosť|Kráľovskej spoločnosti]] (* [[4. január]] [[1643]], [[Woolsthorpe-by-Colsterworth]], [[Anglicko]] – † [[31. marec]] [[1727]], [[Londýn|Kensington]],) bol anglický [[fyzik]], [[matematik]] a [[filozof]].

Založil [[Diferenciálny [[a integrálny počet]]|infinitezimálny počet]] a formuloval prvú teóriu sily a gravitácie. Jeho objavy v [[matematika|matematike]], [[optika (odbor)|optike]] a [[mechanika|mechanike]] položili základy pre modernú [[fyzika|fyziku]].

Je jednou z najväčších postáv v dejinách ľudského poznania a od neho sa vlastne počíta [[fyzika]] ako novodobá [[veda]]. Newton nadviazal na výsledky svojich predchodcov – [[Galileo Galilei|Galileiho]], [[Johannes Kepler|Keplera]], [[René Descartes|Descarta]] a ďalších. Presne sformuloval základné zákony [[Mechanika|mechanického pohybu]], dal im podobu [[Rovnica (matematika)|matematických rovníc]] a vytvoril [[diferenciálny a integrálny počet]], pomocou ktorého vieme tieto rovnice riešiť. Až od čias Newtona sa stalo možným vypočítať [[mechanický pohyb|pohyby]] [[planéta|planét]], predpovedať presné termíny [[zatmenie Slnka|zatmenia Slnka]] a [[Zatmenie Mesiaca|Mesiaca]], čas návratu periodických planét (hlavne známej [[Halleyho kométa|Halleyovej kométy]]), a dokonca vypočítať i polohu a pohyb doteraz neznámych telies. Tak bola v minulom storočí predpovedaná existencia niektorých planétok a novej planéty [[Neptún]]a, ktoré potom hvezdári na oblohe skutočne našli. Newtonov [[gravitačný zákon]] umožnil určiť hmotnosť [[Nebeské teleso|nebeských telies]] a sily pôsobiace medzi nimi, odvážiť [[zem]]eguľu. Newton dokázal, že nie je rozdiel medzi zákonmi pozemských a nebeských pohybov, ako sa domnieval [[Aristoteles]], ale že sila, ktorá spôsobuje pohyb planét okolo [[Slnko|Slnka]] je tá istá, ako sila, ktorá spôsobuje, že padáme zo schodov.

Newton sa ako skutočný [[vedec]] pridržiaval len pozorovaných [[fakt]]ov a výsledkov [[pokus|experiment]]ov a nepúšťal sa do nepodložených špekulácií. Vedel, že ešte nemôže vysvetliť príčiny a podstatu [[gravitácia|gravitácie]] a vyhlasoval, že hypotézy si nevymýšľa. Bol si pritom vedomý, do akej miery vďačí za svoje výsledky svojim predchodcom a napísal, že ak videl ďalej ako ostatní, bolo to preto, že stál na ramenách obrov.<ref>''stáť na ramenách obrov'' je [[metafora]] a znamená "používať infomácie získané od bývalých veľkých mysliteľov, za účelom intelektuálneho progresu" [http://www.phrases.org.uk/meanings/268025.html]</ref> Zároveň si uvedomoval, že čím viac [[veda|vedu]] poznáva, tým viac sa rozširujú aj obzory nepoznaného a prirovnával sa k malému chlapcovi, ktorý sa len hrá s peknými kamienkami a mušličkami na brehu nekonečného oceánu poznania. V Newtonových súčasníkoch vzbudzovali jeho objavy obdiv a nadšenie. Zdalo sa im, ako keby príroda náhle odhalila svoje tajomstvá a všetko sa stalo jasným. Svedčia o tom verše dobového [[básnik]]a [[Alexander Pope|Alexandra Popea]]: ''Poriadok prírody bol dlho tmou noci zastrený. Boh povedal: Buď Newton! A deň zažiari jasný.''

Až nasledujúci vývoj ukázal, ako veľa ešte nepoznáme a o koľko je svet zložitejší, bohatší a zaujímavejší, než mohol tušiť Newton a jeho súčasníci. Napriek oprávnenej sláve, ktorou je Newtonovo meno obostreté, nebol on sám ako človek bez ľudských nedostatkov a jeho život, ktorý prebiehal v nepokojných časoch [[Dejiny Spojeného kráľovstva|anglickej histórie]], sa neobišiel bez výkyvov. Newton mal obdobie, kedy sa dokázal hlboko sústrediť a plodiť jeden geniálny [[objav]] za druhým a pritom, ako to u vedcov býva, sa nestaral o svoje okolie, ani o [[životospráva|životosprávu]] a telesne a duševne sa vyčerpával. Potom sa zase dlhé roky vedeckej práci nevenoval, vyžíval sa v osobných a prestížnych sporoch, zaoberal sa pochybnými činnosťami v oblasti [[alchýmia|alchýmie]], hľadaním [[kameň mudrcov|kameňa mudrcov]], [[Mytológia (veda)|mytologickými]] [[letopočet|letopočtami]], a dokonca prežíval aj roky vyslovene duševných kríz a porúch.

== Životopis ==
[[File:Woolsthorpe-manor.jpg|thumb|Miesto narodenia Isaaca Newtona]]
Narodil sa na samote Woolsthorpe v [[Lincolnshire (grófstvo)|Lincolnskom grófstve]] na severovýchod od [[Londýn]]a, podľa starého [[Juliánsky kalendár|juliánskeho kalendára]], ktorý vtedy v [[Anglicko|Anglicku]] platil, na [[Vianoce]] v roku [[1642]]. Otec mu zomrel ešte pred narodením, matka sa druhýkrát vydala a o malého chlapca sa väčšinou starala stará matka. Newton bol ako chlapec samotár a často chorý a nič nenasvedčovalo tomu, že je mimoriadne nadaný. Bol ale zručný, konštruoval pre svoje potešenie slnečné a vodné hodiny, vodné mlynčeky a rôzne mechanické hračky, brúsil sklenené [[Šošovka (optika)|šošovky]] a robil [[chémia|chemické]] pokusy. Do školy chodil najprv vo svojej rodnej dedine a potom do neďalekého Granthamu, kde býval v rodine lekárnika Clarka. Tu získal prístup k rozsiahlej [[knižnica|knižnici]], rýchlo začal ovládať klasické [[Jazyk (jazykoveda)|jazyky]] a zoznámil sa napríklad s [[Euklidovská geometria|Euklidovými základmi geometrie]]. V Granthame prežil Newton aj svoju mladícku lásku so slečnou Storeyovou, ktorej sľúbil manželstvo. Nakoniec sa však Newton oddal [[univerzita|univerzitnej]] dráhe a zostal po celý život slobodný.

[[Súbor:NewtonsTelescopeReplica.jpg|náhľad|Replika [[Newtonov ďalekohľad|Newtonovho ďalekohľadu]] z roku [[1672]] pre [[Kráľovská spoločnosť|Kráľovskú spoločnosť]]]]
V roku [[1661]] odišiel študovať na Trinity College v [[Cambridge (Cambridgeshire)|Cambridgei]], kde bol jeho učiteľom výborný [[matematik]] a [[fyzik]] [[Isaac Barrow]]. Newtonove štúdiá na univerzite prerušila [[Čierna smrť|morová epidémia]] v rokoch [[1665]]{{--}}[[1667]]. Newton sa vrátil do rodnej dediny a premýšľal tu nad svojimi budúcimi [[objav]]mi. Podľa známej legendy mu vtedy vraj na hlavu spadlo [[jablko]], ktoré ho priviedlo na myšlienku o [[gravitácia|zemskej príťažlivosti]]. Po návrate do Cambridgea ukončil Newton štúdium a prevzal katedru [[geometria|geometrie]] po svojom učiteľovi Barrowovi. Počas ďalších rokov sa usilovne venoval vedeckej práci. Jej prvým výsledkom bola konštrukcia zrkadlového [[ďalekohľad]]u (pozri ''[[Newtonov ďalekohľad]]''), ktorý nemá [[Optika (odbor)|optické]] nedostatky spôsobené [[Šošovka (optika)|šošovkami]]. Vo svojej práci o optike z roku [[1672]] Newton ukázal, že biele [[Viditeľné svetlo|svetlo]] je možné zložiť z farebných spektrálnych [[Svetelný lúč|lúčov]] a vysvetlil zákonitosti dúhových [[Farba (fyzika)|farieb]]. Jeho najvýznamnejšie dielo ''Principia mathematica philosophiae naturalis'' ([[1687]]), Matematické základy prírodnej [[filozofia|filozofie]], vyšlo v roku [[1687]] na naliehanie a za materiálnej pomoci známeho [[astronóm]]a [[Edmund Halley|Edmunda Halleyho]]. Newton v ňom formuloval svoje tri známe [[newtonove pohybové zákony|pohybové zákony]] – [[zákon zotrvačnosti]], [[zákon sily]] a [[zákon akcie a reakcie]]. Podľa týchto zákonov [[sila]] nie je príčinou [[Mechanický pohyb|pohybu]], ale zmeny pohybu. Ak nebude na teleso pôsobiť žiadna sila, bude teleso v pokoji, alebo sa bude samo pohybovať rovnomerným, priamočiarym pohybom. Newton tu tiež uvádza [[gravitačný zákon]], podľa ktorého príťažlivá sila medzi dvoma hmotnými bodmi alebo guľovými telesami sa mení nepriamo úmerne štvorcu vzdialenosti medzi ich stredmi. Na Newtonovu počesť bola pomenovaná jednotka sily, newton.

[[Súbor:Isaac Newton grave in Westminster Abbey.jpg|náhľad|Newtonov hrob vo [[Westminsterské opátstvo|Westminsterskom opátstve]]]]
Newton žil osamelo, nikam necestoval, mal len málo priateľov a veľkú nechuť k publikovaniu a verejnému vystupovaniu. Jeho [[Prednáška|prednášky]] na [[univerzita|univerzite]] neboli príliš zaujímavé, lebo v nich [[detail]]ne popisoval svoje [[pokus|experiment]]y a [[Žiak (škola)|študenti]] na ne veľmi nechodili. Viedol vleklé spory o pôvodnosti svojich prác s [[Nemecko|nemeckým]] matematikom [[Gottfried Wilhelm Leibniz|Gottfriedom Leibnizom]] ([[1646]]{{--}}[[1716]]), [[Anglicko|anglickým]] fyzikom [[Robert Hooke|Robertom Hookom]] ([[1635]]{{--}}[[1703]]), objaviteľom zákona pružných síl a s ďalšími. Napriek svojej ostýchavosti sa Newton angažoval aj vo verejnom živote a bol dvakrát zvolený za člena [[parlament]]u. Jeho život sa zmenil po odchode z Cambridgea v roku [[1696]] do [[Londýn]]a, kde mu viedla domácnosť jeho pôvabná a duchaplná neter Bartonová. Páčila sa i Charlesovi Montagueovi, ktorý ako lord Halifax zastával významné politické postavenie a vymohol Newtonovi výnosné miesto správcu kráľovskej mincovne. Newton si plnil svoje úradné povinnosti veľmi svedomito a poslal na popravisko 20 odhalených peňazokazov. Jeho spoločenská prestíž stále rástla, v roku [[1703]] sa stal prezidentom vedeckej [[Kráľovská spoločnosť|Londýnskej kráľovskej spoločnosti]], v roku [[1705]] bol povýšený do šľachtického stavu. Newton zomrel v Kensingtone, ktorý je dnes súčasťou [[Londýn]]a a bol pochovaný s najvyššími poctami vo [[Westminsterské opátstvo|Westminsterskom opátstve]].

Známe sú jeho [[newtonove pohybové zákony|pohybové zákony]]:
# [[Zákon zotrvačnosti]]: Každé hmotné teleso v inerciálnej súradnicovej sústave zotrváva v relatívnom pokoji alebo v rovnomernom priamočiarom pohybe, pokiaľ nie je nútené pôsobením sily tento stav zmeniť.
# [[Zákon sily]]: V inerciálnej vzťažnej sústave je veľkosť sily pôsobiacej na hmotný bod určená hodnotou derivácie hybnosti tohto hmotného bodu podľa času, pričom zmena hybnosti má smer rovnobežný s pôsobiacou silou.
# [[Zákon akcie a reakcie]]: Sily, ktorými na seba pôsobia každé dve telesá vo vzájomnej interakcii, sú rovnako veľké, opačného smeru a súčasne vznikajú a zanikajú.

== Diela ==
{{Gutenberg autor|id=Isaac+Newton|meno=Isaac Newton}}
* ''Teória svetla a farieb'' – [[1672]]
* ''Teória svetla a farieb, obsahujúca hypotézu vysvetľujúcu vlastnosti svetla, ktorú autor vyložil v predchádzajúcich spisoch, ako aj opis najdôležitejších javov rozličných farieb jemných vrstiev a mydlových bubliniek, ktoré tak isto závisia od skôr charakterizovaných vlastností svetla'' – [[1675]]
* ''O pohybe'' (rukopis) – [[1684]]
* ''Matematické princípy prírodnej filozofie'' – [[1687]], [[1713]]
* ''Pravidlá filozofovania'' (Pravidlá usudzovania vo fyzike)
* ''Nová teória svetla a farieb'' – [[1704]] ?
* ''Optika'' (latinské doplnené vydanie) – [[1705]], 2. anglické [[1717]], ďalšie [[1721]], [[1730]] [http://books.google.com/books?id=XXu4AkRVBBoC&printsec=frontcover&dq=newton&as_brr=1&hl=sk#PPP9,M1]

== Poznámky ==
<references />

== Pozri aj ==
* [[Newtonove pohybové zákony]]
* [[Diferenciálny a integrálny počet]]
* [[Gravitačný zákon]]
* [[Newtonov ďalekohľad]]
* [[Dejiny fyziky]]

== Iné projekty ==
{{Projekt|q=Isaac Newton|commonscat=Isaac Newton|wikisource=Author:Isaac Newton|wikisource_štítok=Isaac Newton (v angličtine)}}

== Zdroje ==
* FARA, Patricia: ''Newton : Formování génia.'' Praha : BB/art [[2004]]. 334 s. ISBN 80-7341-181-4
* KUZNECOV, Boris Grigorjevič: ''Od Galileiho po Einsteina.'' Bratislava : Nakladateľstvo Pravda [[1975]]. 614 s. [Preklad: M. Zigo, F. Novosad]

{{DEFAULTSORT:Newton, Isaac}}
[[Kategória:Anglickí filozofi]]
[[Kategória:Anglickí fyzici]]
[[Kategória:Anglickí matematici]]
[[Kategória:Anglickí astronómovia]]
[[Kategória:Anglickí vynálezcovia]]
[[Kategória:Optici]]
[[Kategória:Alchymisti]]
[[Kategória:Okultisti]]
[[Kategória:Geometri]]
[[Kategória:Hermetici]]
[[Kategória:Filozofi vedy]]
[[Kategória:Filozofi 17. storočia]]
[[Kategória:Teoretickí fyzici]]
[[Kategória:Nebeská mechanika]]
[[Kategória:Kresťanskí filozofi]]
[[Kategória:Absolventi University of Cambridge]]
[[Kategória:Členovia Kráľovskej spoločnosti]]
[[Kategória:Prezidenti Kráľovskej spoločnosti]]
[[Kategória:Osobnosti na britských bankovkách]]
[[Kategória:Osobnosti na britských poštových známkach]]
[[Kategória:Osobnosti na francúzskych poštových známkach]]
[[Kategória:Osobnosti na nemeckých poštových známkach]]
'''

ANCHOR_PATTERN = '(?=(\[\[(?>[^[]]|(?1))*+\]\]))'
ANCHOR_PATTERN2 = '(?<=\[\[)[^]]+(?=\]\])'
ANCHOR_PATTERN3 = '(?=(\[(?>[^[]]|(?1))*+\]))'

ANCHOR_PATTERN4 = '\[\[(^())\]\]'


