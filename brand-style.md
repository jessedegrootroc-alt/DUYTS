# Brand Style

Merklaag gedestilleerd uit **https://www.duyts.nl/** (Duyts Bouwconstructies BV).
Alleen kleur en typografie. Geen layout, componenten, spacing of interacties.

Bronnen van deze analyse:
`wp-content/uploads/logisco-style-custom.css` (de themaconfiguratie van de site zelf),
`themes/logisco/css/style-core.css`, de inline `<style>`-blokken in de pagina's,
en een pixelanalyse van het logo (`DuytsLogo.png`).

---

## Brand Direction

Zakelijk en betrouwbaar, met een technische, constructieve inslag. Het merk leunt op
één diepe indigo-paarse tint uit het logo, ondersteund door een donker marineblauw en
veel wit. Rustig en ingenieursachtig in plaats van luid: geen felle kleurvlakken, wel
duidelijke, zware koppen en veel witruimte. De uitstraling is gevestigd en solide,
passend bij een bureau dat sinds 1981 aan constructies rekent.

---

## Color System

### Primary

- **Name:** Duyts Indigo
- **HEX:** `#463878`
- **Usage:** De merkkleur. 75% van alle logopixels is exact deze tint, en de site gebruikt
  hem voor de header, de footer, de overlay van de paginakopbanden en de check-iconen in
  de USP's. Dit is de kleur waaraan het merk herkend wordt: gebruik hem voor grote
  merkoppervlakken en dominante merkvlakken.

### Secondary

- **Name:** Duyts Mist
- **HEX:** `#C7D8E0`
- **Usage:** Lichte, koele steuntint. Op de bronsite de kleur van de navigatielabels op de
  indigo header, de footertekst en de copyrightregel. Bedoeld voor tekst, iconen en
  details **op** indigo of marineblauwe vlakken, en als zachte ondersteunende merktint.
  Niet gebruiken als tekstkleur op wit (te weinig contrast, 1,25:1).

### Accent

- **Name:** Duyts Navy
- **HEX:** `#143369`
- **Usage:** De enige interactiekleur die op de live site daadwerkelijk zichtbaar is: alle
  verzendknoppen van het contact- en offerteformulier staan hierop, met witte tekst.
  Gebruik voor CTA's, links, labels en kleine highlights. Eén accentkleur, niet meer.

### Background

- **HEX:** `#FFFFFF`
- **Usage:** De dominante basis. Alle content- en paginaoppervlakken van de bronsite staan
  op wit; het is met 117 voorkomens de meest gebruikte kleur in de stylesheet.

### Background Subtle

- **HEX:** `#F5F5F5`
- **Usage:** Zachte afwijkende achtergrond voor rustige vlakken en ingesloten blokken
  (op de bronsite: blockquotes en formuliervelden). Eén subtiele tint, geen reeks.

### Text Primary

- **HEX:** `#383838`
- **Usage:** Koppen en bodytekst. Op de bronsite de kleur van `h1`–`h6`. Contrast op wit
  is 11,73:1 (AAA).

### Text Muted

- **HEX:** `#636363`
- **Usage:** Ondersteunende tekst: intro's van mindere orde, captions, meta-informatie,
  labels bij formulieren. Op de bronsite de bodytekstkleur. Contrast op wit 6,01:1 (AA).

### Border Soft

- **HEX:** `#E6E6E6`
- **Usage:** Alleen waar het bestaande template al een lijn of scheiding tekent. Deze token
  vervangt uitsluitend de *kleur* van bestaande randen; hij voegt geen nieuwe randen,
  dikte of radius toe.

---

## 60 30 10 Distribution

### 60%

- **Color:** `#FFFFFF` (Background)
- **Usage:** Hoofdachtergronden, alle grote pagina-oppervlakken, contentgebieden. Dit is de
  basis waarop het merk rust; wit is op de bronsite met afstand het dominante oppervlak.

### 30%

- **Color:** `#463878` (Primary — Duyts Indigo)
- **Usage:** De merklaag. Contrasterende secties en grote merkvlakken: header, footer,
  paginakopbanden en eventuele volvlakse merksecties. Tekst en details binnen deze vlakken
  in `#FFFFFF` of `#C7D8E0` (Secondary).

