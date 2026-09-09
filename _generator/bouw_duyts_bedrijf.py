# -*- coding: utf-8 -*-
"""Over ons, historie, het team, de registerconstructeur, werkwijze, vacatures.

Zes pagina's die op de bronsite onder 'Over ons' hangen. De teksten komen
integraal uit de export; de indeling in secties is die van dit template.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *          # noqa: F401,F403
import inhoud_duyts as D
import inhoud_copy as C

UIT = pathlib.Path(__file__).resolve().parent.parent


def _p(alineas, klasse=''):
    k = f' class="{klasse}"' if klasse else ''
    return "\n".join(f'              <p{k}>{D._tekens(a)}</p>' for a in D.splits_lang(alineas))


def _tekstsectie(nr, ident, kop, alineas, subtitel=None, achtergrond='white'):
    label = (f'            <span class="subtitle" style="margin-bottom:var(--space-500)">{subtitel}</span>\n'
             if subtitel else '')
    kopregel = f'            <h2 class="section-heading">{D._tekens(kop)}</h2>\n' if kop else ''
    return f'''  <section class="content-block" id="s{nr}-{ident}">
    <div class="container">
      <div class="content-block--container background--{achtergrond}">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
{label}{kopregel}            <div class="article-body" style="margin-top:var(--space-500)">
{_p(alineas)}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>'''


# --------------------------------------------------------------------- over ons
def over_ons():
    secties = D.OVER_ONS          # de vijf blokken van /over-ons/
    k = C.BEDRIJF['over-ons.html']
    delen = [paginahero('01', 'over-ons', 'Over ons', k['h1'], 'duyts-kantoor-groep'),
             _tekstsectie('02', 'lead', None, k['lead'])]
    nr = 2
    for sec in secties:
        nr += 1
        alineas = sec['paragraphs']
        if not alineas:
            continue
        kop = sec['heading'] if sec['heading'] != 'Sinds 1981 stevig gebouwd' else None
        delen.append(_tekstsectie(f'{nr:02d}', 'over', kop, alineas,
                                  achtergrond='grey' if nr % 2 == 0 else 'white'))
    nr += 1
    delen.append(f'''  <section class="content-block" id="s{nr:02d}-verder">
    <div class="container">
      <div class="row g-0">
{beeldkaart("Historie", "Van JH Duyts Adviesbureau voor Bouwconstructies in 1981 tot nu.",
            'duyts-directie', alt="", kleur="grey", href="historie.html")}
{beeldkaart("Het team", "Circa 25 tekenaars, constructeurs en specialisten.",
            'duyts-team', alt="", kleur="white", href="het-team.html")}
{beeldkaart("Werkwijze", "Hoe een opdracht bij ons verloopt, van offerte tot uitvoering.",
            'duyts-registerconstructeur', alt="", kleur="white", href="werkwijze.html")}
{beeldkaart("Registerconstructeur", "Kwaliteitscontrole en toetsing binnen ons eigen bureau.",
            'duyts-dienst-constructieberekening', alt="", kleur="grey", href="registerconstructeur.html")}
      </div>
    </div>
  </section>''')
    nr += 1
    delen.append(logoslider(f'{nr:02d}'))
    nr += 1
    delen.append(ctablok(f'{nr:02d}', k['slot_kop']))

    (UIT / 'over-ons.html').write_text(pagina(
        bestand='over-ons.html',
        titel=f'Over ons | {D.NAAM}',
        omschrijving=('Vanuit ons kantoor in Amsterdam werken we met circa 25 tekenaars, '
                      'constructeurs en specialisten aan een breed scala van projecten.'),
        namespace='over-ons',
        pagina_css='over-ons.css',
        css_naam='over-ons',
        inhoud="\n\n".join(delen),
    ), encoding='utf-8')
    return 'over-ons.html'


# --------------------------------------------------------------------- historie
def historie():
    alineas = [a for sec in D.HISTORIE for a in sec['paragraphs']]
    k = C.BEDRIJF['historie.html']
    delen = [paginahero('01', 'historie', 'Over ons', 'Historie', 'duyts-directie'),
             _tekstsectie('02', 'lead', None, k['lead']),
             _tekstsectie('03', 'historie', 'Van 1981 tot nu', alineas, achtergrond='grey'),
             logoslider('04'),
             ctablok('05', k['slot_kop'])]
    (UIT / 'historie.html').write_text(pagina(
        bestand='historie.html', titel=f'Historie | {D.NAAM}',
        omschrijving=('Duyts Bouwconstructies is in 1981 opgericht door Jan Duyts. '
                      'De geschiedenis van het bureau in het kort.'),
        namespace='historie', pagina_css='over-ons.css', css_naam='over-ons',
        inhoud="\n\n".join(delen),
    ), encoding='utf-8')
    return 'historie.html'


# --------------------------------------------------------------------- het team
def het_team():
    alineas = D.alinea_lijst(D.TEAM_TEKST)
    # De functielijst van de bronsite als vlakkenrij: tien functies, dus twee
    # rijen van de vier kleuren plus twee.
    rollen = D.TEAM_ROLLEN
    delen = [
        paginahero('01', 'team', 'Over ons', 'Het team', 'duyts-team'),
        _tekstsectie('02', 'team', None, C.BEDRIJF['het-team.html']['lead']),
        f'''  <section class="content-block" id="s03-functies">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Functies</span>
            <h2 class="section-heading">Wie er bij Duyts werkt</h2>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{chr(10).join(f"""        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">{i + 1:02d}</span>
            <h3 class="panel__title">{D._tekens(r)}</h3>
          </div>
        </div>""" for i, r in enumerate(rollen))}
      </div>
    </div>
  </section>''',
        _tekstsectie('04', 'honkvast', 'Typerend: honkvastheid', alineas[1:], achtergrond='grey'),
        f'''  <section class="content-block" id="s05-lunch">
    <div class="container">
      <figure class="case-bleed">
        {foto('duyts-team-lunch', maten="100vw")}
      </figure>
    </div>
  </section>''',
        logoslider('06'),
        ctablok('07', C.BEDRIJF['het-team.html']['slot_kop'],
                'Bekijk onze vacatures, of stuur een open sollicitatie.'),
    ]
    (UIT / 'het-team.html').write_text(pagina(
        bestand='het-team.html', titel=f'Het team | {D.NAAM}',
        omschrijving=('Ons team bestaat uit circa 25 tekenaars, constructeurs en specialisten. '
                      'Meer dan driekwart werkt tien jaar of langer bij Duyts.'),
        namespace='het-team', pagina_css='over-ons.css', css_naam='over-ons',
        inhoud="\n\n".join(delen),
    ), encoding='utf-8')
    return 'het-team.html'


# ------------------------------------------------------------ registerconstructeur
def registerconstructeur():
    alineas = D.alinea_lijst(D.REGISTERCONSTRUCTEUR)
    delen = [paginahero('01', 'registerconstructeur', 'Over ons', 'Registerconstructeur',
                        'duyts-registerconstructeur'),
             _tekstsectie('02', 'lead', None, C.BEDRIJF['registerconstructeur.html']['lead']),
             _tekstsectie('03', 'registerconstructeur', 'Wat de registerconstructeur doet',
                          alineas[:2], achtergrond='grey'),
             _tekstsectie('04', 'register', 'Wat het Constructeursregister RC/RO zegt',
                          alineas[2:]),
             logoslider('05'),
             ctablok('06', C.BEDRIJF['registerconstructeur.html']['slot_kop'])]
    (UIT / 'registerconstructeur.html').write_text(pagina(
        bestand='registerconstructeur.html', titel=f'Registerconstructeur | {D.NAAM}',
        omschrijving=('Onze registerconstructeur stuurt collega\'s aan en bewaakt de interne '
                      'kwaliteitscontrole.'),
        namespace='registerconstructeur', pagina_css='over-ons.css', css_naam='over-ons',
        inhoud="\n\n".join(delen),
    ), encoding='utf-8')
    return 'registerconstructeur.html'


# -------------------------------------------------------------------- werkwijze
def werkwijze():
    alineas = D.alinea_lijst(D.WERKWIJZE)
    k = C.BEDRIJF['werkwijze.html']
    delen = [paginahero('01', 'werkwijze', 'Over ons', 'Werkwijze', 'duyts-dienst-constructieberekening'),
             _tekstsectie('02', 'lead', None, k['lead']),
             _tekstsectie('03', 'werkwijze', 'Van offerte tot uitgangspunten', alineas[:2], achtergrond='grey'),
             _tekstsectie('03', 'software', 'Rekenen en tekenen', alineas[2:3], achtergrond='grey'),
             _tekstsectie('04', 'hoofdconstructeur', 'Als hoofdconstructeur', alineas[3:4]),
             _tekstsectie('05', 'duurzaam', 'Duurzaam bouwen', alineas[4:], achtergrond='grey'),
             logoslider('06'),
             ctablok('07', k['slot_kop'],
                     D._tekens(D.OFFERTE['intro'].split('Om ervoor')[0].strip()))]
    (UIT / 'werkwijze.html').write_text(pagina(
        bestand='werkwijze.html', titel=f'Werkwijze | {D.NAAM}',
        omschrijving=('Lees hoe een opdracht bij Duyts verloopt: van offerte en uitgangspunten '
                      'tot uitvoering en controle op de bouwplaats.'),
        namespace='werkwijze', pagina_css='over-ons.css', css_naam='over-ons',
        inhoud="\n\n".join(delen),
    ), encoding='utf-8')
    return 'werkwijze.html'


# -------------------------------------------------------------------- vacatures
def vacatures():
    alineas = D.alinea_lijst(D.VACATURES)
    # De bronsite noemt in de footer welke functies open staan en verwijst voor de
    # uitgebreide beschrijving naar het externe vacaturesysteem.
    delen = [
        paginahero('01', 'vacatures', 'Over ons', C.BEDRIJF['vacatures.html']['h1'], 'duyts-team-lunch'),
        _tekstsectie('02', 'vacatures', None, C.BEDRIJF['vacatures.html']['lead']),
        f'''  <section class="content-block" id="s03-open">
    <div class="container">
      <div class="content-block--container background--grey">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Open functies</span>
            <h2 class="section-heading">Ter uitbreiding van ons team</h2>
            <div class="article-body" style="margin-top:var(--space-500)">
              <p>{D._tekens(alineas[1]) if len(alineas) > 1 else ''}</p>
              <p>De volledige beschrijving van onze vacatures staat op ons vacaturesysteem.</p>
            </div>
            <div style="margin-top:var(--space-600)">
              {knop("Bekijk de vacatures", D.VACATURESITE, extra='target="_blank" rel="noopener"')}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>''',
        _tekstsectie('04', 'solliciteren', 'Solliciteren', alineas[2:3]),
        logoslider('05'),
        ctablok('06', C.BEDRIJF['vacatures.html']['slot_kop'],
                'Stuur uw sollicitatie via het contactformulier of bel ons.'),
    ]
    (UIT / 'vacatures.html').write_text(pagina(
        bestand='vacatures.html', titel=f'Werken bij Duyts | {D.NAAM}',
        omschrijving=('Wat Duyts Bouwconstructies uniek maakt is de combinatie van jarenlange '
                      'ervaring, technische diepgang en persoonlijke betrokkenheid.'),
        namespace='vacatures', pagina_css='over-ons.css', css_naam='over-ons',
        inhoud="\n\n".join(delen),
    ), encoding='utf-8')
    return 'vacatures.html'


def main():
    gemaakt = [over_ons(), historie(), het_team(), registerconstructeur(),
               werkwijze(), vacatures()]
    print(f'{len(gemaakt)} bedrijfspagina\'s geschreven')
    return gemaakt


if __name__ == '__main__':
    main()
