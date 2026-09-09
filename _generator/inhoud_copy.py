# -*- coding: utf-8 -*-
"""Herschreven copy: dezelfde feiten als www.duyts.nl, anders geformuleerd.

De bronteksten in `duyts/` blijven staan zoals ze zijn; dat is de feitenbasis en
de herkomst. Dit bestand zet daar de webcopy tegenover: korter, actiever, met de
reden vooraan en de techniek als onderbouwing erachter.

REGEL BIJ ELKE REGEL HIERONDER
  Elk feit moet in de bron staan. Geen nieuwe diensten, mogelijkheden,
  certificaten, cijfers, doorlooptijden, garanties of opdrachtgevers. Waar een
  formulering een voordeel benoemt, staat dat voordeel al in de brontekst of in
  de meta description die Duyts zelf voor die pagina schreef.

WAT HIER IS VERANDERD TEN OPZICHTE VAN DE BRON
  - Openingszinnen. De bron begint vaak met een definitie in de lijdende vorm
    ("Bij een restauratie- en/of renovatieproject is een grote variëteit aan
    constructieve werkzaamheden mogelijk"). Dat is nu een zin die zegt wat de
    bezoeker eraan heeft.
  - Koppen. Kale zelfstandige naamwoorden zijn vervangen door koppen die iets
    zeggen, behalve de H1: die blijft de naam van de dienst, omdat dat het woord
    is waarop mensen zoeken en waarmee het in het menu staat. Het voordeel staat
    direct daaronder en in de eerste H2.
  - Wij-vorm. "Wij beschikken over" is waar het kon "u krijgt" of "dat betekent".
  - Lengte. Alinea's van vijf regels zijn er twee geworden; herhaling eruit.

Een pagina zonder regel hieronder valt terug op de brontekst. Dat is expliciet:
zo is aan dit bestand te zien welke pagina's herschreven copy hebben en welke
nog letterlijk de bron volgen.
"""

# ---------------------------------------------------------------------------
#  Homepage
# ---------------------------------------------------------------------------
# De bron had als hero-kop "Wij kijken verder dan vandaag". Als merkregel is die
# goed, als H1 niet: je leest er niet in wat Duyts doet. De regel is daarom
# verplaatst naar de sectie over de werkwijze, waar hij op zijn plek staat, en de
# H1 zegt nu wat het bureau doet en voor welk werk.
HOME = {
    'eyebrow': 'Constructief advies sinds 1981',
    'h1': 'Constructief advies voor verbouwing, fundering en nieuwbouw',
    # Eén korte alinea, en met opzet kort: de hero stond op 58 woorden in twee
    # alinea's, en daardoor vielen de twee knoppen eronder op de meeste
    # telefoons buiten beeld (222 px op een iPhone SE, 314 px liggend). De
    # opdrachtgeverslijst die hier stond is naar het statement hieronder
    # verhuisd; hij stond nergens anders op de site, dus weglaten zou hem
    # helemaal doen verdwijnen.
    'lead': [
        'Van een muurdoorbraak in een woning tot de volledige draagconstructie van '
        'een appartementencomplex. Vanuit Amsterdam rekenen wij aan constructies die '
        'blijven staan.',
    ],
    'cta_primair': ('Vraag een offerte aan', 'offerte.html'),
    'cta_secundair': ('Bekijk de projecten', 'projecten.html'),

    # Sectie direct onder de logoband: waar je terecht kunt en waarom.
    'statement_kop': 'Van monumentrestauratie tot volledige nieuwbouw',
    'statement': [
        'Restauraties van monumentale panden, verbouwingen van woningen en kantoren, '
        'kleinschalige ingrepen en volledige nieuwbouw: voor al die projecten maken wij '
        'de berekeningen en tekeningen van de draagconstructie.',
        'Een belangrijk deel van onze expertise ligt bij funderingsonderzoek en '
        'funderingsherstel, met name bij oudere Amsterdamse panden. We kennen de stad, '
        'haar bodem en haar gebouwen, en de problemen die daarbij horen.',
            'Onze opdrachtgevers zijn particulieren, VvE&rsquo;s, architecten, aannemers, '
        'projectontwikkelaars en woningbouwverenigingen. Wat hen verbindt, is de behoefte '
        'aan een constructieve partner die meedenkt en overzicht houdt.',
],
    'statement_cta': ('Bekijk alle werkzaamheden', 'verbouwing.html'),

    'werkzaamheden_kop': 'Waar wij aan rekenen',
    'werkzaamheden_lead': 'Drie hoofdrichtingen, met daaronder de ingrepen waarvoor '
                          'opdrachtgevers ons het meest vragen.',
    'losse_kop': 'Ook los aan te vragen',
    'losse_lead': 'Een losse berekening, een schaderapport of een second opinion op het '
                  'advies van een andere partij.',

    'projecten_kop': 'Waar we aan hebben gerekend',
    'projecten_cta': ('Alle projecten', 'projecten.html'),

    'over_kop': 'Klein genoeg om persoonlijk te blijven',
    'over': [
        'Vanuit ons kantoor aan de Van Slingelandtstraat in Amsterdam werken circa 25 '
        'tekenaars, constructeurs en specialisten aan projecten door het hele land. '
        'Groot genoeg voor complexe vraagstukken, klein genoeg om persoonlijk te blijven.',
        'U schakelt direct met de mensen die aan uw project rekenen. Geen lagen, geen '
        'omwegen. Meer dan driekwart van onze medewerkers werkt hier tien jaar of langer, '
        'dus de ervaring blijft in huis.',
    ],
    'over_cta': ('Over ons', 'over-ons.html'),

    'slot_kop': 'Overleg over uw project',
    'slot': 'Vertel kort wat er verbouwd, hersteld of gebouwd wordt. Wij brengen zo '
            'spoedig mogelijk een offerte uit, of nemen eerst contact op als we nog '
            'iets moeten weten.',
}


