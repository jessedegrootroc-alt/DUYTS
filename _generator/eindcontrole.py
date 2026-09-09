# -*- coding: utf-8 -*-
"""Controleert de gegenereerde pagina's op fouten die je met het oog mist.

    python3 _generator/eindcontrole.py

Draai dit na `bouw_alles.py`. Het kijkt niet of de site mooi is; het kijkt of er
niets kapot of dubbel is. Wat het nagaat:

  - kapotte interne links
  - precies één <h1> per pagina, en geen sprong in de koppenniveaus
  - unieke <title> en meta-omschrijving, en geen lege
  - resten van het oude template (madegro, lorem, TODO-CONTENT)
  - oude contactgegevens en oude merkkleuren
  - lege alinea's en afbeeldingen zonder alt
  - dubbele labels in de navigatie
  - hoeveel [CONTENT NODIG]-markeringen er staan (die horen er te zijn)
"""
import collections
import pathlib
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
PAGINAS = sorted(WORTEL.glob('*.html'))

# Dingen die er niet meer in mogen staan.
VERBODEN = [
    (r'(?i)madegro', 'madegro'),
    (r'(?i)lorem ipsum', 'lorem'),
    (r'TODO-CONTENT', 'todo'),
    (r'0182[\s-]?\d{6}', 'oud telefoonnummer'),
    (r'(?i)gouda|moordrecht', 'oud adres'),
    (r'#017E84|#0d7377|rgba\(1,\s*126,\s*132', 'oude merkkleur'),
]


def tekst(el):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', el)).strip()


def main():
    print(f'EINDCONTROLE ({len(PAGINAS)} pagina\'s)\n')
    fouten = []
    bestanden = {p.name for p in PAGINAS}
    titels, omschrijvingen = collections.defaultdict(list), collections.defaultdict(list)
    markeringen = 0

    kapot, geen_h1, sprongen, leeg_alinea, geen_alt, dubbel_nav = [], [], [], [], [], []

    for p in PAGINAS:
        h = p.read_text(encoding='utf-8')

        # interne links
        for m in re.finditer(r'href="(?!https?:|mailto:|tel:|#)([^"#?]+)', h):
            doel = m.group(1)
            if doel.endswith('.html') and doel not in bestanden:
                kapot.append(f'{p.name} -> {doel}')

        # koppen
        h1 = re.findall(r'<h1\b', h)
        if len(h1) != 1:
            geen_h1.append(f'{p.name} ({len(h1)})')
        niveaus = [int(m.group(1)) for m in re.finditer(r'<h([1-6])\b', h)]
        vorig = 0
        for n in niveaus:
            if vorig and n > vorig + 1:
                sprongen.append(f'{p.name}: h{vorig} -> h{n}')
            vorig = n

        # title en omschrijving
        t = re.search(r'<title>(.*?)</title>', h, re.S)
        d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
        titels[tekst(t.group(1)) if t else ''].append(p.name)
        omschrijvingen[tekst(d.group(1)) if d else ''].append(p.name)

        # Lege alinea's. Een live region mag wél leeg zijn: die wordt door
        # JavaScript gevuld, en hij moet al in de DOM staan voordat er iets in
        # komt, anders kondigt een schermlezer de wijziging niet aan. Zo werkt
        # de tellerregel op projecten.html.
        for m in re.finditer(r'<p((?:[^>"]|"[^"]*")*)>\s*</p>', h):
            attr = m.group(1)
            if 'aria-live' in attr or 'role="status"' in attr:
                continue
            leeg_alinea.append(p.name)
        for m in re.finditer(r'<img\b((?:[^>"]|"[^"]*")*)>', h):
            if 'alt=' not in m.group(1):
                geen_alt.append(p.name)

        # dubbele labels in de balk
        nav = re.search(r'<nav class="submenu".*?</nav>', h, re.S)
        if nav:
            labels = [tekst(x.group(2)) for x in
                      re.finditer(r'<(a|button)[^>]*>(.*?)</\1>', nav.group(), re.S)]
            labels = [l for l in labels if l]
            for label, aantal in collections.Counter(labels).items():
                if aantal > 1:
                    dubbel_nav.append(f'{p.name}: "{label}" {aantal}x')

        markeringen += len(re.findall(r'\[CONTENT NODIG\]', h))

    def regel(naam, lijst, toon=3):
        vlag = 'FOUT' if lijst else 'ok  '
        extra = f'  {lijst[:toon]}' if lijst else ''
        print(f'  {vlag} {naam:34s} {len(lijst)}{extra}')
        if lijst:
            fouten.append(naam)

    regel('kapotte interne links', kapot)
    regel('pagina\'s zonder precies 1 h1', geen_h1)
    regel('sprongen in koppenniveaus', sprongen)
    regel('lege alinea\'s', leeg_alinea)
    regel('afbeeldingen zonder alt', sorted(set(geen_alt)))
    regel('dubbele labels in de navigatie', dubbel_nav)

    for veld, kaart in (('title', titels), ('omschrijving', omschrijvingen)):
        dubbel = {k: v for k, v in kaart.items() if k and len(v) > 1}
        leeg = kaart.get('', [])
        regel(f'dubbele {veld}', [f'{k[:30]}: {v}' for k, v in dubbel.items()], 1)
        regel(f'lege {veld}', leeg)

    for patroon, label in VERBODEN:
        treffers = [p.name for p in PAGINAS
                    if re.search(patroon, p.read_text(encoding='utf-8'))]
        regel(label, treffers)

    print(f'\n  [CONTENT NODIG]-markeringen: {markeringen} (bewust: ontbrekende brondata)')
    print('\nRESULTAAT: ' + ('ALLES OK' if not fouten else 'AANDACHT: ' + ', '.join(fouten)))
    return 1 if fouten else 0


if __name__ == '__main__':
    sys.exit(main())