### 10%

- **Color:** `#143369` (Accent — Duyts Navy)
- **Usage:** CTA-kleur, links, labels en kleine highlights. Belangrijke interactie-elementen
  krijgen deze kleur met witte tekst (12,30:1, AAA). Bewust klein gehouden zodat het accent
  accent blijft.

---

## Color Tokens

```css
:root {
  --color-primary:            #463878; /* Duyts Indigo - merkvlakken, header, footer */
  --color-secondary:          #C7D8E0; /* Duyts Mist - tekst/details op donkere merkvlakken */
  --color-accent:             #143369; /* Duyts Navy - CTA, links, highlights */
  --color-background:         #FFFFFF; /* hoofdachtergrond (60%) */
  --color-background-subtle:  #F5F5F5; /* rustige afwijkende achtergrond */
  --color-text:               #383838; /* koppen en bodytekst */
  --color-text-muted:         #636363; /* ondersteunende tekst, captions, meta */
  --color-border-soft:        #E6E6E6; /* kleur van bestaande randen */
}
```

RGB-waarden, alleen waar nuttig voor overlays of transparantie:

```css
:root {
  --color-primary-rgb: 70, 56, 120;  /* #463878 */
  --color-accent-rgb:  20, 51, 105;  /* #143369 */
}
```

---

## Typography

### Heading Font

- **Font:** Assistant
- **Fallback:** `font-family: "Assistant", "Helvetica Neue", Helvetica, Arial, sans-serif;`
- **Weights:** 700 (standaard voor koppen), 800 (uitsluitend Display)
- **Usage:** Alle koptekstniveaus. De bronsite zet `h1`–`h6` op Assistant 700 en de grote
  paginakop op 800.

### Body Font

- **Font:** Karla
- **Fallback:** `font-family: "Karla", "Helvetica Neue", Helvetica, Arial, sans-serif;`
- **Weights:** 400 (bodytekst), 600 (labels en kleine nadruk)
- **Usage:** Bodytekst, intro's, lijsten, formuliertekst, navigatielabels en buttonlabels.
  De bronsite zet body op Karla met een line-height van 1.7.

> **Let op bij implementatie:** de bronsite declareert Assistant en Karla in CSS, maar laadt
> de webfonts nergens (geen `@font-face`, geen Google Fonts-link, geen woff-bestanden).
> Bezoekers zien nu dus de systeem-sans van hun browser. Beide fonts zijn gratis via Google
> Fonts beschikbaar; laad ze in het template wél, anders blijft de typografische merklaag
> een intentie op papier.

---

## Typography Tokens

