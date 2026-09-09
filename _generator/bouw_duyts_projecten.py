# -*- coding: utf-8 -*-
"""Het projectenoverzicht met filters, en een pagina per project.

De bronsite heeft 43 portfolio-items, waarvan zes projecten meerdere keren zijn
opgevoerd onder een andere categorie. Die zijn hier samengevoegd tot 36
projecten, elk met alle categorieën waaronder ze op de bronsite stonden.

De projectcategorie-overzichten van de bronsite geven een WordPress-fout en
tonen daar niets. Dit overzicht neemt die taak over: het filtert op dezelfde
drie categorieën, met het filtercomponent dat al in het template zat.

WAT ER PER PROJECT UIT DE BRON KOMT
  Titel, de regel eronder, de omschrijving (uit de og:description van de
  bronpagina: drie tot vier volledige zinnen), de categorie en de foto's.

WAT ER IS BIJGESCHREVEN
  De werkzaamheden per project worden afgeleid uit de projecttekst zelf: staat
  er "kelder" in, dan komt er een regel over de kelderconstructie bij, met een
  link naar de dienst die daarover gaat. Dat is dus een lezing van de brontekst
  en geen nieuwe informatie over het project.

WAT ER NIET IN STAAT
  Geen opdrachtgever, jaartal, bouwsom, doorlooptijd of citaat. De bronsite
  noemt die niet, en het zijn harde feiten over een echt project; die kunnen
  alleen van Duyts komen. Op de pagina staan ze als markering, zodat zichtbaar
  is dat er iets ontbreekt in plaats van dat er iets is verzonnen.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *          # noqa: F401,F403
from schil import _plat
import inhoud_duyts as D
import inhoud_copy as C

UIT = pathlib.Path(__file__).resolve().parent.parent

VINKJE = ('<svg class="filter-pil__vink" width="14" height="14" viewBox="0 0 24 24" aria-hidden="true">'
          '<path d="M9.6 16.2 5.4 12l-1.4 1.4 5.6 5.6L20.4 8.2 19 6.8 9.6 16.2Z"/></svg>')

# Waar de projecttekst over gaat, en welke dienst daarover meer vertelt. Zo
# krijgt een project een lijstje werkzaamheden dat klopt met zijn eigen
# omschrijving, en loopt de bezoeker vanaf een project door naar de dienst.
WERK_UIT_TEKST = [
    (('funderingsherstel',), 'Funderingsherstel',
     'Nieuwe funderingspalen onder het bestaande pand, met een betonconstructie '
     'die de bouwmuren overneemt.', 'funderingsherstel.html'),
    (('funderingsonderzoek', 'funderingsrisico'), 'Funderingsonderzoek',
     'De staat van de bestaande fundering opgenomen en beoordeeld.',
     'funderingsonderzoek.html'),
    (('kelder', 'souterrain'), 'Kelderconstructie',
     'Een kelder onder of naast het pand, met de waterdichting en het opdrijvend '
     'vermogen als bepalende factoren.', 'funderingsherstel-kelderbak.html'),
    (('staalconstructie', 'stalen', 'staal'), 'Staalconstructie',
     'Stalen liggers, kolommen of portalen die de belasting overnemen.',
     'stabiliteitsportalen.html'),
    (('stabiliteit', 'windbelasting', 'portaal'), 'Stabiliteit',
     'De voorzieningen die de horizontale krachten van wind opnemen.',
     'stabiliteitsberekening.html'),
    (('dakterras', 'dakopbouw', 'dakkapel'), 'Dakconstructie',
     'Het dak geschikt gemaakt voor extra belasting.', 'dakterras.html'),
    (('vide', 'trapgat', 'sparing'), 'Vloeropening',
     'Een opening in de vloer, met een raveling die de krachten eromheen verdeelt.',
     'trapgat.html'),
    (('balklaag', 'vloerbalk', 'verdiepingsvloer'), 'Vloeren en balklagen',
     'Balklagen gecontroleerd en waar nodig verstijfd of vervangen.',
     'vloerbalklagen.html'),
    (('appartement', 'woon-zorg'), 'Woningbouw',
     'De draagconstructie voor woningen of appartementen.',
     'appartementencomplex.html'),
    (('muurdoorbraak', 'draagmuur', 'doorbraak'), 'Muurdoorbraak',
     'Een sparing of doorbraak in een dragende wand.', 'muurdoorbraak.html'),
    (('schade', 'betonrot', 'scheur'), 'Schadeonderzoek',
     'De schade opgenomen en de oorzaak vastgesteld.', 'schaderapportage.html'),
    (('monument', 'restaura'), 'Monument en restauratie',
     'Ingrepen in een pand dat zichzelf moet blijven.', 'verbouwing.html'),
    (('nieuwbouw',), 'Nieuwbouw',
     'De volledige draagconstructie, van funderingsplan tot dak.',
     'nieuwbouw.html'),
    (('verbouwing', 'uitbreiding', 'verbouwd'), 'Verbouwing',
     'Constructieve aanpassingen in een bestaand pand.', 'verbouwing.html'),
    (('gevel', 'pui'), 'Gevelconstructie',
     'De draagconstructie achter de gevel, en wat er nodig is als die verandert.',
     'stabiliteitsportalen.html'),
    (('kantoor',), 'Kantoorgebouw',
     'De draagconstructie van een kantoor, met vrij indeelbare vloervelden.',
     'kantoorgebouwen.html'),
    (('bedrijfsgebouw', 'bedrijfshal', 'hal '), 'Bedrijfsgebouw',
     'De draagconstructie van een hal of bedrijfsgebouw.', 'bedrijfsgebouwen.html'),
    (('villa', 'woonhuis', 'woning'), 'Woonhuis',
     'De draagconstructie en de stabiliteit van een woonhuis.', 'woonhuizen.html'),
    (('renovatie', 'gerenoveerd', 'herbestemming'), 'Renovatie',
     'Werken in een bestaand casco, met hergebruik van wat er nog kan.',
     'verbouwing.html'),
    (('brug', 'loopbrug'), 'Loopbrug',
     'Een vrijstaande stalen constructie, los van het pand.',
     'stabiliteitsberekening.html'),
]

# Elk project van Duyts is constructief advies; staat er niets specifieker in de
# tekst, dan is dat de regel die er hoort te staan.
WERK_TERUGVAL = ('Constructief advies',
                 'De berekeningen en tekeningen van de draagconstructie voor dit project.',
                 'constructieberekening.html')

DIENST_BIJ_CATEGORIE = {
    'Verbouwing': ('verbouwing.html', 'Verbouwing', 'duyts-dienst-verbouwing'),
    'Funderingsherstel': ('funderingsherstel.html', 'Funderingsherstel',
                          'duyts-dienst-funderingsherstel'),
    'Nieuwbouw': ('nieuwbouw.html', 'Nieuwbouw', 'duyts-dienst-nieuwbouw'),
}


def sleutelvorm(t):
    return "".join(c if c.isalnum() else '-' for c in t.lower()).strip('-')


def _copy(t):
    """Brontekst met de herschreven zinnen erin, en lange alinea's gesplitst."""
    for oud, nieuw in C.PROJECT_HERSCHRIJF.items():
        t = t.replace(oud, nieuw)
    return t


