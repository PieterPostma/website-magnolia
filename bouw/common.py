# -*- coding: utf-8 -*-
"""Gedeelde bouwstenen: head, navigatie, footer, subpagina's, basis-CSS en JS."""
import html
from content import *

A = "../assets/"
KOP_STIJL = "zij"  # of "midden" (groot logo gecentreerd boven de navigatie)


def esc(s):
    return html.escape(s, quote=False)


def head(titel, beschrijving, thema, extra_css="", prefix=""):
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titel)}</title>
<meta name="description" content="{esc(beschrijving)}">
<meta property="og:title" content="{esc(titel)}">
<meta property="og:description" content="{esc(beschrijving)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{prefix}{A}foto/portret-lach.jpg">
<link rel="icon" type="image/png" href="{prefix}{A}favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={thema['fonts']}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}stijl.css">
{extra_css}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Liesbeth Postma – Psychosociaal en lichaamsgericht therapeut","telephone":"{TEL_RAW}","email":"{MAIL}","address":{{"@type":"PostalAddress","streetAddress":"Dijkstraat 20","addressLocality":"Bemmel","addressCountry":"NL"}},"image":"{prefix}{A}foto/portret-lach.jpg","priceRange":"€€"}}
</script>
</head>
"""


def nav(actief="", prefix=""):
    """prefix = '../' voor pagina's in een submap."""
    items = []
    for m in MENU:
        if m[1] is None:
            sub = []
            for s in m[2]:
                if s[0] == "—":
                    sub.append('<li class="sep" role="separator"></li>')
                else:
                    sub.append(f'<li><a href="{prefix}{s[1]}">{esc(s[0])}</a></li>')
            items.append(f'''<li class="heeft-sub"><button type="button" aria-expanded="false" aria-haspopup="true">{esc(m[0])}<svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></button><ul class="sub">{''.join(sub)}</ul></li>''')
        else:
            cls = ' class="actief"' if actief == m[1] else ""
            items.append(f'<li><a{cls} href="{prefix}{m[1]}">{esc(m[0])}</a></li>')
    hamburger = '<button class="hamburger" type="button" aria-label="Menu openen" aria-expanded="false" aria-controls="mobiel"><span></span><span></span><span></span></button>'
    if KOP_STIJL == "midden":
        kop = f"""<header class="kop kop-midden" id="kop">
  <div class="kop-in">
    <a class="merk" href="{prefix}index.html" aria-label="Liesbeth Postma – home">
      <img src="{prefix}{A}logo.png" alt="Liesbeth Postma – Leer te voelen, durf te vertrouwen" width="1391" height="850">
    </a>
    <div class="kop-rij">
      <nav class="navi" aria-label="Hoofdmenu"><ul>{''.join(items)}</ul></nav>
      <a class="knop knop-klein kop-cta" href="{prefix}contact.html">Kennismaken</a>
    </div>
    {hamburger}
  </div>
</header>"""
    else:
        kop = f"""<header class="kop" id="kop">
  <div class="kop-in">
    <a class="merk" href="{prefix}index.html" aria-label="Liesbeth Postma – home">
      <img src="{prefix}{A}beeldmerk.png" alt="" width="48" height="48">
      <span class="merk-tekst"><span class="merk-naam">Liesbeth Postma</span><span class="merk-sub">Psychosociaal en lichaamsgericht therapeut</span></span>
    </a>
    <nav class="navi" aria-label="Hoofdmenu"><ul>{''.join(items)}</ul></nav>
    <a class="knop knop-klein kop-cta" href="{prefix}contact.html">Kennismaken</a>
    {hamburger}
  </div>
</header>"""
    return f"""<a class="skip" href="#inhoud">Naar de inhoud</a>
{kop}
<div class="mobiel" id="mobiel" hidden>
  <ul>{''.join(items)}</ul>
  <a class="knop" href="{prefix}contact.html">Neem contact op</a>
</div>
"""


