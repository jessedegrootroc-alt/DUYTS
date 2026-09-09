# -*- coding: utf-8 -*-
"""De inhoud van de site: alles komt uit de gemirrorde Duyts-website.

De teksten staan niet in dit bestand maar in `duyts/`, de contentexport van
www.duyts.nl. Hier staat wat er met welke tekst gebeurt: welke pagina's er zijn,
welke dienst onder welke hoofddienst hangt, welke foto erbij hoort en welk kopje
een vraag in de veelgestelde vragen wordt.

Zo hoeft een tekstwijziging maar op één plek: in de export. En een nieuw project
of een nieuwe dienst is één regel in de tabellen hieronder.

Er wordt niets bijverzonnen. Ontbreekt iets in de bron, dan staat er
NIET_GEVONDEN en dat rendert als een zichtbare markering, zodat het niet per
ongeluk zo live gaat.
"""
import json
import pathlib
import re

DATA = pathlib.Path(__file__).resolve().parent / 'duyts'
NIET_GEVONDEN = '[CONTENT NODIG]'
BRON_MARKER = '[CONTENT NIET GEVONDEN]'      # zo heet het in de export


def _laad(naam):
    return json.loads((DATA / naam).read_text(encoding='utf-8'))


_services = {s['slug']: s for s in _laad('services.json')}
_projecten = _laad('projects.json')
_bedrijf = _laad('company.json')
_contact = _laad('contact.json')
_seo = {s['sourceUrl']: s for s in _laad('seo-metadata.json')}


def _schoon(t):
    """Bronmarkering omzetten naar onze eigen markering."""
    if not t or t == BRON_MARKER:
        return NIET_GEVONDEN
    return t


def splits_lang(alineas, maximum=55):
    """Een alinea van meer dan `maximum` woorden opknippen op zinsgrens.

       De woorden veranderen niet; er komt alleen een alineagrens waar toch al
       een punt stond. De bronsite heeft alinea's van zeventig woorden en die
       lezen op een scherm als een muur."""
    uit = []
    for a in alineas:
        if len(a.split()) <= maximum:
            uit.append(a)
            continue
        zinnen = re.split(r'(?<=[.!?])\s+', a.strip())
        blok = []
        for zin in zinnen:
            blok.append(zin)
            if sum(len(z.split()) for z in blok) >= maximum * 0.6:
                uit.append(' '.join(blok))
                blok = []
        if blok:
            if uit and len(' '.join(blok).split()) < 12:
                uit[-1] += ' ' + ' '.join(blok)
            else:
                uit.append(' '.join(blok))
    return uit


def _tekens(t):
    """Losse aanhalings- en deeltekens netjes maken; de tekst zelf blijft."""
    if not t:
        return t
    t = (t.replace('’', '&rsquo;').replace('‘', '&lsquo;')
          .replace('“', '&ldquo;').replace('”', '&rdquo;')
          .replace('–', '&ndash;').replace('—', '&mdash;')
          .replace('é', '&eacute;').replace('ë', '&euml;').replace('ï', '&iuml;')
          .replace('ö', '&ouml;').replace('ü', '&uuml;').replace('è', '&egrave;')
          .replace('á', '&aacute;').replace('í', '&iacute;').replace('ó', '&oacute;')
          .replace('ú', '&uacute;').replace('ç', '&ccedil;').replace('â', '&acirc;')
          .replace('ê', '&ecirc;').replace('î', '&icirc;').replace('û', '&ucirc;')
          .replace('É', '&Eacute;').replace('Ë', '&Euml;')
          .replace('²', '&sup2;').replace('€', '&euro;').replace('…', '&hellip;'))
    return t


# ---------------------------------------------------------------------------
#  Regels om brontekst te sorteren
# ---------------------------------------------------------------------------
# Deze regels staan aan het eind van een dienstpagina op de bronsite. Het is
# geen lopende tekst maar een oproep; ze gaan naar het slotblok in plaats van in
# de body te blijven staan.
_CTA_START = ('Ben je op zoek', 'Bent u op zoek', 'Ben jij op zoek')
_CTA_LOS = ('Vraag een offerte aan.', 'Vraag dan een offerte aan.',
            'Je kunt een berekening aanvragen door een offerte aan te vragen.')


