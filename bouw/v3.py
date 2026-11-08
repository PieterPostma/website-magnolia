# -*- coding: utf-8 -*-
"""Versie 3 – 'Water': fotografisch, lichtblauw/sage met oudroze, verhalende scroll-sectie waarin de magnolia groeit."""
from common import *
from boom import boom_svg, BOOM_CSS, BOOM_JS

THEMA = dict(
    naam="Water",
    fonts="Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Figtree:wght@300;400;500;600&family=Great+Vibes",
)

CSS = r"""
:root{
  --f-head:'Fraunces',Georgia,serif;--f-body:'Figtree',system-ui,sans-serif;--f-script:'Great Vibes',cursive;--merk-size:1.6rem;--head-w:400;
  --bg:#f9f7f5;--surface:#ffffff;--tint:#eef1f3;--line:#e4e4e2;
  --accent:#b85860;--accent-d:#9a4850;--accent-l:#efa6a2;
  --head:#3a3a40;--ink:#555560;--muted:#7d7f88;
  --blush:#f8d8d0;--lavendel:#d9d0e6;--blauw:#cfdce9;--blauw-d:#9fb4c8;--sage:#adb48f;--sage-d:#8f9872;
  --kop-bg:rgba(249,247,245,.84);
  --pag-hero-bg:linear-gradient(120deg,#e9eef2,#e6e3ee 60%,#f6e4e4);
  --slot-bg:linear-gradient(120deg,#dfe7ee,#e6e0ec 55%,#f8e2df);
  --voet-bg:#e9eef2;--voet-ink:#4a4a52;--voet-kop:#b85860;--voet-muted:#7d7f88;--voet-lijn:#d4dbe2;--voet-tint:#fff;
  --r-foto:6px;--r-knop:8px;
  --boom-stam:#a98a7c;--boom-wortel:#cdb7ad;--boom-bloesem:#f4c3c3;--boom-bloesem2:#fbe3dc;--boom-bloesem-rand:#efa6a2;--boom-hart:#b85860;
}
h1 em,h2 em{font-style:italic;color:var(--accent);font-weight:300}
.pag-foto,.kader,.tarief,.pijler,.contact-kaart,.blog-kaart,.citaat,.slotband{border-radius:8px}
.knop{letter-spacing:.02em}

/* hero: volledig beeld */
.hero{position:relative;min-height:100vh;display:grid;place-items:center;text-align:center;color:#fff;overflow:hidden;isolation:isolate}
.hero-bg{position:absolute;inset:0;z-index:-2}
.hero-bg img{width:100%;height:100%;object-fit:cover;object-position:32% 60%;animation:zoomuit 12s ease-out both}
@keyframes zoomuit{from{transform:scale(1.12)}to{transform:scale(1)}}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(58,58,64,.15),rgba(58,58,64,.35) 60%,rgba(184,88,96,.55))}
.hero-in{max-width:900px;padding:7rem 1.25rem 6rem}
.hero .boventitel{color:#fff;opacity:.9}
.hero h1{color:#fff;font-size:clamp(3rem,8vw,6.4rem);font-weight:300;letter-spacing:-.02em;line-height:1;margin:0 0 .3em}
.hero h1 em{color:#f8d8d0}
.hero-lead{font-size:1.25rem;max-width:36rem;margin:0 auto;color:#fff;opacity:.95}
.hero-knoppen{display:flex;flex-wrap:wrap;justify-content:center;gap:.8rem;margin-top:2.2rem}
.hero .knop{background:#fff;color:var(--accent);border-color:#fff}.hero .knop:hover{background:var(--blush)}
.hero .knop-licht{background:rgba(255,255,255,.12);color:#fff;border-color:rgba(255,255,255,.6);backdrop-filter:blur(6px)}
.hero-in>*{animation:inkomen 1.2s cubic-bezier(.2,.7,.2,1) both}.hero-in>*:nth-child(2){animation-delay:.2s}.hero-in>*:nth-child(3){animation-delay:.4s}.hero-in>*:nth-child(4){animation-delay:.6s}
@keyframes inkomen{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}
.hero-merk{position:absolute;bottom:2rem;left:50%;transform:translateX(-50%);width:60px;opacity:.9;animation:dobber 4s ease-in-out infinite}
@keyframes dobber{0%,100%{transform:translate(-50%,0)}50%{transform:translate(-50%,-10px)}}

/* intro / herken: drie kolommen met rand */
.herken{background:var(--surface)}
.herken-kop{max-width:820px;margin:0 auto 3rem;text-align:center}
.herken-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.herken-grid p{padding:2rem 1.6rem;margin:0;border-left:1px solid var(--line);font-size:1rem}
.herken-grid p:first-child{border-left:0}
.herken-grid p::before{content:"0" counter(herk);counter-increment:herk;display:block;font-family:var(--f-head);color:var(--accent-l);font-size:1.6rem;margin-bottom:.6rem}
.herken-grid{counter-reset:herk}
.herken-slot{text-align:center;font-family:var(--f-head);font-size:clamp(1.6rem,3vw,2.3rem);font-style:italic;font-weight:300;color:var(--head);max-width:800px;margin:3rem auto 0;line-height:1.3}

/* video + stroom */
.video{padding:0 1.25rem}
.video-kaart{max-width:1160px;margin:0 auto;position:relative;border-radius:8px;overflow:hidden;aspect-ratio:21/9;background:#000}
.video-kaart img{width:100%;height:100%;object-fit:cover;opacity:.8}
.afspelen{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1rem;color:#fff;text-decoration:none;background:linear-gradient(to top,rgba(58,58,64,.65),rgba(58,58,64,.1))}
.afspelen b{width:84px;height:84px;border-radius:50%;background:rgba(255,255,255,.92);display:grid;place-items:center;color:var(--accent);animation:puls 2.4s infinite}
@keyframes puls{0%{box-shadow:0 0 0 0 rgba(255,255,255,.55)}100%{box-shadow:0 0 0 28px rgba(255,255,255,0)}}
.afspelen span{font-family:var(--f-head);font-size:1.6rem;font-style:italic}
.afspelen small{opacity:.85;letter-spacing:.14em;text-transform:uppercase;font-size:.72rem}

/* thema's: horizontale rij hoge fotokaarten */
.themas{padding-left:0;padding-right:0;background:linear-gradient(180deg,var(--bg),#e9eef2)}
.themas-kop{max-width:1160px;margin:0 auto 2.5rem;padding:0 1.25rem;display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:end}
.thema-rij{display:flex;gap:1.2rem;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 max(1.25rem,calc((100vw - 1160px)/2)) 1.5rem;scrollbar-width:thin;scrollbar-color:var(--accent-l) transparent}
.thema{flex:0 0 min(78vw,330px);scroll-snap-align:start;position:relative;border-radius:8px;overflow:hidden;aspect-ratio:3/4.2;text-decoration:none;color:#fff;display:flex;align-items:flex-end;isolation:isolate}
.thema img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1;transition:transform 1.2s}
.thema::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(58,58,64,.85),rgba(58,58,64,.1) 60%);z-index:-1}
.thema:hover img{transform:scale(1.06)}
.thema-tekst{padding:1.6rem}.thema h3{color:#fff;font-size:1.5rem;font-weight:400}.thema p{font-size:.92rem;margin:0 0 .6rem;opacity:.9}
.thema .pijl-link{color:#f8d8d0;font-size:.9rem}
.voorwie{max-width:1160px;margin:2.5rem auto 0;padding:0 1.25rem;display:flex;flex-wrap:wrap;gap:.6rem}
.voorwie span{display:inline-flex;align-items:center;gap:.5rem;padding:.6rem 1.1rem;background:#fff;border:1px solid var(--line);border-radius:999px;font-size:.92rem}
.voorwie span::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--accent-l)}

/* verhalende groeisectie */
.groei{position:relative;background:linear-gradient(180deg,#e9eef2 0%,#ebe6ee 50%,#f8e6e3 100%)}
.groei-sticky{position:sticky;top:0;height:100vh;display:grid;grid-template-columns:1fr 1fr;align-items:center;max-width:1160px;margin:0 auto;padding:0 1.25rem;overflow:hidden}
.groei-sticky .boom{height:min(80vh,620px);width:auto;max-width:100%;justify-self:center}
.groei-stappen{position:relative;height:70vh}
.stap{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;opacity:0;transform:translateY(30px);transition:opacity .6s,transform .6s;pointer-events:none}
.stap.aan{opacity:1;transform:none;pointer-events:auto}
.stap .pijler-nr{font-family:var(--f-head);font-size:3rem;color:var(--accent-l);line-height:1}
.stap h3{font-size:clamp(1.6rem,3vw,2.3rem);font-weight:400}
.stap p{font-size:1.1rem;max-width:32rem}
.groei-ruimte{height:calc(100vh * 7)}
.groei-voortgang{position:absolute;left:1.25rem;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:.6rem;z-index:2}
.groei-voortgang i{width:8px;height:8px;border-radius:50%;background:var(--line);display:block;transition:background .3s,transform .3s}
.groei-voortgang i.aan{background:var(--accent);transform:scale(1.4)}

/* aanbod */
.aanbod-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}
.aanbod{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:2.2rem;position:relative;transition:transform .35s,border-color .35s}
.aanbod:hover{transform:translateY(-6px);border-color:var(--accent-l)}
.aanbod h3{font-size:1.6rem;font-weight:400}
.aanbod .nr{font-family:var(--f-head);color:var(--accent-l);font-size:1.4rem}

/* over mij parallax */
.voorstellen{position:relative;overflow:hidden;color:#fff;isolation:isolate;padding:clamp(5rem,12vw,10rem) 1.25rem}
.voorstellen-bg{position:absolute;inset:-20% 0;z-index:-2}
.voorstellen-bg img{width:100%;height:100%;object-fit:cover;object-position:50% 40%}
.voorstellen::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(58,58,64,.8),rgba(58,58,64,.35))}
.voorstellen-in{max-width:1160px;margin:0 auto}
.voorstellen-tekst{max-width:560px;background:rgba(255,255,255,.1);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.25);border-radius:8px;padding:2.4rem}
.voorstellen h2,.voorstellen .boventitel{color:#fff}.voorstellen h2 em{color:#f8d8d0}
.voorstellen .pijl-link{color:#f8d8d0}
.handtekening{font-family:var(--f-script);font-size:2.6rem;color:#f8d8d0;line-height:1;margin:1.2rem 0 .2rem}

.slot-home{text-align:center}
.slot-home .handtekening{color:var(--accent)}

@media (max-width:1000px){.herken-grid{grid-template-columns:1fr 1fr}.herken-grid p:nth-child(3){border-left:0}.aanbod-grid{grid-template-columns:1fr}.themas-kop{grid-template-columns:1fr}}
@media (max-width:860px){
  .groei-sticky{grid-template-columns:1fr;grid-template-rows:45vh 1fr;align-items:start;padding-top:1rem}.groei-sticky .boom{height:42vh}.groei-stappen{height:50vh}.stap p{font-size:1rem}.groei-voortgang{display:none}
  .hero{min-height:88vh}
}
@media (max-width:560px){.herken-grid{grid-template-columns:1fr}.herken-grid p{border-left:0;padding:1.4rem 0}}
""" + BOOM_CSS