def footer(prefix=""):
    thema_links = "".join(f'<li><a href="{prefix}{t["slug"]}.html">{esc(t["kop"])}</a></li>' for t in THEMAS)
    pijler_links = "".join(f'<li><a href="{prefix}werkwijze/{p["slug"]}.html">{esc(p["kop"].split(" – ")[0])}</a></li>' for p in PIJLERS)
    return f"""<footer class="voet">
  <div class="voet-in">
    <div class="voet-merk">
      <img src="{prefix}{A}logo-wit.png" alt="Liesbeth Postma – Leer te voelen, durf te vertrouwen" width="260" loading="lazy">
      <p class="voet-motto">{esc(STROOM)}</p>
      <p class="voet-social">
        <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.5M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></svg></a>
        <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8.5A.5.5 0 0 1 14 8z"/></svg></a>
      </p>
    </div>
    <div class="voet-kol">
      <h3>Waarmee kan ik je helpen?</h3>
      <ul>{thema_links}<li><a href="{prefix}familieopstellingen.html">Familieopstellingen</a></li><li><a href="{prefix}workshops.html">Workshops</a></li></ul>
    </div>
    <div class="voet-kol">
      <h3>Werkwijze</h3>
      <ul>{pijler_links}<li><a href="{prefix}werkwijze.html">Wat kan mijn begeleiding jou brengen</a></li></ul>
    </div>
    <div class="voet-kol">
      <h3>Contact</h3>
      <ul>
        <li><a href="tel:{TEL_RAW}">{TEL}</a></li>
        <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        <li>{esc(ADRES)}<br><small>tijdelijke praktijklocatie</small></li>
        <li><a href="{prefix}praktische-informatie.html">Praktische info &amp; tarieven</a></li>
        <li><a href="{prefix}blog.html">Blog</a></li>
      </ul>
    </div>
  </div>
  <div class="voet-onder">
    <p>© 2026 Liesbeth Postma · Psychosociaal en lichaamsgericht therapeut · KvK {KVK} · BTW {BTW}</p>
    <p><a href="{prefix}privacy.html">Privacyverklaring</a> · <a href="{prefix}algemene-voorwaarden.html">Algemene voorwaarden</a></p>
  </div>
</footer>
"""


# ---------- blokken op subpagina's ----------

def blok_html(b, prefix=""):
    t = b[0]
    if t == "h2":
        return f"<h2>{esc(b[1])}</h2>"
    if t == "p":
        return f"<p>{b[1]}</p>"
    if t == "ul":
        return "<ul class='lijst'>" + "".join(f"<li>{esc(x)}</li>" for x in b[1]) + "</ul>"
    if t == "quote":
        return f'<blockquote class="citaat"><p>{esc(b[1])}</p></blockquote>'
    if t == "motto":
        return f'<p class="motto-regel"><strong>{esc(MOTTO)}.</strong><br>{esc(STROOM)}</p>'
    if t == "stroom":
        return f'<p class="motto-regel"><em>{esc(STROOM)}</em></p>'
    if t == "cta":
        return f'<p class="cta-rij"><a class="knop" href="{prefix}{b[2]}">{esc(b[1])}</a></p>'
    if t == "cta2":
        return f'<p class="cta-rij"><a class="knop knop-licht" href="{prefix}{b[2]}">{esc(b[1])}</a> <a class="knop" href="{prefix}{b[4]}">{esc(b[3])}</a></p>'
    if t == "box":
        return f'<aside class="kader"><h3>{esc(b[1])}</h3>' + "".join(f"<p>{esc(p)}</p>" for p in b[2]) + "</aside>"
    if t == "begeleiding":
        return f"""<aside class="kader kader-zacht"><h3>Hoe ik je kan begeleiden</h3>
<p>Afhankelijk van jouw hulpvraag combineren we psychosociale en lichaamsgerichte begeleiding met innerlijk-kindwerk, delenwerk en ACT. We onderzoeken wat jouw gevoelens en lichaam aangeven, welke beschermingspatronen mogelijk meespelen en welke stappen bij jou passen.</p>
<p>Verdieping over de vijf pijlers vind je op de pagina <a href="{prefix}werkwijze.html">Werkwijze</a>.</p></aside>"""
    if t == "tarieven":
        kaarten = "".join(f"""<div class="tarief"><span class="tarief-naam">{esc(n)}</span><span class="tarief-duur">{esc(d)}</span><span class="tarief-prijs">{esc(p)}</span><p>{esc(txt)}</p></div>""" for n, d, p, txt in TARIEVEN)
        return f'<div class="tarieven">{kaarten}</div>'
    if t == "pijlers":
        kaarten = "".join(f"""<article class="pijler" id="{p['slug']}"><span class="pijler-nr">0{i+1}</span><h3>{esc(p['kop'])}</h3><p>{esc(p['tekst'])}</p><a class="pijl-link" href="{prefix}werkwijze/{p['slug']}.html">Lees meer <span aria-hidden="true">→</span></a></article>""" for i, p in enumerate(PIJLERS))
        return f'<h2 id="pijlers">Mijn vijf pijlers</h2><p>De vijf pijlers hieronder vormen de basis van mijn begeleiding. Klik door voor een verdiepende uitleg per pijler.</p><div class="pijlers">{kaarten}</div>'
    if t == "reviews":
        return reviews_html("Wat cliënten zeggen", "Ervaringen van mensen die ik mocht begeleiden")
    if t == "contact":
        return f"""<div class="contact-kaart">
  <div class="contact-gegevens">
    <p class="contact-naam"><strong>{NAAM}</strong><br>{TITEL}</p>
    <p><a class="contact-regel" href="tel:{TEL_RAW}"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>{TEL}</a></p>
    <p><a class="contact-regel" href="mailto:{MAIL}"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>{MAIL}</a></p>
    <p class="contact-regel"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 22s7-7 7-12a7 7 0 0 0-14 0c0 5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>{esc(ADRES)} <small>(tijdelijke locatie)</small></p>
  </div>
  <form class="formulier" action="mailto:{MAIL}" method="post" enctype="text/plain" onsubmit="return window.verstuur ? window.verstuur(this) : true">
    <label>Je naam<input type="text" name="naam" required autocomplete="name"></label>
    <label>Je e-mailadres<input type="email" name="email" required autocomplete="email"></label>
    <label>Je telefoonnummer <small>(voor het kennismakingsgesprek)</small><input type="tel" name="telefoon" autocomplete="tel"></label>
    <label>Waar wil je het over hebben?<textarea name="bericht" rows="5" required></textarea></label>
    <button class="knop" type="submit">Verstuur bericht</button>
    <p class="formulier-nb"><small>Een kennismakingsgesprek vindt telefonisch plaats. Ik neem binnen twee werkdagen contact met je op.</small></p>
  </form>
</div>"""
    return ""