# ---------------------------------------------------------------------------
#  Diensten
# ---------------------------------------------------------------------------
# Per dienst:
#   lead        de eerste alinea's op de pagina: waarom dit relevant is
#   wanneer_kop de eerste H2, die iets zegt in plaats van "Wanneer is dit iets voor u?"
#   uitleg_kop  de kop boven de technische uitleg uit de bron
#   uitleg      alleen bij de drie hoofddiensten: de brontekst herschreven
#   cta         (label, bestand) voor de knop in het statement
DIENST = {
    # ------------------------------------------------------------ hoofddiensten
    'verbouwing.html': {
        'lead': [
            'Een muur eruit, een vide erin, een verdieping erop: zodra u iets weghaalt '
            'of toevoegt, verandert de weg die de belasting door het pand aflegt. Wij '
            'rekenen die nieuwe weg door en leggen hem vast in een berekening en een '
            'tekening waarmee uw aannemer kan bouwen en de gemeente kan toetsen.',
        ],
        'wanneer_kop': 'Waarvoor opdrachtgevers ons bellen',
        'uitleg_kop': 'Wat er bij een verbouwing constructief kan spelen',
        'uitleg': [
            'Bij een woning waarbij de muur tussen woonkamer en keuken wordt '
            'doorgebroken, is naast de bouwkundige tekening een constructieadvies nodig '
            'voor de draagconstructie die de muur vervangt.',
            'Bij een grootschalige renovatie of een verbouwing van woningen, woongebouwen '
            'en kantoorpanden komen er meer draagconstructies bij. Denk aan een '
            'balklaagcontrole, sparingen in vloeren, een extra verdieping, een dakopbouw '
            'of een tussenvloer, en aan stabiliteitsvoorzieningen en uitbouwen.',
        ],
        'lijst_kop': 'De ingrepen waarvoor wij rekenen',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'fundering.html': {
        'lead': [
            'De fundering draagt het hele pand naar de ondergrond. Bij nieuwbouw '
            'ontwerpen wij die op basis van de dragende grondlagen en het gewicht van '
            'het gebouw; bij een bestaand pand begint het met de vraag wat de fundering '
            'die er ligt nog kan.',
        ],
        'wanneer_kop': 'Wanneer een fundering aandacht vraagt',
        'uitleg_kop': 'Van onderzoek naar herstel',
        'uitleg': [
            'Een fundering brengt de belasting van het gebouw naar de ondergrond. Dat '
            'kan een fundering &ldquo;op staal&rdquo; zijn, of een fundering op palen.',
            'Bij renovatie gelden meer randvoorwaarden. Een funderingsonderzoek stelt de '
            'kwaliteit van de bestaande fundering vast. Daarna bepalen we de '
            'restcapaciteit en of de fundering aangepast of vervangen moet worden.',
            'Bij de keuze van het paalsysteem weegt de bereikbaarheid van het project '
            'zwaar mee, naast de gewenste draagkracht en de toelaatbare trillingen. Het '
            'paaltype kiezen we in overleg met een geotechnisch adviseur.',
            'Zit er een kelder onder het pand, dan kan de renovatie van de kelderbak '
            'gecombineerd worden met het funderingsherstel: twee ingrepen, één keer open.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'nieuwbouw.html': {
        'lead': [
            'Bij nieuwbouw volgen wij het ontwerp van de architect en maken daar een '
            'draagconstructie bij die past en uitvoerbaar is. Worden wij vroeg in het '
            'ontwerpproces betrokken, dan is er nog ruimte om te kiezen: samen met de '
            'opdrachtgever, de architect en de andere adviseurs komen we tot een goed '
            'doordacht, duurzaam en economisch ontwerp.',
        ],
        'wanneer_kop': 'Voor welke gebouwen wij rekenen',
        'uitleg_kop': 'Wat er in elk nieuwbouwproject terugkomt',
        'uitleg': [
            'Woonhuizen, appartementencomplexen, hotels, kantoorgebouwen, scholen en '
            'bedrijfsgebouwen: elke categorie heeft zijn eigen specificaties. Een '
            'funderingsplan, stabiliteitsvoorzieningen, vloeren, daken en gevels komen '
            'bij alle categorieën voor.',
        ],
        'lijst_kop': 'Categorieën waarvoor wij ontwerpen',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },

    # ------------------------------------------------------------- verbouwing
    'muurdoorbraak.html': {
        'lead': ['Een draagmuur weghalen kan, maar de belasting van vloeren, dak en '
                 'bovenliggende wanden moet ergens anders naartoe. Wij bepalen welke '
                 'voorziening daarvoor nodig is en hoe het pand tijdens het werk wordt '
                 'opgevangen.'],
        'wanneer_kop': 'Draagt uw muur, of niet?',
        'uitleg_kop': 'Een draagmuur herkennen en vervangen',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'vloerbalklagen.html': {
        'lead': ['Verandert de belasting op een vloer of de functie van een verdieping, '
                 'dan moet de bestaande balklaag opnieuw worden nagerekend. Wij '
                 'controleren wat de balken aankunnen en berekenen de verstijving die '
                 'doorbuiging vermindert, trillingen wegneemt en de draagkracht verhoogt.'],
        'wanneer_kop': 'Wanneer een balklaag tekortkomt',
        'uitleg_kop': 'Hoe een balklaag wordt versterkt',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'trapgat.html': {
        'lead': ['Voor een trapgat moeten dragende balken worden doorgezaagd. Dat vraagt '
                 'een raveling die de krachten rond de opening verdeelt, zodat de balken '
                 'hun draagkracht houden. Wij rekenen uit hoe de vloerbalken worden '
                 'opgevangen en waar versteviging nodig is.'],
        'wanneer_kop': 'Een opening in een bestaande vloer',
        'uitleg_kop': 'De raveling rond het trapgat',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'vide.html': {
        'lead': ['Een vide levert licht en hoogte op en maakt van een weinig gebruikte '
                 'zolder een leefruimte. Omdat het de draagconstructie aantast, is een '
                 'officiële constructieberekening nodig en in veel gevallen een '
                 'omgevingsvergunning.'],
        'wanneer_kop': 'Meer licht en hoogte, veilig uitgevoerd',
        'uitleg_kop': 'Hoe een vide constructief wordt opgevangen',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'dakterras.html': {
        'lead': ['Bestaande daken zijn zelden gemaakt voor de belasting van een terras; '
                 'de regelgeving voor veranderlijke belasting is daarbij bepalend. Wij '
                 'rekenen na wat uw dakconstructie aankan en ontwerpen de aanpassing die '
                 'nodig is.'],
        'wanneer_kop': 'Kan uw dak een terras dragen?',
        'uitleg_kop': 'De constructie onder het terras',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'stabiliteitsportalen.html': {
        'lead': ['Een pand of pandenblok moet de windbelasting zelfstandig kunnen '
                 'opnemen. Verdwijnt er een stabiliteitsmuur, dan neemt een stalen '
                 'portaal die functie over. Bij monumentale gevels plaatsen we het '
                 'portaal nabij de gevel, zodat de bestaande gevel gehandhaafd blijft.'],
        'wanneer_kop': 'Stijfheid terugbrengen in een bestaand pand',
        'uitleg_kop': 'Wat een stabiliteitsportaal doet',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'dakkapel-dakopbouw.html': {
        'lead': ['Een dakkapel of dakopbouw verandert de belasting op de kap- en '
                 'dakconstructie, en door de windbelasting ook de stabiliteit van het '
                 'pand. Wij controleren de capaciteit van de bestaande constructie en '
                 'werken de aanvullende dragende elementen uit.'],
        'wanneer_kop': 'Uitbreiden op het dak',
        'uitleg_kop': 'Dakkapel of dakopbouw: wat er verandert',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'achteraanbouw.html': {
        'lead': ['Een uitbouw achter de achtergevel vergroot de woning. De zwaarste '
                 'ingreep is de geveldoorbraak: om de bovenliggende verdiepingen en het '
                 'dak te dragen komt daar een stalen ligger op penanten of kolommen. Wij '
                 'werken de fundering, de gevels, de puien en de daken uit.'],
        'wanneer_kop': 'De woning naar achteren uitbreiden',
        'uitleg_kop': 'Waaruit een achteraanbouw bestaat',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'stutconstructie.html': {
        'lead': ['Bouwen in een bestaand pand betekent dat er van alles tijdelijk moet '
                 'worden opgevangen: de muur boven een doorbraak, een gevel boven een '
                 'portaal, of de wanden van een bouwput. Wij rekenen en tekenen die '
                 'tijdelijke constructie, en adviseren bij een calamiteit over de '
                 'noodvoorzieningen.'],
        'wanneer_kop': 'Tijdelijk opvangen wat er al staat',
        'uitleg_kop': 'Waar een stut- of stempelconstructie wordt toegepast',
        'cta': ('Bespreek uw project', 'contact.html'),
    },

    # -------------------------------------------------------------- fundering
    'funderingsonderzoek.html': {
        'lead': ['Een funderingsonderzoek voorkomt ernstige schade aan uw pand en geeft '
                 'zekerheid bij aankoop of splitsing. Wij brengen de kwaliteit van de '
                 'fundering nauwgezet in kaart en geven het funderingslabel af.',
                 'Onze inspecteurs kennen de Amsterdamse bouwstijl en de bodemgesteldheid, '
                 'en dat is precies wat het funderingsrisico bepaalt.'],
        'wanneer_kop': 'Wanneer funderingsonderzoek aan de orde is',
        'uitleg_kop': 'Hoe wij een fundering beoordelen',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'funderingsherstel.html': {
        'lead': ['Scheuren, een scheve vloer of klemmende deuren kunnen erop wijzen dat '
                 'de fundering niet meer voldoet. Bij herstel komen er nieuwe '
                 'funderingspalen onder het pand, die via een betonconstructie met '
                 'inkassingen in de bouwmuren het gewicht overnemen.',
                 'Wij werken het plan uit waarmee de aannemer het herstel kan uitvoeren. '
                 'Zelf voeren we geen herstel uit, dus ons advies is niet gekleurd door '
                 'wat wij zouden willen bouwen.'],
        'wanneer_kop': 'Signalen dat de fundering het niet meer houdt',
        'uitleg_kop': 'Varianten en paalsystemen',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'funderingsherstel-kelderbak.html': {
        'lead': ['Is er een kelder aanwezig of gewenst, dan kunnen de herstelplannen '
                 'gecombineerd worden met een kelderbak. U krijgt er ondergrondse ruimte '
                 'bij en de fundering wordt in dezelfde ingreep aangepakt.',
                 'De grondwaterstand bepaalt het ontwerp: die stelt het opdrijvend '
                 'vermogen vast en beslist of de kelder droog blijft.'],
        'wanneer_kop': 'Herstellen en ruimte maken in één ingreep',
        'uitleg_kop': 'Hoe de belasting wordt afgedragen',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'zelfdragende-kelderbak.html': {
        'lead': ['Verkeert de bestaande fundering nog in goede staat, dan kan er een '
                 'kelder in het pand worden aangebracht zonder die fundering te '
                 'vervangen. Een prefab kelderbak wordt in de fabriek gemaakt en als één '
                 'stuk geplaatst: direct waterdicht, zonder naden en met minimale '
                 'bouwtijd op locatie.'],
        'wanneer_kop': 'Ruimte bijmaken onder een goed pand',
        'uitleg_kop': 'Wat een zelfdragende kelderbak is',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'tafelconstructie.html': {
        'lead': ['Kan de oorspronkelijke fundering haar functie niet meer volledig '
                 'volbrengen, dan adviseren wij een tafelconstructie. Die hulpconstructie '
                 'draagt de belasting tijdelijk af op de nieuwe palen, waarna de woning '
                 'in enkele maanden geleidelijk op de nieuwe fundering komt te rusten.'],
        'wanneer_kop': 'Het pand overzetten op nieuwe palen',
        'uitleg_kop': 'Hoe een tafelconstructie werkt',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },

    # -------------------------------------------------------------- nieuwbouw
    'appartementencomplex.html': {
        'lead': ['Bij een appartementencomplex vertalen wij de eisen van de '
                 'opdrachtgever naar het ontwerp van de draagconstructie: fundering, '
                 'vloeren, wanden en balkons, met constructieve veiligheid en stabiliteit '
                 'als uitgangspunt.'],
        'wanneer_kop': 'Wat een complex constructief vraagt',
        'uitleg_kop': 'Onze kerntaken per ontwerpfase',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'woonhuizen.html': {
        'lead': ['Wij vertalen de tekeningen van de architect naar concrete cijfers en '
                 'bouwtekeningen, zodat het huis veilig, stevig en volgens de wet wordt '
                 'gebouwd. Als constructiebedrijf zijn wij verantwoordelijk voor de '
                 'draagconstructie en de stabiliteit van de woning.'],
        'wanneer_kop': 'Van architectontwerp naar bouwbare constructie',
        'uitleg_kop': 'Wat wij voor een woonhuis uitwerken',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'kantoorgebouwen.html': {
        'lead': ['Bij een kantoorgebouw verwerken wij de eisen van de opdrachtgever in '
                 'het ontwerp van de draagconstructie. In elke fase leveren wij de '
                 'constructieve uitgangspunten voor de architect en de kostendeskundige, '
                 'en uiteindelijk de uitvoeringstekeningen voor de aannemer.'],
        'wanneer_kop': 'Wat een kantoor constructief vraagt',
        'uitleg_kop': 'Onze kerntaken bij een kantoorgebouw',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'bedrijfsgebouwen.html': {
        'lead': ['Een bedrijfsgebouw kan een hal voor opslag zijn, of een combinatie met '
                 'bijvoorbeeld een kantoorgedeelte. Wij werken de constructieve '
                 'onderdelen uit: van het palenplan en het funderingsplan met '
                 'wapeningstekeningen tot de plantekening van de staalconstructie, '
                 'ankerplannen en kraanbanen.'],
        'wanneer_kop': 'Vrije ruimte, zware belasting',
        'uitleg_kop': 'Onze kerntaken bij een bedrijfsgebouw',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },

    # ---------------------------------------------------------- losse diensten
    'constructieberekening.html': {
        'lead': ['Vraagt u een omgevingsvergunning aan, dan heeft u een '
                 'constructieberekening en bouwtekeningen nodig. Die berekening laat zien '
                 'dat alle dragende delen de belasting aankunnen: is de constructie niet '
                 'goed doorgerekend, dan heeft dat grote gevolgen voor de veiligheid van '
                 'het gebouw.',
                 'Een goede constructeur levert naast de berekening een efficiënt ontwerp '
                 'dat de aannemer in de praktijk goed kan uitvoeren.'],
        'wanneer_kop': 'Wanneer u een berekening nodig heeft',
        'uitleg_kop': 'Wat er wordt doorgerekend',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'stabiliteitsberekening.html': {
        'lead': ['Een stabiliteitsberekening toetst de weerstand van een gebouw tegen '
                 'horizontale krachten: wind, stootbelastingen of aardbevingen. Die '
                 'toetsing zorgt ervoor dat het bouwwerk niet omvalt, schuin wegzakt of '
                 'bezwijkt door knik of torsie.',
                 'Voor vergunningsplichtige verbouwingen en nieuwbouw is de berekening '
                 'wettelijk verplicht. Wij leveren een uitgebreid rapport, opgesteld door '
                 'een van onze gecertificeerde constructeurs.'],
        'wanneer_kop': 'Wanneer stabiliteit een vraag wordt',
        'uitleg_kop': 'Wat de berekening toetst',
        'cta': ('Vraag een offerte aan', 'offerte.html'),
    },
    'schaderapportage.html': {
        'lead': ['Scheuren, verzakkingen of andere gebreken in het casco: wij '
                 'inventariseren de schade, zoeken de oorzaak en stellen een '
                 'reparatieadvies op. De omvang varieert van een scheur in één gevel tot '
                 'het verzakken van een hele woonwijk.',
                 'Door onze jarenlange ervaring met historisch bouwen, onze '
                 'onafhankelijke positie en onze goede naam schakelen ook rechtbanken, '
                 'advocatenkantoren en beheermaatschappijen ons in.'],
        'wanneer_kop': 'Schade, een geschil of twijfel over een advies',
        'uitleg_kop': 'Wat wij onderzoeken en rapporteren',
        'cta': ('Bespreek uw situatie', 'contact.html'),
    },
    'certificaat-funderingsherstel.html': {
        'lead': ['De certificatieregeling voor funderingsherstel waarborgt de kwaliteit '
                 'van advies en herstelwerkzaamheden. Voor een opdrachtgever betekent dat '
                 'zekerheid: elke stap, van beoordeling tot uitvoering, is door een '
                 'onafhankelijke partij gecontroleerd en gevalideerd.',
                 'Duyts Bouwconstructies was in 2013 actief in de begeleidingscommissie '
                 'BRL Funderingsherstel, die de Nationale Beoordelingsrichtlijn voor het '
                 'KOMO Procescertificaat heeft opgesteld.'],
        'wanneer_kop': 'Waarom certificering uitmaakt',
        'uitleg_kop': 'Waar de regeling over gaat',
        'cta': ('Bespreek uw project', 'contact.html'),
    },
}


# ---------------------------------------------------------------------------
#  Projecten
# ---------------------------------------------------------------------------
# De projectteksten van de bron beginnen bijna allemaal met dezelfde constructie:
# "Duyts Bouwconstructies heeft voor dit project de constructieve adviezen
# uitgewerkt". Feitelijk klopt dat, maar als openingsregel op zesendertig
# pagina's zegt het niets. Deze koppen en kaders zetten het project vooraan; de
# brontekst zelf blijft er onder staan.
PROJECT = {
    'lead_kop': None,                       # de regel van de bron blijft de lead
    'project_kop': 'De opgave',
    'werk_kop': 'Wat wij hebben uitgewerkt',
    'werk_lead': 'De onderdelen hieronder komen uit de projectomschrijving. Per onderdeel '
                 'staat waar u leest hoe wij dat aanpakken.',
    'gegevens_kop': 'Projectgegevens',
    'slot_kop': 'Een vergelijkbaar project?',
    'slot': 'Vertel kort wat er speelt. Wij kijken of we hetzelfde voor u kunnen doen.',
    'cta': ('Bespreek uw project', 'contact.html'),
}

PROJECTEN_OVERZICHT = {
    'h1': 'Waar we aan hebben gerekend',
    'kop': 'Van monumentrestauratie tot volledige nieuwbouw',
    'lead': 'Restauraties, verbouwingen, funderingsherstel en nieuwbouw, door het hele '
            'land. Een project staat soms onder meer dan één categorie, omdat er in '
            'hetzelfde pand aan meerdere dingen tegelijk is gerekend.',
    'slot_kop': 'Een vergelijkbaar project?',
}


# ---------------------------------------------------------------------------
#  Over ons
# ---------------------------------------------------------------------------
BEDRIJF = {
    'over-ons.html': {
        'h1': 'Sinds 1981 stevig gebouwd',
        'lead': [
            'Duyts Bouwconstructies is sinds 1981 gevestigd in Amsterdam. Vanuit ons '
            'kantoor op het Westerkwartier werken circa 25 tekenaars, constructeurs en '
            'specialisten aan een brede variatie aan projecten.',
            'Door de jaren heen dachten we mee aan nieuwbouw, verbouwingen, renovaties en '
            'restauraties van monumenten. Die staat van dienst geeft ons het overzicht en '
            'het vertrouwen om ook complexe vraagstukken helder en beheersbaar te maken.',
        ],
        'slot_kop': 'Kennismaken?',
    },
    'werkwijze.html': {
        'lead': [
            'Elke opdracht begint bij een offerte. Daarin staat welke werkzaamheden wij '
            'hebben ingeschat, of dat een vaste prijs of een regie-opdracht is, binnen '
            'welke termijn wij kunnen starten en welke gegevens wij nog van u nodig '
            'hebben. Zo weet u vooraf waar u aan toe bent.',
        ],
        'slot_kop': 'Een offerte op uw situatie afgestemd',
    },
    'het-team.html': {
        'lead': [
            'Ons team bestaat uit circa 25 mensen: mbo&rsquo;ers, hbo&rsquo;ers en '
            'TU&rsquo;ers, in functies van tekenaar en modelleur tot constructeur, '
            'rapporteur en projectleider.',
        ],
        'slot_kop': 'Interesse om bij ons te komen werken?',
    },
    'historie.html': {
        'lead': [
            'Duyts Bouwconstructies is in 1981 opgericht door Jan Duyts, onder de naam '
            'JH Duyts Adviesbureau voor Bouwconstructies. Hieronder de stappen van toen '
            'naar nu.',
        ],
        'slot_kop': 'Overleg over uw project',
    },
    'registerconstructeur.html': {
        'lead': [
            'Onze registerconstructeur stelt eigen berekeningen op, geeft adviezen, '
            'stuurt collega&rsquo;s aan en bewaakt de interne kwaliteitscontrole. Voor u '
            'betekent dat dat er binnen ons bureau iemand op de kwaliteit van het werk '
            'toeziet.',
        ],
        'slot_kop': 'Overleg over uw project',
    },
    'vacatures.html': {
        'h1': 'Werken bij Duyts',
        'lead': [
            'Wat Duyts Bouwconstructies onderscheidt, is de combinatie van jarenlange '
            'ervaring, technische diepgang en persoonlijke betrokkenheid bij elk project. '
            'Door onze omvang zijn de lijnen kort en de samenwerking intensief.',
        ],
        'slot_kop': 'Ook een open sollicitatie is welkom',
    },
}


# ---------------------------------------------------------------------------
#  Contact en offerte
# ---------------------------------------------------------------------------
CONTACT = {
    'h1': 'Neem contact op',
    'lead': [
        'Heeft u al informatie over een specifiek project? Vraag dan direct een offerte '
        'aan; met een opdrachtomschrijving en de beschikbare stukken kunnen wij de '
        'offerte zo goed mogelijk op uw situatie afstemmen.',
        'Weet u nog niet precies wat u nodig heeft? Bel of mail ons dan gerust. Dan '
        'kijken we eerst samen waar het om vraagt.',
    ],
    'formulier_kop': 'Stuur ons een bericht',
    'formulier_lead': 'Vertel kort waar het over gaat. Wij nemen zo spoedig mogelijk '
                      'contact met u op.',
}

OFFERTE = {
    'h1': 'Offerte aanvragen',
    'lead': [
        'Vraag hieronder vrijblijvend een offerte aan. Geef een zo uitgebreid mogelijke '
        'opdrachtomschrijving en stuur de beschikbare stukken mee, dan kunnen wij de '
        'offerte goed op uw situatie afstemmen.',
    ],
    'formulier_kop': 'Vertel ons over uw project',
    'formulier_lead': 'Na ontvangst brengen wij zo spoedig mogelijk de offerte uit, of '
                      'nemen eerst contact met u op voor de aanvullende informatie.',
}


# De bron gebruikt bij één project de uitdrukking "van A tot Z". Dat is precies
# de lege formulering die we elders vermijden, en het feit erachter staat er ook
# gewoon: Duyts was hoofdconstructeur en heeft het hele traject begeleid.
PROJECT_HERSCHRIJF = {
    'Duyts heeft dit project van A tot Z constructief begeleid.':
        'Als hoofdconstructeur begeleidde Duyts het project van het eerste ontwerp '
        'tot de uitvoering.',
}


def dienst(bestand):
    """De herschreven copy voor een dienstpagina, of een leeg blok."""
    return DIENST.get(bestand, {})