```css
:root {
  --font-heading: "Assistant", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-body:    "Karla", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

---

## Type Hierarchy

Bewust **zonder font-sizes**. De responsive type scale van het bestaande template blijft
volledig intact; alleen family, weight, line-height en letter-spacing komen uit deze
merklaag.

### Display

- **Font:** `var(--font-heading)` — Assistant
- **Weight:** 800
- **Line height:** 1.15
- **Letter spacing:** 0

### H1

- **Font:** `var(--font-heading)` — Assistant
- **Weight:** 700
- **Line height:** 1.2
- **Letter spacing:** 0

### H2

- **Font:** `var(--font-heading)` — Assistant
- **Weight:** 700
- **Line height:** 1.2
- **Letter spacing:** 0

### H3

- **Font:** `var(--font-heading)` — Assistant
- **Weight:** 700
- **Line height:** 1.3
- **Letter spacing:** 0

### Body Large

- **Font:** `var(--font-body)` — Karla
- **Weight:** 400
- **Line height:** 1.6
- **Letter spacing:** 0

### Body

- **Font:** `var(--font-body)` — Karla
- **Weight:** 400
- **Line height:** 1.7
- **Letter spacing:** 0

### Small

- **Font:** `var(--font-body)` — Karla
- **Weight:** 400
- **Line height:** 1.6
- **Letter spacing:** 0

### Label

- **Font:** `var(--font-body)` — Karla
- **Weight:** 600
- **Line height:** 1.4
- **Letter spacing:** 0.06em

---

## Font Consolidation

**Gevonden op de bronwebsite (3 fontfamilies):**

| Font | Waar gebruikt op de bronsite |
|---|---|
| Assistant | `h1`–`h6`, `.logisco-title-font`, paginakoppen |
| Karla | body, paragrafen, navigatie, inputs, buttons, info- en testimonialtekst |
| PT Sans | uitsluitend `blockquote` en `.gdlr-core-quote-font` |

**Behouden:** Assistant (headings) en Karla (body). Dat is precies het systeem dat de site
zelf declareert, het valt binnen het maximum van twee families, en beide families hebben een
duidelijke, gescheiden rol plus alle benodigde weights.

**Bewust niet meegenomen:** PT Sans. Die kleeft aan één enkel element (blockquote) en voegt
een derde sans toe zonder merkwaarde. Blockquotes vallen in het nieuwe template onder de
bestaande componentstijl en krijgen simpelweg de bodyfont.

**Weights opgeschoond:** de bronsite gebruikt door elkaar 400, 600, 700, 800 plus `normal`
en `bold`. Teruggebracht tot vier duidelijke waarden: 700 en 800 op de headingfont, 400 en
600 op de bodyfont. De 800 blijft alleen voor Display, omdat het merk daar echt op leunt:
iedere pagina op de site heeft een paginakopband op 800. Trefwoorden als `normal` en `bold`
zijn vervangen door numerieke waarden zodat weights voorspelbaar zijn.

**Waarom dit consistenter is:** twee families met één taak elk in plaats van drie families
met overlappende taken, en een vaste set van vier weights in plaats van zes losse
declaraties. Als het template liever met één familie werkt, is Assistant voor zowel headings
als body een verdedigbare vereenvoudiging; het systeem hierboven blijft dan gelijk, met
`--font-body` gelijk aan `--font-heading`.

**Waargenomen maar niet in deze spec:** de bronsite zet navigatielabels in uppercase met
1px letterspacing. De letterspacing is meegenomen in de Label-stijl (0.06em); `text-transform`
niet, omdat dat onder de interface van jouw template valt en niet onder de merklaag.

---

## Color Consolidation

**Gevonden:** meer dan 40 losse hex-waarden in de themastylesheet. De relevante:

| Kleur | Voorkomens | Rol op de bronsite |
|---|---|---|
| `#ffffff` | 117 | achtergrond, tekst op donkere vlakken, buttontekst |
| `#143369` | 63 | buttons, breadcrumbs, tags, gradiëntbasis |
| `#e53c35` + `#e53d34` | 59 | ingesteld accent (top bar, pagination, sliderdots, blog-hovers) |
| `#e57875` + `#e57f7b` | 33 | hover-tinten van dat rood, alleen in demo-skins |
| `#463878` | 6 in CSS + 261 inline | logo, header, footer, paginakop-overlay, USP-iconen |
| `#727272`, `#383838`, `#636363`, `#4e4e4e`, `#b5b5b5`, `#adadad`, `#cecece`, `#191919`, `#313131`, `#393939`, `#424242`, `#575757`, `#666666`, `#747474`, `#777777` | 5–15 elk | grijstinten voor tekst, placeholders en randen |
| `#f5f5f5`, `#f3f3f3`, `#e6e6e6` | 9 / 9 / 6 | subtiele achtergronden en randen |
| `#516487`, `#53689b` | 20 | hover- en gradiëntvarianten van `#143369` |
| `#c7d8e0` | 4 | navigatielabels en footertekst op de indigo |
| `#4f1212`, `#0000ff`, `#8224e3`, `#7b8596` | 6 / 1 / 1 / 1 | losse uitschieters (zie hieronder) |

**Samengevoegd:**

- **Vijftien grijstinten → twee tokens.** `#383838` wordt `--color-text` (koppen én body),
  `#636363` wordt `--color-text-muted`. Alle overige grijzen (`#727272`, `#4e4e4e`,
  `#575757`, `#666666`, `#747474`, `#777777`, `#393939`, `#424242`, `#313131`, `#191919`)
  liggen daar zo dicht tegenaan dat ze visueel niets toevoegen.