def _werkzaamheden(p):
    """De werkzaamheden die uit de projecttekst zelf naar voren komen."""
    tekst = (p['intro'] + ' ' + p['beschrijving']).lower()
    uit = []
    for woorden, titel, toelichting, bestand in WERK_UIT_TEKST:
        if any(w in tekst for w in woorden) and titel not in [u[0] for u in uit]:
            uit.append((titel, toelichting, bestand))
    return uit[:4] or [WERK_TERUGVAL]


# ---------------------------------------------------------------- overzicht
def _filtergroep(label, naam, waarden, alles):
    pillen = [f'''          <button type="button" class="filter-pil is-actief" data-filter="{naam}" data-waarde="alles" aria-pressed="true">
            {VINKJE}<span>{alles}</span>
          </button>''']
    for w in waarden:
        pillen.append(f'''          <button type="button" class="filter-pil" data-filter="{naam}" data-waarde="{sleutelvorm(w)}" aria-pressed="false">
            {VINKJE}<span>{w}</span>
          </button>''')
    return f'''        <div class="filter-groep" role="group" aria-label="{label}">
{chr(10).join(pillen)}
        </div>'''


def _kaart(p):
    cats = " ".join(sleutelvorm(c) for c in p['categorieen'])
    labels = "".join(f'<span class="case-kaart__label">{c}</span>' for c in p['categorieen'])
    plaats = f'<span class="case-kaart__label">{p["plaats"]}</span>' if p['plaats'] else ''
    return f'''        <article class="case-kaart" data-categorie="{cats}">
          <a class="case-kaart__link hover--icon" href="{p['bestand']}">
            <figure class="case-kaart__beeld">
              {foto(p['beeld'], maten="(max-width: 767px) 100vw, (max-width: 1199px) 50vw, 33vw", alt="")}
            </figure>
            <div class="case-kaart__inhoud">
              <div class="case-kaart__meta">{labels}{plaats}</div>
              <h2 class="case-kaart__titel">{D.afbreek(D._tekens(p['titel']))}</h2>
              <p class="case-kaart__tekst">{D._tekens(p['intro'])}</p>
              <div class="case-kaart__voet">
                <span class="case-kaart__lees">Bekijk het project</span>
                {icoonknop("", "button--secundair")}
              </div>
            </div>
          </a>
        </article>'''


