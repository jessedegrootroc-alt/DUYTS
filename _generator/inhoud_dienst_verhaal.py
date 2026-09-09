# -*- coding: utf-8 -*-
"""De verhaallaag onder de dienstpagina's.

De bronsite legt per dienst goed uit *wat* iets technisch is, maar niet wat een
opdrachtgever ermee moet: wanneer je hiervoor aanklopt, hoe het traject loopt,
wat je aan het eind in handen hebt en wat er van jou wordt verwacht. Dat deel
staat hier, in de secties die het template daarvoor heeft.

WAT HIER VANDAAN KOMT
  - De technische uitleg en de teksten over de constructies zelf: die komen
    onveranderd uit `duyts/services.json`, de export van www.duyts.nl.
  - De vragen over vergunningen: die staan als vraag-en-antwoord op de bronsite
    en zijn hier alleen naar de accordeon verplaatst.

WAT HIER IS BIJGESCHREVEN
  - Situaties, processtappen, wat het oplevert, wat je krijgt aangeleverd en de
    overige vragen. Dat is vakinhoud over hoe dit werk in Nederland verloopt,
    geschreven op basis van de KCAF-richtlijn Funderingen onder gebouwen (2023,
    opvolger van de twee F3O-richtlijnen), de Wet kwaliteitsborging voor het
    bouwen (Wkb, sinds 1 januari 2024 voor gevolgklasse 1), het Besluit
    bouwwerken leefomgeving en de gangbare ontwerpfasen VO/DO/UO.

WAT HIER BEWUST NIET STAAT
  Geen doorlooptijden, tarieven, certificaten, klantnamen, aantallen of
  garanties. Dat zijn uitspraken over dít bedrijf en die kan alleen Duyts doen.
  Waar zo'n getal het verhaal zou helpen, staat er een formulering die klopt
  zonder te beloven ("in de offerte staat binnen welke termijn wij kunnen
  starten" - dat zegt de bronsite zelf).

Een dienst zonder eigen regel hieronder valt terug op de familie waar hij bij
hoort (FAMILIE_STANDAARD). Zo blijft een nieuwe dienst één regel werk.
"""

# ---------------------------------------------------------------------------
#  Bouwstenen per familie
# ---------------------------------------------------------------------------
# Iedere ingreep in een bestaand pand volgt in de praktijk dezelfde route: kijken
# wat er staat, doorrekenen, vastleggen op tekening, en meelopen tot het er ligt.
STAPPEN_VERBOUWING = [
    ("Opname en uitgangspunten",
     "We beginnen bij wat er al staat. Aan de hand van uw tekeningen, of anders "
     "een opname ter plaatse, stellen we vast welke wanden en vloeren dragend "
     "zijn en welke belasting er nu op staat.",
     "Zijn er geen tekeningen, dan meten we de bestaande toestand in."),
    ("Constructief ontwerp",
     "We rekenen de nieuwe situatie door en kiezen de constructie die past: een "
     "stalen ligger, een portaal, een verzwaarde balklaag. Niet de zwaarste "
     "oplossing, maar de oplossing die uitvoerbaar is op deze plek.",
     "Belastingen volgens de Eurocode, inclusief de tijdelijke situatie tijdens de bouw."),
    ("Berekening en tekening",
     "U krijgt een constructieberekening en een tekening waarmee de aannemer aan "
     "de slag kan, en waarmee de gemeente of de kwaliteitsborger de aanvraag kan "
     "toetsen. Het benodigde stut- en stempelwerk staat erop aangegeven.",
     "Compleet genoeg om in te dienen, concreet genoeg om mee te bouwen."),
    ("Meelopen tot het staat",
     "Tijdens de uitvoering blijven we bereikbaar. Komt de aannemer iets tegen "
     "wat afwijkt van de tekening, dan kijken we mee en passen we aan.",
     "Als hoofdconstructeur controleren we ook het werk van derden."),
]

STAPPEN_FUNDERING = [
    ("Vooronderzoek en archief",
     "Eerst kijken we wat er bekend is: bouwjaar, oorspronkelijke funderingswijze, "
     "eerdere ingrepen en wat de omgeving doet. Vaak verklaart dat al de helft van "
     "het schadebeeld.",
     "Volgens de fasering van de KCAF-richtlijn Funderingen onder gebouwen."),
    ("Inspectie en metingen",
     "We nemen het pand op: scheurvorming, vloervervormingen, scheefstand en "
     "hoogtemetingen. Zo weten we of het pand nog beweegt of dat het tot rust is "
     "gekomen.",
     "Een pand dat stilstaat vraagt een andere aanpak dan een pand dat zakt."),
    ("Inspectieput en houtonderzoek",
     "Om de fundering echt te beoordelen moet je hem zien. We graven een "
     "inspectieput, nemen de opbouw op en kunnen monsters van de houten palen "
     "laten onderzoeken op aantasting door bacteri&euml;n of schimmels.",
     "Laboratoriumonderzoek via de Stichting Hout Research."),
    ("Beoordeling en handelingsperspectief",
     "U krijgt een rapport met de kwaliteit van de fundering, de resterende "
     "onderhoudsvrije termijn en wat dat betekent: niets doen, monitoren, of "
     "herstellen. Met bij herstel de varianten die in uw situatie kunnen.",
     "Inclusief het funderingslabel waar de gemeente of een splitsing om vraagt."),
]

