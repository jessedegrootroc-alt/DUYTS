# -*- coding: utf-8 -*-
import hashlib
import pathlib
import inhoud_duyts as D
"""
Gedeelde paginaschil voor de site van Duyts Bouwconstructies.

Dit script schrijft platte HTML-bestanden weg. De site zelf heeft geen
build-stap: wat hier uitkomt is gewone HTML die je met een statische server
serveert. Dit bestand hoort dan ook niet bij de site, het is gereedschap om de
drieënzeventig pagina's identiek te houden terwijl ze gebouwd worden.

De componenten hieronder zijn die van het oorspronkelijke template en zijn niet
van vorm veranderd. Wat eruit is gehaald: de band met klantlogo's en de
citatenslider. Die vragen logo's van opdrachtgevers en getuigenissen, en die
heeft Duyts niet aangeleverd; ze vullen met andermans logo's of met verzonnen
citaten zou de bezoeker voorliegen.
"""

# Zolang er geen domein aan hangt staat hier de plek waar de site nu staat.
# Canonical, sitemap, robots en de deelafbeelding verwijzen hierheen.
BASIS = "https://www.duyts.nl"

# Het hoofdmenu. Een item is óf een gewone link, óf een uitklapper met sublinks
# en een kaart ernaast. De drie diensten en de vier cursussen stonden hier
# eerder allemaal los naast elkaar; dat waren zeven items op één balk.
#
# De sublinks komen uit SERVICES en CURSUSSEN verderop in dit bestand, zodat een
# wijziging daar meteen in het menu, de voet en de overzichtspagina's landt.
# Daarom wordt NAV pas onderaan opgebouwd, in bouw_nav().
NAV = []

# De diensten van Duyts, in de vorm die de componenten hieronder verwachten:
# (bestand, titel, ondertitel, beeldsleutel). De ondertitel is de meta
# description van de bronpagina, ingekort tot één regel voor de kaart.
def _kort(t, n=95):
    t = (t or '').strip()
    if t.startswith('['):
        return ''
    return t if len(t) <= n else t[:t.rfind(' ', 0, n)] + '&hellip;'


SERVICES = [(b, t, _kort(D.dienst(b)['seo_omschrijving']), beeld)
            for b, sl, t, beeld in D.HOOFDDIENSTEN]

# De onderliggende werkzaamheden per hoofddienst.
WERKZAAMHEDEN = {t: [(b, tt, _kort(D.dienst(b)['seo_omschrijving']), beeld)
                     for b, sl, tt, ouder, beeld in D.kinderen(t)]
                 for _, _, t, _ in D.HOOFDDIENSTEN}

# De losse diensten die niet onder een hoofddienst hangen.
LOSSE_DIENSTEN = [(b, tt, _kort(D.dienst(b)['seo_omschrijving']), beeld)
                  for b, sl, tt, ouder, beeld in D.LOSSE_DIENSTEN]

PROJECTEN = D.PROJECTEN
CATEGORIEEN = D.CATEGORIEEN


def bouw_nav():
    """Het hoofdmenu, met dezelfde structuur als op de bronsite.

       Daar staan Werkzaamheden en Projecten als uitklapper in de balk, met
       Offerte, Over ons, Vacatures en Contact ernaast. Die indeling is
       overgenomen; de vorm van het menu blijft die van dit template."""
    NAV.extend([
        {"soort": "link", "href": "index.html", "label": "Home"},
        {
            "soort": "uitklap", "id": "werkzaamheden", "label": "Werkzaamheden",
            "links": ([(b, t, o) for b, t, o, _ in SERVICES]
                      + [(b, t, o) for b, t, o, _ in LOSSE_DIENSTEN]),
            "kaart": {
                "kop": "Weten wat uw project nodig heeft?",
                "tekst": "Vertel kort wat er verbouwd, hersteld of gebouwd wordt; we denken mee over de constructieve aanpak.",
                "knop": "Vraag een offerte aan",
                "href": "offerte.html",
                "foto": "duyts-dienst-constructieberekening",
            },
        },
        {
            "soort": "uitklap", "id": "projecten", "label": "Projecten",
            "links": ([("projecten.html", "Alle projecten",
                        "Alles waar we aan hebben gerekend, op een rij")]
                      + [(f"projecten.html#{c.lower()}", c,
                          f"{len(D.projecten_in(c))} projecten") for c in CATEGORIEEN]),
            "kaart": {
                "kop": "Van monument tot nieuwbouw",
                "tekst": "Restauraties, verbouwingen, funderingsherstel en volledige nieuwbouw, door het hele land.",
                "knop": "Bekijk de projecten",
                "href": "projecten.html",
                "foto": "duyts-project-kloveniersburgwal",
            },
        },
        {"soort": "link", "href": "offerte.html", "label": "Offerte"},
        {"soort": "link", "href": "over-ons.html", "label": "Over ons"},
        {"soort": "link", "href": "contact.html", "label": "Contact"},
    ])


# Alle gegevens hieronder komen letterlijk van www.duyts.nl (footer, contact- en
# offertepagina). Er staat niets in dat de bronsite niet noemt.
TELEFOON_WEERGAVE = D.TELEFOON_WEERGAVE
TELEFOON_LINK = D.TELEFOON_LINK
EMAIL = D.EMAIL
ADRES = D.ADRES
KVK = D.KVK
# De bronsite noemt geen reactietermijn. Op de offertepagina staat alleen "zo
# spoedig mogelijk"; die formulering is overgenomen in plaats van een aantal
# dagen te verzinnen.
REACTIETIJD = "zo spoedig mogelijk"




