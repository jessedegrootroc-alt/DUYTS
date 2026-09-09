# -*- coding: utf-8 -*-
"""Bouwt de hele site opnieuw op uit de Duyts-content.

    python3 bouw_alles.py

De HTML in de hoofdmap is gegenereerd; pas je daar met de hand iets aan, dan is
dat weg zodra dit script draait. Tekst wijzig je in _generator/duyts/ (de
contentexport van www.duyts.nl), de indeling in de bouwscripts hieronder.

De afbeeldingen worden hier NIET opnieuw omgezet; dat doet maak_assets.py en dat
hoeft alleen als er beeld bijkomt of verandert.
"""
import bouw_duyts_home
import bouw_duyts_dienst
import bouw_duyts_projecten
import bouw_duyts_bedrijf
import bouw_duyts_contact
import bouw_duyts_sitemap

bouw_duyts_dienst.main()
bouw_duyts_projecten.main()
bouw_duyts_bedrijf.main()
bouw_duyts_contact.main()
bouw_duyts_sitemap.main()
print('klaar')