def reviews_html(boven, kop, extra_cls=""):
    kaarten = "".join(f"""<figure class="review reveal vertraag-{(i%4)+1}"><blockquote><strong>{esc(k)}</strong><p>{esc(t)}</p></blockquote><figcaption>{esc(n)}</figcaption></figure>""" for i, (n, k, t) in enumerate(REVIEWS))
    return f'<div class="reviews {extra_cls}"><div class="reviews-kop reveal"><p class="boventitel">{esc(boven)}</p><h2>{esc(kop)}</h2></div><div class="reviews-grid">{kaarten}</div></div>'


def subpagina(slug, pag, thema, prefix=""):
    """Volledige subpagina (artikel-layout)."""
    body = "".join(blok_html(b, prefix) for b in pag["blokken"])
    foto = pag.get("foto")
    hero_foto = f'<div class="pag-foto"><img src="{prefix}{A}foto/{foto}" alt="" loading="eager"></div>' if foto else ""
    return (head(pag["seo_titel"], pag["seo"], thema, prefix=prefix) + f"""<body class="pagina pagina-{slug}">
{nav(slug + '.html', prefix)}
<main id="inhoud">
  <section class="pag-hero">
    <div class="pag-hero-in">
      <div class="pag-hero-tekst reveal">
        <p class="boventitel">{esc(pag.get('boven', 'Liesbeth Postma'))}</p>
        <h1>{esc(pag['kop'])}</h1>
        <p class="pag-sub">{esc(pag['sub'])}</p>
      </div>
      {hero_foto}
    </div>
  </section>
  <article class="pag-inhoud">
    <div class="tekst reveal">{body}</div>
  </article>
  {slotband(prefix)}
</main>
{footer(prefix)}
{scripts(prefix)}
</body></html>""")


def pijlerpagina(p, thema):
    pag = dict(kop=p["kop"], sub="Een van mijn vijf pijlers", foto=None, seo_titel=p["seo_titel"], seo=p["seo"], boven="Werkwijze",
               blokken=[("p", esc(p["tekst"])), ("h2", "Wat betekent dit in de begeleiding?"), ("p", esc(p["praktijk"])),
                        ("h2", "Leer te voelen – durf te vertrouwen"), ("p", "We werken vanuit rust, gelijkwaardigheid en veiligheid. Samen onderzoeken we wat bij jou past."),
                        ("cta2", "Alle pijlers bekijken", "werkwijze.html#pijlers", "Neem contact op", "contact.html")])
    andere = "".join(f'<li><a href="{q["slug"]}.html"{" aria-current=page" if q is p else ""}>{esc(q["kop"].split(" – ")[0])}</a></li>' for q in PIJLERS)
    h = subpagina("werkwijze", pag, thema, prefix="../")
    return h.replace('<article class="pag-inhoud">', f'<nav class="pijler-nav" aria-label="Pijlers"><ul>{andere}</ul></nav><article class="pag-inhoud">')