# (naam, groot, groothoogte, klein, kleinhoogte, alt, map, midden)
#
# Middenmaat staat op None voor alle foto's, en dat is een bewuste keuze. Er
# hebben tussenmaten van 800px in gezeten, want op een telefoon van 412 CSS-
# pixels met dpr 1,75 is 721px nodig en dan slaat de browser 640 over en neemt
# 1200. Op papier drie keer zoveel pixels als er te zien is.
#
# In beeld pakte dat verkeerd uit. Een kandidaat die net boven de gevraagde
# breedte ligt wordt door de browser met een goedkoper filter verkleind dan een
# kandidaat die er ruim boven ligt: 800 naar 720 werd zichtbaar zachter dan 1200
# naar 720. Vergeleken op schermafdrukken van voor en na, en nagerekend: de
# scherpte van het gebied zakte met ruim zestig procent. Dat is precies wat we
# niet wilden inleveren, dus de tussenmaten zijn eruit.
#
# Bij de patronen staat wel een tussenmaat, want daar zit geen fijn detail in
# dat zachter kan worden; het zijn vloeiende verlopen.
FOTOS = {
    'bouwplaats':   ('bouwplaats', 2400, 1350, 1200, 675, 'Bouwplaats met torenkraan', 'foto', None),
    # Het eerste beeldje van de herovideo, zodat het stilstaande beeld en de
    # eerste frame van de film op elkaar aansluiten.
    'logistiek':    ('logistiek', 2400, 1350, 1200, 675, 'Vrachtwagen op een dijkweg langs het water', 'foto', None),
    'productiehal': ('productiehal', 1024, 309, 640, 193, 'Productiehal met medewerkers aan de lijn', 'foto', None),
    'lassen':       ('lassen', 1024, 683, 640, 427, 'Lasser aan het werk aan een constructie', 'foto', None),
    'overleg':      ('overleg', 960, 640, 640, 427, 'Werkoverleg met een klein team', 'foto', None),
    'transport':    ('transport', 1024, 683, 640, 427, 'Industri\u00eble transportbrug en constructie', 'foto', None),
    'haven':        ('haven', 960, 540, 640, 360, 'Zeeschip aan de kade van een containerterminal', 'foto', None),
    'martin-band':  ('martin-band', 800, 800, 440, 440,
                     'Martin de Groot, zittend op een trap voor het Viaduc de Passy in Parijs', 'foto', None),
    # Cursusfoto's, aangeleverd door Jesse op 3 september 2026 (assets/foto/bron/).
    # De maten staan in MATEN; width/height hier zijn die van de grootste maat.
    'cursus-bewustzijn-bouw': ('cursus-bewustzijn-bouw', 1920, 1280, 480, 320,
                     'Uitvoerder in oranje veiligheidsjas kijkt toe terwijl twee bouwvakkers wapening vlechten op een bouwplaats', 'foto', 1200),
    'cursus-risico-lijn':     ('cursus-risico-lijn', 2400, 1600, 480, 320,
                     'Medewerker in blauwe overall en gele helm bedient een machine aan een productielijn vol slangen en kabels', 'foto', 1200),
    'cursus-ladder-helmen':   ('cursus-ladder-helmen', 2400, 1347, 480, 269,
                     'Twee medewerkers met helm en hesje kijken omhoog in een installatie, een van hen met een tekening in de hand', 'foto', 1200),
    'cursus-rie-tablet':      ('cursus-rie-tablet', 700, 525, 480, 360,
                     'Man met tablet op een bordes boven een productielijn met robotarmen', 'foto', None),
    # Dienstfoto's, aangeleverd door Jesse op 3 september 2026 (assets/foto/bron/).
    # Hero van de dienstpagina en de dienstkaart op de homepage; zelfde beeld
    # op beide plekken, zodat je na een klik ziet waar je vandaan komt.
    'dienst-gedrag': ('dienst-gedrag', 1024, 683, 480, 320,
                     'Twee medewerkers in oranje hesje en gele helm kijken toe hoe een collega een machine in de werkplaats bedient', 'foto', None),
    'dienst-rie':    ('dienst-rie', 1024, 565, 480, 265,
                     'Adviseur in geel hesje en blauwe helm legt iets uit aan drie collega\u2019s op een bouwlocatie', 'foto', None),
    'dienst-checks': ('dienst-checks', 1200, 670, 480, 268,
                     'Veiligheidskundige met helm en klembord test de noodstop van een machine in een productiehal, terwijl een collega met tablet de afscherming controleert', 'foto', None),
}


# De beelden uit de Duyts-export. maak_assets.py heeft ze naar WebP omgezet en
# heeft in beeldmaten.json vastgelegd welke breedtes er van elk bestand bestaan
# en hoe groot de grootste is. Dat bestand wordt hier ingelezen, zodat een nieuwe
# foto alleen in beeldplan.json hoeft te staan en niet ook nog hier.
import json as _json
_maten_bestand = pathlib.Path(__file__).resolve().parent / 'beeldmaten.json'
_duyts_maten = (_json.loads(_maten_bestand.read_text(encoding='utf-8'))
                if _maten_bestand.exists() else {})
for _naam, _r in _duyts_maten.items():
    FOTOS[_naam] = (_naam, _r['breed'], _r['hoog'], min(_r['breedtes']), None,
                    _r['alt'], 'foto', None)


# Hoe breed een kaart werkelijk is, voor het sizes-attribuut. Zonder dit haalt
# de browser het grootste bestand op voor een kaart van een kwart pagina breed.
BEELD_MATEN_4 = "(max-width: 767px) 100vw, (max-width: 991px) 50vw, 25vw"
BEELD_MATEN_3 = "(max-width: 991px) 100vw, 33vw"


def foto(sleutel, klasse='', laden='lazy', maten='100vw', alt=None):
    """Eén beeld, in AVIF met WebP als terugval, in meerdere breedtes.

       <picture> met een AVIF-bron en een WebP-<img>. AVIF is bij gelijke
       kwaliteit ruwweg een derde tot de helft kleiner dan WebP; elke browser van
       de laatste jaren kan het lezen, en wie het niet kan krijgt de WebP. De
       browser kiest de breedte zelf, op grond van sizes en de pixeldichtheid.

       De breedtes komen uit MATEN[sleutel] als die er is, anders uit de tuple
       (kleine, middel, grote maat). Bestanden heten <naam>-<breedte>.<ext>.
       width en height zijn die van de grootste maat; ze leggen de verhouding
       vast, zodat er niets verspringt terwijl het beeld nog laadt.

       De alt-tekst beschrijft wat er te zien is; bij puur decoratief beeld geef
       je alt='' mee."""
    naam, gb, gh, kb, kh, standaard_alt, map_, mb = FOTOS[sleutel]
    tekst = standaard_alt if alt is None else alt
    # Een beeld dat lazy geladen wordt, is per definitie niet nodig om de
    # pagina te tekenen, dus krijgt het lage prioriteit. Dat verandert niets aan
    # óf het wordt opgehaald, alleen aan de plek in de rij: de browser gaf de
    # foto's onder de vouw evenveel bandbreedte als de stylesheet en het
    # lettertype, en op een mobiele lijn wachtte de hero-tekst daardoor op
    # ruim twee megabyte aan beeld dat niemand nog zag.
    prioriteit = (' fetchpriority="high" decoding="async"' if laden == 'eager'
                  else ' fetchpriority="low" decoding="async"')
    breedtes = sorted(MATEN.get(sleutel) or ({kb, gb} | ({mb} if mb else set())))
    bron = lambda ext: ', '.join(f'assets/{map_}/{naam}-{b}.{ext} {b}w' for b in breedtes)
    klasse_attr = f' class="{klasse}"' if klasse else ''

    # Vangnet. Een <source> naar een bestand dat er niet is, is erger dan geen
    # <source>: de browser kiest de AVIF-bron op type, en valt bij een 404 NIET
    # terug op de WebP. Je krijgt dan een kapot beeld. Dat is precies wat er
    # gebeurde toen zes foto's wel een WebP hadden en nog geen AVIF. Dus: alleen
    # een AVIF-bron als elk bestand in die srcset ook echt op schijf staat, en
    # anders hard stoppen als ook de WebP ontbreekt, want dan is de build fout.
    wortel = pathlib.Path(__file__).resolve().parent.parent
    ontbreekt = [b for b in breedtes if not (wortel / f'assets/{map_}/{naam}-{b}.webp').exists()]
    if ontbreekt:
        raise FileNotFoundError(f'foto {sleutel!r}: WebP ontbreekt voor breedte(s) {ontbreekt}')
    avif_compleet = all((wortel / f'assets/{map_}/{naam}-{b}.avif').exists() for b in breedtes)
    avif_bron = f'<source type="image/avif" srcset="{bron("avif")}" sizes="{maten}">' if avif_compleet else ''

    return (f'<picture>{avif_bron}'
            f'<img src="assets/{map_}/{naam}-{gb}.webp" srcset="{bron("webp")}" sizes="{maten}" '
            f'width="{gb}" height="{gh}" alt="{tekst}" loading="{laden}"{prioriteit}{klasse_attr}>'
            f'</picture>')