JS = BASIS_JS + PETALS_JS + BOOM_JS + r"""
(function(){
  startPetals({aantal:26,kleuren:['#f4c6c6','#f8d8d0','#efa6a2','#d9d0e6','#cfdce9']});
  var sec=document.getElementById('groei'),svg=document.getElementById('boom'),stappen=document.querySelectorAll('.stap'),dots=document.querySelectorAll('.groei-voortgang i');
  var klaar=false;
  function upd(){if(!sec)return;var r=sec.getBoundingClientRect();var tot=r.height-innerHeight;var p=Math.max(0,Math.min(1,-r.top/tot));
    var k=groeiBoom(svg,p);if(k!==klaar){klaar=k;petalsAan(k)}
    var n=stappen.length,i=Math.min(n-1,Math.floor(p*n));stappen.forEach(function(s,j){s.classList.toggle('aan',j===i)});dots.forEach(function(d,j){d.classList.toggle('aan',j===i)})}
  upd();addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);
  // parallax over mij
  var pb=document.querySelector('.voorstellen-bg img');if(pb&&!matchMedia('(prefers-reduced-motion: reduce)').matches){addEventListener('scroll',function(){var r=pb.parentNode.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;var p=(r.top+r.height/2-innerHeight/2)/innerHeight;pb.style.transform='translateY('+(p*-60)+'px)'},{passive:true})}
})();
"""