def _is_cta(p):
    p = p.strip()
    return p.startswith(_CTA_START) or p in _CTA_LOS


def _blokken(slug):
    """De secties van een dienstpagina uit de export, gesorteerd op soort.

       Levert (intro, secties, faq, cta_regel):
         intro   - de eerste alinea's van de pagina
         secties - kopjes met alinea's en eventueel een lijst
         faq     - elk kopje dat op een vraagteken eindigt
         cta     - de wervende slotregel, als de bron die heeft
    """
    s = _services[slug]
    intro, secties, faq, cta = [], [], [], None

    for i, sec in enumerate(s['sections']):
        kop = sec['heading']
        alineas = [p for p in sec['paragraphs'] if not _is_cta(p)]
        weg = [p for p in sec['paragraphs'] if _is_cta(p)]
        if weg and cta is None:
            cta = weg[0]
        lijsten = sec['lists']

        if i == 0 and (kop == s['title'] or kop.lower() == s['title'].lower()):
            # De eerste sectie herhaalt de paginatitel; die kop hoeft niet nog
            # een keer als h2 op de pagina.
            intro = alineas
            if lijsten:
                secties.append({'kop': None, 'alineas': [], 'lijsten': lijsten})
            continue

        if kop.rstrip().endswith('?'):
            # Als losse alinea's, niet als één blok: een antwoord van 229 woorden
            # in de accordeon is een tekstmuur. De lijst eronder blijft een lijst.
            antwoord = list(alineas) + [', '.join(l) for l in lijsten]
            faq.append((kop, antwoord or [NIET_GEVONDEN]))
            continue

        secties.append({'kop': kop if kop != BRON_MARKER else None,
                        'alineas': alineas, 'lijsten': lijsten})

    if not intro and secties:
        # Geen sectie met dezelfde naam als de pagina: neem de eerste alinea's.
        eerste = secties[0]
        if eerste['kop'] is None or not eerste['alineas']:
            pass
        intro = eerste['alineas'][:1]
        eerste['alineas'] = eerste['alineas'][1:]

    return intro, secties, faq, cta


# ---------------------------------------------------------------------------
#  Afbreken van lange samenstellingen
# ---------------------------------------------------------------------------
# De dienstnamen van Duyts zijn Nederlandse samenstellingen van twintig tekens
# en meer. In een hero van 80px of een kaart van een kwart pagina moeten die
# afbreken. De automatische afbreking van de browser zet de streep op de
# verkeerde plek ("Fundering-sonderzoek"), dus geven we hem zelf op met een
# zacht afbreekstreepje: dat is onzichtbaar zolang het woord past.
#
# Alleen voor zichtbare koppen. In een <title>, meta description of schema.org
# hoort geen zacht afbreekstreepje, dus die gebruiken de gewone titel.
AFBREEKPUNTEN = [
    ('Funderingsonderzoek', 'Funderings&shy;onderzoek'),
    ('Funderingsherstel', 'Funderings&shy;herstel'),
    ('Stabiliteitsportalen', 'Stabiliteits&shy;portalen'),
    ('Stabiliteitsberekening', 'Stabiliteits&shy;berekening'),
    ('Constructieberekening', 'Constructie&shy;berekening'),
    ('constructieberekening', 'constructie&shy;berekening'),
    ('vloerbalklagen', 'vloerbalk&shy;lagen'),
    ('Appartementencomplex', 'Appartementen&shy;complex'),
    ('Bedrijfsgebouwen', 'Bedrijfs&shy;gebouwen'),
    ('Kantoorgebouwen', 'Kantoor&shy;gebouwen'),
    ('Schaderapportage', 'Schade&shy;rapportage'),
    ('deskundigenadvies', 'deskundigen&shy;advies'),
    ('Deskundigenadvies', 'Deskundigen&shy;advies'),
    ('Tafelconstructie', 'Tafel&shy;constructie'),
    ('tafelconstructie', 'tafel&shy;constructie'),
    ('stempelconstructie', 'stempel&shy;constructie'),
    ('Zelfdragende', 'Zelf&shy;dragende'),
    ('Registerconstructeur', 'Register&shy;constructeur'),
    ('funderingsherstel', 'funderings&shy;herstel'),
    ('funderingsonderzoek', 'funderings&shy;onderzoek'),
    ('appartementencomplex', 'appartementen&shy;complex'),
]