# Per fotosleutel de breedtes die er als bestand van bestaan. Staat een sleutel
# hier niet in, dan gelden de maten uit de FOTOS-tuple. De ladder is afgestemd
# op waar het beeld staat: een band over de volle breedte gaat tot 2400, een
# kaart van een derde pagina hoeft niet verder dan 960.
MATEN = {
    'cursus-bewustzijn-bouw': [480, 800, 1200, 1800, 1920],
    'cursus-risico-lijn':     [480, 800, 1200, 1800, 2400],
    'cursus-ladder-helmen':   [480, 800, 1200, 1800, 2400],
    'cursus-rie-tablet':      [480, 700],
    'dienst-gedrag':          [480, 800, 1024],
    'dienst-rie':             [480, 800, 1024],
    'dienst-checks':          [480, 800, 1200],
}


for _naam, _r in _duyts_maten.items():
    MATEN[_naam] = _r['breedtes']


PIJL = ('<svg class="arrow--animation is-{n}" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg>')


SPOOR = ('<span class="button__spoor" aria-hidden="true">'
         + PIJL.format(n=1).replace('width="16" height="16"', 'width="14" height="14"')
         + PIJL.format(n=2).replace('width="16" height="16"', 'width="14" height="14"')
         + '</span>')


def _inhoud(label):
    return f'<span class="button__inhoud">{label}{SPOOR}</span>'


def knop(label, href, soort='primary', extra=''):
    """De grote CTA-knop met dezelfde pijlwissel als de ronde icoonknop."""
    attr = f' {extra}' if extra else ''
    return f'<a href="{href}" class="button button--{soort}"{attr}>{_inhoud(label)}</a>'


def icoonknop(maat="", soort=""):
    """De ronde icoonknop uit §6.6.2. Decoratief: de hele kaart is de link.

       soort="button--secundair" geeft de diepgroene variant; die is voor de
       cases, die naast diensten en cursussen de tweede keus zijn."""
    klasse = f"button--icon {maat} {soort}".strip()
    return (f'<span class="{klasse}" aria-hidden="true" inert>'
            f'<span class="button--circle"><span class="circle-container">'
            f'{PIJL.format(n=1)}{PIJL.format(n=2)}'
            f'</span></span></span>')


CHEVRON = ('<svg class="submenu--chevron" width="12" height="12" viewBox="0 0 24 24" aria-hidden="true">'
           '<path d="M12 15.4 5.6 9 7 7.6l5 5 5-5L18.4 9 12 15.4Z"/></svg>')


def header(actief):
    """De balk met het logo, het hoofdmenu en de hamburger, plus de uitklappers
       en het mobiele paneel.

       De uitklappers staan buiten .header--container: ze lopen over de volle
       breedte onder de balk door, en dat kan niet binnen een flexrij. De balk
       is position:fixed en dus het ankerpunt voor hun position:absolute."""

    def is_actief(item):
        if item["soort"] == "link":
            return item["href"] == actief
        return any(b == actief for b, _, _ in item["links"])

    def bureau_item(item):
        aan = is_actief(item)
        klasse = "submenu--link is-actief" if aan else "submenu--link"
        if item["soort"] == "link":
            huidig = ' aria-current="page"' if aan else ""
            return f'      <a class="{klasse}" href="{item["href"]}"{huidig}>{item["label"]}</a>'
        return (f'      <button type="button" class="{klasse} submenu--trigger" '
                f'data-uitklap="{item["id"]}" aria-expanded="false" '
                f'aria-controls="uitklap-{item["id"]}">{item["label"]}{CHEVRON}</button>')

    def paneel(item):
        if item["soort"] != "uitklap":
            return ""
        k = item["kaart"]
        links = "\n".join(
            f'          <li><a class="uitklap__link" href="{b}">'
            f'<span class="uitklap__naam">{titel}</span>'
            f'<span class="uitklap__uitleg">{onder}</span></a></li>'
            for b, titel, onder in item["links"])
        return f'''  <div class="uitklap" id="uitklap-{item["id"]}" data-uitklap-paneel="{item["id"]}" inert>
    <div class="uitklap__inner">
      <div class="uitklap__kolom">
        <span class="subtitle">{item["label"]}</span>
        <ul class="uitklap__lijst" role="list">
{links}
        </ul>
      </div>
      <div class="uitklap__kaart">
        {foto(k["foto"], maten="(max-width: 1199px) 0px, 40vw", alt="")}
        <span class="uitklap__sluier" aria-hidden="true"></span>
        <div class="uitklap__kaart-tekst">
          <p class="uitklap__kaart-kop">{k["kop"]}</p>
          <p class="uitklap__kaart-body">{k["tekst"]}</p>
          {knop(k["knop"], k["href"])}
        </div>
      </div>
    </div>
  </div>'''

    def mobiel_item(item, i):
        vertraging = f'style="transition-delay:{i * 60}ms"'
        rol = (f'<span class="mobile-panel--text-slide"><span class="mobile-panel--text-slide-inner">'
               f'<span>{item["label"]}</span><span>{item["label"]}</span></span></span>')
        if item["soort"] == "link":
            return (f'      <li><a class="mobile-panel--nav-link" href="{item["href"]}" '
                    f'data-panel-sluit {vertraging}>{rol}</a></li>')
        sub = "\n".join(
            f'          <li><a class="mobile-panel--sublink" href="{b}" data-panel-sluit>{titel}</a></li>'
            for b, titel, _ in item["links"])
        return f'''      <li>
        <button type="button" class="mobile-panel--nav-link mobile-panel--nav-knop"
                data-mobiel-uitklap="{item["id"]}" aria-expanded="false"
                aria-controls="mobiel-{item["id"]}" {vertraging}>{rol}{CHEVRON}</button>
        <ul class="mobile-panel--sublijst" id="mobiel-{item["id"]}" role="list" hidden>
{sub}
        </ul>
      </li>'''

    links = "\n".join(bureau_item(n) for n in NAV)
    panelen = "\n".join(filter(None, (paneel(n) for n in NAV)))
    paneel_links = "\n".join(mobiel_item(n, i) for i, n in enumerate(NAV))

    return f'''<header class="header header--scrolled" id="siteHeader">
  <div class="header--container">
    <a href="index.html" class="header--logo" aria-label="Duyts Bouwconstructies, naar de homepage">
      <img class="header--logo-kleur" src="assets/logo/duyts-logo.webp" alt="Duyts Bouwconstructies" width="112" height="40">
      <img class="header--logo-wit" src="assets/logo/duyts-logo-wit.webp" alt="" aria-hidden="true" width="112" height="40">
    </a>

    <nav class="submenu" aria-label="Hoofdmenu">
{links}
      <a class="submenu--link highlight" href="contact.html">Contact</a>
    </nav>

    <button type="button" id="hamburger" class="hamburger" aria-expanded="false" aria-controls="mobilePanel">
      Menu
      <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 5h20v2H2V5Zm0 6h20v2H2v-2Zm0 6h20v2H2v-2Z"/></svg>
    </button>
  </div>

{panelen}
</header>

<div class="mobile-panel--overlay" id="panelOverlay" hidden></div>
<div class="mobile-panel" id="mobilePanel" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-panel--topbar">
    <a class="mobile-panel--chip" href="contact.html">Contact</a>
    <button type="button" class="mobile-panel--chip is-close" id="panelSluit">
      Sluiten
      <svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.4 17.6 5 12 10.6 6.4 5 5 6.4 10.6 12 5 17.6 6.4 19l5.6-5.6 5.6 5.6 1.4-1.4-5.6-5.6L19 6.4Z"/></svg>
    </button>
  </div>
  <nav class="mobile-panel--nav" aria-label="Hoofdmenu">
    <span class="mobile-panel--label">Menu</span>
    <ul class="mobile-panel--list" role="list">
{paneel_links}
    </ul>
  </nav>
  <div class="mobile-panel--cta button__mobile-width">
    {knop("Bespreek uw project", "contact.html")}
  </div>
</div>'''


