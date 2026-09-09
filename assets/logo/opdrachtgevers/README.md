# Beeldmerken van opdrachtgevers

Deze map is leeg zolang er geen logo's zijn. De band op de site laat nu
woordmerken zien (de groepen die Duyts zelf op /over-ons/ noemt).

## Een logo toevoegen

1. Zet het bestand hier neer. SVG heeft de voorkeur; anders PNG met
   transparante achtergrond, op minimaal 380px breed (2x voor retina).
2. Zet het in `OPDRACHTGEVERS` in `_generator/schil.py`, als paar van
   bestand en naam:

   ```python
   OPDRACHTGEVERS = [
       ("ballast-nedam.svg", "Ballast Nedam"),
       ("stork.svg",         "Stork"),
   ]
   ```

3. `python3 _generator/bouw_alles.py`

Namen en woordmerken kunnen door elkaar in dezelfde lijst staan.

## Maten

De band rendert elk logo op **40px hoog** (32px onder 768px breed) met
`max-width: 190px` en `object-fit: contain`. Een breed liggend logo loopt dus
tegen de breedte aan en wordt iets lager; een compact logo houdt de volle
hoogte. Dat is bewust: zo krijgen merken van heel verschillende verhouding
optisch ongeveer gelijk gewicht in plaats van gelijke hoogte.

Lever het logo aan met zo weinig mogelijk witruimte in het bestand zelf,
anders lijkt het kleiner dan de rest.

## Let op

Een logo in deze band leest als "dit bedrijf is klant van Duyts". Zet er dus
alleen beeldmerken in van opdrachtgevers die dat daadwerkelijk zijn en die
toestemming hebben gegeven voor gebruik van hun merk.

Bij het template zat een band met Huhtamaki, Ballast Nedam, Alstom, Stork, TES
en Electrabel. Dat zijn geen klanten van Duyts; die bestanden zijn bij de
migratie verwijderd en staan hier niet.
