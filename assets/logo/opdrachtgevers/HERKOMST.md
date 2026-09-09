# assets/partners: logo's van opdrachtgevers

In de logoband staan dertien opdrachtgevers van MADEGRO, met de logo's die
Martin heeft aangeleverd (1 september 2026). Ze komen overeen met de lijst die
hij op zijn LinkedIn-profiel noemt.

| Bestand | Opdrachtgever |
|---|---|
| `alstom.webp` | Alstom |
| `ballast-nedam.webp` | Ballast Nedam |
| `bilfinger.webp` | Bilfinger |
| `cosun.webp` | Cosun Beet Company |
| `ebert-hera.webp` | Ebert Hera |
| `electrabel.webp` | Electrabel / GDF Suez |
| `freesmij.webp` | Freesmij |
| `ge-vernova.webp` | GE Vernova |
| `huhtamaki.webp` | Huhtamaki |
| `ivens.webp` | Ivens |
| `ooms.webp` | Ooms Bouw &amp; Ontwikkeling |
| `stork.webp` | Stork |
| `tes.webp` | TES Industrial Systems |

Van vijf opdrachtgevers die Martin noemt is geen logo aangeleverd: BAM Infra,
NEM Standaard Kessel, Fisia Babcock, AEB Amsterdam en Fitweld. Die staan niet in
de band; logo's en losse namen door elkaar leest rommelig.

## Hoe ze gemaakt zijn

De aangeleverde bestanden staan onveranderd in `bron/`: PNG's van 640x240 met
veel wit eromheen. Ongesneden zouden ze allemaal even klein worden, dus de rand
gaat eraf voordat er geschaald wordt.

    # wit en doorzichtig eraf snijden, dan naar 80px hoog
    # (zie de functie snij() in de bouwscripts)
    cwebp -q 78 -alpha_q 100 bron/<naam>.png -o <naam>.webp

80 px hoog omdat de band ze op 40 px toont; dat dekt een scherm met dubbele
pixeldichtheid precies. Samen 118 kB.

De echte breedte per logo staat in `OPDRACHTGEVERS` in het bouwscript en komt
als `width` in de HTML, zodat er geen sprong in de band zit terwijl ze laden.

**Geen `loading="lazy"` op deze afbeeldingen.** Het venster van de band knipt af
met `overflow: hidden`, dus de browser ziet alles rechts van de rand als "niet in
beeld" en laadt het nooit. De laatste vier logo's bleven daardoor leeg.

## Nog te regelen

Dit zijn beeldmerken van bestaande bedrijven. Laat Martin per opdrachtgever
bevestigen dat hij hun logo op zijn site mag tonen. Bij de meeste klanten is dat
een formaliteit, bij sommige ligt er een geheimhoudingsafspraak over de opdracht
of over het noemen van de naam.

## origineel/

Daar staan nog zestien PNG's uit een eerdere ronde: logo's die uit de
referentiesite kwamen en géén klant van MADEGRO zijn. Ze worden nergens gebruikt
en kunnen weg.