def footer():
    # De footer van de bronsite heeft alleen een adresblok en een regel over de
    # vacatures. Dit template heeft vier kolommen; die worden gevuld met de
    # werkzaamheden en de projectcategorieën, zodat de belangrijkste pagina's
    # van onderaf bereikbaar zijn.
    werkzaamheden = "\n".join(f'            <li><a href="{b}">{t}</a></li>'
                              for b, t, _, _ in SERVICES + LOSSE_DIENSTEN)
    projecten = "\n".join(
        f'            <li><a href="projecten.html#{c.lower()}">{c}</a></li>'
        for c in CATEGORIEEN)
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer--widgets">
      <div class="row footer--gap">
        <div class="col-lg-3 col-md-4 col-12 widget">
          <img src="assets/logo/duyts-logo.webp" alt="Duyts Bouwconstructies" width="112" height="40" style="margin-bottom:var(--space-500)">
          <p class="footer--intro">Constructieve adviezen voor verbouwing, funderingsherstel en nieuwbouw. Sinds 1981 vanuit Amsterdam, door het hele land.</p>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h2 class="footer__kop">Werkzaamheden</h2>
          <ul role="list">
{werkzaamheden}
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h2 class="footer__kop">Projecten</h2>
          <ul role="list">
{projecten}
            <li><a href="werkwijze.html">Werkwijze</a></li>
            <li><a href="vacatures.html">Vacatures</a></li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h2 class="footer__kop">Contact</h2>
          <ul role="list">
            <li><a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <p class="footer--adres">{D.STRAAT}<br>{D.POSTCODE_PLAATS}<br>KvK {KVK}</p>
        </div>
      </div>
    </div>
    <div class="footer--line"></div>
    <div class="footer--copyright">
      <span>&copy; {D.NAAM_VOLUIT}</span>
      <a href="privacybeleid.html">Privacybeleid</a>
      <a href="cookies.html">Cookies</a>
    </div>
  </div>
</footer>'''


COOKIEBALK = '''<!-- ================= COOKIEMELDING ================= -->
<aside id="cookiebalk" class="cookiebalk" hidden aria-label="Cookiemelding">
  <h2>Cookie-instellingen</h2>
  <p>Deze site plaatst alleen wat nodig is om hem te laten werken. Zet je analytische cookies aan, dan help je ons te zien wat werkt en wat niet. Lees het <a href="cookies.html">cookiebeleid</a>.</p>

  <div id="cookieKeuzes" class="cookie-keuzes" hidden>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" checked disabled aria-label="Functionele cookies, altijd aan">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Functioneel</span>
        <p>Nodig om de site te laten werken. Staat altijd aan.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieAnalytisch" aria-label="Analytische cookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Analytisch</span>
        <p>Laat ons zien welke pagina&rsquo;s bezocht worden, zodat we de site kunnen verbeteren.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieMarketing" aria-label="Marketingcookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Marketing</span>
        <p>Voor advertenties en het meten daarvan. Nu niet in gebruik.</p>
      </div>
    </div>
  </div>

  <div class="cookie-knoppen">
    <button type="button" class="cookie-knop" data-cookie="weigeren">Weigeren</button>
    <button type="button" class="cookie-knop" data-cookie="aanpassen">Aanpassen</button>
    <button type="button" class="cookie-knop cookie-knop--donker" data-cookie="toestaan">Toestaan</button>
  </div>
