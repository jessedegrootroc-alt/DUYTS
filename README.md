# Duyts Bouwconstructies: website

Statische site: HTML, CSS en vanilla JavaScript, geen build-stap en geen
npm-afhankelijkheden. Van een CDN komen alleen GSAP (met ScrollTrigger en
ScrollSmoother) en Barba.js; samen doen die de pagina-overgangen en het vloeiende
scrollen. De lettertypen staan lokaal in `assets/fonts/`.

## Lokaal draaien

Open `index.html` in de browser, of draai een server vanuit deze map:

    python3 -m http.server 5500 --bind 127.0.0.1

Alle links zijn relatief, dus de map kan zonder aanpassing als eigen site
gepubliceerd worden.

## De pagina's zijn gegenereerd

De 73 HTML-bestanden in deze map worden gemaakt door de scripts in
`_generator/`. **Pas je een HTML-bestand met de hand aan, dan is die wijziging
weg zodra de generator opnieuw draait.**

    cd _generator && python3 bouw_alles.py

| bestand | wat het doet |
|---|---|
| `duyts/` | de contentexport van www.duyts.nl: hier staan alle teksten |
| `inhoud_duyts.py` | welke pagina's er zijn, welke dienst waar hangt, welke foto erbij hoort |
| `inhoud_dienst_verhaal.py` | de verhaallaag onder de dienstpagina's (situaties, aanpak, oplevering, vragen) |
| `schil.py` | de gedeelde onderdelen: balk, voettekst, hero's, knoppen, kaarten, beeld |
| `bouw_duyts_home.py` | `index.html` |
| `bouw_duyts_dienst.py` | de 25 dienstpagina's |
| `bouw_duyts_projecten.py` | het projectenoverzicht en de 36 projectpagina's |
| `bouw_duyts_bedrijf.py` | over ons, historie, team, registerconstructeur, werkwijze, vacatures |
| `bouw_duyts_contact.py` | contact, offerte, privacybeleid, cookies |
| `bouw_duyts_sitemap.py` | `sitemap.xml` en `robots.txt` |
| `maak_assets.py` | zet de beelden uit de export om naar responsive WebP (alleen nodig bij nieuw beeld) |

De CSS, de JavaScript en alles in `assets/` worden **niet** gegenereerd; die
bewerk je rechtstreeks.

## Structuur

```
index.html                  Home
verbouwing.html             ┐
fundering.html              ├ drie hoofddiensten
nieuwbouw.html              ┘
muurdoorbraak.html ... tafelconstructie.html    vijftien werkzaamheden
constructieberekening.html  stabiliteitsberekening.html
schaderapportage.html       certificaat-funderingsherstel.html
projecten.html              overzicht met filter op categorie
project-*.html              36 projectpagina's
over-ons.html  historie.html  het-team.html
registerconstructeur.html  werkwijze.html  vacatures.html
offerte.html  contact.html
privacybeleid.html  cookies.html

brand-style.md              de merklaag: kleuren en typografie
STYLEGUIDE.md               het ontwerpsysteem en waar deze site afwijkt
SECTIONS.md                 het sectieskelet dat de pagina's delen
CONTENT-TODO.md             wat er nog van Duyts nodig is
```

## Werken aan deze site

- Een tekst wijzigen: in `_generator/duyts/` (de export), daarna opnieuw bouwen.
- Een nieuw project of een nieuwe dienst: één regel in `inhoud_duyts.py`.
- Nieuwe kleuren of fonts: alleen de tokens in `styleguide.css`, zie `brand-style.md`.
- Het contactformulier verstuurt nog niets: zet het endpoint in `contactformulier.js`.
- Statistieken laden pas na toestemming en alleen met een meet-ID in `analytics.js`.