def afbreek(titel):
    """Zachte afbreekstreepjes in een zichtbare kop."""
    if not titel:
        return titel
    uit = titel
    for heel, gebroken in AFBREEKPUNTEN:
        uit = uit.replace(heel, gebroken)
    return uit

# ---------------------------------------------------------------------------
#  Diensten
# ---------------------------------------------------------------------------
# (bestand, slug in de export, titel op de site, hoofddienst, beeldsleutel)
#
# De titels zijn die van de bronsite. Twee zijn ingekort omdat de bron een
# volledige zin als kop gebruikt ("Constructie ten behoeve van een vide"); in
# een menu en een kaart leest dat niet. De tekst op de pagina zelf is niet
# aangeraakt.
HOOFDDIENSTEN = [
    ('verbouwing.html', 'verbouwing', 'Verbouwing', 'duyts-dienst-verbouwing'),
    ('fundering.html',  'fundering',  'Fundering',  'duyts-dienst-fundering'),
    ('nieuwbouw.html',  'nieuwbouw',  'Nieuwbouw',  'duyts-dienst-nieuwbouw'),
]

DIENSTEN = [
    # ---- Verbouwing ----
    ('muurdoorbraak.html', 'verbouwing/muurdoorbraak', 'Muurdoorbraak',
     'Verbouwing', 'duyts-dienst-muurdoorbraak'),
    ('vloerbalklagen.html', 'verbouwing/verstijving-van-de-vloerbalklagen',
     'Verstijving van de vloerbalklagen', 'Verbouwing', 'duyts-dienst-vloerbalklagen'),
    ('trapgat.html', 'verbouwing/constructie-ten-behoeve-van-een-trapgat',
     'Trapgat', 'Verbouwing', 'duyts-dienst-trapgat'),
    ('vide.html', 'verbouwing/vide-constructie', 'Vide', 'Verbouwing',
     'duyts-dienst-trapgat'),
    ('dakterras.html', 'verbouwing/constructie-ten-behoeve-van-een-dakterras',
     'Dakterras', 'Verbouwing', 'duyts-dienst-dakterras'),
    ('stabiliteitsportalen.html', 'verbouwing/stabiliteitsportalen',
     'Stabiliteitsportalen', 'Verbouwing', 'duyts-dienst-stabiliteitsportalen'),
    ('dakkapel-dakopbouw.html', 'verbouwing/dakkapel-dakopbouw',
     'Dakkapel en dakopbouw', 'Verbouwing', 'duyts-dienst-dakkapel'),
    ('achteraanbouw.html', 'verbouwing/achteraanbouw-constructie',
     'Achteraanbouw', 'Verbouwing', 'duyts-dienst-achteraanbouw'),
    ('stutconstructie.html', 'verbouwing/stutconstructie-stempelconstructie',
     'Stut- en stempelconstructie', 'Verbouwing', 'duyts-dienst-stutconstructie'),
    # ---- Fundering ----
    ('funderingsonderzoek.html', 'fundering/funderingsonderzoek',
     'Funderingsonderzoek', 'Fundering', 'duyts-dienst-funderingsonderzoek'),
    ('funderingsherstel.html', 'fundering/funderingsherstel',
     'Funderingsherstel', 'Fundering', 'duyts-dienst-funderingsherstel'),
    ('funderingsherstel-kelderbak.html', 'fundering/funderingsherstel-met-kelderbak',
     'Funderingsherstel met kelderbak', 'Fundering', 'duyts-dienst-kelderbak'),
    ('zelfdragende-kelderbak.html', 'fundering/zelfdragende-kelderbak',
     'Zelfdragende kelderbak', 'Fundering', 'duyts-dienst-zelfdragende-kelderbak'),
    ('tafelconstructie.html', 'fundering/stutconstructie-tafelconstructie',
     'Stut- en tafelconstructie', 'Fundering', 'duyts-dienst-tafelconstructie'),
    # ---- Nieuwbouw ----
    ('appartementencomplex.html', 'nieuwbouw/appartementencomplex',
     'Appartementencomplex', 'Nieuwbouw', 'duyts-dienst-appartementencomplex'),
    ('woonhuizen.html', 'nieuwbouw/woonhuizen', 'Woonhuizen', 'Nieuwbouw',
     'duyts-dienst-woonhuizen'),
    ('kantoorgebouwen.html', 'nieuwbouw/kantoorgebouwen', 'Kantoorgebouwen',
     'Nieuwbouw', 'duyts-dienst-kantoorgebouwen'),
    ('bedrijfsgebouwen.html', 'nieuwbouw/bedrijfsgebouwen', 'Bedrijfsgebouwen',
     'Nieuwbouw', 'duyts-dienst-bedrijfsgebouwen'),
    # ---- Losse diensten ----
    ('constructieberekening.html', 'constructieberekening', 'Constructieberekening',
     None, 'duyts-dienst-constructieberekening'),
    ('stabiliteitsberekening.html', 'stabiliteitsberekening', 'Stabiliteitsberekening',
     None, 'duyts-dienst-dakkapel'),
    ('schaderapportage.html', 'advies-rechtbanksituaties',
     'Schaderapportage en deskundigenadvies', None, 'duyts-dienst-schaderapportage'),
    ('certificaat-funderingsherstel.html', 'certificaat-funderingsherstel',
     'Certificaat funderingsherstel', None, 'duyts-dienst-certificaat'),
]