</aside>'''


ORGANISATIE_LD = f'''{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{D.NAAM_VOLUIT}",
  "alternateName": "{D.NAAM}",
  "foundingDate": "{D.OPRICHTING}",
  "url": "{BASIS}/",
  "logo": "{BASIS}/assets/logo/duyts-logo.png",
  "email": "{EMAIL}",
  "telephone": "{TELEFOON_LINK}",
  "vatID": null,
  "identifier": {{ "@type": "PropertyValue", "name": "KvK", "value": "{KVK}" }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{D.STRAAT}",
    "postalCode": "{D.POSTCODE_PLAATS.split()[0]} {D.POSTCODE_PLAATS.split()[1]}",
    "addressLocality": "{D.POSTCODE_PLAATS.split(maxsplit=2)[2]}",
    "addressCountry": "NL"
  }}
}}'''


# ---------------------------------------------------------------------------
#  Versiehash op lokale stylesheets en scripts
# ---------------------------------------------------------------------------
# De site heeft geen build-stap, dus de bestandsnamen liggen vast: styleguide.css
# heet altijd styleguide.css. Een browser die de site eerder bezocht mag dat
# bestand daarom uit zijn cache halen, en blijft dan op de oude versie hangen na
# een update. Dat is geen theoretisch geval: tijdens het bouwen hield de browser
# hier drie keer een oude stylesheet of een oude site.js vast terwijl het bestand
# op schijf al nieuw was.
#
# Elke lokale verwijzing krijgt daarom ?v=<acht tekens uit de sha256 van de
# inhoud> mee. Verandert het bestand, dan verandert de query en haalt de browser
# hem opnieuw op; verandert het niet, dan blijft de cache gewoon werken.
#
# Alleen lokale bestanden. GSAP en Barba komen van jsDelivr en hebben hun
# versienummer al in het pad staan.
_VERSIES = {}


def v(bestand):
    """Verwijzing naar een lokaal bestand: `<naam>?v=<hash van de inhoud>`.

       Staat er een geminificeerde versie naast (`styleguide.min.css`), dan
       verwijst dit naar die, en is de hash die van het geminificeerde bestand:
       dat is immers wat de browser ophaalt. Die bestanden maakt `minify.py`;
       ontbreken ze, dan gaat het gewone bestand mee en werkt de site
       ongewijzigd, alleen wat zwaarder.

       Bestaat het bestand helemaal niet, dan komt de naam onveranderd terug:
       een ontbrekend bestand is een fout die zichtbaar moet blijven in de
       netwerktab, niet iets om hier te maskeren."""
    if bestand not in _VERSIES:
        pad = pathlib.Path(__file__).resolve().parent.parent / bestand
        klein = pad.with_name(f'{pad.stem}.min{pad.suffix}')
        if klein.exists():
            pad, naam = klein, klein.name
        else:
            naam = bestand
        try:
            hash8 = hashlib.sha256(pad.read_bytes()).hexdigest()[:8]
            _VERSIES[bestand] = f'{naam}?v={hash8}'
        except OSError:
            _VERSIES[bestand] = bestand
    return _VERSIES[bestand]


def inline(bestand):
    """De inhoud van een klein stylesheet, om in de pagina te zetten.

       Twee stylesheets zijn zo klein dat het ophalen ervan meer kost dan de
       inhoud: `transitions.css` is 0,5 kB geminificeerd en de pagina-stylesheets
       zijn 0,3 tot 6 kB. Op een mobiele verbinding blokkeerde elk van die twee
       het tekenen 304 ms, en dat is bijna helemaal het heen-en-weer van het
       verzoek. In de pagina gezet is die wachttijd nul.

       styleguide.css blijft wél een los bestand: 59 kB in elke pagina zetten
       maakt de HTML zwaarder dan wat het aan wachttijd scheelt, en dan is het
       bovendien op elke pagina opnieuw ophalen in plaats van één keer uit de
       cache.

       De pagina-overgang kan hiermee om: page-transitions.js kopieert het
       element met data-page-css uit het opgehaalde document en behandelt een
       <style> apart van een <link> ("een <style> geldt meteen")."""
    wortel = pathlib.Path(__file__).resolve().parent.parent
    pad = wortel / bestand
    klein = pad.with_name(f'{pad.stem}.min{pad.suffix}')
    bron = klein if klein.exists() else pad
    try:
        return bron.read_text(encoding='utf-8').strip()
    except OSError:
        return ''


def pagina(bestand, titel, omschrijving, namespace, pagina_css, css_naam,
           inhoud, scripts=(), extra_ld=None, actief=None, body_klasse=""):
    """Zet één complete HTML-pagina in elkaar."""
    ld_blokken = f'<script type="application/ld+json">\n{ORGANISATIE_LD}\n</script>'
    if extra_ld:
        ld_blokken += f'\n<script type="application/ld+json">\n{extra_ld}\n</script>'

    script_regels = "\n".join(f'<script src="{v(s)}"></script>' for s in scripts)
    body_attr = f' class="{body_klasse}"' if body_klasse else ""

    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{titel}</title>
<meta name="description" content="{omschrijving}" />
<link rel="canonical" href="{BASIS}/{bestand}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="{D.NAAM_VOLUIT}" />
<meta name="theme-color" content="#FFFFFF" />
<meta name="color-scheme" content="light" />

<!-- GSAP en Barba komen van jsDelivr. Het opzetten van die verbinding (dns,
     tcp, tls) kost op een telefoon een paar honderd ms en begint nu al terwijl
     de HTML nog binnenkomt, in plaats van pas onderaan de pagina. -->
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />

<!-- Het lettertype staat in de kop van de pagina en is dus onderdeel van de
     LCP. Zonder preload vindt de browser het pas nadat styleguide.css binnen is
     en ontleed is. crossorigin moet erbij, ook al staat het bestand op dezelfde
     server: een font wordt altijd in CORS-modus opgehaald, en zonder dat woord
     haalt de browser het twee keer op. -->
<link rel="preload" href="assets/fonts/assistant-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="assets/fonts/karla-latin.woff2" as="font" type="font/woff2" crossorigin />

<link rel="stylesheet" href="{v("styleguide.css")}" />
<style>{inline("transitions.css")}</style>
<!-- De cookiebalk verschijnt pas als cookiebalk.js hem opbouwt, dus zijn stijl
     hoeft de eerste weergave niet op te houden. media="print" laat de browser
     hem buiten het kritieke pad ophalen; onload zet hem daarna alsnog aan. De
     noscript-regel vangt op dat zonder JavaScript ook die onload niet afgaat. -->
<link rel="stylesheet" href="{v("cookiebalk.css")}" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="{v("cookiebalk.css")}" /></noscript>
<style data-page-css="{css_naam}">{inline(pagina_css)}</style>

<link rel="icon" href="assets/favicon/duyts-favicon.ico" sizes="16x16 32x32 48x48" />
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/duyts-favicon-32.png" />
<link rel="icon" type="image/png" sizes="192x192" href="assets/favicon/duyts-favicon-192.png" />
<link rel="apple-touch-icon" href="assets/favicon/duyts-apple-touch-icon.png" />

<meta property="og:type" content="website" />
<meta property="og:site_name" content="{D.NAAM}" />
<meta property="og:locale" content="nl_NL" />
<meta property="og:url" content="{BASIS}/{bestand}" />
<meta property="og:title" content="{titel}" />
<meta property="og:description" content="{omschrijving}" />
<meta property="og:image" content="{BASIS}/assets/social/duyts-deelafbeelding.png" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="{D.NAAM}: constructieve adviezen sinds 1981" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="{BASIS}/assets/social/duyts-deelafbeelding.png" />
<meta name="twitter:title" content="{titel}" />
<meta name="twitter:description" content="{omschrijving}" />

{ld_blokken}
</head>

<body{body_attr}>
<a class="skip-link" href="#main-content">Naar de inhoud</a>

<!-- De header en het mobiele paneel staan bewust BUITEN #smooth-wrapper.
     ScrollSmoother verschuift de inhoud met een transform, en onder een
     transform hangt position:fixed aan dat element in plaats van aan het
     scherm. Ze blijven daardoor ook staan bij een pagina-overgang; welke
     menulink actief is wordt in page-transitions.js bijgewerkt. -->
{header(actief or bestand)}

<div id="smooth-wrapper">
<div id="smooth-content">

<div data-barba="wrapper">
<div class="app__wrapper" data-barba="container" data-barba-namespace="{namespace}">
<div class="content__wrapper">

<main id="main-content">

{inhoud}

</main>

{footer()}

<script src="{v("site.js")}"></script>
<script src="{v("contactformulier.js")}"></script>
{script_regels}
</div><!-- /.content__wrapper -->
</div><!-- /[data-barba=container] -->
</div><!-- /[data-barba=wrapper] -->

</div><!-- /#smooth-content -->
</div><!-- /#smooth-wrapper -->

{COOKIEBALK}

<!-- ================= PAGINA-OVERGANGEN =================
     Barba wisselt alleen de container hierboven om, GSAP animeert de wissel. -->
<!-- defer: de browser haalt ze op terwijl hij de pagina nog aan het ontleden is
     en voert ze daarna uit, in deze volgorde. Die volgorde is nodig, want
     ScrollTrigger heeft gsap nodig en page-transitions.js heeft Barba nodig. -->
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollSmoother.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/@barba/core@2.10.3/dist/barba.umd.js"></script>
<script defer src="{v("cookiebalk.js")}"></script>
<script defer src="{v("analytics.js")}"></script>
<script defer src="{v("smooth-scroll.js")}"></script>
<script defer src="{v("page-transitions.js")}"></script>

</body>
</html>
'''


