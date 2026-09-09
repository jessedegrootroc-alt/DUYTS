#!/usr/bin/env python3
"""Zet de afbeeldingen uit de Duyts-export om naar de assets van deze site.

Twee dingen gebeuren hier:

1. Het logo. Het bestand uit de export is een wit merk op een indigo vlak. De
   header vraagt twee losse varianten op een doorzichtige achtergrond: een
   gekleurde voor de witte balk en een witte voor de indigo balk. De indigo
   wordt daarom uit het beeld gehaald en de dekking van elke pixel komt uit hoe
   wit die pixel was; zo blijven de ruwe randen van de getekende kubus zacht.

2. De foto's. De template vraagt per beeld meerdere breedtes in WebP (zie
   foto() in schil.py). cwebp maakt ze; de ladder hangt af van waar het beeld
   staat, precies zoals bij de bestaande foto's.

Draaien:  python3 maak_assets.py
"""
import json, pathlib, subprocess, sys
from PIL import Image

HIER   = pathlib.Path(__file__).resolve().parent
WORTEL = HIER.parent
EXPORT = pathlib.Path('/tmp/duyts/export')          # uitgepakte duyts-website-export.zip
FOTO   = WORTEL / 'assets' / 'foto'
LOGO   = WORTEL / 'assets' / 'logo'

INDIGO = (70, 56, 120)

# ---------------------------------------------------------------- logo
def _alfa_uit_wit(im):
    """Dekking = hoe wit de pixel was; de indigo achtergrond wordt doorzichtig."""
    im = im.convert('RGB')
    lum_bg = 0.2126*INDIGO[0] + 0.7152*INDIGO[1] + 0.0722*INDIGO[2]
    lum_wit = 255.0
    breed, hoog = im.size
    alfa = Image.new('L', (breed, hoog))
    bron, doel = im.load(), alfa.load()
    for y in range(hoog):
        for x in range(breed):
            r, g, b = bron[x, y]
            lum = 0.2126*r + 0.7152*g + 0.0722*b
            t = (lum - lum_bg) / (lum_wit - lum_bg)
            doel[x, y] = max(0, min(255, round(t * 255)))
    return alfa

def maak_logos():
    bron = EXPORT / 'images' / 'brand' / 'duyts-logo.png'
    im = Image.open(bron)
    alfa = _alfa_uit_wit(im)
    vak = alfa.getbbox()                      # wegsnijden wat leeg is
    marge = 6
    vak = (max(0, vak[0]-marge), max(0, vak[1]-marge),
           min(im.size[0], vak[2]+marge), min(im.size[1], vak[3]+marge))
    alfa = alfa.crop(vak)
    LOGO.mkdir(parents=True, exist_ok=True)
    gemaakt = []
    for naam, kleur in [('duyts-logo-wit.png', (255, 255, 255)), ('duyts-logo.png', INDIGO)]:
        vlak = Image.new('RGBA', alfa.size, kleur + (0,))
        vlak.putalpha(alfa)
        hoogte = 120                          # 3x de 40px uit de balk
        breedte = round(alfa.size[0] * hoogte / alfa.size[1])
        vlak = vlak.resize((breedte, hoogte), Image.LANCZOS)
        vlak.save(LOGO / naam, optimize=True)
        gemaakt.append((naam, vlak.size))
    return gemaakt, round(alfa.size[0] / alfa.size[1], 3)

# ---------------------------------------------------------------- foto's
LADDERS = {
    'hero':    [640, 1200, 1800, 2400],
    'kaart':   [480, 800, 1200, 1800],
    'inhoud':  [480, 800, 1200],
}

def webp(bron, naam, breedtes, kwaliteit=82):
    """Schrijft <naam>-<breedte>.webp voor elke breedte die het origineel haalt."""
    FOTO.mkdir(parents=True, exist_ok=True)
    im = Image.open(bron)
    bb, bh = im.size
    gedaan = []
    kandidaten = [b for b in breedtes if b <= bb] or [bb]
    if bb not in kandidaten and bb < max(breedtes):
        kandidaten.append(bb)                 # de eigen breedte als grootste trap
    for b in sorted(set(kandidaten)):
        uit = FOTO / f'{naam}-{b}.webp'
        r = subprocess.run(['cwebp', '-quiet', '-q', str(kwaliteit), '-m', '6',
                            '-resize', str(b), '0', str(bron), '-o', str(uit)],
                           capture_output=True)
        if r.returncode != 0:
            raise SystemExit(f'cwebp faalde op {bron}: {r.stderr.decode()[:200]}')
        gedaan.append(b)
    grootste = max(gedaan)
    hoogte = round(bh * grootste / bb)
    return gedaan, grootste, hoogte

def main():
    if not EXPORT.exists():
        sys.exit(f'export niet gevonden op {EXPORT} - pak duyts-website-export.zip daar uit')
    logos, ratio = maak_logos()
    print('logo:', logos, 'verhouding', ratio)

    plan = json.loads((HIER / 'beeldplan.json').read_text(encoding='utf-8'))
    uit = {}
    for naam, regel in plan.items():
        # Een bron staat in de Duyts-export, of - voor beeld dat hier zelf is
        # gemaakt, zoals het eerste beeldje van de herovideo - in het project.
        bron = EXPORT / regel['bron'].lstrip('/')
        if not bron.exists():
            bron = HIER / regel['bron'].lstrip('/')
        if not bron.exists():
            raise SystemExit(f'{naam}: bron ontbreekt: {regel["bron"]}')
        breedtes, gb, gh = webp(bron, naam, LADDERS[regel['rol']])
        uit[naam] = {'breedtes': breedtes, 'breed': gb, 'hoog': gh,
                     'alt': regel['alt'], 'bron': regel['bron']}
        print(f'  {naam:38s} {breedtes} -> {gb}x{gh}')
    (HIER / 'beeldmaten.json').write_text(json.dumps(uit, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'\n{len(uit)} beelden omgezet, maten in beeldmaten.json')

if __name__ == '__main__':
    main()