STAPPEN_NIEUWBOUW = [
    ("Voorlopig ontwerp",
     "We schuiven vroeg aan bij de architect en de opdrachtgever. In deze fase "
     "gaat het om het constructieprincipe: waar komt de stabiliteit vandaan, "
     "welke overspanningen zijn haalbaar, wat betekent dat voor de fundering.",
     "Hoe eerder we meedenken, hoe meer ruimte er nog is om te kiezen."),
    ("Definitief ontwerp",
     "Het principe wordt een uitgewerkt plan: funderingsplan, stabiliteits&shy;"
     "voorzieningen, vloeren, daken en gevels. De kostendeskundige kan hierop "
     "begroten, de architect kan er zijn detaillering op afstemmen.",
     "Met de constructieve uitgangspunten voor alle andere adviseurs."),
    ("Uitvoeringsfase",
     "Wapeningstekeningen, ankerplannen en detailtekeningen: de stukken waarmee "
     "op de bouwplaats gewerkt wordt. Prefab onderdelen komen van de leverancier; "
     "wij leveren de uitgangspunten en controleren wat er terugkomt.",
     "Systeemvloeren, trappen, balkons en staalconstructies inbegrepen."),
    ("Toezicht op de bouw",
     "We komen op de bouwplaats kijken of het uitgevoerde werk klopt met wat er "
     "berekend is, en sturen bij als de praktijk anders uitpakt dan de tekening.",
     "Als hoofdconstructeur houden we de constructieve veiligheid in de hand."),
]

VOORDELEN_BESTAAND = [
    ("schild", "Veilig, en aantoonbaar",
     "Een ingreep in de draagconstructie is geen detail. Onze berekening laat "
     "zien dat het klopt, en is dat ook voor een toetser."),
    ("klok", "Geen vertraging bij de aanvraag",
     "Aanvragen lopen vast op onvolledige stukken. U krijgt wat de gemeente of "
     "kwaliteitsborger nodig heeft, in &eacute;&eacute;n keer."),
    ("mensen", "Direct contact met wie het rekent",
     "Geen accountmanager ertussen. U schakelt met de constructeur die aan uw "
     "project werkt."),
    ("document", "Uitvoerbaar op de bouwplaats",
     "Wij ontwerpen wat de aannemer daadwerkelijk kan bouwen, inclusief het "
     "tijdelijke werk dat daarvoor nodig is."),
]

VOORDELEN_FUNDERING = [
    ("lijst", "Eerst weten, dan beslissen",
     "Funderingsherstel is ingrijpend en kostbaar. Onderzoek vooraf voorkomt dat "
     "u meer doet dan nodig, of te laat bent."),
    ("schild", "Amsterdamse bodem en bouwwijze",
     "We kennen de stad, haar ondergrond en haar panden, en de problemen die "
     "daarbij horen."),
    ("grafiek", "Waarde en verkoopbaarheid",
     "Een beoordeelde, solide fundering is harde informatie bij verkoop, "
     "splitsing of een financieringsaanvraag."),
    ("mensen", "Onafhankelijk van de uitvoerder",
     "Wij voeren geen herstel uit. Ons advies is dus niet gekleurd door wat wij "
     "zelf zouden willen bouwen."),
]

VOORDELEN_NIEUWBOUW = [
    ("grafiek", "Vroeg meedenken loont",
     "In het voorlopig ontwerp is een constructieve keuze nog gratis. In de "
     "uitvoering kost dezelfde keuze geld."),
    ("document", "E&eacute;n set stukken die klopt",
     "Berekening, tekening en uitgangspunten sluiten op elkaar aan, en op wat de "
     "andere adviseurs nodig hebben."),
    ("schild", "Hoofdconstructeur van begin tot eind",
     "Wij houden de constructieve veiligheid over het hele traject in de hand, "
     "ook waar derden onderdelen uitwerken."),
    ("vinkje", "Duurzaam waar het kan",
     "Bij renovatie hergebruiken we zoveel mogelijk van de bestaande "
     "hoofddraagconstructie en de paalfundering."),
]

OPLEVERING_BESTAAND = [
    ("document", "Constructieberekening",
     "De onderbouwing van de nieuwe situatie, met de belastingen en de toetsing "
     "waar een vergunningaanvraag om vraagt."),
    ("lijst", "Constructietekening",
     "Waar de nieuwe constructie komt, welke profielen dat zijn en hoe ze worden "
     "opgelegd."),
    ("trap", "Stut- en stempelplan",
     "Hoe het bestaande werk tijdelijk wordt opgevangen zolang de nieuwe "
     "constructie er nog niet staat."),
    ("mensen", "Bereikbaarheid tijdens de bouw",
     "Vragen van de aannemer lopen via ons, ook nadat de stukken de deur uit zijn."),
]

OPLEVERING_FUNDERING = [
    ("document", "Onderzoeksrapport",
     "De opbouw en de staat van de bestaande fundering, met de metingen en de "
     "uitkomsten van het houtonderzoek."),
    ("grafiek", "Funderingslabel en termijn",
     "De kwaliteitsklasse en de onderhoudsvrije termijn: de informatie waar een "
     "gemeente of een splitsing om vraagt."),
    ("lijst", "Handelingsperspectief",
     "Niets doen, monitoren of herstellen, en bij herstel de varianten die op "
     "deze plek uitvoerbaar zijn."),
    ("trap", "Herstelplan als het nodig is",
     "Berekening en tekening van het funderingsherstel, waarmee de aannemer het "
     "werk kan uitvoeren."),
]