def dienst(bestand):
    """Alle gegevens voor één dienstpagina, klaar voor de bouwer."""
    rij = next((d for d in DIENSTEN if d[0] == bestand), None)
    if rij:
        _, slug, titel, ouder, beeld = rij
    else:
        rij = next(d for d in HOOFDDIENSTEN if d[0] == bestand)
        _, slug, titel, beeld = rij
        ouder = None

    s = _services[slug]
    intro, secties, faq, cta = _blokken(slug)
    return {
        'bestand': bestand,
        'titel': titel,
        'ouder': ouder,
        'is_hoofddienst': bestand in [h[0] for h in HOOFDDIENSTEN],
        'beeld': beeld,
        'h1': s['title'] if s['title'] != BRON_MARKER else titel,
        'intro': intro,
        'secties': secties,
        'faq': faq,
        'cta': cta,
        'seo_titel': _schoon(s['seoTitle']),
        'seo_omschrijving': _schoon(s['metaDescription']),
        'bron': s['sourceUrl'],
    }


def kinderen(hoofddienst_titel):
    """De diensten onder een hoofddienst, in de volgorde van de tabel."""
    return [d for d in DIENSTEN if d[3] == hoofddienst_titel]


LOSSE_DIENSTEN = [d for d in DIENSTEN if d[3] is None]


