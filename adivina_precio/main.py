from requests_html import HTMLSession
from append import speak, listen

session = HTMLSession()
main_site = session.get("https://www.coolmod.com/")
categories = main_site.html.find(".subfamilyheadertittle")
print (categories)

#<li class="sc-ezredP gfszhj"><div class="sc-fFucqa sc-iktFfs gNKfuN hMiGLm"><a href="https://www.pccomponentes.com/portatiles/windows-10-64-bits/windows-10-home-64-bits/windows-10-pro-64-bits/windows-10-s/windows-11-home/windows-11-pro/windows-11-s" title="Portátiles con Windows" class="sc-bqyKOL kLzqrr sc-bBrNTY gpUgjV">Portátiles con Windows</a></div></li>