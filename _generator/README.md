# _generator

De 73 HTML-pagina's in de hoofdmap worden hier gemaakt en zijn dus
**gegenereerde bestanden**. Pas je een pagina met de hand aan, dan is die
wijziging weg zodra hier iets opnieuw draait.

```
python3 bouw_alles.py
```

Dat schrijft alle pagina's opnieuw. `bouw_alles.py` roept de andere scripts aan:

| bestand | wat het maakt |
|---|---|
| `schil.py` | de gedeelde onderdelen: balk, voettekst, hero's, knoppen, kaarten, beeld |
| `bouw_duyts_home.py` | `index.html` |
| `bouw_duyts_dienst.py` | de 25 dienstpagina's |
| `bouw_duyts_projecten.py` | `projecten.html` en de 36 projectpagina's |
| `bouw_duyts_bedrijf.py` | over ons, historie, het team, registerconstructeur, werkwijze, vacatures |
| `bouw_duyts_contact.py` | contact, offerte, privacybeleid, cookies |
| `bouw_duyts_sitemap.py` | `sitemap.xml` en `robots.txt` |

## Waar de inhoud staat

| bestand | wat erin staat |
|---|---|
| `duyts/` | de contentexport van www.duyts.nl: alle teksten, ongewijzigd |
| `inhoud_duyts.py` | welke pagina's er zijn, de hiërarchie, welke foto waar hoort |
| `inhoud_dienst_verhaal.py` | de verhaallaag onder de dienstpagina's |
| `inhoud_copy.py` | de herschreven koppen, leads, CTA's en losse alinea's |

`inhoud_dienst_verhaal.py` bevat de enige tekst op deze site die niet van
www.duyts.nl komt: situaties, processtappen, oplevering en veelgestelde vragen.
Bovenaan dat bestand staat waar die vakinhoud op gebaseerd is en wat er bewust
niet in staat. Alles wat over Duyts als bedrijf gaat, komt uit de export.

`inhoud_copy.py` is de conversielaag. Hier staat per pagina de herschreven kop,
lead, tussenkop en CTA. De feiten komen onveranderd uit `duyts/`; alleen de
formulering is anders. Waar een bronalinea inhoudelijk klopte maar zwak
communiceerde, staat de herschreven versie hier en schuift de bronalinea naar
het uitlegblok verderop de pagina. `PROJECT_HERSCHRIJF` vervangt losse zinnen
uit de bron die als cliché lezen, ook in de meta-omschrijving en de JSON-LD.

Nagerekend: elk inhoudelijk woord in deze laag is teruggezocht in de export.
Wat overblijft zijn werkwoorden en voegwoorden, geen feiten. Er staat dus geen
dienst, cijfer, certificering of bedrijfsclaim in die niet uit `duyts/` komt.

Twee bewuste keuzes in deze laag:

- De H1 van een dienstpagina is de dienstnaam zelf ("Funderingsonderzoek"),
  niet de belofte. Dat houdt de kop gelijk aan het menu en aan waar mensen op
  zoeken; het voordeel staat in de eerste H2 eronder ("Wanneer
  funderingsonderzoek aan de orde is"). Alleen de homepage, `projecten.html`
  en `over-ons.html` hebben een H1 die wél een belofte is.
- Van de 25 dienstpagina's hebben `verbouwing`, `fundering` en `nieuwbouw` een
  volledig herschreven body. De 22 onderliggende diensten houden de brontekst
  in het uitlegblok, met een herschreven lead, tussenkoppen en CTA eromheen.

## Beeld

`maak_assets.py` zet de afbeeldingen uit de export om naar responsive WebP en
maakt de twee logovarianten. Dat hoeft alleen als er beeld bijkomt of verandert:

```
python3 maak_assets.py
```

Het leest `beeldplan.json` (welke bron, welke rol, welke alt-tekst) en schrijft
`beeldmaten.json`, dat `schil.py` weer inleest. Het verwacht de uitgepakte
export op `/tmp/duyts/export`; staat die er niet, dan stopt het script met een
melding in plaats van met halve bestanden.

De CSS, de JavaScript en alles in `assets/` worden **niet** gegenereerd; die
bewerk je rechtstreeks.

## Versiehash op CSS en JavaScript

Elke lokale stylesheet en elk lokaal script krijgt `?v=<acht tekens>` mee,
berekend uit de sha256 van de inhoud van dat bestand:

```html
<link rel="stylesheet" href="styleguide.css?v=424acdcc" />
<script src="site.js?v=f105a2ab"></script>
```

Waarom: de site heeft geen build-stap, dus de bestandsnamen liggen vast.
`styleguide.css` heet altijd `styleguide.css`, dus een browser die de site eerder
bezocht mag hem uit zijn cache halen en blijft na een update op de oude versie
hangen. Tijdens het bouwen gebeurde dat hier drie keer: een gewijzigde
stylesheet of `site.js` kwam niet door, en een wijziging leek niet te werken
terwijl het bestand op schijf al goed was.

Verandert een bestand, dan verandert de hash en haalt de browser hem opnieuw op.
Verandert het niet, dan blijft de cache gewoon werken; dat is het verschil met
een tijdstempel of een willekeurig getal.

Dat gebeurt in `v()` in `schil.py`. Aandachtspunten:

- **Alleen lokale bestanden.** GSAP en Barba komen van jsDelivr en hebben hun
  versienummer al in het pad.
- **Niet op de lettertypen.** Die worden aangeroepen uit `@font-face` in
  `styleguide.css`, en dat pad kan dit script niet bijwerken. Zou de
  `<link rel="preload">` in de kop wél een hash krijgen en de `@font-face` niet,
  dan zijn dat twee verschillende URL's en haalt de browser elk font twee keer op.
  Beide staan daarom zonder hash.
- **Bestaat het bestand niet, dan komt de naam onveranderd terug.** Een
  ontbrekend bestand moet als 404 in de netwerktab zichtbaar blijven, niet hier
  gemaskeerd worden.
- **De pagina-overgang kan hier tegen.** `page-transitions.js` kloont de
  `<link data-page-css>` uit het opgehaalde document en vergelijkt op de naam in
  `data-page-css`, niet op de href. De hash loopt dus automatisch mee.

## Let op: het uitvoerpad

De bouwscripts schrijven naar de map boven deze (`UIT = ...parent.parent`), dus
naar de hoofdmap van de site. Verplaats je `_generator/`, dan verhuist de
uitvoer mee.