# ---------------------------------------------------------------------------
#  Projecten
# ---------------------------------------------------------------------------
# De bronsite heeft 43 portfolio-items, waarvan 6 projecten meerdere keren zijn
# opgevoerd onder een andere categorie (artis, artis-2 en artis-3 zijn hetzelfde
# project). Hier staat elk project één keer, met al zijn categorieën bij elkaar.
#
# De omschrijving komt uit de og:description van de bronpagina. Die is langer
# dan de regel die op de site zichtbaar was: drie tot vier volledige zinnen in
# plaats van één. Yoast kapt hem af met "[...]"; dat wordt hieronder tot de
# laatste hele zin teruggesneden, zodat er geen halve zin op de pagina staat.
BEELD_BIJ_PROJECT = {
    'artis': 'duyts-project-artis',
    'bibliotheek-woerden': 'duyts-project-bibliotheek-woerden',
    'boerderij-amstel': 'duyts-project-boerderij-amstel',
    'buitenveldert': 'duyts-project-buitenveldert',
    'charlotte-montpensierlaan': 'duyts-project-charlotte-montpensierlaan',
    'cornelis-branderhorststraat': 'duyts-project-cornelis-branderhorststraat',
    'dam': 'duyts-project-dam',
    'de-ruijterkade': 'duyts-project-de-ruijterkade',
    'duivendrechtsekade': 'duyts-project-duivendrechtsekade',
    'emmastraat': 'duyts-project-emmastraat',
    'fagelstraat': 'duyts-project-fagelstraat',
    'funderingsherstel-chassekerk': 'duyts-project-chassekerk',
    'haringpakkersteeg': 'duyts-project-haringpakkersteeg',
    'het-saentje': 'duyts-project-het-saentje',
    'het-waterschild-muiderslot': 'duyts-project-waterschild-muiderslot',
    'ijburg': 'duyts-project-ijburg',
    'jan-luijkenstraat': 'duyts-project-jan-luijkenstraat',
    'kerktoren': 'duyts-project-kerktoren',
    'kloveniersburgwal': 'duyts-project-kloveniersburgwal',
    'minervalaan-2': 'duyts-project-minervalaan',
    'molukkenstraat': 'duyts-project-molukkenstraat',
    'oranje-nassaulaan': 'duyts-project-oranje-nassaulaan',
    'p-c-hooftstraat': 'duyts-project-p-c-hooftstraat',
    'p-c-hooftstraat-2': 'duyts-project-p-c-hooftstraat-2',
    'prinsengracht': 'duyts-project-prinsengracht',
    'prinses-margrietstraat': 'duyts-project-prinses-margrietstraat',
    'schade-rapportage': 'duyts-project-schade-rapportage',
    'school-ijsselmeerstraat': 'duyts-project-school-ijsselmeerstraat',
    'smederij': 'duyts-project-smederij',
    'stadsvilla-amstelveen': 'duyts-project-stadsvilla-amstelveen',
    'stadsvilla-amsterdam': 'duyts-project-stadsvilla-amsterdam',
    'tweede-van-swindenstraat': 'duyts-project-tweede-van-swindenstraat',
    'valeriusplein': 'duyts-project-valeriusplein',
    'van-eeghenstraat': 'duyts-project-van-eeghenstraat',
    'willem-kesstraat': 'duyts-project-willem-kesstraat',
    'rhoneweg-makerstoren': 'duyts-dienst-kantoorgebouwen',
}

# Extra beeld bij een project, als de bron er een tweede foto van had.
TWEEDE_BEELD = {
    'funderingsherstel-chassekerk': 'duyts-project-chassekerk-detail',
    'kloveniersburgwal': 'duyts-project-kloveniersburgwal-detail',
    'p-c-hooftstraat-2': 'duyts-project-p-c-hooftstraat-2-detail',
}

# De plaats staat niet als veld in de bron. Waar de projecttekst zelf een plaats
# noemt, staat die hier; anders blijft het veld leeg. Niet geraden.
PLAATS = {
    'bibliotheek-woerden': 'Woerden',
    'boerderij-amstel': 'Amsterdam',
    'smederij': 'Amstelveen',
    'stadsvilla-amstelveen': 'Amstelveen',
    'het-waterschild-muiderslot': 'Muiden',
    'artis': 'Amsterdam',
    'dam': 'Amsterdam',
}


def _laatste_hele_zin(t):
    """De afkapping van Yoast eraf, tot de laatste afgeronde zin."""
    t = t.replace('[…]', '').replace('[...]', '').strip()
    if t.endswith(('.', '!', '?')):
        return t
    knip = max(t.rfind('. '), t.rfind('! '), t.rfind('? '))
    return t[:knip + 1].strip() if knip > 40 else t.rstrip(' ,;') + '.'


def _canoniek(slugs):
    """Van een groep dubbel opgevoerde projecten de slug zonder telnummer.

       De bronsite voert zes projecten meerdere keren op, elke keer onder een
       andere categorie: artis, artis-2 en artis-3. WordPress hangt daar een
       cijfer achter. Wij houden de versie zonder cijfer aan als adres, en
       verzamelen de categorieën van alle varianten op dat ene project."""
    zonder = [s for s in slugs if not re.search(r'-\d+$', s)]
    return sorted(zonder or slugs, key=len)[0]