def blogpagina(thema):
    kaarten = ""
    for i, a in enumerate(ARTIKELEN):
        label = f"{esc(a['datum'])} · Nieuw" if i == 0 else esc(a['datum'])
        kaarten += f"""<article class="blog-kaart reveal{' blog-kaart-klein' if i else ''}">
  <a href="blog/{a['slug']}.html" class="blog-foto"><img src="{A}foto/{a['foto']}" alt="" loading="lazy"></a>
  <div class="blog-tekst"><p class="boventitel">{label}</p><h2><a href="blog/{a['slug']}.html">{esc(a['titel'])}</a></h2><p class="blog-onder">{esc(a['onder'])}</p><p>{esc(a['intro'])}</p><a class="pijl-link" href="blog/{a['slug']}.html">Lees het hele artikel <span aria-hidden="true">→</span></a></div>
</article>"""
    pag = dict(kop=BLOG["kop"], sub=BLOG["sub"], foto=None, seo_titel=BLOG["seo_titel"], seo=BLOG["seo"], boven="Blog", blokken=[("p", x) for x in BLOG["intro"]])
    h = subpagina("blog", pag, thema)
    return h.replace('</article>\n', f'</article>\n<section class="blog-lijst">{kaarten}</section>\n', 1)


def artikelpagina(a, thema):
    pag = dict(kop=a["titel"], sub=a["onder"], foto=a["foto"], seo_titel=a["seo_titel"], seo=a["seo"], boven=f"Blog · {a['datum']}", blokken=a["blokken"] + [("cta2", "Terug naar het blogoverzicht", "blog.html", "Neem contact op", "contact.html")])
    return subpagina("blog", pag, thema, prefix="../")


def juridisch(slug, kop, thema):
    tekst = {"privacy": PRIVACY, "algemene-voorwaarden": VOORWAARDEN}[slug]
    pag = dict(kop=kop, sub="Liesbeth Postma", foto=None, seo_titel=f"{kop} | Liesbeth Postma", seo=kop, blokken=tekst)
    return subpagina(slug, pag, thema)


def slotband(prefix=""):
    return f"""<section class="slotband reveal">
  <div class="slotband-in">
    <img class="slot-merk" src="{prefix}{A}beeldmerk.png" alt="" width="90" loading="lazy">
    <h2>{esc(MOTTO)}</h2>
    <p>{esc(STROOM)}</p>
    <a class="knop" href="{prefix}contact.html">Plan een kennismaking</a>
  </div>
</section>"""


def scripts(prefix=""):
    return f'<script src="{prefix}script.js" defer></script>'


# ---------- basis CSS, gedeeld door alle versies (thema-variabelen worden per versie gezet) ----------

