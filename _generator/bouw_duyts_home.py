# -*- coding: utf-8 -*-
"""De homepage.

De bronsite heeft op de homepage vier tekstblokken onder elkaar en verder niets:
geen dienstenoverzicht, geen projecten, geen cijfers. Die vier blokken zijn hier
verdeeld over de secties van dit template, en daaronder staan de hoofddiensten
en een paar projecten, zodat een bezoeker vanaf de homepage verder kan.

Alle tekst komt van www.duyts.nl. Er is niets bijgeschreven.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *          # noqa: F401,F403
from schil import _plat
import inhoud_duyts as D
import inhoud_copy as C

UIT = pathlib.Path(__file__).resolve().parent.parent

# De vier blokken van de bronhomepage, op naam.
USP = dict(D.USPS)
KIJKEN_VERDER = USP['Wij kijken verder dan vandaag']
KLEIN_GENOEG = USP['Klein genoeg om persoonlijk te blijven']
MONUMENT_NIEUWBOUW = USP['Van monument tot nieuwbouw']
SAMEN_VERDER = USP['Samen kom je verder']


def _zinnen(tekst, vanaf=0, tot=None):
    """Een blok in losse alinea's knippen op zinsgrens, zodat een lange
       bronalinea in een kolom te lezen blijft. De woorden veranderen niet: er
       wordt alleen een alineagrens gelegd waar toch al een punt stond."""
    zinnen = re.split(r'(?<=[.!?])\s+', tekst.strip())
    delen, huidig = [], []
    for zin in zinnen:
        huidig.append(zin)
        if sum(len(z) + 1 for z in huidig) > 220:
            delen.append(' '.join(huidig))
            huidig = []
    if huidig:
        delen.append(' '.join(huidig))
    return delen[vanaf:tot]


def _p(alineas):
    return "\n".join(f'          <p>{D._tekens(a)}</p>' for a in alineas)


def _projectrijen(maximaal=3):
    rijen = []
    gekozen = (D.projecten_in('Funderingsherstel', 1)
               + D.projecten_in('Verbouwing', 1)
               + D.projecten_in('Nieuwbouw', 1))[:maximaal]
    for i, p in enumerate(gekozen):
        cat = p['categorieen'][0]
        meta = "".join(f'<span class="cases-grid__meta-item">{m}</span>'
                       for m in [cat] + ([p['plaats']] if p['plaats'] else []))
        rijen.append(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="{p['bestand']}" aria-label="{_plat(p['titel'])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">{meta}</div>
          <h3 class="cases-grid__title">{D._tekens(p['titel'])}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{D._tekens(p['intro'])}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(p['beeld'], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>''')
    return "\n".join(rijen)


# Alle diensten op de homepage: de drie hoofddiensten als brede kaart, en de
# vier losse diensten daaronder in een rij van vier. De werkzaamheden die onder
# een hoofddienst hangen staan op die hoofddienstpagina zelf.
hoofddiensten = "\n".join(dienstkaart(i, d, '') for i, d in enumerate(SERVICES))
losse_diensten = "\n".join(dienstkaart(i, d, '', kolom="col-lg-6")
                           for i, d in enumerate(LOSSE_DIENSTEN))

inhoud = f'''  <!-- ================= 01 INTRODUCTIE =================
       De film ligt over het stilstaande beeld heen en komt pas in beeld als hij
       speelt. site.js hangt de bron er pas in als beweging aan staat en de lijn
       het aankan; zonder JavaScript, met prefers-reduced-motion of op een trage
       verbinding blijft het bij de foto hieronder, en dat is het eerste beeldje
       van dezelfde film. Het audiospoor is eruit gehaald: de film staat muted
       en loopt rond, dus geluid is alleen gewicht. -->
  <section class="hero" id="s01-introductie" data-header-theme="light">
    <div class="hero--beeld" aria-hidden="true">
      {foto("duyts-hero-still", laden="eager", maten="100vw", alt="")}
      <video class="hero--video" data-herovideo="assets/video/duyts-hero.mp4"
             width="1280" height="720" muted loop playsinline preload="none"></video>
      <span class="hero--sluier"></span>
    </div>
    <div class="container hero--container">
      <div class="hero--content">
        <span class="subtitle" style="color:var(--color-white)">{C.HOME['eyebrow']}</span>
        <h1 class="hero--title">{D.afbreek(C.HOME['h1'])}</h1>
        <div class="hero--intro article-body">
{_p(C.HOME['lead'])}
        </div>
        <div class="hero--actions">
          {knop(*C.HOME['cta_primair'])}
          {knop(*C.HOME['cta_secundair'], "secondary")}
        </div>
      </div>
    </div>
  </section>

{logoslider("02")}

  <!-- ================= 03 WAT DUYTS DOET ================= -->
  <section class="content-text-side-cta" id="s03-wat-we-doen">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{C.HOME['statement_kop']}</h2>
            <div class="content-text-side-cta--body article-body">
{_p(C.HOME['statement'])}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop(*C.HOME['statement_cta'])}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 04 WERKZAAMHEDEN ================= -->
{citaten("04")}

  <section class="content-block" id="s05-werkzaamheden">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Werkzaamheden</span>
            <h2 class="section-heading">{C.HOME['werkzaamheden_kop']}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              {C.HOME['werkzaamheden_lead']}
            </p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{hoofddiensten}
      </div>
      <div class="content-block--container background--white"
           style="padding-top:var(--space-700); padding-bottom:var(--space-600)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <h3 class="font-size--md">{C.HOME['losse_kop']}</h3>
            <p class="article-body" style="margin-top:var(--space-400); max-width:var(--content-max-half)">
              {C.HOME['losse_lead']}
            </p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{losse_diensten}
      </div>
    </div>
  </section>

  <!-- ================= 05 PROJECTEN ================= -->
  <section class="cases-grid" id="s06-projecten">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">{C.HOME['projecten_kop']}</h2>
        {knop(*C.HOME['projecten_cta'], "secundair")}
      </div>
      <div class="cases-grid__list">
{_projectrijen()}
      </div>
    </div>
  </section>

  <!-- ================= 06 OVER ONS =================
       De groepsfoto staat op zijn eigen verhouding over de inhoudsbreedte, niet
       in een vak met een vaste hoogte: op een foto van het hele team mag er
       niemand worden afgesneden. -->
  <section class="content-block" id="s07-over-ons">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Over ons</span>
            <h2 class="section-heading">{C.HOME['over_kop']}</h2>
            <div class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
{_p(C.HOME['over'])}
            </div>
            <div style="margin-top:var(--space-600)">
              {knop(*C.HOME['over_cta'], "secundair")}
            </div>
          </div>
        </div>
      </div>
      <figure class="beeldband">
        {foto("duyts-kantoor-groep", maten="(max-width: 1352px) calc(100vw - 32px), 1320px")}
      </figure>
    </div>
  </section>

{ctablok("08", C.HOME['slot_kop'], C.HOME['slot'])}
'''

(UIT / 'index.html').write_text(pagina(
    bestand='index.html',
    titel=f'Constructief advies voor verbouwing, fundering en nieuwbouw | {D.NAAM}',
    omschrijving=('Constructieve adviezen voor verbouwing, funderingsonderzoek, '
                  'funderingsherstel en nieuwbouw. Sinds 1981 vanuit Amsterdam, '
                  'door het hele land.'),
    namespace='home',
    pagina_css='index.css',
    css_naam='index',
    inhoud=inhoud,
    scripts=('index.js',),
    extra_ld=json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": D.NAAM,
        "url": BASIS + "/",
        "inLanguage": "nl-NL",
    }, ensure_ascii=False, indent=2),
), encoding='utf-8')
print('index.html geschreven')