- **`#e53c35` en `#e53d34`** zijn hetzelfde rood met 1 bit verschil; behandeld als één kleur.
- **`#f5f5f5` en `#f3f3f3`** zijn niet van elkaar te onderscheiden; teruggebracht tot
  `#F5F5F5`.
- **`#516487`, `#53689b`, `#e57875`, `#e57f7b`** zijn hover- en gradiëntafgeleiden. Hovers
  en gradiënten horen bij de interface van jouw template, dus ze zijn niet als merkkleur
  opgenomen.
- **`#b5b5b5`, `#adadad`, `#cecece`** waren placeholder- en randgrijzen. Randkleur is
  geconsolideerd naar `#E6E6E6`; de te lichte tekstgrijzen zijn geschrapt (zie Accessibility).

**Verwijderd, met reden:**

- **`#e53c35` (rood).** Dit is in de themaopties als globale accentkleur ingesteld, maar het
  is op geen enkele pagina zichtbaar: de selectors waar het aan hangt (top bar, pagination,
  flexslider, accordions, blogtitels, cart-teller) komen in de 84 gecrawlde pagina's
  **nul keer** voor. Het als 10%-accent doorzetten zou een kleur introduceren die op de
  huidige site nergens te zien is, en die als normale tekst ook geen AA haalt (4,18:1).
  Bewust niet opgenomen. Wil de opdrachtgever alsnog een rood accent, dan is dat een
  expliciete merkbeslissing en moet de tint eerst worden verdiept naar minimaal 4,5:1.
- **`#463878` als headerkleur klopt wél** en is juist gepromoveerd tot primary: het is
  letterlijk de logokleur (`#463878`: 499.620 van de 662.337 pixels in het logo, 75,4%).
- **`#4f1212`** (donker kastanje) zit alleen in `[data-skin="..."]`-blokken van de
  themademo, niet in de site zelf.
- **`#0000ff` en `#8224e3`** waren de link- en linkhoverkleur: pure browserblauw en een
  willekeurig paars. Geen merkkleuren, wel de meest zichtbare inconsistentie op de site.
  Vervangen door respectievelijk `--color-accent` (`#143369`) en `--color-primary`
  (`#463878`), zodat links binnen het merk blijven.
- **`#7b8596`** was de linkkleur in de footer en haalde daar 2,69:1. Vervangen door
  `--color-secondary` (`#C7D8E0`, 6,83:1).

**De basis:** één merkkleur (indigo), één steuntint (mist), één accent (navy), wit, één
subtiele achtergrond, twee tekstkleuren en één randkleur. Acht tokens in plaats van veertig
losse waarden, allemaal terug te voeren op iets wat op de site daadwerkelijk zichtbaar is.

**Waarom dit consistenter is:** de bronsite had drie concurrerende kleurfamilies naast elkaar
(indigo in de chrome, marineblauw in de buttons, rood in de themaopties) plus een dozijn
bijna identieke grijzen. Dit systeem kiest één identiteitskleur, geeft de tweede blauwe tint
de duidelijke rol van accent, en schrapt de derde familie die toch niet in beeld kwam.

---

## Accessibility

Alle combinaties in dit systeem zijn gemeten en halen minimaal WCAG AA voor normale tekst:

| Combinatie | Ratio | Niveau |
|---|---|---|
| `--color-text` `#383838` op `--color-background` | 11,73:1 | AAA |
| `--color-text` `#383838` op `--color-background-subtle` | 10,76:1 | AAA |
| `--color-text-muted` `#636363` op `--color-background` | 6,01:1 | AA |
| `--color-text-muted` `#636363` op `--color-background-subtle` | 5,51:1 | AA |
| `#FFFFFF` op `--color-primary` `#463878` | 10,01:1 | AAA |
| `--color-secondary` `#C7D8E0` op `--color-primary` | 6,83:1 | AA |
| `--color-accent` `#143369` op `--color-background` (links) | 12,30:1 | AAA |
| `--color-accent` `#143369` op `--color-background-subtle` | 11,28:1 | AAA |
| `#FFFFFF` op `--color-primary` (CTA-knop) | 10,01:1 | AAA |
| `--color-primary` `#463878` op `--color-background` | 10,01:1 | AAA |