BASIS_CSS = r"""
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}}
body{margin:0;font-family:var(--f-body);font-size:1.05rem;line-height:1.7;color:var(--ink);background:var(--bg);overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:3px}
h1,h2,h3,h4{font-family:var(--f-head);font-weight:var(--head-w,500);line-height:1.15;color:var(--head);margin:0 0 .5em;letter-spacing:-.01em}
h1{font-size:clamp(2.4rem,5.5vw,4.2rem)}
h2{font-size:clamp(1.8rem,3.6vw,2.6rem)}
h3{font-size:1.35rem}
p{margin:0 0 1.1em}
.skip{position:absolute;left:-999px;top:0;background:var(--accent);color:#fff;padding:.5rem 1rem;z-index:1000}.skip:focus{left:1rem}
.boventitel{font-family:var(--f-body);text-transform:uppercase;letter-spacing:.18em;font-size:.78rem;color:var(--accent);margin-bottom:1rem;font-weight:600}
.knop{display:inline-flex;align-items:center;gap:.5rem;background:var(--accent);color:#fff;border:1px solid var(--accent);padding:.9rem 1.7rem;border-radius:var(--r-knop,999px);font-weight:600;font-family:var(--f-body);text-decoration:none;font-size:.98rem;transition:transform .25s,box-shadow .25s,background .25s;cursor:pointer}
.knop:hover{transform:translateY(-2px);box-shadow:0 10px 24px -10px var(--accent);background:var(--accent-d)}
.knop-licht{background:transparent;color:var(--accent)}.knop-licht:hover{background:var(--accent);color:#fff}
.knop-klein{padding:.6rem 1.2rem;font-size:.9rem}
.pijl-link{font-weight:600;text-decoration:none;display:inline-flex;gap:.4rem;align-items:center}.pijl-link span{transition:transform .25s}.pijl-link:hover span{transform:translateX(4px)}

/* ---- kop / navigatie ---- */
.kop{position:sticky;top:0;z-index:50;background:var(--kop-bg);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);transition:box-shadow .3s,background .3s}
.kop.gescrold{box-shadow:0 6px 30px -16px rgba(80,40,50,.35)}
.kop-in{max-width:1240px;margin:0 auto;padding:.7rem 1.25rem;display:flex;align-items:center;gap:1.5rem}
.merk{display:flex;align-items:center;gap:.7rem;text-decoration:none;color:var(--head)}
.merk img{width:46px;height:auto}
.merk-tekst{display:flex;flex-direction:column;line-height:1.1}
.merk-naam{font-family:var(--f-script,var(--f-head));font-size:var(--merk-size,1.5rem);color:var(--accent)}
.merk-sub{font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.navi{margin-left:auto}.navi>ul{list-style:none;margin:0;padding:0;display:flex;gap:.2rem;align-items:center}
.navi a,.navi button{white-space:nowrap;display:inline-flex;align-items:center;gap:.35rem;padding:.55rem .85rem;border-radius:999px;color:var(--head);text-decoration:none;font-size:.93rem;font-weight:500;background:none;border:0;font-family:inherit;cursor:pointer;transition:background .2s,color .2s}
.navi a:hover,.navi button:hover,.navi a.actief{background:var(--tint);color:var(--accent)}
.heeft-sub{position:relative}
.sub{position:absolute;top:calc(100% + .4rem);left:0;min-width:270px;background:var(--surface);border-radius:18px;box-shadow:0 20px 50px -20px rgba(80,40,50,.35);padding:.6rem;list-style:none;margin:0;opacity:0;visibility:hidden;transform:translateY(8px);transition:opacity .25s,transform .25s,visibility .25s}
.heeft-sub:hover .sub,.heeft-sub:focus-within .sub,.heeft-sub.open .sub{opacity:1;visibility:visible;transform:none}
.sub a{display:block;border-radius:12px;padding:.55rem .8rem}
.sub .sep{height:1px;background:var(--line);margin:.4rem .6rem}
.kop-cta{white-space:nowrap}
.hamburger{display:none;width:44px;height:44px;border:0;background:none;flex-direction:column;justify-content:center;gap:5px;cursor:pointer;margin-left:auto}
.hamburger span{display:block;height:2px;background:var(--head);border-radius:2px;transition:transform .3s,opacity .3s}
.hamburger[aria-expanded=true] span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.hamburger[aria-expanded=true] span:nth-child(2){opacity:0}
.hamburger[aria-expanded=true] span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.mobiel{position:fixed;inset:var(--mobiel-top,66px) 0 0;background:var(--bg);z-index:49;padding:1.5rem;overflow:auto}
.mobiel ul{list-style:none;padding:0;margin:0 0 1.5rem}.mobiel li{border-bottom:1px solid var(--line)}
.mobiel a,.mobiel button{display:block;width:100%;text-align:left;padding:.9rem 0;font-size:1.1rem;color:var(--head);text-decoration:none;background:none;border:0;font-family:inherit}
.mobiel .sub{position:static;opacity:1;visibility:visible;transform:none;box-shadow:none;background:none;padding:0 0 .5rem 1rem}
.mobiel .sub a{font-size:1rem;padding:.5rem 0}
.mobiel .sep{display:none}
.mobiel .heeft-sub svg{display:none}
@media (max-width:1120px){.navi,.kop-cta{display:none}.hamburger{display:flex}}

.kop-midden .kop-in{flex-direction:column;gap:.5rem;padding:.9rem 1.25rem .6rem;position:relative}
.kop-midden .merk img{width:auto;height:var(--logo-h,118px);transition:height .35s cubic-bezier(.2,.7,.2,1)}
.kop-midden.gescrold .merk img{height:62px}
.kop-midden .kop-rij{display:flex;align-items:center;gap:1rem}
.kop-midden .navi{margin:0}
.kop-midden .hamburger{position:absolute;right:1rem;top:50%;transform:translateY(-50%)}
@media (max-width:1120px){.kop-midden .kop-in{padding:.6rem 1.25rem}.kop-midden .merk img{height:72px}.kop-midden.gescrold .merk img{height:54px}.kop-midden .kop-rij{display:none}}
.blog-kaart-klein{grid-template-columns:.55fr 1.45fr}.blog-kaart-klein .blog-foto{min-height:200px}.blog-kaart-klein .blog-tekst h2{font-size:1.4rem}.blog-kaart-klein .blog-tekst>p:nth-of-type(3){display:none}
@media (max-width:900px){.blog-kaart-klein{grid-template-columns:1fr}}

/* ---- algemene secties ---- */
.sectie{padding:clamp(4rem,9vw,7.5rem) 1.25rem}
.binnen{max-width:1160px;margin:0 auto}
.smal{max-width:760px;margin:0 auto}
.reveal{opacity:0;transform:translateY(26px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.reveal.zichtbaar{opacity:1;transform:none}
.vertraag-1{transition-delay:.12s}.vertraag-2{transition-delay:.24s}.vertraag-3{transition-delay:.36s}.vertraag-4{transition-delay:.48s}.vertraag-5{transition-delay:.6s}

/* ---- subpagina's ---- */
.pag-hero{padding:clamp(3rem,7vw,6rem) 1.25rem 0;background:var(--pag-hero-bg)}
.pag-hero-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:center}
.pag-sub{font-family:var(--f-head);font-size:1.45rem;color:var(--muted);font-style:italic;line-height:1.35}
.pag-foto{border-radius:var(--r-foto);overflow:hidden;aspect-ratio:4/3;transform:translateY(2.5rem);box-shadow:0 30px 60px -30px rgba(80,40,50,.4)}
.pag-foto img{width:100%;height:100%;object-fit:cover}
.pag-inhoud{padding:clamp(4rem,8vw,7rem) 1.25rem 2rem}
.tekst{max-width:740px;margin:0 auto}
.tekst h2{margin-top:2.2em;font-size:clamp(1.5rem,2.6vw,2rem)}
.tekst p{font-size:1.08rem}
.lijst{padding-left:0;list-style:none;margin:0 0 1.5em}
.lijst li{position:relative;padding-left:1.8rem;margin:.45em 0}
.lijst li::before{content:"";position:absolute;left:0;top:.55em;width:12px;height:12px;border-radius:50% 50% 50% 0;background:var(--accent-l);transform:rotate(-45deg)}
.citaat{margin:2.2em 0;padding:1.4rem 1.8rem;border-left:3px solid var(--accent-l);background:var(--tint);border-radius:0 20px 20px 0}
.citaat p{font-family:var(--f-head);font-size:1.45rem;font-style:italic;color:var(--head);margin:0;line-height:1.35}
.motto-regel{margin:2.5em 0 1.5em;font-family:var(--f-head);font-size:1.35rem;color:var(--accent);line-height:1.45}
.cta-rij{display:flex;flex-wrap:wrap;gap:.8rem;margin:1.5em 0 2.5em}
.kader{background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:1.8rem 2rem;margin:2em 0}
.kader h3{margin-bottom:.5em}
.kader-zacht{background:var(--tint);border-color:transparent}
.tarieven{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin:1.5em 0}
.tarief{background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:1.6rem;display:flex;flex-direction:column;transition:transform .3s,box-shadow .3s}
.tarief:hover{transform:translateY(-4px);box-shadow:0 24px 50px -30px rgba(80,40,50,.4)}
.tarief-naam{font-family:var(--f-head);font-size:1.4rem;color:var(--head)}
.tarief-duur{font-size:.85rem;text-transform:uppercase;letter-spacing:.12em;color:var(--muted)}
.tarief-prijs{font-family:var(--f-head);font-size:2.2rem;color:var(--accent);margin:.6rem 0 .4rem}
.tarief p{font-size:.95rem;margin:0}
.pijlers{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.2rem;margin:1.5em 0 3em}
.pijler{background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:1.6rem;scroll-margin-top:100px;transition:transform .3s,box-shadow .3s}
.pijler:hover{transform:translateY(-4px);box-shadow:0 24px 50px -30px rgba(80,40,50,.4)}
.pijler-nr{font-family:var(--f-head);font-size:2rem;color:var(--accent-l);line-height:1}
.pijler h3{font-size:1.2rem;margin:.4rem 0 .6rem}
.pijler p{font-size:.93rem}
.pijler-nav{max-width:740px;margin:2.5rem auto 0;padding:0 1.25rem}
.pijler-nav ul{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.5rem}
.pijler-nav a{display:inline-block;padding:.45rem 1rem;border-radius:999px;background:var(--tint);text-decoration:none;font-size:.9rem;color:var(--head)}
.pijler-nav a[aria-current]{background:var(--accent);color:#fff}
.contact-kaart{display:grid;grid-template-columns:1fr 1.3fr;gap:2.5rem;margin:1.5em 0 2em;background:var(--surface);border:1px solid var(--line);border-radius:28px;padding:2rem}
.contact-regel{display:inline-flex;gap:.6rem;align-items:center;text-decoration:none;color:var(--head);font-weight:500}
.formulier label{display:block;font-size:.9rem;font-weight:600;color:var(--head);margin-bottom:1rem}
.formulier input,.formulier textarea{display:block;width:100%;margin-top:.35rem;padding:.75rem 1rem;border:1px solid var(--line);border-radius:14px;font:inherit;background:var(--bg);color:var(--ink)}
.formulier input:focus,.formulier textarea:focus{outline:2px solid var(--accent-l);border-color:var(--accent)}
.formulier-nb{margin-top:1rem;color:var(--muted)}
.blog-lijst{max-width:860px;margin:0 auto;padding:0 1.25rem 4rem;display:grid;gap:2rem}
.blog-kaart{display:grid;grid-template-columns:.8fr 1.2fr;gap:2rem;background:var(--surface);border:1px solid var(--line);border-radius:28px;overflow:hidden}
.blog-foto{display:block;height:100%;min-height:260px}.blog-foto img{width:100%;height:100%;object-fit:cover;transition:transform .8s}.blog-kaart:hover .blog-foto img{transform:scale(1.04)}
.blog-tekst{padding:2rem 2rem 2rem 0}.blog-tekst h2{font-size:1.7rem}.blog-tekst h2 a{color:var(--head);text-decoration:none}
.blog-onder{font-family:var(--f-head);font-style:italic;color:var(--muted);font-size:1.15rem}
.slotband{margin:3rem 1.25rem 0;padding:clamp(3.5rem,7vw,6rem) 1.5rem;background:var(--slot-bg);border-radius:36px;text-align:center}
.slotband-in{max-width:720px;margin:0 auto}
.slot-merk{margin:0 auto 1rem;width:90px}
.slotband h2{font-size:clamp(1.8rem,3.5vw,2.6rem)}
.slotband p{font-family:var(--f-head);font-style:italic;font-size:1.3rem;color:var(--muted);margin-bottom:1.8rem}

/* ---- reviews ---- */
.reviews{margin:3em 0 2em}
.reviews-kop{max-width:640px;margin-bottom:2rem}
.reviews-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.4rem}
.review{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:28px;padding:2rem 2.2rem;position:relative;display:flex;flex-direction:column}
.review::before{content:"\201C";position:absolute;top:.6rem;left:1.6rem;font-family:var(--f-head);font-size:5rem;line-height:1;color:var(--accent-l);opacity:.7}
.review blockquote{margin:0;flex:1;padding-top:1.4rem}
.review strong{display:block;font-family:var(--f-head);font-weight:500;font-size:1.3rem;color:var(--head);margin-bottom:.6rem;line-height:1.3}
.review p{font-size:.98rem;margin:0}
.review figcaption{margin-top:1.2rem;font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);font-weight:600}
.review figcaption::before{content:"";display:inline-block;width:22px;height:1px;background:var(--accent);vertical-align:middle;margin-right:.6rem}
.tekst .reviews-grid{grid-template-columns:1fr}
@media (max-width:760px){.reviews-grid{grid-template-columns:1fr}}

/* ---- footer ---- */
.voet{margin-top:5rem;padding:4rem 1.25rem 2rem;background:var(--voet-bg);color:var(--voet-ink)}
.voet-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:2.5rem}
.voet-merk img{background:#fff;border-radius:18px;padding:.4rem;width:240px}
.voet-motto{font-family:var(--f-head);font-style:italic;font-size:1.15rem;margin-top:1.2rem;color:var(--voet-ink)}
.voet-social{display:flex;gap:.8rem}.voet-social a{color:var(--voet-ink);display:inline-flex;padding:.5rem;border-radius:50%;background:var(--voet-tint);transition:transform .25s}.voet-social a:hover{transform:translateY(-3px)}
.voet h3{font-size:.8rem;text-transform:uppercase;letter-spacing:.16em;color:var(--voet-kop);margin-bottom:1rem;font-family:var(--f-body);font-weight:700}
.voet ul{list-style:none;padding:0;margin:0}.voet li{margin:.45rem 0;font-size:.95rem}
.voet a{color:var(--voet-ink);text-decoration:none}.voet a:hover{text-decoration:underline}
.voet-onder{max-width:1160px;margin:3rem auto 0;padding-top:1.5rem;border-top:1px solid var(--voet-lijn);font-size:.8rem;color:var(--voet-muted);display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem}
.voet-onder p{margin:0}.voet-onder a{color:inherit}

/* ---- bloesem/petals canvas ---- */
.petals{position:fixed;inset:0;pointer-events:none;z-index:40}

@media (max-width:900px){
  .pag-hero-in{grid-template-columns:1fr;gap:1.5rem}.pag-foto{transform:none;margin-top:1rem;aspect-ratio:16/10}
  .tarieven{grid-template-columns:1fr}
  .contact-kaart{grid-template-columns:1fr;padding:1.5rem}
  .blog-kaart{grid-template-columns:1fr}.blog-tekst{padding:0 1.5rem 1.5rem}
  .voet-in{grid-template-columns:1fr 1fr}
}
@media (max-width:560px){.voet-in{grid-template-columns:1fr}.kop-in{padding:.6rem 1rem}.merk-sub{display:none}}
"""

