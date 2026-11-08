# -*- coding: utf-8 -*-
"""Versie 1 – 'Bloesem': licht, luchtig, blush → lavendel; magnolia groeit mee naast de pijlers."""
from common import *
from boom import boom_svg, BOOM_CSS, BOOM_JS

THEMA = dict(
    naam="Bloesem",
    fonts="Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500;600&family=Great+Vibes",
)

CSS = r"""
:root{
  --f-head:'Cormorant Garamond',Georgia,serif;--f-body:'Jost',system-ui,sans-serif;--f-script:'Great Vibes',cursive;--merk-size:1.7rem;
  --bg:#fdf8f6;--surface:#ffffff;--tint:#fbeae5;--line:#f0dcd8;
  --accent:#b85860;--accent-d:#9a4850;--accent-l:#efa6a2;
  --head:#4a343a;--ink:#574449;--muted:#8a7378;
  --blush:#f8d8d0;--lavendel:#d9d0e6;--blauw:#cfdce9;--sage:#adb48f;
  --kop-bg:rgba(253,248,246,.82);
  --pag-hero-bg:linear-gradient(135deg,#fbeae5 0%,#f3e4ea 50%,#e4e2ef 100%);
  --slot-bg:linear-gradient(135deg,#fbeae5,#e6e0ee 60%,#dbe3ee);
  --voet-bg:#f4e4e3;--voet-ink:#574449;--voet-kop:#b85860;--voet-muted:#8a7378;--voet-lijn:#e9d2d0;--voet-tint:#fff;
  --r-foto:32px;
  --boom-stam:#b08878;--boom-wortel:#d9bfb5;--boom-bloesem:#f4c3c3;--boom-bloesem2:#fbe3dc;--boom-bloesem-rand:#efa6a2;--boom-hart:#b85860;
}
h1 em,h2 em{font-style:italic;color:var(--accent);font-weight:400}

/* hero */
.hero{position:relative;overflow:hidden;background:linear-gradient(160deg,#fdf3f0 0%,#f6e6ec 45%,#e6e3f1 80%,#dde5ef 100%)}
.hero::before,.hero::after{content:"";position:absolute;border-radius:50%;filter:blur(60px);opacity:.7;pointer-events:none}
.hero::before{width:520px;height:520px;background:#f8d8d0;top:-160px;left:-120px;animation:zweef 14s ease-in-out infinite}
.hero::after{width:460px;height:460px;background:#d9d0e6;bottom:-200px;right:5%;animation:zweef 18s ease-in-out infinite reverse}
@keyframes zweef{0%,100%{transform:translate(0,0)}50%{transform:translate(30px,40px)}}
.hero-in{position:relative;max-width:1160px;margin:0 auto;padding:clamp(3rem,7vw,6rem) 1.25rem clamp(3rem,6vw,5rem);display:grid;grid-template-columns:1.05fr .95fr;gap:3rem;align-items:center;min-height:calc(100vh - 70px)}
.hero h1{margin:.3em 0 .5em}
.hero-lead{font-size:1.25rem;max-width:34rem;color:var(--ink)}
.hero-knoppen{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:2rem}
.hero-beeld{position:relative;justify-self:center;width:min(100%,460px)}
.hero-beeld img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:230px 230px 36px 36px;box-shadow:0 40px 80px -40px rgba(120,60,70,.5);animation:inkomen 1.4s cubic-bezier(.2,.7,.2,1) both}
.hero-beeld::before{content:"";position:absolute;inset:-14px -14px auto auto;width:70%;height:60%;border:1.5px solid var(--accent-l);border-radius:230px 230px 0 0;opacity:.6;z-index:-1;animation:inkomen 1.6s .2s cubic-bezier(.2,.7,.2,1) both}
.hero-kaartje{position:absolute;left:-1.5rem;bottom:2.5rem;background:rgba(255,255,255,.9);backdrop-filter:blur(10px);border-radius:20px;padding:.9rem 1.2rem;box-shadow:0 20px 40px -24px rgba(120,60,70,.5);font-family:var(--f-head);font-size:1.25rem;font-style:italic;color:var(--head);animation:inkomen 1.6s .5s cubic-bezier(.2,.7,.2,1) both;max-width:250px;line-height:1.3}
@keyframes inkomen{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}
.hero-tekst>*{animation:inkomen 1s cubic-bezier(.2,.7,.2,1) both}
.hero-tekst>*:nth-child(2){animation-delay:.12s}.hero-tekst>*:nth-child(3){animation-delay:.24s}.hero-tekst>*:nth-child(4){animation-delay:.36s}
.scroll-hint{position:absolute;left:50%;bottom:1.2rem;transform:translateX(-50%);font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);display:flex;flex-direction:column;align-items:center;gap:.4rem}
.scroll-hint i{width:1px;height:38px;background:var(--accent-l);display:block;animation:lijn 2s ease-in-out infinite;transform-origin:top}
@keyframes lijn{0%{transform:scaleY(0)}50%{transform:scaleY(1)}100%{transform:scaleY(0);transform-origin:bottom}}

/* herken */
.herken{background:var(--surface)}
.herken-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:.9fr 1.1fr;gap:4rem;align-items:start}
.herken h2{position:sticky;top:110px}
.herken-tekst p{font-size:1.12rem}
.herken-slot{font-family:var(--f-head);font-size:1.6rem;font-style:italic;color:var(--accent);line-height:1.3;margin-top:1.5em}
.stroom{text-align:center;max-width:900px;margin:0 auto;padding:clamp(3rem,6vw,5rem) 1.25rem 0}
.stroom p{font-family:var(--f-head);font-size:clamp(1.8rem,3.6vw,2.8rem);font-style:italic;color:var(--head);line-height:1.25}
.stroom p span{display:inline-block;opacity:0;transform:translateY(12px);transition:opacity .8s,transform .8s}
.stroom.zichtbaar p span{opacity:1;transform:none}

/* video */
.video{padding:clamp(3rem,6vw,5rem) 1.25rem 0}
.video-kaart{max-width:900px;margin:0 auto;position:relative;border-radius:32px;overflow:hidden;aspect-ratio:16/8;background:#000}
.video-kaart img{width:100%;height:100%;object-fit:cover;opacity:.85}
.video-kaart .afspelen{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1rem;color:#fff;text-decoration:none;background:linear-gradient(to top,rgba(74,52,58,.6),rgba(74,52,58,.1))}
.afspelen b{width:84px;height:84px;border-radius:50%;background:rgba(255,255,255,.92);display:grid;place-items:center;color:var(--accent);box-shadow:0 0 0 0 rgba(255,255,255,.6);animation:puls 2.4s infinite}
@keyframes puls{0%{box-shadow:0 0 0 0 rgba(255,255,255,.55)}100%{box-shadow:0 0 0 28px rgba(255,255,255,0)}}
.afspelen span{font-family:var(--f-head);font-size:1.5rem;font-style:italic;text-shadow:0 2px 12px rgba(0,0,0,.3)}
.afspelen small{opacity:.85;letter-spacing:.14em;text-transform:uppercase;font-size:.72rem}

/* thema's */
.themas-kop{text-align:center;max-width:720px;margin:0 auto 3rem}
.thema-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem}
.thema{position:relative;border-radius:28px;overflow:hidden;aspect-ratio:3/4;text-decoration:none;color:#fff;display:flex;align-items:flex-end;isolation:isolate}
.thema img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.7,.2,1);z-index:-1}
.thema::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(74,52,58,.85) 0%,rgba(74,52,58,.25) 55%,transparent 100%);z-index:-1;transition:opacity .4s}
.thema:hover img{transform:scale(1.06)}
.thema-tekst{padding:1.6rem}
.thema h3{color:#fff;font-size:1.5rem;margin-bottom:.4rem}
.thema p{font-size:.92rem;margin:0;opacity:0;max-height:0;transition:opacity .4s,max-height .5s;overflow:hidden}
.thema:hover p,.thema:focus p{opacity:.95;max-height:120px}
.thema .pijl-link{color:#fff;margin-top:.6rem;font-size:.9rem}
.voorwie{margin-top:3.5rem;display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.voorwie div{background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:1.2rem 1.4rem;font-size:.95rem}
.voorwie strong{display:block;font-family:var(--f-head);font-size:1.25rem;color:var(--head);margin-bottom:.2rem}

/* werkwijze + boom */
.groei{background:linear-gradient(180deg,var(--bg) 0%,#f6ecf0 50%,#e9e4f1 100%);position:relative}
.groei-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:.8fr 1.2fr;gap:4rem;align-items:start}
.groei-boom{position:sticky;top:90px;height:calc(100vh - 110px);display:flex;align-items:center;justify-content:center}
.groei-boom .boom{max-height:100%;width:auto;max-width:100%}
.groei-tekst p.intro{font-size:1.15rem}
.pijler-lijst{display:grid;gap:1.2rem;margin:2.5rem 0}
.pijler-lijst .pijler{display:grid;grid-template-columns:auto 1fr;gap:1.2rem;align-items:start;background:rgba(255,255,255,.75);backdrop-filter:blur(6px)}
.pijler-lijst .pijler-nr{font-size:2.6rem;color:var(--accent-l);line-height:1;padding-top:.2rem}
.groei-slot{font-family:var(--f-head);font-size:1.35rem;font-style:italic;color:var(--head)}

/* aanbod */
.aanbod-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
.aanbod{background:var(--surface);border:1px solid var(--line);border-radius:28px;padding:2rem;position:relative;overflow:hidden;transition:transform .35s,box-shadow .35s}
.aanbod::before{content:"";position:absolute;width:160px;height:160px;border-radius:50%;background:var(--tint);right:-60px;top:-60px;transition:transform .5s}
.aanbod:hover{transform:translateY(-6px);box-shadow:0 30px 60px -35px rgba(120,60,70,.45)}.aanbod:hover::before{transform:scale(1.5)}
.aanbod>*{position:relative}
.aanbod h3{font-size:1.6rem}

/* voorstellen */
.voorstellen{background:var(--surface)}
.voorstellen-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:1fr 1.1fr;gap:4rem;align-items:center}
.voorstellen-foto{position:relative}
.voorstellen-foto img{border-radius:36px 200px 36px 36px;aspect-ratio:4/5;object-fit:cover;box-shadow:0 40px 80px -40px rgba(120,60,70,.5)}
.voorstellen-foto::after{content:"";position:absolute;inset:auto auto -24px -24px;width:140px;height:140px;border-radius:50%;background:var(--lavendel);z-index:-1}
.handtekening{font-family:var(--f-script);font-size:2.6rem;color:var(--accent);line-height:1;margin:1.2rem 0 .2rem}

/* slot */
.slot-home{text-align:center;position:relative;overflow:hidden;background:linear-gradient(160deg,#fbeae5,#ece4ef 50%,#dbe3ee)}
.slot-home .binnen{max-width:760px}
.slot-home p{font-size:1.15rem}
.slot-home h2{font-size:clamp(2.2rem,4.5vw,3.4rem)}

@media (max-width:1000px){.thema-grid{grid-template-columns:repeat(2,1fr)}.aanbod-grid{grid-template-columns:1fr}.voorwie{grid-template-columns:1fr 1fr}}
@media (max-width:860px){
  .hero-in{grid-template-columns:1fr;min-height:0;padding-top:2.5rem}.hero-beeld{width:min(100%,360px)}.hero-kaartje{left:0}
  .herken-in,.voorstellen-in{grid-template-columns:1fr;gap:2rem}.herken h2{position:static}
  .groei-in{grid-template-columns:1fr}.groei-boom{position:relative;top:0;height:auto}.groei-boom .boom{max-width:320px}
  .scroll-hint{display:none}
}
@media (max-width:560px){.thema-grid{grid-template-columns:1fr}.voorwie{grid-template-columns:1fr}.thema{aspect-ratio:4/3}.thema p{opacity:.95;max-height:none}}
""" + BOOM_CSS