OPLEVERING_NIEUWBOUW = [
    ("lijst", "Funderings- en palenplan",
     "Met wapeningstekeningen, afgestemd op de bodemgesteldheid en het gewicht "
     "van het gebouw."),
    ("schild", "Stabiliteitsvoorzieningen",
     "De elementen die de horizontale krachten opnemen: schijven, kernen of "
     "stalen verbanden."),
    ("document", "Uitvoeringstekeningen",
     "Vloeren, daken, staalconstructies en de details waarmee op de bouwplaats "
     "gewerkt wordt."),
    ("vinkje", "Controle van derden",
     "De uitgangspunten voor prefab leveranciers, en de toetsing van wat zij "
     "uitwerken."),
]

FAQ_VERGUNNING_ALGEMEEN = [
    ("Wat heb ik nodig voor de vergunningaanvraag?",
     "Voor een technische bouwactiviteit vraagt de gemeente een bouwtekening en "
     "een constructieberekening. Bij een verbouwing van enige omvang kan daar meer "
     "bij horen; we geven in de offerte aan welke stukken wij leveren en welke "
     "gegevens wij van u nodig hebben."),
    ("Werkt u samen met mijn architect en aannemer?",
     "Ja, en het liefst vanaf het begin. We werken nauw samen met opdrachtgevers, "
     "architecten, aannemers en andere adviseurs, en kijken verder dan de vraag op "
     "papier."),
    ("Hoe snel kunnen jullie starten?",
     "Dat verschilt per periode en per opdracht. In de offerte vermelden wij "
     "binnen welke termijn wij kunnen starten, welke werkzaamheden wij hebben "
     "ingeschat en welke aanvullende gegevens er nog nodig zijn."),
]

FAQ_WKB = ("Wat betekent de Wet kwaliteitsborging (Wkb) voor mijn project?",
           "Sinds 1 januari 2024 wordt bij nieuwbouw in gevolgklasse 1 - denk aan "
           "grondgebonden woningen en kleinere bedrijfsgebouwen - niet meer door de "
           "gemeente getoetst, maar door een onafhankelijke kwaliteitsborger. Die "
           "controleert tijdens de bouw of er volgens de berekening en de tekeningen "
           "wordt gewerkt. Onze stukken zijn daarop ingericht.")

FAQ_DNR = ("Op welke voorwaarden werken jullie?",
           "Voor al onze opdrachten hanteren wij de DNR 2011, die we standaard "
           "meesturen met de offerte. Die regeling beschrijft de rechtsverhouding "
           "tussen opdrachtgever, architect, ingenieur en adviseur. Voor al onze "
           "advieswerkzaamheden hebben wij een beroepsaansprakelijkheidsverzekering "
           "afgesloten.")


# ---------------------------------------------------------------------------
#  Per familie: waar een dienst niets eigens heeft, geldt dit
# ---------------------------------------------------------------------------
FAMILIE_STANDAARD = {
    'Verbouwing': {
        'wanneer_kop': 'Wanneer is dit iets voor uw project?',
        'wanneer_intro': 'Een ingreep in een bestaand pand raakt bijna altijd de '
                         'draagconstructie. Deze drie situaties komen het meest voor.',
        'stappen_kop': 'Van opname tot uitvoering',
        'stappen_intro': 'Bij een verbouwing werk je in wat er al staat. Daarom begint '
                         'het bij opnemen en eindigt het pas als de constructie er ligt.',
        'stappen': STAPPEN_VERBOUWING,
        'voordelen_kop': 'Wat u eraan heeft',
        'voordelen': VOORDELEN_BESTAAND,
        'oplevering_kop': 'Wat u van ons krijgt',
        'oplevering': OPLEVERING_BESTAAND,
        'faq': FAQ_VERGUNNING_ALGEMEEN + [FAQ_DNR],
    },
    'Fundering': {
        'wanneer_kop': 'Wanneer is funderingsonderzoek aan de orde?',
        'wanneer_intro': 'Funderingsproblemen kondigen zich vaak jaren vooraf aan. '
                         'Deze drie aanleidingen zien we het meest.',
        'stappen_kop': 'Onderzoek in fasen',
        'stappen_intro': 'Onderzoek gaat stap voor stap: elke fase levert informatie op '
                         'waarmee u kunt besluiten of de volgende fase nodig is.',
        'stappen': STAPPEN_FUNDERING,
        'voordelen_kop': 'Wat u eraan heeft',
        'voordelen': VOORDELEN_FUNDERING,
        'oplevering_kop': 'Wat u van ons krijgt',
        'oplevering': OPLEVERING_FUNDERING,
        'faq': [
            ("Moet mijn pand op de schop voor onderzoek?",
             "Nee. Voor de beoordeling graven we een inspectieput, meestal aan de "
             "binnenzijde bij een bouwmuur. Dat is lokaal werk; het pand blijft in "
             "gebruik. De put wordt na het onderzoek weer dichtgemaakt."),
            ("Ik wil mijn pand splitsen in appartementsrechten. Wat is er nodig?",
             "Bij splitsing moet u aantonen dat de fundering nog minimaal 25 jaar "
             "onderhoudsvrij is, kwaliteitsklasse code 2. Daarvoor is een "
             "funderingsonderzoek veelal vereist. Wij voeren dit soort onderzoeken "
             "regelmatig uit, juist voor die reden."),
        ] + FAQ_VERGUNNING_ALGEMEEN[1:] + [FAQ_DNR],
    },
    'Nieuwbouw': {
        'wanneer_kop': 'Wanneer schuiven wij aan?',
        'wanneer_intro': 'Bij nieuwbouw bepaalt de constructie in hoge mate wat er '
                         'architectonisch en financieel kan. Hoe eerder dat op tafel '
                         'ligt, hoe meer keuze er is.',
        'stappen_kop': 'De ontwerpfasen',
        'stappen_intro': 'Het ontwerpproces is opgedeeld in fasen. In elke fase leveren '
                         'wij de constructieve uitgangspunten die de andere partijen '
                         'op dat moment nodig hebben.',
        'stappen': STAPPEN_NIEUWBOUW,
        'voordelen_kop': 'Wat u eraan heeft',
        'voordelen': VOORDELEN_NIEUWBOUW,
        'oplevering_kop': 'Wat u van ons krijgt',
        'oplevering': OPLEVERING_NIEUWBOUW,
        'faq': [FAQ_WKB] + FAQ_VERGUNNING_ALGEMEEN[1:] + [FAQ_DNR],
    },
    None: {   # de losse diensten
        'wanneer_kop': 'Wanneer is dit iets voor u?',
        'wanneer_intro': 'Deze drie situaties komen het meest voor.',
        'stappen_kop': 'Hoe wij werken',
        'stappen_intro': 'Over het algemeen starten wij na een eerste contact met het '
                         'opstellen van een offerte, waarin staat wat wij doen en wat '
                         'wij van u nodig hebben.',
        'stappen': STAPPEN_VERBOUWING,
        'voordelen_kop': 'Wat u eraan heeft',
        'voordelen': VOORDELEN_BESTAAND,
        'oplevering_kop': 'Wat u van ons krijgt',
        'oplevering': OPLEVERING_BESTAAND,
        'faq': FAQ_VERGUNNING_ALGEMEEN + [FAQ_DNR],
    },
}