BASIS_JS = r"""
(function(){
  // kop schaduw
  var kop=document.getElementById('kop');
  function sc(){kop.classList.toggle('gescrold',window.scrollY>12)}sc();window.addEventListener('scroll',sc,{passive:true});
  // mobiel menu
  var hb=document.querySelector('.hamburger'),mob=document.getElementById('mobiel');
  if(hb){hb.addEventListener('click',function(){var open=hb.getAttribute('aria-expanded')==='true';hb.setAttribute('aria-expanded',String(!open));hb.setAttribute('aria-label',open?'Menu openen':'Menu sluiten');mob.hidden=open;document.body.style.overflow=open?'':'hidden';});}
  // submenu via toetsenbord/klik
  document.querySelectorAll('.heeft-sub>button').forEach(function(b){b.addEventListener('click',function(){var li=b.parentNode,o=li.classList.toggle('open');b.setAttribute('aria-expanded',String(o));});});
  document.addEventListener('click',function(e){if(!e.target.closest('.heeft-sub'))document.querySelectorAll('.heeft-sub.open').forEach(function(l){l.classList.remove('open');l.querySelector('button').setAttribute('aria-expanded','false')})});
  // reveal
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('zichtbaar');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
  var revs=Array.prototype.slice.call(document.querySelectorAll('.reveal'));revs.forEach(function(el){io.observe(el)});
  var tk=false;function fb(){tk=false;var h=innerHeight;revs=revs.filter(function(el){if(el.classList.contains('zichtbaar'))return false;var r=el.getBoundingClientRect();if(r.top<h*0.94&&r.bottom>0){el.classList.add('zichtbaar');return false}return true})}
  addEventListener('scroll',function(){if(!tk){tk=true;requestAnimationFrame(fb)}},{passive:true});setTimeout(fb,600);
  // formulier (mailto-fallback)
  window.verstuur=function(f){var b='Naam: '+f.naam.value+'\nE-mail: '+f.email.value+'\nTelefoon: '+f.telefoon.value+'\n\n'+f.bericht.value;location.href='mailto:'+'__MAIL__'+'?subject='+encodeURIComponent('Kennismaken via de website')+'&body='+encodeURIComponent(b);return false;};
})();
""".replace("__MAIL__", MAIL)

