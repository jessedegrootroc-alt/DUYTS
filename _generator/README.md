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

## Snelheid: wat er gedaan is en waarom

Gemeten met Lighthouse tegen een server die comprimeert en cache-headers stuurt,
zoals een echte host. Mobiel, mediaan van vijf runs:

| | voor | na |
|---|---|---|
| Performance | 77 | **98** |
| Accessibility | 98 | **100** |
| Best Practices | 100 | 100 |
| SEO | 100 | 100 |
| First Contentful Paint | 2,6 s | 0,8 s |
| Largest Contentful Paint | 4,4 s | 2,4 s |
| Speed Index | 5,2 s | 1,4 s |
| Total Blocking Time | 40 ms | 0 ms |
| Layout shift | 0 | 0 |

Desktop staat op 100 / 100 / 100 / 100.

Wat het opleverde, in volgorde van effect:

1. **Minificeren** (`minify.py`). styleguide.css was 116 kB en blokkeerde het
   tekenen 1661 ms. Geminificeerd 60 kB, met gzip 10,7 kB over de lijn. Alle
   stylesheets en scripts gaan hierdoor.

2. **Een terugvalletter met dezelfde metriek.** Dit was de verrassing. Met
   `font-display: swap` tekent de browser de tekst eerst in de systeemletter en
   daarna opnieuw in Assistant of Karla, en die tweede tekening heeft andere
   regelafmetingen. Chrome zag dat als een nieuw grootste tekstblok en
   registreerde de LCP dus op de tweede tekening: 0,5 seconde later en drie
   punten lager. De twee `@font-face`-blokken bovenaan `styleguide.css` zetten
   dezelfde systeemletter op maat met `size-adjust` en de ascent/descent-
   overrides, zodat de wissel geen herschikking meer is. De getallen komen uit
   de fontbestanden zelf; wordt een font vervangen, dan moeten ze opnieuw
   berekend worden.

3. **Twee stylesheets in de pagina** in plaats van als los bestand
   (`transitions.css` en de pagina-stylesheets). Die zijn 0,3 tot 6 kB, en het
   ophalen kostte per stuk 304 ms aan heen-en-weer. Zie `inline()` in
   `schil.py`. styleguide.css blijft wél een los bestand: 60 kB in elke pagina
   zetten is duurder dan het één keer ophalen.

4. **Lage prioriteit voor beeld onder de vouw.** Een lazy afbeelding is niet
   nodig om te tekenen, dus krijgt hij `fetchpriority="low"`. De browser gaf de
   ruim twee megabyte beeld op de homepage eerst evenveel bandbreedte als de
   stylesheet en het lettertype.

5. **De logo's naar lossless WebP.** 42,8 kB aan PNG werd 24 kB, pixel voor
   pixel identiek (nagerekend met een pixelvergelijking).

6. **De koppen in de voet van h4 naar h2.** Dat was een sprong van twee niveaus
   na de h2 van het slotblok, op 72 van de 73 pagina's, en de enige fout die
   Lighthouse op toegankelijkheid gaf.

### Wat bewust NIET is aangeraakt

**De herovideo.** Die moest blijven draaien. Nagemeten met de video geblokkeerd:
dat scheelt niets in de score en de LCP wordt er zelfs marginaal slechter van,
dus die beperking kost geen snelheid. De film wordt nog steeds pas door
`site.js` ingehangen, en niet bij databesparing, een trage lijn of
`prefers-reduced-motion`.

**De ongebruikte CSS.** Lighthouse meldt dat er op de homepage 32 kB van
styleguide.css niet gebruikt wordt. Dat is inherent aan één gedeelde
stylesheet: wat de homepage niet gebruikt, gebruikt een dienstpagina wel.
Regels weghalen zou andere pagina's breken, en de kritieke CSS eruit halen en de
rest achteraf laden geeft een pagina die een moment zonder opmaak staat.

**"Properly size images" (-171 kB).** Dat gaat vooral om de twee verborgen
citaten in de referentieslider. Die zijn 2,8 seconde later in beeld, dus ze
moeten geladen worden; ze staan al op lage prioriteit.

**"Label in Name".** Deze audit weegt nul en de site voldoet aan het
onderliggende criterium: de zichtbare tekst zit in de toegankelijke naam
("Verbouwing" in "Verbouwing: Om de kwaliteit..."). WCAG 2.5.3 vraagt dat de
zichtbare naam erin zit, niet dat hij er gelijk aan is.

### Meten

```bash
python3 -m http.server 8080          # of een server die comprimeert
npx lighthouse http://127.0.0.1:8080/index.html --view
```

`python3 -m http.server` comprimeert niet en stuurt geen cache-headers, dus
daar meet je ongeveer vijf punten te laag. Zie `DEPLOY.md`. Reken ook op een
spreiding van vijf punten tussen runs: neem de mediaan van vijf, niet één run.

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