# ---------------------------------------------------------------------------
#  De band met opdrachtgevers
# ---------------------------------------------------------------------------
# ===========================================================================
#  DEZE LOGO'S ZIJN VAN KLANTEN VAN MADEGRO, NIET VAN DUYTS. Ze staan er op
#  verzoek, en moeten vóór livegang vervangen worden door opdrachtgevers van
#  Duyts. Zie CONTENT-TODO.md; de herkomst staat in
#  assets/logo/opdrachtgevers/HERKOMST.md.
# ===========================================================================
#
# Een logo in deze band leest als "dit bedrijf is klant". Deze dertien zijn dat
# van MADEGRO: het bedrijf waar dit template van komt. Martin heeft ze zelf
# aangeleverd voor die site, en ze komen overeen met de klantenlijst op zijn
# LinkedIn. Voor Duyts geldt dat niet: Duyts is een ander bedrijf, dus zolang
# ze hier staan zegt de band iets wat niet klopt.
#
# Wat er wél feitelijk onderbouwd was: op /over-ons/ noemt Duyts zelf voor wie
# ze werken (particulieren, VvE's, architecten, aannemers, projectontwikkelaars,
# woningbouwverenigingen). Die groepen stonden hier als woordmerk. Die lijst
# staat hieronder nog, onder OPDRACHTGEVERS_GROEPEN, zodat er met één regel
# teruggeschakeld kan worden.
#
# Elk item is (bestand, naam, breedte, hoogte). Breedte en hoogte zijn de
# natuurlijke maten van het bestand en dienen alleen om de verhouding vast te
# leggen: de stylesheet zet ze op 40px hoog met max-width 190px. Zonder die twee
# attributen weet de browser de verhouding niet voordat het bestand binnen is en
# verspringt de band tijdens het laden.
LOGOMAP = "assets/logo/opdrachtgevers/"

OPDRACHTGEVERS = [
    ("alstom.webp", "Alstom", 408, 80),
    ("ballast-nedam.webp", "Ballast Nedam", 452, 80),
    ("bilfinger.webp", "Bilfinger", 210, 80),
    ("cosun.webp", "Cosun Beet Company", 345, 80),
    ("ebert-hera.webp", "Ebert Hera", 389, 80),
    ("electrabel.webp", "Electrabel", 203, 80),
    ("freesmij.webp", "Freesmij", 309, 80),
    ("ge-vernova.webp", "GE Vernova", 362, 80),
    ("huhtamaki.webp", "Huhtamaki", 478, 80),
    ("ivens.webp", "Ivens", 237, 80),
    ("ooms.webp", "Ooms Bouw &amp; Ontwikkeling", 248, 80),
    ("stork.webp", "Stork", 197, 80),
    ("tes.webp", "TES Industrial Systems", 160, 80),
]

# De feitelijk onderbouwde variant: de groepen die Duyts zelf noemt. Zet deze
# lijst op OPDRACHTGEVERS en de band rendert weer woordmerken in tekst.
OPDRACHTGEVERS_GROEPEN = [
    "Particulieren", "VvE&rsquo;s", "Architecten", "Aannemers",
    "Projectontwikkelaars", "Woningbouwverenigingen", "Beheermaatschappijen",
    "Rechtbanken", "Advocatenkantoren",
]


def _logoset(verborgen=False):
    """Eén reeks merken. De band zet er twee achter elkaar en schuift precies de
       helft op, zodat hij naadloos doorloopt; de tweede reeks is aria-hidden,
       dus een schermlezer hoort de namen één keer. Daarom krijgen de logo's in
       die tweede reeks een leeg alt: anders leest hij ze alsnog voor.

       Geen loading="lazy" op deze afbeeldingen. Het venster van de band knipt af
       met overflow: hidden, dus de browser ziet alles rechts van de rand als
       "niet in beeld" en laadt het nooit; de laatste logo's bleven daardoor
       leeg."""
    attr = ' aria-hidden="true"' if verborgen else ''
    regels = []
    for item in OPDRACHTGEVERS:
        if isinstance(item, (tuple, list)):
            bestand, naam = item[0], item[1]
            breedte = item[2] if len(item) > 2 else 190
            hoogte = item[3] if len(item) > 3 else 40
            alt = '' if verborgen else naam
            regels.append(
                f'          <li class="logo-slider__logo">'
                f'<img src="{LOGOMAP}{bestand}" alt="{alt}" '
                f'width="{breedte}" height="{hoogte}" '
                f'fetchpriority="low" decoding="async"></li>')
        else:
            regels.append(
                f'          <li class="logo-slider__logo">'
                f'<span class="logo-slider__woord">{item}</span></li>')
    return f'        <ul class="logo-slider__set"{attr}>\n' + "\n".join(regels) + '\n        </ul>'


def logoslider(nr, kop="Voor wie wij werken"):
    """De doorlopende band. Pauzeert bij hover en staat stil bij
       prefers-reduced-motion; dat gedrag zit in de CSS van het template."""
    return (f'  <section class="logo-slider" id="s{nr}-opdrachtgevers" '
            f'aria-label="{kop}" data-logoband>\n'
            '    <div class="logo-slider__venster">\n'
            '      <div class="logo-slider__spoor">\n'
            f'{_logoset()}\n{_logoset(verborgen=True)}\n'
            '      </div>\n'
            '    </div>\n'
            '  </section>')


def ctablok(nr, kop, tekst=None):
    """De afsluitende oproep: één merkvlak over de volle breedte, gecentreerd,
       met een knop naar de contactpagina. Het formulier zelf staat op contact.html
       en op offerte.html; dit is de aanloop erheen.

       De regel eronder komt waar mogelijk uit de bron: op de dienstpagina's van
       Duyts staat onderaan een eigen wervende regel, en die wordt hier
       doorgegeven. Staat die er niet, dan valt hij terug op de vaste regel."""
    regel = tekst or ('Vertel kort wat er verbouwd, hersteld of gebouwd wordt. '
                      f'Wij nemen {REACTIETIJD} contact met u op.')
    return (f'  <section class="cta-slot" id="s{nr}-contact">\n'
            '    <div class="container">\n'
            '      <div class="cta-slot__hoofd">\n'
            '        <span class="subtitle cta-slot__label">Contact</span>\n'
            f'        <h2 class="cta-slot__kop">{kop}</h2>\n'
            f'        <p class="cta-slot__tekst">{regel}</p>\n'
            '        <div class="cta-slot__actie">\n'
            f'          {knop("Vraag een offerte aan", "offerte.html")}\n'
            f'          {knop("Bespreek uw project", "contact.html", "secondary")}\n'
            '        </div>\n'
            '      </div>\n'
            '    </div>\n'
            '  </section>')


def paginahero(nr, ident, label, titel, beeld, alt=None, positie=None):
    """De hero met links de kop op grijs en rechts een foto. De <h1> staat in de
       HTML voor het beeld; onder 768px zet de CSS het beeld met order bovenaan,
       zodat de leesvolgorde blijft kloppen."""
    stijl = f' style="object-position:{positie}"' if positie else ""
    beeldtag = foto(beeld, laden="eager", maten="(max-width: 767px) 100vw, 50vw", alt=alt)
    if stijl:
        beeldtag = beeldtag.replace("<img ", f"<img{stijl} ")
    return (f'  <section class="paginahero" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld">\n'
            f'      {beeldtag}\n'
            '    </div>\n'
            '  </section>')


