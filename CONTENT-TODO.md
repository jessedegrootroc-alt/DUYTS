# Wat er nog van Duyts nodig is

Deze site is gevuld met de content van www.duyts.nl. Wat de bronsite niet had,
staat op de pagina's als `[CONTENT NODIG]` in een opvallend blokje, zodat het
niet per ongeluk zo live gaat. Op dit moment zijn dat 107 markeringen.

## 1. Projectgegevens (36 projecten, 2 velden per project)

De bronsite noemt bij geen enkel project een **opdrachtgever** of een
**jaar van uitvoering**. Beide velden staan op elke projectpagina leeg.

Bij vier projecten noemt de tekst zelf de opdrachtgever (Vast Food BV, Gerose
Vastgoed Ontwikkeling BV en twee ontwikkelaars zonder naam); die staan nog niet
in het veld omdat niet zeker is of ze genoemd mogen worden. **Voor het tonen van
een opdrachtgevernaam is toestemming van die partij nodig.**

Ook de **plaats** ontbreekt bij 29 van de 36 projecten. Waar de projecttekst een
plaats noemt, is die overgenomen (Amsterdam, Amstelveen, Woerden, Muiden).

## 2. Openingstijden

Staan niet op de bronsite en staan nu **nergens** op de site. Ze stonden als
markering op de contactpagina, maar die gegevens hangen daar sinds 9 september
in de vlakkenrij onder het formulier, en een leeg gekleurd vlak met
`[CONTENT NODIG]` erin leest als een fout in het ontwerp.

Zodra Duyts ze aanlevert: in `bouw_duyts_contact.py`, in de lijst `gegevens`,
achter het telefoonnummer aan het telefoonvlak toevoegen. Dan blijft de rij op
vier vlakken; een vijfde vlak begint de kleurenreeks opnieuw en breekt het
ritme.

## 3. Privacyverklaring en cookieverklaring

De bronsite heeft geen van beide. Op `privacybeleid.html` en `cookies.html` staat
nu alleen de AVG-passage die bij de formulieren van Duyts stond, plus een
markering. Dit is een juridische tekst: die moet van Duyts komen, niet van ons.
De cookiemelding op de site linkt naar deze twee pagina's.

## 4. Het formulier verstuurt niets

`ENDPOINT` in `contactformulier.js` is leeg. Je krijgt wel een succesmelding,
maar er gaat geen bericht de deur uit. Dit gold al voor het template.

Op de offertepagina kunnen **geen bestanden** worden meegestuurd. De bronsite
had daar een upload tot 20 MB; de tekst eronder verwijst nu naar de mail, zoals
de bronsite dat zelf ook doet voor grotere bestanden.

## 5. Twee cijfers die elkaar tegenspreken

De bronsite zegt op één plek "al 25 jaar" (meta description homepage) en op
andere plekken "sinds 1981". Ook: "circa 25 tekenaars, constructeurs en
specialisten" naast "een groep van 25 enthousiaste personen". Deze site gebruikt
**1981** en **circa 25**. Laat Duyts vaststellen wat klopt.

## 6. Wat er is bijgeschreven en gecontroleerd moet worden

De dienstpagina's hebben naast de technische uitleg van de bronsite een
verhaallaag: wanneer iets aan de orde is, hoe het traject verloopt, wat je krijgt
aangeleverd en veelgestelde vragen. Dat is vakinhoud, geschreven op basis van de
KCAF-richtlijn Funderingen onder gebouwen (2023), de Wet kwaliteitsborging voor
het bouwen en de gangbare ontwerpfasen. Het staat in
`_generator/inhoud_dienst_verhaal.py`, met bovenaan dat bestand precies wat uit
de bron komt en wat is bijgeschreven.

**Laat Duyts die teksten nalezen.** Er staan geen doorlooptijden, tarieven,
certificaten of garanties in, juist omdat dat uitspraken over het bedrijf zijn.
Wil Duyts die er wél in, dan kunnen ze erbij.

## 7. Beeld

Alle foto's komen van de bronsite en zijn eigendom van Duyts. Op enkele foto's
staan medewerkers; die stonden ook op de bronsite. Herkomst per bestand staat in
`assets/foto/HERKOMST.md`.

De film in de hero is door de opdrachtgever aangeleverd.

## Logoband met opdrachtgevers

**De dertien logo's in de band zijn klanten van MADEGRO, niet van Duyts.** Ze
staan er sinds 9 september op verzoek. Net als bij de citaten *staat* hier iets
wat niet klopt in plaats van dat er iets ontbreekt: er is geen
`[CONTENT NODIG]`-markering die je eraan herinnert.