**Correcties die nodig waren.** Drie kleuren van de bronsite zijn vervangen omdat ze
onvoldoende contrast haalden. Het merkkarakter is daarbij intact gelaten: elke vervanging
blijft binnen dezelfde kleurfamilie.

1. **Footerlinks** `#7b8596` op indigo haalde 2,69:1 (onvoldoende). Vervangen door
   `#C7D8E0`, dezelfde koele tint die de site daar al voor de gewone footertekst gebruikt:
   6,83:1.
2. **Placeholder- en meta-grijs** `#b5b5b5` haalde 2,05:1 op wit. Geschrapt; de muted-token
   `#636363` (6,01:1) neemt die rol over.
3. **Links** `#0000ff` haalde weliswaar 8,59:1, maar is pure browserblauw en valt buiten het
   merk. Vervangen door `--color-accent` `#143369` (12,30:1), dus zowel toegankelijker als
   binnen de merkidentiteit.

### Gemeten op de site zelf

De tabel hierboven is de merklaag op papier. Op de gebouwde site is elk element
met eigen tekst nagemeten tegen zijn werkelijke achtergrond, inclusief
doorgerekende transparantie: **1.394 tekstelementen over 13 pagina's, nul
gevallen onder de eis.** De laagste geslaagde meting is 9,18:1 (een indigo kop
op het subtiele grijs, eis 3:1).

Na het herschrijven van de copy is die controle opnieuw gedaan, omdat andere
tekst in andere vlakken terechtkomt: **1.301 tekstelementen over twaalf
pagina's op 1440px, nul gevallen onder de eis**, en dezelfde twaalf pagina's ook
schoon op 375, 768 en 1024px. Nul horizontale overloop, en de randen van
formuliervelden en knoppen halen alle 3:1.

Bij die controle kwamen vijf dingen boven die wél gecorrigeerd moesten worden.
Alle vijf komen uit dezelfde oorzaak: het accent was in het oude template geel
en licht, en is nu marineblauw en donker. Waar zwarte tekst op geel goed las,
verdwijnt die op marineblauw.

| Waar | Was | Nu | Correctie |
|---|---|---|---|
| Cookieknop "Toestaan" | zwart op accent, 1,71:1 | wit op accent, 12,30:1 | `--color-text-on-accent` |
| Skip-link "Naar de inhoud" | zwart op accent, 1,71:1 | wit op accent, 12,30:1 | `--color-text-on-accent` |
| Primaire knop | zwart op accent | wit op accent, 12,30:1 | `--color-text-on-accent` |
| Pijl in de ronde icoonknop | donker op accent, 1,05:1 | wit op accent, 12,30:1 | `--color-white`, in rust en bij hover |
| Link op een indigo vlak | naar accent bij hover, 1,23:1 | naar `--color-secondary`, 6,83:1 | mist-tint |

### Witte tekst over de herofilm

De hero heeft een filmopname met witte tekst erover. Daar helpt een berekening
op vlakke kleuren niet: een echte opname heeft lichte frames. De sluier over de
film is daarom nagemeten door tien frames op canvas te leggen en per tekstvlak
de **lichtste pixel** te nemen, met de dekking van de sluier op die hoogte
erover.

Met de oorspronkelijke sluier (`rgba(0,0,0,.30)` naar `.70`) haalde de witte
navigatie boven in de hero **2,34:1**, ruim onder de 4,5:1 die tekst van 14px
nodig heeft. De sluier heeft nu drie stops in plaats van twee: donkerder waar
tekst staat, iets lichter in het midden waar niets staat en de foto mag ademen.

| Tekstvlak | Grootte | Eis | Slechtste frame |
|---|---|---|---|
| Navigatie | 14px | 4,5:1 | 6,31:1 |
| Label boven de kop | 11px | 4,5:1 | 5,23:1 |
| Paginakop | 72px | 3:1 | 4,85:1 |
| Introtekst | 18px | 4,5:1 | 6,68:1 |