# ---------------------------------------------------------------------------
#  Per dienst: de situaties, en waar nodig eigen stappen, voordelen of vragen
# ---------------------------------------------------------------------------
PER_DIENST = {
    # ------------------------------------------------------------ Verbouwing
    'verbouwing.html': {
        'situaties': [
            ("Meer ruimte in een bestaand huis",
             "Een muur eruit, een vide erin, een aanbouw achter. Zodra er dragend "
             "werk verdwijnt, moet de belasting ergens anders naartoe."),
            ("Een pand met een nieuwe functie",
             "Van pakhuis naar woningen, van winkel naar kantoor. Een andere functie "
             "betekent andere belastingen op dezelfde vloeren."),
            ("Grootschalige renovatie of restauratie",
             "Balklaagcontrole, sparingen, een extra verdieping, stabiliteits&shy;"
             "voorzieningen: bij een monument komt daar de eis bij dat het pand "
             "zichzelf blijft."),
        ],
    },
    'muurdoorbraak.html': {
        'situaties': [
            ("Keuken en woonkamer bij elkaar",
             "De klassieke doorbraak. Draagt de muur, dan komt er een stalen ligger "
             "in met kolommen of penanten eronder."),
            ("U weet niet of de muur dragend is",
             "Doorloopt van beneden naar boven, dikker dan een scheidingswand, "
             "klinkt massief bij kloppen. Twijfelt u, dan beoordelen wij het ter plaatse."),
            ("U woont in een appartement",
             "Naast de gemeente is dan vaak toestemming van de VvE nodig. Wij leveren "
             "de constructiestukken die daarbij horen."),
        ],
        'faq': [
            ("Hoe weet ik of mijn muur dragend is?",
             "Een draagmuur maakt deel uit van de draagconstructie en verdeelt de "
             "belasting van vloeren, dak en bovenliggende wanden. Hij loopt van "
             "beneden naar boven door, is dikker dan een lichte scheidingswand, draagt "
             "vloerbalken of kanaalplaten en klinkt massief bij kloppen. Op "
             "constructietekeningen staan dragende wanden en opleggingen duidelijk "
             "aangegeven; heeft u die niet, dan beoordelen wij de situatie op locatie "
             "en meten we de bestaande toestand in."),
            ("Wat heb ik nodig om de berekening te laten maken?",
             "De gewenste sparingmaat, dus de opening die gemaakt moet worden voor een "
             "kozijn of deur, en een hoogtedoorsnede van het pand. Tekeningen van het "
             "pand kunnen dat verduidelijken. Zijn die er niet, dan meten wij in."),
            ("Moet het pand tijdens het werk gestut worden?",
             "Ja. De muur boven de opening en de vloeren die daarin rusten moeten "
             "tijdelijk worden opgevangen. Het benodigde stut- en stempelwerk geven "
             "wij op de tekening aan."),
        ] + [FAQ_DNR],
    },
    'vloerbalklagen.html': {
        'situaties': [
            ("De vloer veert of trilt",
             "Een balklaag die net aan voldeed, voldoet niet meer zodra de belasting "
             "of het gebruik verandert."),
            ("De verdieping krijgt een andere functie",
             "Van zolder naar slaapkamer, van kantoor naar archief: meer belasting op "
             "dezelfde balken."),
            ("Er komt een zwaardere afwerking op",
             "Een gietvloer, tegels of een dekvloer wegen mee. Wij rekenen na of de "
             "balklaag dat aankan."),
        ],
    },
    'trapgat.html': {
        'situaties': [
            ("Een trap naar de zolder of het souterrain",
             "Voor een trapgat moeten dragende balken worden doorgezaagd. Dat vraagt "
             "een raveling die de krachten eromheen verdeelt."),
            ("Een schoorsteen of leidingschacht erbij",
             "Elke sparing in een vloer werkt constructief hetzelfde als een trapgat."),
            ("U wilt weten wat er kan",
             "De plek van de opening bepaalt hoeveel er nodig is. Soms kan een trapgat "
             "een meter verder een stuk eenvoudiger."),
        ],
    },
    'vide.html': {
        'situaties': [
            ("Meer licht en hoogte",
             "Een deel van de vloer eruit geeft ruimte onder de nok, en maakt een "
             "zolder tot leefruimte."),
            ("De omliggende balken moeten meer dragen",
             "Rond een vide worden de balken verzwaard of dubbel uitgevoerd, met een "
             "raveelbalk die de afgezaagde balken opvangt."),
            ("Het pand is een monument",
             "Dan weegt mee wat je wel en niet mag wegnemen. We zoeken de ingreep die "
             "constructief werkt en het pand respecteert."),
        ],
    },
    'dakterras.html': {
        'situaties': [
            ("Buitenruimte op een plat dak",
             "Bestaande daken zijn niet gemaakt voor de veranderlijke belasting van "
             "een terras. Meestal moet de dakconstructie mee."),
            ("U weet niet of het dak het houdt",
             "Voor een terras is doorgaans minimaal 250 kg/m&sup2; nodig. Wij rekenen "
             "na wat de bestaande constructie kan."),
            ("Er komt ook een dakopbouw",
             "Dakterras en dakopbouw komen vaak samen. Dan speelt naast het gewicht "
             "ook de windbelasting mee."),
        ],
    },
    'stabiliteitsportalen.html': {
        'situaties': [
            ("Er verdwijnt een stabiliteitswand",
             "Bij een grote doorbraak of uitbouw neemt een stalen portaal de dragende "
             "en stabiliserende functie over."),
            ("Het pand moet de wind zelf opnemen",
             "Bij renovatie moet een pand of pandenblok zelfstandig de windbelasting "
             "kunnen opnemen. Veelal met portalen in de voor- of achtergevel."),
            ("De gevel is monumentaal",
             "Dan plaatsen we de portalen nabij de gevel, zodat de bestaande gevel "
             "gehandhaafd kan blijven."),
        ],
    },
    'dakkapel-dakopbouw.html': {
        'situaties': [
            ("Een dakkapel op een schuin dak",
             "De belasting op de kapconstructie verandert. Niet alleen de dakkapel "
             "zelf, ook het dak eronder moet het aankunnen."),
            ("Een dakopbouw voor een hele verdieping",
             "Groter dan een dakkapel, en vaak hoger dan het hoogste punt van het dak. "
             "Daarmee komt ook de stabiliteit in beeld."),
            ("Een oudere woning",
             "Bij oudere kapconstructies is de reservecapaciteit beperkt. Wij "
             "controleren wat er is en wat er bij moet."),
        ],
    },
    'achteraanbouw.html': {
        'situaties': [
            ("De woning wordt aan de achterkant vergroot",
             "Fundering, muren en dak van de aanbouw, plus de geveldoorbraak naar het "
             "bestaande huis."),
            ("De geveldoorbraak is de zwaarste ingreep",
             "Om de bovenliggende verdiepingen en het dak te dragen komt er een stalen "
             "ligger, op penanten of kolommen."),
            ("U wilt weten of het vergunningsvrij kan",
             "Een vergunningsvrije aanbouw is doorgaans niet dieper dan 4 meter. Check "
             "vooraf via het Omgevingsloket; ook dan is een berekening verstandig."),
        ],
    },
    'stutconstructie.html': {
        'situaties': [
            ("Er moet iets tijdelijk worden opgevangen",
             "Bij een muurdoorbraak, een portaal in de gevel of werk aan de fundering "
             "draagt een stut- of stempelconstructie de last zolang het nodig is."),
            ("Een bouwput moet op zijn plek blijven",
             "Bij kelderplannen of werk onder het grondwater wordt vaak een damwandkuip "
             "toegepast. De stempeling daarvan rekenen en tekenen wij uit."),
            ("Er is een calamiteit",
             "Bij het bezwijken van een geveldraagconstructie adviseren wij over de "
             "noodvoorzieningen die als eerste moeten staan."),
        ],
    },
    # ------------------------------------------------------------- Fundering
    'fundering.html': {
        'situaties': [
            ("Scheuren, klemmende deuren, scheve vloeren",
             "Signalen dat de fundering niet meer doet wat hij moet doen. Of dat de "
             "beweging al jaren achter ons ligt."),
            ("U koopt of splitst een pand",
             "Bij aankoop wilt u weten wat u koopt; bij splitsing moet u aantonen dat "
             "de fundering nog 25 jaar meegaat."),
            ("Er komt een kelder of een verdieping bij",
             "Meer gewicht, of graven onder het pand. Beide vragen eerst een oordeel "
             "over wat de bestaande fundering nog kan."),
        ],
    },
    'funderingsonderzoek.html': {
        'situaties': [
            ("Het casco vertoont gebreken",
             "Scheurvorming, vervorming of verzakking. Onderzoek maakt onderscheid "
             "tussen een pand dat beweegt en een pand dat tot rust is gekomen."),
            ("Splitsing in appartementsrechten",
             "Dan is aantonen dat de fundering nog minimaal 25 jaar onderhoudsvrij is "
             "(code 2) veelal vereist."),
            ("U staat op het punt te kopen",
             "Een funderingsonderzoek voorkomt ernstige schade aan uw toekomstige "
             "pand, en een solide fundering levert een hogere vastgoedprijs op."),
        ],
    },
    'funderingsherstel.html': {
        'situaties': [
            ("Uit het onderzoek komt: herstellen",
             "De bestaande fundering kan zijn functie niet meer volbrengen. Dan komen "
             "er nieuwe palen onder het pand."),
            ("U wilt weten welke variant past",
             "Herstel met een kelder eronder, palen buiten het pand, of palen in de "
             "muurdikte. De bereikbaarheid van de plek weegt zwaar mee."),
            ("Trillingen zijn een probleem",
             "In een gesloten straat met oude panden is trillingsvrij werken vaak een "
             "voorwaarde. Dat bepaalt het paalsysteem."),
        ],
        'faq': [
            ("Welke paalsystemen zijn er?",
             "Inwendig geheide stalen buispalen, getrokken stalen buispalen, "
             "SOBU-palen, trillingsvrije schroefinjectiepalen, VDM-palen, casing "
             "draaipalen en grout injectiepalen. Met al deze systemen hebben wij ruime "
             "ervaring. Welke past, hangt af van de bereikbaarheid van het project, de "
             "gewenste draagkracht en de toelaatbare trillingen; het paaltype kiezen we "
             "in overleg met een geotechnisch adviseur."),
            ("Kan ik in het pand blijven wonen?",
             "Dat hangt af van de gekozen variant en van hoe het werk wordt "
             "gefaseerd. Bij herstel waarbij de begane grondvloer eruit gaat is dat "
             "meestal niet mogelijk. Wij werken een plan uit waar de aannemer het "
             "herstel mee kan uitvoeren; hij kan aangeven wat dat voor het gebruik "
             "betekent."),
            ("Voeren jullie het herstel zelf uit?",
             "Nee. Wij zijn constructeur, niet aannemer. Wij werken het plan uit en "
             "adviseren, de uitvoering doet een funderingsaannemer. Dat betekent ook "
             "dat ons advies niet gekleurd is door wat wij zelf zouden willen bouwen."),
        ] + [FAQ_DNR],
    },
    'funderingsherstel-kelderbak.html': {
        'situaties': [
            ("Er is al een kelder onder het pand",
             "Dan kan de renovatie van de kelderbak gecombineerd worden met het "
             "funderingsherstel: twee ingrepen, &eacute;&eacute;n keer open."),
            ("U wilt ruimte bijmaken",
             "Een kelder levert vierkante meters op waar u ze anders niet krijgt, "
             "midden in de stad."),
            ("De grondwaterstand is hoog",
             "Dan bepaalt het opdrijvend vermogen het ontwerp, en is een droge kelder "
             "de eigenlijke opgave."),
        ],
    },
    'zelfdragende-kelderbak.html': {
        'situaties': [
            ("De bestaande fundering is nog goed",
             "Dan kan er een kelder in het pand worden aangebracht zonder de fundering "
             "te vervangen."),
            ("U wilt snel klaar zijn",
             "Een prefab kelderbak wordt in de fabriek gemaakt en in &eacute;&eacute;n "
             "stuk geplaatst. De bouwtijd op locatie is minimaal."),
            ("Er is ruimte voor een kraan",
             "De bak gaat over de weg en wordt ingehesen. Dat stelt eisen aan de ruimte "
             "rondom de bouwplaats."),
        ],
    },
    'tafelconstructie.html': {
        'situaties': [
            ("De oude fundering kan het niet meer alleen",
             "Een tafelconstructie draagt de belasting tijdelijk af op de nieuwe palen, "
             "terwijl de oude fundering blijft zitten."),
            ("De begane grondvloer gaat eruit",
             "Nieuwe palen en een nieuwe betonvloer, constructief verbonden met "
             "inkassingen in de bestaande dragende muren."),
            ("Het pand moet langzaam overnemen",
             "Na enkele maanden rust de woning geheel op de nieuwe fundering. Dat "
             "geleidelijke overzetten is precies de bedoeling."),
        ],
    },
    # ------------------------------------------------------------- Nieuwbouw
    'nieuwbouw.html': {
        'situaties': [
            ("Het ontwerp staat, de constructie nog niet",
             "Wij volgen het ontwerp van de architect en maken er een draagconstructie "
             "bij die past en uitvoerbaar is."),
            ("U wilt vroeg weten wat het kost",
             "Betrek ons in het voorlopig ontwerp, dan kan de kostendeskundige op "
             "constructieve uitgangspunten begroten in plaats van op aannames."),
            ("Het gebouw combineert functies",
             "Woningen boven een parkeerlaag, kantoor bij een hal. Elke functie brengt "
             "zijn eigen belastingen en overspanningen mee."),
        ],
    },
    'appartementencomplex.html': {
        'situaties': [
            ("Woningen boven een parkeerlaag",
             "Grote overspanningen onderin, kleinere daarboven. Dat vraagt een "
             "doordachte krachtsafdracht."),
            ("Balkons en uitkragingen",
             "Constructief en bouwfysisch de lastigste onderdelen van een complex."),
            ("Prefab waar het kan",
             "Systeemvloeren, trappen en balkons komen van de leverancier. Wij leveren "
             "de uitgangspunten en controleren het resultaat."),
        ],
    },
    'woonhuizen.html': {
        'situaties': [
            ("Een vrijstaand huis naar ontwerp",
             "Wij vertalen de tekeningen van de architect naar concrete cijfers en "
             "bouwtekeningen."),
            ("Grote glaspartijen en open plattegronden",
             "Weinig wanden betekent dat de stabiliteit ergens anders vandaan moet "
             "komen."),
            ("Bouwen op slechte grond",
             "De bodemgesteldheid bepaalt of het op staal kan of op palen moet."),
        ],
    },
    'kantoorgebouwen.html': {
        'situaties': [
            ("Vrij indeelbare vloervelden",
             "Een kantoor moet mee kunnen met zijn gebruikers. Dat vraagt vloeren die "
             "meer kunnen dan het eerste inrichtingsplan."),
            ("Installaties door de constructie",
             "Sparingen, liftputten en schachten leg je vast v&oacute;&oacute;r de "
             "wapening, niet erna."),
            ("Transformatie in plaats van nieuwbouw",
             "Bij hergebruik van een bestaand casco begint het met de vraag wat het "
             "nog kan."),
        ],
    },
    'bedrijfsgebouwen.html': {
        'situaties': [
            ("Een hal met grote overspanningen",
             "Vrije ruimte is de kern van het gebouw. De staalconstructie bepaalt hoe "
             "vrij die ruimte wordt."),
            ("Een kraanbaan of zware installatie",
             "Puntlasten en dynamische belasting vragen een ander ontwerp dan een "
             "gewone vloer."),
            ("Hal plus kantoorgedeelte",
             "Twee bouwdelen met verschillende eisen, in &eacute;&eacute;n constructie."),
        ],
    },
    # -------------------------------------------------------- losse diensten
    'constructieberekening.html': {
        'situaties': [
            ("U vraagt een omgevingsvergunning aan",
             "Dan zijn een bouwtekening en een constructieberekening nodig. Zonder die "
             "stukken komt de aanvraag niet in behandeling."),
            ("U verandert iets aan een dragend deel",
             "Kolommen, vloeren, balken, daken, funderingen of wanden. Ook zonder "
             "vergunningplicht is doorrekenen verstandig."),
            ("De aannemer vraagt om cijfers",
             "Een goede berekening levert naast de toetsing ook een ontwerp dat op de "
             "bouwplaats uitvoerbaar is."),
        ],
        'faq': [
            ("Wanneer heb ik een constructieberekening nodig?",
             "Wanneer u verplicht bent een omgevingsvergunning aan te vragen, heeft u "
             "een constructieberekening en bouwtekeningen nodig. Ook wanneer u geen "
             "vergunning nodig heeft, raden wij een berekening aan zodra u iets "
             "verandert aan bestaande dragende delen: kolommen, vloeren, balken, "
             "daken, funderingen of wanden. Is de constructie niet goed doorgerekend, "
             "dan kan dat grote gevolgen hebben voor de veiligheid van het gebouw."),
            ("Hoe vraag ik een berekening aan?",
             "Via het offerteformulier. Wilt u eerst weten of een berekening in uw "
             "geval nodig is, neem dan contact op; dan kijken we er eerst naar."),
            FAQ_WKB,
        ] + [FAQ_DNR],
    },
    'stabiliteitsberekening.html': {
        'situaties': [
            ("Er verdwijnt een stabiliteitselement",
             "Een muurdoorbraak, trapgat, vide of dakterras haalt stijfheid uit het "
             "pand. Die moet ergens terugkomen."),
            ("Het gebouw wordt hoger",
             "Een dakopbouw vergroot het aangrijppunt van de wind. Daarmee verandert de "
             "hele krachtsafdracht."),
            ("Het is wettelijk verplicht",
             "Voor vergunningsplichtige verbouwingen en nieuwbouw is een "
             "stabiliteitsberekening maatwerk en verplicht."),
        ],
    },
    'schaderapportage.html': {
        'situaties': [
            ("Er is schade en de oorzaak is onduidelijk",
             "Scheuren, verzakkingen of andere gebreken in het casco. Wij inventariseren "
             "en adviseren over vervolgonderzoek en herstel."),
            ("Twee partijen komen er niet uit",
             "Rechtbanken, advocatenkantoren en beheermaatschappijen schakelen ons in "
             "om een geschil onafhankelijk in kaart te brengen."),
            ("U twijfelt aan een advies van derden",
             "Wij voeren een second opinion uit op een berekening of ontwerp van een "
             "andere adviseur, op hoofdlijnen of tot in detail."),
        ],
        'stappen_kop': 'Hoe een onderzoek verloopt',
        'stappen_intro': 'De omvang varieert van een scheur in een gevel tot het '
                         'verzakken van een hele woonwijk. De route is hetzelfde.',
        'stappen': [
            ("Opname van het schadebeeld",
             "We leggen vast wat er te zien is: aard, plaats en omvang van de "
             "gebreken, en wat de omgeving doet.",
             "Met foto's bij elke bevinding."),
            ("Oorzaak bepalen",
             "Schade is een symptoom. We zoeken naar wat het veroorzaakt: de "
             "fundering, de belasting, de bouwwijze of iets in de omgeving.",
             "Zo nodig met aanvullend funderings- of grondonderzoek."),
            ("Rapportage",
             "Een rapport met de bevindingen, de oorzaak en een reparatieadvies. "
             "Feitelijk, en leesbaar voor wie geen constructeur is.",
             "Bij een rechtbankopdracht: antwoord op de gestelde vragen."),
            ("Vervolg",
             "Waar herstel nodig is, kunnen wij de constructieve uitwerking daarvan "
             "op ons nemen.",
             "En als het tot een procedure komt, staan we onze opdrachtgever bij."),
        ],
        'voordelen': [
            ("schild", "Onafhankelijk",
             "Wij hebben geen belang bij de uitkomst. Dat is precies waarom "
             "rechtbanken ons vragen."),
            ("klok", "Jarenlange ervaring met historisch bouwen",
             "Veel schade in oude panden is bekend gedrag. Dat scheelt tijd bij het "
             "zoeken naar de oorzaak."),
            ("document", "Feitelijk en navolgbaar",
             "Een rapport dat standhoudt, ook als er een andere deskundige naar kijkt."),
            ("mensen", "Vaste opdrachtgevers",
             "Woningbouwverenigingen en beheermaatschappijen vragen ons hier "
             "regelmatig voor."),
        ],
        'oplevering': [
            ("document", "Schaderapport",
             "Inventarisatie van de gebreken, de vermoedelijke oorzaak en een advies "
             "over vervolgonderzoek."),
            ("lijst", "Reparatieadvies",
             "Wat er moet gebeuren om het te herstellen, en in welke orde."),
            ("schild", "Deskundigenrapport",
             "Bij een rechtbankopdracht: onafhankelijk antwoord op de vragen die de "
             "rechtbank stelt."),
            ("vinkje", "Second opinion",
             "Een controle op hoofdlijnen of tot in detail van een advies van een "
             "andere partij."),
        ],
        'faq': [
            ("Kunnen jullie als onafhankelijk deskundige optreden?",
             "Ja. Door onze jarenlange ervaring met bouwconstructies, onze "
             "onafhankelijke positie en onze goede naam worden wij door rechtbanken "
             "regelmatig ingeschakeld om een deskundigenrapport op te stellen. Wij "
             "onderzoeken dan op onafhankelijke basis het geschil tussen twee of meer "
             "partijen en rapporteren over de vragen die de rechtbank opstelt."),
            ("Doen jullie ook een second opinion op andermans berekening?",
             "Ja. Afhankelijk van uw wensen voeren wij die controle op hoofdlijnen of "
             "op detailniveau uit. Aannemers vragen ons ook om voor bestaande "
             "bouwplannen alternatieven te beoordelen en eventueel uit te werken, "
             "waarbij het economische aspect meestal een rol speelt zonder dat de "
             "kwaliteit eronder mag lijden."),
            ("Wij zijn zelf uw constructeur en er ontstaat een geschil. Wat dan?",
             "Zijn wij als constructeur bij een project betrokken, dan staan wij onze "
             "opdrachtgever graag terzijde als die op de een of andere manier in een "
             "juridische kwestie betrokken raakt."),
        ] + [FAQ_DNR],
    },
    'certificaat-funderingsherstel.html': {
        'situaties': [
            ("U wilt zekerheid over de kwaliteit",
             "De certificatieregeling waarborgt de kwaliteit van advies en "
             "herstelwerkzaamheden aan funderingen."),
            ("U werkt met meerdere partijen",
             "Certificering betekent dat elke stap, van beoordeling tot uitvoering, "
             "door een onafhankelijke partij is gecontroleerd."),
            ("U zoekt achtergrond bij de richtlijn",
             "Duyts was in 2013 actief in de begeleidingscommissie die de "
             "Beoordelingsrichtlijn heeft opgesteld."),
        ],
        'stappen_kop': 'Waar de regeling over gaat',
        'stappen_intro': 'De regeling dekt de hele keten van funderingsherstel, van het '
                         'eerste oordeel tot de oplevering.',
        'stappen': [
            ("Onderzoek, beoordeling en advies",
             "Vaststellen wat de staat van de fundering is en wat er nodig is.", ""),
            ("Ontwerp en engineering",
             "Het herstel uitwerken tot een plan waarmee gebouwd kan worden.", ""),
            ("Procesbegeleiding",
             "Het traject van aanbesteding tot uitvoering begeleiden.", ""),
            ("Uitvoering van funderingsherstel",
             "Het werk zelf, door een uitvoerende partij.", ""),
        ],
    },
}


def verhaal(bestand, ouder):
    """De verhaalvelden voor één dienstpagina: eigen invulling waar die er is,
       anders die van de familie."""
    basis = dict(FAMILIE_STANDAARD.get(ouder, FAMILIE_STANDAARD[None]))
    basis.update(PER_DIENST.get(bestand, {}))
    return basis