def home():
    themas = "".join(f"""<a class="thema reveal vertraag-{i+1}" href="{t['slug']}.html"><img src="{A}foto/{t['foto']}" alt="" loading="lazy"><div class="thema-tekst"><h3>{esc(t['kop'])}</h3><p>{esc(t['kort'])}</p><span class="pijl-link">Lees meer <span aria-hidden="true">→</span></span></div></a>""" for i, t in enumerate(THEMAS))
    voorwie = "".join(f'<span class="reveal vertraag-{(i%3)+1}"><strong>{esc(k)}</strong>&nbsp;· {esc(v)}</span>' for i, (k, v) in enumerate(HOME["voorwie"]))
    stappen = f"""<div class="stap aan"><p class="boventitel">Mijn werkwijze</p><h3>Opnieuw leren <em>voelen</em> en vertrouwen</h3>{"".join(f'<p>{esc(x)}</p>' for x in HOME['werkwijze'])}</div>"""
    stappen += "".join(f"""<div class="stap"><span class="pijler-nr">0{i+1}</span><h3>{esc(p['kop'])}</h3><p>{esc(p['kort'])}</p><a class="pijl-link" href="werkwijze/{p['slug']}.html">Lees meer <span aria-hidden="true">→</span></a></div>""" for i, p in enumerate(PIJLERS))
    stappen += f"""<div class="stap"><p class="boventitel">Samen</p><h3>Wat gevoeld mag worden, kan weer gaan <em>stromen</em></h3>{"".join(f'<p>{esc(x)}</p>' for x in HOME['werkwijze_slot'])}<p><a class="knop" href="werkwijze.html">Meer over mijn werkwijze</a></p></div>"""
    dots = "<i></i>" * 7
    aanbod = "".join(f"""<article class="aanbod reveal vertraag-{i+1}"><span class="nr">0{i+1}</span><h3>{esc(k)}</h3><p>{esc(t)}</p><a class="pijl-link" href="{h}">{esc(l)} <span aria-hidden="true">→</span></a></article>""" for i, (k, t, h, l) in enumerate(HOME["aanbod"]))
    herken = "".join(f"<p class='reveal vertraag-{i+1}'>{esc(x)}</p>" for i, x in enumerate(HOME["herken"]))
    return head(HOME["seo_titel"], HOME["seo"], THEMA) + f"""<body class="home v3">
{nav('index.html')}
<main id="inhoud">
<section class="hero">
  <div class="hero-bg"><img src="{A}foto/water-zit-breed.jpg" alt="" fetchpriority="high"></div>
  <div class="hero-in">
    <p class="boventitel">{esc(NAAM)} · {esc(TITEL)}</p>
    <h1>Leer te voelen.<br><em>Durf te vertrouwen.</em></h1>
    <p class="hero-lead">{esc(HOME['doelgroep'])}</p>
    <div class="hero-knoppen"><a class="knop" href="contact.html">Plan een kennismaking</a><a class="knop knop-licht" href="#helpen">Waarmee kan ik je helpen?</a></div>
  </div>
  <img class="hero-merk" src="{A}beeldmerk.png" alt="" loading="lazy">
</section>

<section class="sectie herken">
  <div class="binnen">
    <div class="herken-kop reveal"><p class="boventitel">Misschien herken je dit…</p><h2>Aan de buitenkant gaat het <em>best goed</em></h2></div>
    <div class="herken-grid">{herken}</div>
    <p class="herken-slot reveal">{esc(HOME['herken_slot'])}<br><span style="color:var(--accent)">{esc(STROOM)}</span></p>
  </div>
</section>

<section class="video reveal">
  <div class="video-kaart"><img src="{A}foto/strand-wandel.jpg" alt="" loading="lazy"><a class="afspelen" href="over-mij.html" aria-label="Persoonlijk verhaal van Liesbeth (video volgt)"><b><svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></b><span>Mijn persoonlijke verhaal</span><small>Video volgt binnenkort</small></a></div>
</section>

<section class="sectie themas" id="helpen">
  <div class="themas-kop"><div class="reveal"><p class="boventitel">Waarmee kan ik je helpen?</p><h2>Voor (jong)volwassenen die <em>vastlopen</em> of hun weg zoeken</h2></div><p class="reveal vertraag-1">{esc(HOME['voorwie_intro'])}</p></div>
  <div class="thema-rij">{themas}</div>
  <div class="voorwie">{voorwie}</div>
</section>

<section class="groei" id="groei">
  <div class="groei-voortgang" aria-hidden="true">{dots}</div>
  <div class="groei-sticky">
    {boom_svg()}
    <div class="groei-stappen">{stappen}</div>
  </div>
  <div class="groei-ruimte" aria-hidden="true"></div>
</section>

<section class="sectie">
  <div class="binnen">
    <div class="reveal" style="max-width:640px;margin-bottom:2.5rem"><p class="boventitel">Mijn aanbod</p><h2>Individueel, in een <em>opstelling</em> of in een workshop</h2></div>
    <div class="aanbod-grid">{aanbod}</div>
  </div>
</section>

<section class="voorstellen">
  <div class="voorstellen-bg"><img src="{A}foto/boom-zit-breed.jpg" alt="" loading="lazy"></div>
  <div class="voorstellen-in">
    <div class="voorstellen-tekst reveal">
      <p class="boventitel">Even voorstellen</p>
      <h2>Professionele kennis en <em>doorleefde ervaring</em></h2>
      {"".join(f'<p>{esc(x)}</p>' for x in HOME['voorstellen'][:3])}
      <p>{esc(HOME['voorstellen'][5])}</p>
      <p class="handtekening">Liesbeth</p>
      <a class="pijl-link" href="over-mij.html">Lees meer over mij <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="sectie slot-home">
  <div class="smal reveal">
    <img src="{A}beeldmerk.png" alt="" width="110" style="margin:0 auto 1.5rem" loading="lazy">
    <h2>Leer te voelen – <em>durf te vertrouwen</em></h2>
    {"".join(f'<p>{esc(x)}</p>' for x in HOME['slot'])}
    <p class="handtekening">Lieve groet, Liesbeth</p>
    <p><a class="knop" href="contact.html">Neem contact op</a></p>
  </div>
</section>
</main>
{footer()}
{scripts()}
</body></html>"""