def _projecten_opbouwen():
    ruw = {}
    for p in _projecten:
        sleutel = (p['title'], p['intro'])
        og = _seo[p['sourceUrl']]['og'].get('og:description', '') or ''
        categorieen = [c for c in p['work'] if c != BRON_MARKER]
        if sleutel in ruw:
            for c in categorieen:
                if c not in ruw[sleutel]['categorieen']:
                    ruw[sleutel]['categorieen'].append(c)
            ruw[sleutel]['varianten'].append(p['slug'])
            continue
        ruw[sleutel] = {
            'varianten': [p['slug']],
            'slug': p['slug'],
            'titel': p['title'],
            'intro': p['intro'],
            'beschrijving': _laatste_hele_zin(og) if og else p['description'],
            'categorieen': list(categorieen),
            'bron': p['sourceUrl'],
            'seo_titel': _schoon(p['seoTitle']),
            'seo_omschrijving': _schoon(p['metaDescription']),
        }
    uit = []
    for r in ruw.values():
        r['slug'] = _canoniek(r['varianten'])
        r['beeld'] = BEELD_BIJ_PROJECT.get(r['slug'])
        r['tweede_beeld'] = TWEEDE_BEELD.get(r['slug'])
        r['plaats'] = PLAATS.get(r['slug'], '')
        r['bestand'] = f"project-{r['slug']}.html"
        if not r['categorieen']:
            r['categorieen'] = [NIET_GEVONDEN]
        if r['beeld']:
            uit.append(r)
    uit.sort(key=lambda r: r['titel'].lower())
    return uit


PROJECTEN = _projecten_opbouwen()
CATEGORIEEN = sorted({c for p in PROJECTEN for c in p['categorieen'] if c != NIET_GEVONDEN})


def project(slug):
    return next(p for p in PROJECTEN if p['slug'] == slug)


def projecten_in(categorie, maximaal=None):
    lijst = [p for p in PROJECTEN if categorie in p['categorieen']]
    return lijst[:maximaal] if maximaal else lijst


# ---------------------------------------------------------------------------
#  Bedrijf en contact
# ---------------------------------------------------------------------------
NAAM = _bedrijf['name']
NAAM_VOLUIT = _bedrijf['legalName']
TAGLINE = _bedrijf['tagline']
TELEFOON_WEERGAVE = _bedrijf['phone']
TELEFOON_LINK = '+3120' + _bedrijf['phone'].split('-')[1] if '-' in _bedrijf['phone'] else ''
EMAIL = _bedrijf['email']
KVK = _bedrijf['kvk']
STRAAT = _bedrijf['address']['street']
POSTCODE_PLAATS = _bedrijf['address']['postalCodeCity']
ADRES = f'{STRAAT}, {POSTCODE_PLAATS}'
COPYRIGHT = _bedrijf['copyright']
OPRICHTING = '1981'
TEAMGROOTTE = 'circa 25'

# De vier blokken van de homepage van de bronsite, in de volgorde van daar.
USPS = [(u['heading'], u['text']) for u in _bedrijf['homepageUsps']]

OVER_ONS = _bedrijf['aboutSections']
HISTORIE = _bedrijf['historySections']
TEAM_TEKST = _bedrijf['teamCopy']
TEAM_ROLLEN = _bedrijf['teamRoles']
REGISTERCONSTRUCTEUR = _bedrijf['registerConstructeurCopy']
WERKWIJZE = _bedrijf['werkwijzeCopy']
VACATURES = _bedrijf['vacanciesCopy']

CONTACT = _contact
OFFERTE = _contact['quoteForm']

# Externe links die de bronsite legt.
VACATURESITE = 'https://werkenbij.duyts.nl'
DNR_PDF = ('https://www.duyts.nl/wp-content/uploads/2012/12/'
           'Rechtsverhouding-DNR2011NED-3-bev.pdf')


def alinea_lijst(tekst):
    """Een tekstblok uit de export opsplitsen in losse alinea's."""
    if not tekst or tekst == BRON_MARKER:
        return [NIET_GEVONDEN]
    return [a.strip() for a in tekst.split('\n\n') if a.strip()]
