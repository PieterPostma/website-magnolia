# -*- coding: utf-8 -*-
"""Bouwt versie-1, versie-2 en versie-3 in de projectmap. Draaien: python bouw/build.py"""
import os, sys, importlib
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
ROOT = os.path.dirname(HIER)
from common import *

VERSIES = [("versie-1", "v1"), ("versie-2", "v2"), ("versie-3", "v3")]
if len(sys.argv) > 1:
    VERSIES = [v for v in VERSIES if v[0] in sys.argv[1:]]


def schrijf(pad, inhoud):
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    with open(pad, "w", encoding="utf-8") as f:
        f.write(inhoud)


for map_, mod in VERSIES:
    v = importlib.import_module(mod)
    import common; common.KOP_STIJL = v.THEMA.get("kop", "zij")
    out = os.path.join(ROOT, map_)
    schrijf(os.path.join(out, "stijl.css"), BASIS_CSS + v.CSS)
    schrijf(os.path.join(out, "script.js"), v.JS)
    schrijf(os.path.join(out, "index.html"), v.home())
    for slug, pag in PAGINAS.items():
        schrijf(os.path.join(out, slug + ".html"), subpagina(slug, pag, v.THEMA))
    for p in PIJLERS:
        schrijf(os.path.join(out, "werkwijze", p["slug"] + ".html"), pijlerpagina(p, v.THEMA))
    schrijf(os.path.join(out, "blog.html"), blogpagina(v.THEMA))
    for a in ARTIKELEN:
        schrijf(os.path.join(out, "blog", a["slug"] + ".html"), artikelpagina(a, v.THEMA))
    schrijf(os.path.join(out, "privacy.html"), juridisch("privacy", "Privacyverklaring", v.THEMA))
    schrijf(os.path.join(out, "algemene-voorwaarden.html"), juridisch("algemene-voorwaarden", "Algemene voorwaarden", v.THEMA))
    print("gebouwd:", map_, v.THEMA["naam"])

if len(sys.argv) > 1:
    sys.exit(0)
# keuzepagina
kaarten = ""
beschr = {"v1": ("Bloesem", "Licht en luchtig. Blush dat overloopt in lavendel, een boogportret in de hero en een magnolia die naast de vijf pijlers meegroeit terwijl je scrolt. Aan het eind dwarrelen de bloesemblaadjes over de pagina."),
          "v2": ("Verloop", "Editorial en warm. Groot gecentreerd logo, een diepe mauve hero met handtekening, natuurfoto's als rustige overgangen, video, reviews en thema's met meebewegende foto."),
          "v3": ("Water", "Fotografisch en rustig. Volledig beeld van het water als opening, lichtblauw en salie met oudroze accenten, en een verhalende sectie waarin de magnolia groeit terwijl de vijf pijlers één voor één verschijnen.")}
for map_, mod in VERSIES:
    n, b = beschr[mod]
    kaarten += f'<a class="kaart" href="{map_}/index.html"><span class="nr">{map_[-1]}</span><h2>{n}</h2><p>{b}</p><span class="open">Open versie {map_[-1]} →</span></a>'
schrijf(os.path.join(ROOT, "index.html"), f"""<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Liesbeth Postma – drie voorstellen</title>
<link rel="icon" href="assets/favicon.png"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,400&family=Jost:wght@400;500&display=swap" rel="stylesheet">
<style>body{{margin:0;font-family:Jost,sans-serif;background:linear-gradient(160deg,#fdf3f0,#f0e6ef 50%,#dde5ef);color:#4a343a;min-height:100vh;display:grid;place-items:center;padding:2rem}}
.in{{max-width:1100px;text-align:center}}img{{width:280px;margin:0 auto 1rem}}h1{{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:2.6rem;margin:0 0 .3em}}h1 em{{color:#b85860}}
.lead{{max-width:620px;margin:0 auto 2.5rem;color:#6d5a60}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;text-align:left}}
.kaart{{background:rgba(255,255,255,.75);border:1px solid #f0dcd8;border-radius:28px;padding:2rem;text-decoration:none;color:inherit;transition:transform .3s,box-shadow .3s;display:flex;flex-direction:column}}
.kaart:hover{{transform:translateY(-6px);box-shadow:0 30px 60px -35px rgba(120,60,70,.5)}}.nr{{font-family:'Cormorant Garamond',serif;font-size:2.4rem;color:#efa6a2;line-height:1}}
h2{{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:1.9rem;margin:.2rem 0 .5rem}}p{{flex:1;font-size:.95rem;line-height:1.6}}.open{{color:#b85860;font-weight:500}}
@media(max-width:800px){{.grid{{grid-template-columns:1fr}}}}</style></head><body><div class="in">
<img src="assets/logo-wit.png" alt="Liesbeth Postma" style="border-radius:20px"><h1>Drie voorstellen voor <em>liesbethpostma.nl</em></h1>
<p class="lead">Dezelfde teksten, foto's en huisstijl – drie keer een andere uitstraling. Scrol in elke versie rustig naar beneden: de magnolia groeit mee.</p>
<div class="grid">{kaarten}</div></div></body></html>""")
print("klaar")