JS = BASIS_JS + PETALS_JS + BOOM_JS + r"""
(function(){
  // stroom-zin woord voor woord
  var st=document.querySelector('.stroom');if(st){var p=st.querySelector('p');p.innerHTML=p.textContent.split(' ').map(function(w,i){return '<span style="transition-delay:'+(i*.09)+'s">'+w+'</span>'}).join(' ');}
  // boom groeit met scrollen door de werkwijze-sectie
  var sec=document.getElementById('groei'),svg=document.getElementById('boom');
  if(sec&&svg){startPetals({aantal:22});var klaar=false;
    function upd(){var r=sec.getBoundingClientRect();var h=r.height-innerHeight;var p=Math.max(0,Math.min(1,(-r.top+innerHeight*0.25)/(h+innerHeight*0.25)));var k=groeiBoom(svg,p);if(k!==klaar){klaar=k;petalsAan(k)}}
    upd();addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);}
})();
"""


def home():
    themas = "".join(f"""<a class="thema reveal vertraag-{i+1}" href="{t['slug']}.html"><img src="{A}foto/{t['foto']}" alt="" loading="lazy"><div class="thema-tekst"><h3>{esc(t['kop'])}</h3><p>{esc(t['kort'])}</p><span class="pijl-link">Lees meer <span aria-hidden="true">→</span></span></div></a>""" for i, t in enumerate(THEMAS))
    voorwie = "".join(f'<div class="reveal vertraag-{(i%3)+1}"><strong>{esc(k)}</strong>{esc(v)}</div>' for i, (k, v) in enumerate(HOME["voorwie"]))
    pijlers = "".join(f"""<article class="pijler reveal"><span class="pijler-nr">0{i+1}</span><div><h3>{esc(p['kop'])}</h3><p>{esc(p['kort'])}</p><a class="pijl-link" href="werkwijze/{p['slug']}.html">Lees meer over {esc(p['kop'].split(' – ')[0].lower())} <span aria-hidden="true">→</span></a></div></article>""" for i, p in enumerate(PIJLERS))
    aanbod = "".join(f"""<article class="aanbod reveal vertraag-{i+1}"><h3>{esc(k)}</h3><p>{esc(t)}</p><a class="pijl-link" href="{h}">{esc(l)} <span aria-hidden="true">→</span></a></article>""" for i, (k, t, h, l) in enumerate(HOME["aanbod"]))
    herken = "".join(f"<p>{esc(x)}</p>" for x in HOME["herken"])
    voorst = "".join(f"<p>{esc(x)}</p>" for x in HOME["voorstellen"][:4])
    slot = "".join(f"<p>{esc(x)}</p>" for x in HOME["slot"])
    return head(HOME["seo_titel"], HOME["seo"], THEMA) + f"""<body class="home v1">
{nav('index.html')}
<main id="inhoud">
<section class="hero">
  <div class="hero-in">
    <div class="hero-tekst">
      <p class="boventitel">{esc(TITEL)}</p>
      <h1>Leer te voelen.<br><em>Durf te vertrouwen.</em></h1>
      <p class="hero-lead">{esc(HOME['doelgroep'])}</p>
      <div class="hero-knoppen"><a class="knop" href="contact.html">Plan een kennismaking</a><a class="knop knop-licht" href="#helpen">Waarmee kan ik je helpen?</a></div>
    </div>
    <div class="hero-beeld">
      <img src="{A}foto/portret-lach.jpg" alt="Liesbeth Postma, psychosociaal en lichaamsgericht therapeut" fetchpriority="high">
      <div class="hero-kaartje">“{esc(STROOM)}”</div>
    </div>
  </div>
  <div class="scroll-hint">Scroll <i></i></div>
</section>

<section class="sectie herken">
  <div class="herken-in">
    <div class="reveal"><p class="boventitel">Misschien herken je dit…</p><h2>Aan de buitenkant gaat het <em>best goed</em></h2></div>
    <div class="herken-tekst reveal vertraag-1">{herken}<p class="herken-slot">{esc(HOME['herken_slot'])}</p></div>
  </div>
  <div class="stroom reveal"><p>{esc(STROOM)}</p></div>
  <div class="video reveal">
    <div class="video-kaart"><img src="{A}foto/boom-close.jpg" alt="" loading="lazy"><a class="afspelen" href="over-mij.html" aria-label="Persoonlijk verhaal van Liesbeth (video volgt)"><b><svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></b><span>Mijn persoonlijke verhaal</span><small>Video volgt binnenkort</small></a></div>
  </div>
</section>

<section class="sectie" id="helpen">
  <div class="binnen">
    <div class="themas-kop reveal"><p class="boventitel">Waarmee kan ik je helpen?</p><h2>Voor (jong)volwassenen die <em>vastlopen</em> of hun weg zoeken</h2><p>{esc(HOME['voorwie_intro'])}</p></div>
    <div class="thema-grid">{themas}</div>
    <div class="voorwie">{voorwie}</div>
  </div>
</section>

<section class="sectie groei" id="groei">
  <div class="groei-in">
    <div class="groei-boom">{boom_svg()}</div>
    <div class="groei-tekst">
      <p class="boventitel reveal">Mijn werkwijze</p>
      <h2 class="reveal">Opnieuw leren <em>voelen</em> en vertrouwen</h2>
      {"".join(f'<p class="intro reveal">{esc(x)}</p>' for x in HOME['werkwijze'])}
      <h3 class="reveal" style="margin-top:2rem">Mijn vijf pijlers</h3>
      <div class="pijler-lijst">{pijlers}</div>
      {"".join(f'<p class="groei-slot reveal">{esc(x)}</p>' for x in HOME['werkwijze_slot'])}
      <p class="reveal"><a class="knop" href="werkwijze.html">Meer over mijn werkwijze</a></p>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="binnen">
    <div class="themas-kop reveal"><p class="boventitel">Mijn aanbod</p><h2>Individueel, in een <em>opstelling</em> of in een workshop</h2></div>
    <div class="aanbod-grid">{aanbod}</div>
  </div>
</section>

<section class="sectie voorstellen">
  <div class="voorstellen-in">
    <div class="voorstellen-foto reveal"><img src="{A}foto/portret-deur.jpg" alt="Liesbeth Postma" loading="lazy"></div>
    <div class="reveal vertraag-1">
      <p class="boventitel">Even voorstellen</p>
      <h2>Professionele kennis en <em>doorleefde ervaring</em></h2>
      {voorst}
      <p>{esc(HOME['voorstellen'][5])}</p>
      <p class="handtekening">Liesbeth</p>
      <a class="pijl-link" href="over-mij.html">Lees meer over mij <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="sectie slot-home">
  <div class="binnen reveal">
    <img src="{A}beeldmerk.png" alt="" width="110" style="margin:0 auto 1.5rem" loading="lazy">
    <h2>Leer te voelen – <em>durf te vertrouwen</em></h2>
    {slot}
    <p class="handtekening">Lieve groet, Liesbeth</p>
    <p><a class="knop" href="contact.html">Neem contact op</a></p>
  </div>
</section>
</main>
{footer()}
{scripts()}
</body></html>"""