def patroonhero(nr, ident, label, titel):
    """Dezelfde hero, maar met het merkpatroon in plaats van een foto.

       Twee bestanden, want de compositie verschilt: op breed scherm staat het
       patroon rechts in een liggend vak, op een telefoon als brede band boven de
       titel. <picture> kiest ze op dezelfde grens als de layout zelf omslaat
       (768px), zodat er nooit een verkeerde uitsnede te zien is.

       Hoe hoog die band is, staat in de stylesheet en niet in het bestand: 7:3
       plus de hoogte van de vaste balk, want die ligt eroverheen. Het
       bronbestand is daarom vierkant en niet al op 7:3 gesneden; cover heeft
       verticaal wat over nodig.

       Het patroon is versiering en zegt niets wat de kop niet al zegt, dus
       alt="" en aria-hidden: een schermlezer slaat het over."""
    return (f'  <section class="paginahero paginahero--patroon" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld" aria-hidden="true">\n'
            '      <picture>\n'
            '        <source media="(max-width: 767px)" srcset="assets/patronen/hero-patroon-mobiel-720.webp 720w, assets/patronen/hero-patroon-mobiel-800.webp 800w, assets/patronen/hero-patroon-mobiel-1440.webp 1440w" sizes="100vw" width="1440" height="1440">\n'
            '        <img src="assets/patronen/hero-patroon-1440.webp" srcset="assets/patronen/hero-patroon-720.webp 720w, assets/patronen/hero-patroon-1000.webp 1000w, assets/patronen/hero-patroon-1440.webp 1440w" sizes="50vw" width="1440" height="940" alt="" loading="eager" fetchpriority="high" decoding="async">\n'
            '      </picture>\n'
            '    </div>\n'
            '  </section>')


KLEURENRIJ = ("geel", "grijs", "wit", "groen")


def vlakkenrij(nr, ident, kop, vlakken, subtitel=None):
    """Kop met daaronder vier gekleurde vlakken over de volle breedte. vlakken is
       een lijst van (kop, tekst); de kleuren lopen vast in dezelfde volgorde,
       zodat de rij op elke pagina hetzelfde ritme heeft."""
    label = f'        <span class="subtitle" style="margin-bottom:var(--space-500)">{subtitel}</span>\n' if subtitel else ""
    items = "\n".join(
        f'      <li class="vlak vlak--{KLEURENRIJ[i % 4]}">\n'
        f'        <h3 class="vlak__kop">{titel}</h3>\n'
        f'        <p class="vlak__tekst">{tekst}</p>\n'
        '      </li>'
        for i, (titel, tekst) in enumerate(vlakken)
    )
    return (f'  <section class="vlakkenband" id="s{nr}-{ident}">\n'
            '    <div class="container">\n'
            '      <div class="vlakkenband__kop">\n'
            f'{label}'
            f'        <h2 class="section-heading">{kop}</h2>\n'
            '      </div>\n'
            '    </div>\n'
            '    <ul class="vlakkenrij">\n'
            f'{items}\n'
            '    </ul>\n'
            '  </section>')


# ---------------------------------------------------------------------------
#  Referenties
# ---------------------------------------------------------------------------
# Het citatencomponent van het template: één referentie per keer, de foto van
# het eindresultaat links, het citaat rechts met een streepje boven de naam.
# site.js laat ze automatisch doorlopen met een balkje dat de tijd aangeeft;
# zonder JavaScript staan ze onder elkaar en blijven de pijlen verborgen.
#
# ===========================================================================
#  DE CITATEN HIERONDER ZIJN VERZONNEN. Ze staan er op verzoek, om de sectie
#  af te kunnen maken, en moeten vóór livegang vervangen worden door echte
#  referenties. Zie CONTENT-TODO.md.
# ===========================================================================
#
# Wat er wél echt is: de foto's en de projecten. Dat zijn drie projecten uit de
# export, met hun eigen beeld en plaats.
#
# Twee dingen staan er bewust niet in, ook niet verzonnen:
#
#   1. Namen van bestaande bedrijven. Een verzonnen citaat op naam van een
#      architectenbureau of aannemer die dat nooit gezegd heeft, is een
#      uitspraak over een bestaande partij. De citaten staan daarom op de rol
#      van de opdrachtgever, zoals Duyts die zelf op /over-ons/ noemt.
#   2. Logo's. Zonder bedrijfsnaam is er ook geen logo, en er is geen enkel
#      logobestand van een opdrachtgever. Het slot (.quote__logo) blijft leeg;
#      zie assets/logo/opdrachtgevers/README.md.
#
# De citaten claimen verder niets over Duyts wat niet uit de bron te halen is:
# geen doorlooptijden, geen prijzen, geen certificeringen, geen garanties. Ze
# gaan over hoe het werken met een constructeur voelt, niet over cijfers.
REFERENTIES = [
    # (projectbeeld, projectnaam, plaats, citaat, wie-het-zegt, logobestand)
    ("duyts-project-chassekerk", "Chass&eacute;kerk", "Amsterdam",
     "Niemand wist precies wat er onder dit pand zat. Duyts heeft het "
     "uitgezocht en daarna in gewone taal uitgelegd wat er kon en wat dat "
     "betekende voor het ontwerp.",
     "Architect", None),
    ("duyts-project-artis", "Artis", "Amsterdam",
     "Een monument, een krappe bouwplaats en een opdrachtgever die door wilde. "
     "De berekeningen klopten en lagen er wanneer we ze nodig hadden; dat "
     "scheelt in de uitvoering enorm.",
     "Aannemer", None),
    ("duyts-project-stadsvilla-amsterdam", "Stadsvilla", "Amsterdam",
     "Wij wilden de hele begane grond openbreken. We hebben eerlijk gehoord "
     "welke muur wel kon en welke niet, en ze hebben meegedacht over een "
     "oplossing die uitvoerbaar bleef.",
     "Particuliere opdrachtgever", None),
]


def citaten(nr, ident="referenties", kop="Wat opdrachtgevers zeggen",
            subtitel="Referenties", items=None):
    """De referentiesectie. items is een lijst zoals REFERENTIES; laat je hem
       weg, dan pakt hij die lijst."""
    items = REFERENTIES if items is None else items
    dias = []
    for i, (beeld, project, plaats, citaat, wie, logo) in enumerate(items):
        tekst = (f'<p>{citaat}</p>' if citaat
                 else f'<p><span class="invulveld">{D.NIET_GEVONDEN}</span></p>')
        naam = wie or f'<span class="invulveld">{D.NIET_GEVONDEN}</span>'
        # Het project eronder is wél een feit uit de export: dit is de foto van
        # dat project, dus die regel klopt ook zonder citaat.
        herkomst = f'{project}, {plaats}' if plaats else project
        logotag = ''
        if logo:
            logotag = (f'\n        <p class="quote__logo">'
                       f'<img src="{LOGOMAP}{logo}" alt="{wie or project}" '
                       f'height="32" loading="lazy" decoding="async"></p>')
        dias.append(
            f'      <figure class="quote"{" hidden" if i else ""}>\n'
            f'        <div class="quote__beeld">\n'
            f'          {foto(beeld, maten="(max-width: 767px) 100vw, 33vw", alt=f"Project {project} in {plaats}" if plaats else f"Project {project}")}\n'
            f'        </div>\n'
            f'        <div class="quote__body">\n'
            f'          <blockquote class="quote__tekst">{tekst}</blockquote>\n'
            f'          <hr class="quote__streep">\n'
            f'          <figcaption class="quote__naam">{naam}<br>{herkomst}</figcaption>'
            f'{logotag}\n'
            f'        </div>\n'
            f'      </figure>')
    return (f'  <section class="quotes" id="s{nr}-{ident}">\n'
            '    <div class="container">\n'
            '      <div class="quotes__kop">\n'
            f'        <span class="subtitle">{subtitel}</span>\n'
            f'        <h2 class="section-heading">{kop}</h2>\n'
            '      </div>\n'
            '    </div>\n'
            '    <div class="container">\n'
            '      <div class="quotes__venster" data-quoteslider>\n'
            + "\n".join(dias) + '\n'
            '      </div>\n'
            '      <div class="quotes__nav" hidden>\n'
            '        <button type="button" class="quotes__pijl" data-quote="vorige" aria-label="Vorige referentie">\n'
            f'          {icoonknop("", "button--grijs")}\n'
            '        </button>\n'
            '        <button type="button" class="quotes__pijl" data-quote="volgende" aria-label="Volgende referentie">\n'
            f'          {icoonknop("", "button--grijs")}\n'
            '        </button>\n'
            '        <p class="quotes__teller" data-quote-teller aria-live="polite">1 / '
            f'{len(dias)}</p>\n'
            # Het balkje loopt mee met de tijd die een citaat blijft staan. Het
            # is versiering bij de teller ernaast, die hetzelfde in tekst zegt,
            # dus aria-hidden. Het blijft verborgen tot site.js het doorlopen
            # ook echt aanzet: bij 'beweging uit' gebeurt dat niet.
            '        <div class="quotes__voortgang" data-quote-voortgang hidden aria-hidden="true">'
            '<span></span></div>\n'
            '      </div>\n'
            '    </div>\n'
            '  </section>')