Alstom, Ballast Nedam, Bilfinger, Cosun Beet Company, Ebert Hera, Electrabel,
Freesmij, GE Vernova, Huhtamaki, Ivens, Ooms Bouw &amp; Ontwikkeling, Stork en
TES Industrial Systems. Herkomst en bewerking staan in
`assets/logo/opdrachtgevers/HERKOMST.md`: Martin heeft ze voor de MADEGRO-site
aangeleverd, en ze komen overeen met de klantenlijst op zijn LinkedIn.

Duyts is een ander bedrijf. Zolang deze logo's hier staan, zegt de band dat
Duyts voor Alstom en Ballast Nedam werkt.

- [ ] Vervangen door opdrachtgevers van Duyts, met toestemming per bedrijf om
      hun logo te tonen. Bij sommige klanten ligt er een geheimhoudingsafspraak
      over de opdracht of over het noemen van de naam.

**Terugschakelen naar de onderbouwde variant** kost één regel: in
`_generator/schil.py` staat `OPDRACHTGEVERS_GROEPEN` met de groepen die Duyts
zelf op /over-ons/ noemt (particulieren, VvE's, architecten, aannemers,
projectontwikkelaars, woningbouwverenigingen). Zet die lijst op
`OPDRACHTGEVERS` en de band rendert weer woordmerken in tekst, met hetzelfde
ritme en dezelfde hoogte.

**Nieuwe logo's toevoegen:** zie het README in
`assets/logo/opdrachtgevers/`. Elk item is `(bestand, naam, breedte, hoogte)`,
waarbij breedte en hoogte de natuurlijke maten van het bestand zijn: die leggen
alleen de verhouding vast, want de stylesheet zet elk logo op 40px hoog met
`max-width: 190px`. Geef ze mee, anders verspringt de band tijdens het laden.

**Geen `loading="lazy"` op deze afbeeldingen.** Het venster van de band knipt af
met `overflow: hidden`, dus de browser ziet alles rechts van de rand als "niet
in beeld" en laadt het nooit; de laatste logo's bleven daardoor leeg.

**Ongebruikt:** `assets/logo/opdrachtgevers/origineel/` bevat zestien PNG's uit
een eerdere ronde die nergens meer gebruikt worden, en `samenwerking/` drie die
ook nergens ingehangen zijn. Die kunnen weg.

## Referenties (citaten van opdrachtgevers)

**De drie citaten op de site zijn verzonnen.** Ze staan er op verzoek, zodat de
sectie afgemaakt kon worden, en moeten vóór livegang vervangen worden door
echte referenties. Dit is het enige punt in deze lijst waar iets *staat* wat
niet klopt, in plaats van dat er iets ontbreekt: er is dus geen
`[CONTENT NODIG]`-markering die je eraan herinnert.

De sectie staat op de homepage (onder het statement), op `contact.html` en op
`offerte.html`.

**Wat er wel echt is:** de foto's en de projecten. Drie projecten uit de export
met hun eigen beeld en plaats: Chass&#769;kerk, Artis en Stadsvilla Amsterdam.

**Wat er bewust niet verzonnen is:**

- Namen van bestaande bedrijven. De citaten staan op de rol van de
  opdrachtgever ("Architect", "Aannemer", "Particuliere opdrachtgever"), niet op
  naam van een architectenbureau of aannemer. Een verzonnen citaat op naam van
  een bestaande partij is een uitspraak over die partij.
- Logo's. Zonder bedrijfsnaam is er ook geen logo, en er is geen enkel
  logobestand van een opdrachtgever. Het slot (`.quote__logo`) blijft leeg.
- Feiten over Duyts. De citaten noemen geen doorlooptijden, prijzen,
  certificeringen of garanties; ze gaan over hoe het werken met een
  constructeur gaat.

**Vervangen:** in `_generator/schil.py`, in de lijst `REFERENTIES`. Elk item is
`(projectbeeld, projectnaam, plaats, citaat, wie-het-zegt, logobestand)`. Zet er
een echt citaat en een echte naam in; zet een logobestand in
`assets/logo/opdrachtgevers/` en noem het in het zesde veld, dan komt het logo
onder de naam. Daarna `python3 _generator/bouw_alles.py`.

Vraag bij het ophalen van een citaat ook toestemming om de naam en het logo te
gebruiken; zonder dat mag het er niet op.

**De sectie loopt automatisch door.** Elke seconde het volgende citaat. Die
duur staat op één plek: `QUOTE_DUUR` bovenaan het citatenblok in `site.js`, en
het balkje in de navigatie loopt automatisch mee. Eén seconde is te kort om een
citaat van drie regels te lezen; 6000 tot 7000 ms leest rustiger. Het doorlopen
stopt bij 'beweging uit' in het systeem, staat stil zolang de muis erop staat of
er iets in de sectie focus heeft, en stopt voorgoed zodra iemand zelf op een
pijl klikt.
