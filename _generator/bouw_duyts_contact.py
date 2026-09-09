# -*- coding: utf-8 -*-
"""Contact, offerte, privacybeleid en cookies.

De bronsite heeft twee formulieren: een contactformulier (Contact Form 7) en een
offerteformulier (Gravity Forms) met een projectadres en bestandsuploads. Beide
worden hier door het formuliercomponent van het template gerenderd; op de
offertepagina met het extra veld projectadres, zoals de bron dat ook heeft.

Let op: het formulier verstuurt nog niets. ENDPOINT in contactformulier.js is
leeg. Dat gold al voor het template en is met deze migratie niet veranderd.

Privacybeleid en cookies horen bij de cookiemelding van het template, die naar
beide pagina's linkt. De bronsite heeft die pagina's niet; wat er hier staat is
de AVG-alinea die bij beide formulieren van Duyts stond, en verder een
markering. Er is geen beleid verzonnen.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *          # noqa: F401,F403
import inhoud_duyts as D
import inhoud_copy as C

UIT = pathlib.Path(__file__).resolve().parent.parent

AVG = D.CONTACT['contactForm']['privacyText']


def _p(alineas):
    return "\n".join(f'              <p>{D._tekens(a)}</p>' for a in alineas)


# ---------------------------------------------------------------------- contact
def contact():
    c = D.CONTACT
    # De gegevens staan onder het formulier in de vlakkenrij van het template:
    # vier vlakken in navy, grijs, wit en indigo, tekst onderin, tot de
    # schermrand. De kleuren lopen vast in die volgorde, dus adres, telefoon,
    # e-mail en KvK krijgen op elke pagina hetzelfde vlak.
    #
    # De openingstijden staan er niet bij. Die zijn niet bekend en een leeg
    # gekleurd vlak met een markering erin leest als een fout; de markering
    # staat in CONTENT-TODO.md. Zodra Duyts ze aanlevert horen ze in het
    # telefoonvlak, onder het nummer, zodat de rij op vier vlakken blijft.
    gegevens = [
        ('Adres', f'{D.STRAAT}<br>{D.POSTCODE_PLAATS}'),
        ('Telefoon', f'<a href="tel:{D.TELEFOON_LINK}">{D.TELEFOON_WEERGAVE}</a>'),
        ('E-mail', f'<a href="mailto:{D.EMAIL}">{D.EMAIL}</a>'),
        ('KvK', D.KVK),
    ]

    inhoud = f'''{patroonhero("01", "contact", "Contact", C.CONTACT['h1'])}

  <section class="content-block" id="s02-introductie">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
            <div class="article-body">
{_p(C.CONTACT['lead'])}
            </div>
            <div style="margin-top:var(--space-600)">
              {knop("Vraag een offerte aan", "offerte.html")}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{contactblok({"nr": "03", "waarde": "overig"}, kop=C.CONTACT['formulier_kop'],
             intro=C.CONTACT['formulier_lead'])}

{citaten("04")}

{vlakkenrij("05", "gegevens", D.NAAM, gegevens, subtitel="Gegevens")}

  <section class="content-block" id="s06-privacy">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Uw gegevens</span>
            <div class="article-body" style="margin-top:var(--space-500)">
{_p([AVG])}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''
    (UIT / 'contact.html').write_text(pagina(
        bestand='contact.html',
        titel=c['metaTitle'] if not c['metaTitle'].startswith('[') else f'Contact | {D.NAAM}',
        omschrijving=c['metaDescription'] if not c['metaDescription'].startswith('[') else '',
        namespace='contact', pagina_css='contact.css', css_naam='contact',
        inhoud=inhoud,
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "ContactPage",
            "name": "Contact",
            "url": BASIS + "/contact.html",
        }, ensure_ascii=False, indent=2),
    ), encoding='utf-8')
    return 'contact.html'


# ---------------------------------------------------------------------- offerte
def offerte():
    o = D.OFFERTE
    # De intro van de bronsite bevat het telefoonnummer in de lopende tekst; die
    # blijft staan, maar wordt een link zodat je hem op een telefoon kunt bellen.
    intro = D._tekens(o['intro']).replace(
        D.TELEFOON_WEERGAVE, f'<a href="tel:{D.TELEFOON_LINK}">{D.TELEFOON_WEERGAVE}</a>')
    upload = D._tekens(o['fileUploadNote']).replace(
        'info@duyts.nl', f'<a href="mailto:{D.EMAIL}">{D.EMAIL}</a>')
    na_ontvangst = next((p for s in o['sections'] for p in s['paragraphs']
                         if p.startswith('Na ontvangst')), '')

    inhoud = f'''{paginahero("01", "offerte", "Offerte", C.OFFERTE['h1'], "duyts-dienst-constructieberekening")}

  <section class="content-text-side-cta" id="s02-introductie">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body article-body">
{_p(C.OFFERTE['lead'])}
              <p>Liever bellen? Dat kan ook: <a href="tel:{D.TELEFOON_LINK}">{D.TELEFOON_WEERGAVE}</a>.</p>
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop("Onze werkwijze", "werkwijze.html", "secundair")}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="band background--grey" id="s03-formulier">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle">Offerte</span>
          <h2 class="section-heading" style="margin:var(--space-500) 0">{C.OFFERTE['formulier_kop']}</h2>
          <p class="article-body">{C.OFFERTE['formulier_lead']}</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            Liever bellen? <a href="tel:{D.TELEFOON_LINK}">{D.TELEFOON_WEERGAVE}</a>
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <!-- data-projectadres zet het extra veld aan dat de bronsite hier ook
               vraagt. Bestanden kunnen niet via dit formulier mee: de bron
               verwijst daarvoor naar de mail, en die regel staat eronder. -->
          <div data-contactformulier data-onderwerp="offerte" data-projectadres data-bijlagen></div>
          <noscript>
            <p class="article-body">Het formulier heeft JavaScript nodig. Mail uw aanvraag gerust naar
              <a href="mailto:{D.EMAIL}">{D.EMAIL}</a> of bel {D.TELEFOON_WEERGAVE}.</p>
          </noscript>
          <p class="article-body" style="margin-top:var(--space-600)">{upload}</p>
        </div>
      </div>
    </div>
  </section>

{citaten("04")}

  <section class="content-block" id="s05-privacy">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Uw gegevens</span>
            <div class="article-body" style="margin-top:var(--space-500)">
{_p([o['privacyText']])}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''
    (UIT / 'offerte.html').write_text(pagina(
        bestand='offerte.html', titel=f'Offerte aanvragen | {D.NAAM}',
        omschrijving=('Vraag vrijblijvend een offerte aan voor een constructieberekening, '
                      'funderingsonderzoek of funderingsherstel.'),
        namespace='offerte', pagina_css='contact.css', css_naam='contact',
        inhoud=inhoud,
    ), encoding='utf-8')
    return 'offerte.html'


# ------------------------------------------------------------- tekstpagina's
def _tekstpagina(bestand, titel, omschrijving, kop, blokken):
    secties = []
    for i, (subkop, alineas) in enumerate(blokken, start=2):
        kopregel = f'            <h2 class="font-size--md" style="margin-bottom:var(--space-400)">{subkop}</h2>\n' if subkop else ''
        secties.append(f'''  <section class="content-block" id="s{i:02d}-blok">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
{kopregel}            <div class="article-body">
{_p(alineas)}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>''')
    inhoud = patroonhero('01', 'kop', titel, kop) + "\n\n" + "\n\n".join(secties)
    (UIT / bestand).write_text(pagina(
        bestand=bestand, titel=f'{titel} | {D.NAAM}', omschrijving=omschrijving,
        namespace='tekst', pagina_css='tekstpagina.css', css_naam='tekstpagina',
        inhoud=inhoud,
    ), encoding='utf-8')
    return bestand


def privacybeleid():
    # De bronsite heeft geen privacyverklaring. Wat er wel staat is de AVG-alinea
    # bij de formulieren; die is hier overgenomen. De rest is een markering,
    # want een privacyverklaring verzinnen zou juridisch onjuiste tekst opleveren.
    return _tekstpagina(
        'privacybeleid.html', 'Privacybeleid',
        'Hoe Duyts Bouwconstructies met uw persoonsgegevens omgaat.',
        'Privacybeleid',
        [(None, [AVG]),
         ('Nog aan te leveren',
          [f'{D.NIET_GEVONDEN} De bronsite heeft geen privacyverklaring. Deze pagina bevat '
           'alleen de passage die bij de formulieren van Duyts stond. Een volledige '
           'verklaring moet door Duyts worden aangeleverd: welke gegevens worden '
           'vastgelegd, hoe lang ze worden bewaard, met wie ze worden gedeeld, en hoe '
           'iemand zijn gegevens kan opvragen of laten verwijderen.']),
         ('Contact over uw gegevens',
          [f'Vragen over uw gegevens? Bel {D.TELEFOON_WEERGAVE} of mail naar {D.EMAIL}.'])])


def cookies():
    return _tekstpagina(
        'cookies.html', 'Cookies',
        'Welke cookies deze website plaatst en waarvoor.',
        'Cookies',
        [(None, ['Deze website plaatst alleen cookies die nodig zijn om de site te laten '
                 'werken. Analytische cookies staan uit tot u ze zelf aanzet via de '
                 'cookiemelding; daarin kunt u uw keuze ook weer wijzigen.']),
         ('Nog aan te leveren',
          [f'{D.NIET_GEVONDEN} De bronsite heeft geen cookieverklaring. Zodra bekend is '
           'welk statistiekpakket wordt gebruikt en welke cookies dat plaatst, hoort '
           'die opsomming hier: naam, doel en bewaartermijn per cookie.']),
         ('Contact over cookies',
          [f'Vragen hierover? Bel {D.TELEFOON_WEERGAVE} of mail naar {D.EMAIL}.'])])


def main():
    gemaakt = [contact(), offerte(), privacybeleid(), cookies()]
    print(f'{len(gemaakt)} contact- en tekstpagina\'s geschreven')
    return gemaakt


if __name__ == '__main__':
    main()