def beeldkaart(kop, tekst, beeld, alt=None, kleur="grey", href=None):
    """Een kaart met de foto erboven en de tekst eronder, twee per rij. Dit is de
       verticale variant van .cta-blocks-advanced."""
    binnen = (f'      <figure class="cta-blocks-advanced__banner">\n'
              f'        {foto(beeld, maten="(max-width: 991px) 100vw, 50vw", alt=alt)}\n'
              '        <span class="cta-blocks-advanced__backdrop" aria-hidden="true"></span>\n'
              '      </figure>\n'
              f'      <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{kleur}">\n'
              f'        <h3 class="cta-blocks-advanced__title">{kop}</h3>\n'
              '        <div class="cta-blocks-advanced__wrapper">\n'
              f'          <div class="cta-blocks-advanced__content"><p>{tekst}</p></div>\n'
              '        </div>\n'
              '      </div>')
    if href:
        omhulsel = (f'    <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" '
                    f'href="{href}">\n{binnen}\n    </a>')
    else:
        omhulsel = f'    <div class="cta-blocks-advanced__card">\n{binnen}\n    </div>'
    return f'  <div class="col-lg-6 col-12 kolom--vullend">\n{omhulsel}\n  </div>'

def dienstkaart(i, dienst, intro, kolom="col-lg-4"):
    """Eén dienst als kaart met de foto erboven.

       kolom bepaalt de breedte: col-lg-4 zet er drie op een rij (de
       hoofddiensten), col-lg-3 vier (de losse diensten daaronder)."""
    bestand, titel, sub, beeld = dienst
    return f'''        <div class="{kolom} col-md-6 col-12 kolom--vullend">
          <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" href="{bestand}"
             aria-label="{titel}: {sub}">
            <figure class="cta-blocks-advanced__banner cta-blocks-advanced__banner--verhouding">
              {foto(beeld, maten=BEELD_MATEN_3, alt="")}
            </figure>
            <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{'grey' if i % 2 == 0 else 'white'}">
              <span class="subtitle">Dienst 0{i + 1}</span>
              <div class="cta-blocks-advanced__wrapper">
                <div>
                  <h3 class="cta-blocks-advanced__title" style="margin-bottom:var(--space-500)">{D.afbreek(titel)}</h3>
                  <div class="cta-blocks-advanced__content"><p>{sub}</p>{f"<p>{intro}</p>" if intro else ""}</div>
                </div>
                {icoonknop("button--icon--56")}
              </div>
            </div>
          </a>
        </div>'''


# Voorlopige woordmerken voor de verzonnen opdrachtgevers bij de citaten.
# TODO-CONTENT: dit zijn geen echte logo's. Ze zijn hier gemaakt als grijze
# letters in een websafe schreefloze, zodat de opmaak af is. Een logo van een
# van de dertien echte opdrachtgevers kan hier niet staan: dan hangt er een
# aanbeveling van Alstom of Stork onder een citaat dat niemand heeft gegeven.
# Zie CONTENT-TODO.md.
def contactblok(onderwerp, kop="Neem contact op",
                intro="Vertel kort waar je tegenaan loopt. We reageren binnen "
                      f"{REACTIETIJD}."):
    """Het gedeelde formulier. De HTML wordt door contactformulier.js gerenderd;
       hier staat alleen de haak plus een terugval voor bezoekers zonder JS."""
    return f'''  <section class="band background--grey" id="s{onderwerp["nr"]}-contact">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle">Contact</span>
          <h2 class="section-heading" style="margin:var(--space-500) 0">{kop}</h2>
          <p class="article-body">{intro}</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            Liever bellen? <a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a>
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <div data-contactformulier data-onderwerp="{onderwerp["waarde"]}"></div>
          <noscript>
            <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons gerust op
              <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
          </noscript>
        </div>
      </div>
    </div>
  </section>'''


def faq_blok(nr, items, titel="Veelgestelde vragen"):
    """Drie FAQ-items als accordeon plus de bijbehorende FAQPage-structuurdata."""
    regels = []
    for i, (vraag, antwoorden) in enumerate(items):
        alineas = "".join(f"<p>{a}</p>" for a in antwoorden)
        regels.append(f'''          <div class="accordion__item">
            <button type="button" class="accordion__header" aria-expanded="false" aria-controls="faq-{nr}-{i}">
              <span class="accordion__number">{i + 1:02d}</span>
              <span class="accordion__title">{vraag}</span>
              <span class="accordion__suffix" aria-hidden="true"><span class="accordion__icon"></span></span>
            </button>
            <div class="accordion__details" id="faq-{nr}-{i}">
              <div class="accordion__details-inner article-body">{alineas}</div>
            </div>
          </div>''')
    return f'''  <section class="band background--white" id="s{nr}-faq">
    <div class="container">
      <div class="row">
        <div class="col-md-4 col-12">
          <span class="subtitle">FAQ</span>
          <h2 class="font-size--lg" style="margin-top:var(--space-500)">{titel}</h2>
        </div>
        <div class="col-md-8 col-12">
          <div class="accordion">
{chr(10).join(regels)}
          </div>
        </div>
      </div>
    </div>
  </section>'''


def faq_ld(items):
    import json
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": _plat(v),
             "acceptedAnswer": {"@type": "Answer", "text": " ".join(_plat(a) for a in ant)}}
            for v, ant in items
        ],
    }, ensure_ascii=False, indent=2)


def _plat(tekst):
    import re, html
    return html.unescape(re.sub(r"<[^>]+>", "", tekst))


# NAV verwijst naar SERVICES, CURSUSSEN en foto(); die staan hierboven, dus de
# lijst wordt hier pas gevuld. header() leest hem daarna.
bouw_nav()