# Vallende bloesemblaadjes (canvas), wordt gestart met startPetals(opties)
PETALS_JS = r"""
window.startPetals=function(o){
  o=o||{};var c=document.createElement('canvas');c.className='petals';document.body.appendChild(c);var x=c.getContext('2d');
  var W,H,P=[],n=o.aantal||18,kleuren=o.kleuren||['#f4c6c6','#efa6a2','#f8d8d0','#d8cde6','#c9d9e8'];
  var actief=o.altijd||false;window.petalsAan=function(v){actief=v};
  function rs(){W=c.width=innerWidth;H=c.height=innerHeight}rs();addEventListener('resize',rs);
  function nieuw(p,top){p.x=Math.random()*W;p.y=top?-20:Math.random()*H;p.r=6+Math.random()*9;p.vy=.4+Math.random()*.9;p.vx=(Math.random()-.5)*.6;p.a=Math.random()*6.28;p.va=(Math.random()-.5)*.03;p.k=kleuren[Math.floor(Math.random()*kleuren.length)];p.sw=Math.random()*6.28;p.op=0;return p}
  for(var i=0;i<n;i++)P.push(nieuw({},false));
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function blad(p){x.save();x.translate(p.x,p.y);x.rotate(p.a);x.globalAlpha=p.op*.85;x.fillStyle=p.k;x.beginPath();x.moveTo(0,-p.r);x.bezierCurveTo(p.r*.9,-p.r*.6,p.r*.9,p.r*.6,0,p.r);x.bezierCurveTo(-p.r*.9,p.r*.6,-p.r*.9,-p.r*.6,0,-p.r);x.fill();x.restore()}
  function tick(){x.clearRect(0,0,W,H);var t=Date.now()/1000;P.forEach(function(p){
    if(actief){p.op=Math.min(1,p.op+.01)}else{p.op=Math.max(0,p.op-.02)}
    if(p.op>0||actief){p.sw+=.02;p.x+=p.vx+Math.sin(t+p.sw)*.5;p.y+=p.vy;p.a+=p.va;if(p.y>H+20||p.x<-30||p.x>W+30)nieuw(p,true);blad(p)}
  });if(!rm)requestAnimationFrame(tick)}
  if(!rm)tick();
};
"""