Wordt de film ooit vervangen, dan moet deze meting opnieuw: een lichtere opname
kan dit onderuit halen. Het script staat in de commentaarregels bij
`.hero--sluier` in `index.css`.

De pijl in de ronde icoonknop is daarbij eerst verkeerd gelezen. De correctie
stond aanvankelijk alleen op `:hover`, in de veronderstelling dat de
accentvulling in rust een pilletje rechts naast de pijl is. Dat is niet zo: de
rustklem `inset(8px 8px 8px calc(100% - 50px))` komt bij een knop van 48 of
54px op een linkerinset van 0 tot 6px uit, dus de vulling ligt ook in rust al
onder de pijl. De pijl haalde daar 1,05:1 en was dus in rust onzichtbaar. Hij
is nu wit in beide toestanden.

### Knoppen: het vlak zelf gemeten

Bij de contrastcontrole is eerst alleen tekst gemeten. Een knop is echter ook
zelf een UI-element: het vlak moet 3:1 halen tegen de band eronder, anders zie
je de knop niet staan. Die meting is later toegevoegd en legde vier fouten
bloot, alle vier terug te voeren op één oorzaak: de primaire vulling is navy en
werkt alleen op een lichte ondergrond, de secundaire is wit en werkt alleen op
een donkere. Beide stonden ergens op de verkeerde band.

| Waar | Was | Vorm | Nu | Vorm |
|---|---|---|---|---|
| CTA-vlak, alle pagina's | navy op patroon | 2,05:1 | wit op patroon | 6,00:1 |
| Over-ons op de homepage | wit op wit | 1,00:1 | diepste indigo op wit | 14,93:1 |
| "Onze werkwijze", dienst en offerte | wit op lichtgrijs | 1,09:1 | diepste indigo op lichtgrijs | 13,69:1 |
| Kaart in het uitklapmenu | navy op de sluier | 1,24:1 | wit op de sluier | 9,91:1 |
| Hero homepage | navy op de film | 1,54:1 | **uitgezonderd**, nu paars | 1,25:1 |

In het CTA-vlak wisselen de twee vullingen van rol: primair wordt wit met navy
tekst (vorm 6,00:1, label 12,30:1), secundair wordt Duyts Mist met navy tekst
(vorm 4,10:1, label 8,39:1). Beide blijven massieve vlakken; het template kent
geen omlijnde knop en die is er ook niet bij verzonnen. Het onderscheid zit in
de toon.

Neutraal grijs `#F5F5F5` lag als secundaire vulling meer voor de hand, maar dat
haalt naast wit slechts 1,09:1: de twee knoppen zouden als één vulling lezen.
De mist zit met 1,47:1 plus een koele tint zichtbaar onder het wit, en is een
bestaand merktoken waarvan de rol al "op donkere merkvlakken" is.

**De hero is hier bewust van uitgezonderd.** Daar staat de navy knop over de
film. In de hero is de werkelijke ondergrond de film en niet het indigo vlak
eronder: de knoppen staan op 88% van de hoogte, waar de sluier 65% dekt.
Twaalf frames zijn op canvas bemonsterd over de knoppenstrook, en op de
lichtste pixel die daarbij voorkwam haalt het navy vlak 1,78:1, tegen een eis
van 3:1 voor een UI-element. Dat is een afwijking die op verzoek zo is
gelaten, zodat de hero zijn oorspronkelijke knoppen houdt.

De afwijking raakt alleen de *omtrek* van de knop, niet de leesbaarheid van wat
erin staat: het witte label op het navy vlak haalt 12,30:1. Wie de knop ziet,
kan hem dus lezen; het risico is dat de knop minder opvalt tegen een licht
filmbeeld. Draaien we hem ook daar om, dan haalt wit 6,92:1 en mist 4,72:1 over
diezelfde frames; de regel daarvoor staat bij `.cta-slot__hoofd` in
`styleguide.css`.

**Focus.** De focusring staat standaard in het diepste indigo en viel op een
donker vlak weg (1,3:1). Binnen de donkere vlakken, hero inbegrepen, is die nu
wit; dat haalt 6:1 of meer en voldoet aan de 3:1 die WCAG 2.2 voor de
focusindicator vraagt. Dat is geen knopkleur maar de focusindicator, en die is
dus wel overal aangepast.