def overzicht():
    per_cat = " &middot; ".join(f'{len(D.projecten_in(c))}&times; {c.lower()}'
                                for c in D.CATEGORIEEN)
    inhoud = f'''{patroonhero("01", "projecten", "Projecten", C.PROJECTEN_OVERZICHT['h1'])}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row g-0">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">{C.PROJECTEN_OVERZICHT['kop']}</h2>
          <p class="case-lead">{C.PROJECTEN_OVERZICHT['lead']}</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            {len(D.PROJECTEN)} projecten: {per_cat}.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="cases-overzicht" id="s03-projecten">
    <div class="container">
      <div class="cases-overzicht__filters">
{_filtergroep("Filter projecten op categorie", "categorie", D.CATEGORIEEN, "Alle projecten")}
      </div>

      <p class="cases-overzicht__telling" role="status" aria-live="polite"></p>

      <div class="cases-overzicht__raster" id="caseRaster">
{chr(10).join(_kaart(p) for p in D.PROJECTEN)}
      </div>

      <p class="cases-overzicht__leeg" hidden>Geen projecten in deze categorie. Zet het filter terug op &lsquo;alle projecten&rsquo;.</p>
    </div>
  </section>

{logoslider("04")}

{ctablok("05", C.PROJECTEN_OVERZICHT['slot_kop'], C.PROJECT['slot'])}
'''
    (UIT / 'projecten.html').write_text(pagina(
        bestand='projecten.html',
        titel=f'Projecten | {D.NAAM}',
        omschrijving=('Constructieve adviezen bij restauraties, verbouwingen, funderingsherstel '
                      'en nieuwbouw. Een selectie van projecten van Duyts Bouwconstructies.'),
        namespace='projecten', pagina_css='cases.css', css_naam='cases',
        inhoud=inhoud, scripts=['cases.js'],
    ), encoding='utf-8')
    return 'projecten.html'


# ---------------------------------------------------------------- detailpagina
def _blok(nr, ident, kop, alineas, achtergrond='white', extra=''):
    body = "\n".join(f'          <p>{a}</p>' for a in alineas)
    return f'''  <section class="band background--{achtergrond}" id="s{nr}-{ident}">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="case-blok__kop">{kop}</h2>
        <div class="case-blok__body">
{body}
        </div>
{extra}
      </div>
    </div>
  </section>'''


def detail(p):
    eerste = next((c for c in p['categorieen'] if c in DIENST_BIJ_CATEGORIE), None)
    werk = _werkzaamheden(p)
    nr = [1]

    def volgend():
        nr[0] += 1
        return f'{nr[0]:02d}'

    delen = [paginahero('01', 'project', " &middot; ".join(p['categorieen']),
                        D.afbreek(D._tekens(p['titel'])), p['beeld'])]

    # 02 de lead: de regel van de bronsite, groot gezet
    delen.append(f'''  <section class="band background--white" id="s{volgend()}-lead">
    <div class="container">
      <div class="case-blok__inner">
        <p class="case-lead">{D._tekens(_copy(p['intro']))}</p>
      </div>
    </div>
  </section>''')

    # 03 het project: de omschrijving van de bronsite
    delen.append(_blok(volgend(), 'toelichting', C.PROJECT['project_kop'],
                       [D._tekens(a) for a in D.splits_lang([_copy(p['beschrijving'])])],
                       achtergrond='grey'))

    # 04 wat er is gedaan, afgeleid uit de projecttekst
    if werk:
        punten = "\n".join(
            f'          <li><strong>{t}</strong><br>{tl} '
            f'<a href="{b}">Meer over {t.lower()}</a></li>' for t, tl, b in werk)
        delen.append(f'''  <section class="band background--white" id="s{volgend()}-werkzaamheden">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="case-blok__kop">{C.PROJECT['werk_kop']}</h2>
        <div class="case-blok__body">
          <p>{C.PROJECT['werk_lead']}</p>
        </div>
        <ul class="case-lijst">
{punten}
        </ul>
      </div>
    </div>
  </section>''')

    # 05 tweede foto over de volle breedte
    if p['tweede_beeld']:
        delen.append(f'''  <figure class="case-bleed" id="s{volgend()}-beeld">
    {foto(p['tweede_beeld'], maten="100vw")}
  </figure>''')

    # 06 projectgegevens, met de gaten er eerlijk in
    delen.append(f'''  <section class="band background--grey" id="s{volgend()}-gegevens">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="case-blok__kop">{C.PROJECT['gegevens_kop']}</h2>
        <ul class="case-lijst">
          <li><strong>Categorie</strong><br>{" &middot; ".join(p['categorieen'])}</li>
          <li><strong>Plaats</strong><br>{p['plaats'] or f'<span class="invulveld">{D.NIET_GEVONDEN}</span>'}</li>
          <li><strong>Opdrachtgever</strong><br><span class="invulveld">{D.NIET_GEVONDEN}</span></li>
          <li><strong>Jaar van uitvoering</strong><br><span class="invulveld">{D.NIET_GEVONDEN}</span></li>
        </ul>
        <div class="case-blok__body" style="margin-top:var(--space-500)">
          <p>Opdrachtgever en jaartal staan niet op de bronpagina van dit project.
             Ze zijn daarom leeg gelaten in plaats van ingevuld.</p>
        </div>
      </div>
    </div>
  </section>''')

    # 07 verwante projecten
    if eerste:
        anderen = [q for q in D.projecten_in(eerste) if q['slug'] != p['slug']][:2]
        if anderen:
            rijen = []
            for i, q in enumerate(anderen):
                rijen.append(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="{q['bestand']}" aria-label="{_plat(q['titel'])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta"><span class="cases-grid__meta-item">{eerste}</span></div>
          <h3 class="cases-grid__title">{D.afbreek(D._tekens(q['titel']))}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{D._tekens(q['intro'])}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(q['beeld'], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>''')
            delen.append(f'''  <section class="cases-grid" id="s{volgend()}-verwant">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">Meer {eerste.lower()}</h2>
        {knop("Alle projecten", "projecten.html", "secundair")}
      </div>
      <div class="cases-grid__list">
{chr(10).join(rijen)}
      </div>
    </div>
  </section>''')

    # 08 doorstap naar de dienst en de offerte
    if eerste:
        bestand, titel, beeld = DIENST_BIJ_CATEGORIE[eerste]
        delen.append(f'''  <section class="content-block" id="s{volgend()}-dienst">
    <div class="container">
      <div class="row g-0">
{beeldkaart(titel, "Wat we doen bij dit soort werk, van eerste opname tot uitvoeringstekening.",
            beeld, alt="", kleur="grey", href=bestand)}
{beeldkaart("Offerte aanvragen",
            "Vertel kort wat er verbouwd, hersteld of gebouwd wordt; wij rekenen mee.",
            'duyts-dienst-constructieberekening', alt="", kleur="white", href="offerte.html")}
      </div>
    </div>
  </section>''')

    delen.append(logoslider(volgend()))
    delen.append(ctablok(volgend(), C.PROJECT['slot_kop'], C.PROJECT['slot']))

    zelfde_titel = [q for q in D.PROJECTEN if q['titel'] == p['titel']]
    onderscheid = (f" ({p['categorieen'][0]})"
                   if len(zelfde_titel) > 1 and p['categorieen'][0] != D.NIET_GEVONDEN else '')
    titel = (p['seo_titel'].replace(p['titel'], p['titel'] + onderscheid)
             if not p['seo_titel'].startswith('[')
             else f"{p['titel']}{onderscheid} | {D.NAAM}")
    # Ook de meta-omschrijving door de herschrijftabel: die tekst staat in de
    # zoekresultaten en is dus net zo goed leescopy als de tekst op de pagina.
    omschrijving = _copy(p['seo_omschrijving'] if not p['seo_omschrijving'].startswith('[')
                         else D._tekens(p['intro']))
    (UIT / p['bestand']).write_text(pagina(
        bestand=p['bestand'], titel=titel, omschrijving=omschrijving,
        namespace='project', pagina_css='cases.css', css_naam='cases',
        inhoud="\n\n".join(delen),
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "CreativeWork",
            "name": p['titel'],
            "description": _copy(p['beschrijving']),
            "creator": {"@type": "Organization", "name": D.NAAM_VOLUIT},
        }, ensure_ascii=False, indent=2),
    ), encoding='utf-8')
    return p['bestand']


def main():
    gemaakt = [overzicht()] + [detail(p) for p in D.PROJECTEN]
    print(f"projecten: overzicht + {len(gemaakt) - 1} detailpagina's")
    return gemaakt


if __name__ == '__main__':
    main()