### De CTA-knop staat in de merkkleur, niet in het accent

De primaire knop stond in het navy accent `#143369`. Die is op verzoek naar de
merkkleur `#463878` gegaan, samen met de CTA-pil in de balk: twee CTA's naast
elkaar in twee verschillende kleuren leest als een fout.

| Waar | Rust | Hover | Ingedrukt |
|---|---|---|---|
| `.button--primary` | `#463878` | `#3A2E63` | `#2A2147` |
| `.submenu--link.highlight` | `#463878` | `#3A2E63` | — |

Wit haalt op `#463878` 10,01:1 en het vlak zelf haalt datzelfde tegen wit en
9,18:1 tegen het subtiele grijs; ruim boven de 4,5:1 voor het label en de 3:1
voor het vlak. Het was 12,30:1 op het navy, dus een stap minder maar nog steeds
AAA.

Het accent `#143369` blijft wel het accent voor links en kleine vlakken. Alleen
de knopvulling is veranderd. Wat bewust navy is gebleven: de ronde icoonknoppen
op de kaarten (`.button--icon .button--circle`), het eerste vlak van de
vlakkenrij (`.vlak--geel`) en de markering `[CONTENT NODIG]` (`.invulveld`).
Die horen niet tot de CTA-familie.

**Twee dingen zijn hierdoor slechter geworden, en die staan er bewust zo:**

De hover van de CTA-pil in de balk ging naar `--color-groen`, en dat is nu de
rustkleur zelf; hij gaat daarom een stap donkerder, naar `--color-primary-deep`.

En de knop in de hero. Die valt buiten de omkering voor donkere vlakken, dus
daar staat nu een paarse knop op een donkere film: 1,25:1, waar het navy 1,54:1
haalde. Beide zitten onder de 3:1 die een UI-element vraagt. De meting staat bij
`.cta-slot__hoofd` in `styleguide.css`, met de regel die er wit van maakt
(8,01:1) als dat toch de voorkeur krijgt.

### Twee blinde vlekken in de meting

Twee fouten zijn pas laat gevonden, en beide om dezelfde reden: wat niet
zichtbaar is, wordt niet gemeten.

**Verborgen elementen.** Het contrastscript slaat over wat `display: none`,
`visibility: hidden` of nul groot is. Het uitklapmenu is dat allemaal zolang je
het niet opent, dus de kaart erin is in geen enkele eerdere ronde nagemeten.
Daar stond een navy knop op een donkere sluier: 1,24:1. Gevonden door het menu
in de meting eerst te openen. Dezelfde regel geldt voor de mobiele lade en voor
alles wat achter een klik zit; wie hier later iets aan verandert, moet die
panelen expliciet openzetten voordat hij meet.

**Kleuren in een rgba-notatie.** De kleurwissel van petrol naar indigo is
gedaan op tokens en hexwaarden. Drie sluiers stonden als losse rgba geschreven
(`rgba(1, 126, 132, .20)`) en kwamen daar niet in mee: de kaart in het
uitklapmenu, en de dode regels in `cases.css` en `cursus.css`. Bij de kaart was
het commentaar erboven wél bijgewerkt naar `#463878`, de waarde eronder niet —
de gradient bleef dus groen terwijl de documentatie indigo beloofde. Alle drie
staan nu op `rgba(70, 56, 120, …)`.

De kaarttekst werd daar beter van, want indigo is donkerder dan petrol: de kop
gaat van 5,6 naar 9,06:1 en de body van 5,7 naar 9,51:1.

### Witte tekst op de merkpatronen

Het slotblok met de CTA en de paginahero's dragen een merkpatroon als
achtergrondbitmap, met witte tekst erover. Dat is dezelfde situatie als de
herofilm: op een bitmap zegt een berekening op vlakke kleuren niets, want het is
de lichtste plek die het contrast bepaalt.

Alle acht patroonbestanden zijn daarom pixel voor pixel doorgerekend (elke
tweede pixel, hele bitmap). Voor het CTA-patroon:

| Meetpunt | Wit erop |
|---|---|
| donkerste pixel | 11,32:1 |
| mediaan | 8,57:1 |
| 95e percentiel | 6,84:1 |
| **lichtste pixel** | **6,00:1** |

De lichtste pixel van het hele vlak haalt dus nog 6,00:1, tegen een eis van
4,5:1 voor normale tekst en 3:1 voor de kop. Over alle acht bestanden ligt die
ondergrens tussen 6,00 en 6,29:1. Er is dus geen waas nodig en die zit er ook
niet: het patroon staat op volle sterkte.

Dat is een verandering ten opzichte van het patroon dat er eerder lag. Dat had
lichte gele stralen, en daar zakte het label op de lichtste plekken naar
1,76:1 en de kop naar 2,03:1. Die combinatie stond als bewuste afwijking in de
CSS gedocumenteerd; met het huidige indigo patroon is de afwijking vervallen en
is die documentatie vervangen door de meting hierboven.

Wordt een patroonbitmap vervangen, dan moet dit opnieuw gemeten worden. De
ondergrens is een lichtste pixel die met wit nog 4,5:1 haalt, ongeveer
`#7A7A7A`. Haalt een nieuw patroon dat niet, dan hoort er een waas in de
merkkleur over tot het wel klopt; de regel daarvoor staat in het commentaar bij
`.cta-slot__hoofd` in `styleguide.css`.

### Muted tekst

`--color-text-muted` `#636363` haalt 6,01:1 op wit en 5,51:1 op het subtiele
grijs, dus ook als normale tekst ruim boven de eis. De lichtere grijzen uit de
bronsite (`#b5b5b5` op 2,05:1, `#adadad`, `#cecece`) zijn niet overgenomen: die
zaten onder de eis en zijn in de consolidatie geschrapt. Er staat dus nergens
functionele informatie in een grijs dat te licht is.

### De accentkleur als CTA

Het accent `#143369` is zowel tegen de lichte als tegen de donkere kant
gecontroleerd: 12,30:1 op wit, 11,28:1 op het subtiele grijs, en 12,30:1 voor de
witte tekst óp het accent. Het valt daarmee ook als vlak duidelijk weg van zijn
omgeving.

Eén combinatie is uitgesloten: het accent op de primaire indigo haalt 1,23:1.
Een marineblauwe knop op een indigo vlak is dus niet te zien. Op indigo
secties gebruikt de site daarom de witte knopvariant die het template al had.

Voor `--color-border-soft` `#E6E6E6` geldt geen tekstcontrasteis; gebruik deze token niet
voor tekst of voor randen die informatie moeten dragen.

Twee punten die van het template afhangen en dus buiten deze merklaag vallen: geef links
naast kleur ook een niet-kleurgebonden markering (het template bepaalt of dat onderstreping
of iets anders is), en houd de bestaande focus-indicators intact.

---

## Implementation Rules

### DO

- Pas alleen kleur tokens aan
- Pas alleen font-family tokens aan
- Pas alleen relevante font weights aan (700/800 heading, 400/600 body)
- Pas alleen line-height en letter-spacing per typeniveau aan zoals hierboven
- Behoud de bestaande responsive type scale
- Behoud bestaande componenten
- Behoud bestaande spacing
- Behoud bestaande interacties
- Laad Assistant en Karla daadwerkelijk in (de bronsite doet dat niet)

### DO NOT

- Geen buttonvormen aanpassen
- Geen border radius aanpassen
- Geen padding aanpassen
- Geen margin aanpassen
- Geen gap aanpassen
- Geen grid aanpassen
- Geen flex layouts aanpassen
- Geen container widths aanpassen
- Geen shadows kopiëren
- Geen cards restylen
- Geen hover effects kopiëren
- Geen animations kopiëren
- Geen transitions kopiëren
- Geen component markup aanpassen
- Geen bestaande responsive logica veranderen
- Geen font sizes uit de bronwebsite overnemen
- Geen `text-transform` uit de bronwebsite overnemen
- Geen extra kleuren toevoegen buiten de acht tokens
