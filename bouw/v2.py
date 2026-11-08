# -*- coding: utf-8 -*-
"""Versie 2 – 'Verloop': groot logo gecentreerd, zacht verloop oudroze → lavendel → lichtblauw, overgang naar natuur."""
from common import *
from boom import boom_svg, BOOM_CSS, BOOM_JS

THEMA = dict(
    naam="Verloop",
    kop="midden",
    fonts="Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Nunito+Sans:ital,opsz,wght@0,12..12,300..700;1,12..12,300..700&family=Great+Vibes",
)

CSS = r"""
:root{
  --f-head:'Playfair Display',Georgia,serif;--f-body:'Nunito Sans',system-ui,sans-serif;--f-script:'Great Vibes',cursive;--merk-size:1.6rem;--head-w:500;
  --bg:#fbf7f8;--surface:#ffffff;--tint:#f6e9ec;--line:#ecdde0;
  --accent:#b85860;--accent-d:#9a4850;--accent-l:#efa6a2;
  --head:#3f2b33;--ink:#524047;--muted:#866f77;
  --mauve:#6b4652;--blush:#f8d8d0;--lavendel:#d9d0e6;--blauw:#cfdce9;--sage:#adb48f;--sage-l:#e4e8d8;
  --kop-bg:rgba(251,247,248,.9);--logo-h:118px;--mobiel-top:90px;
  --pag-hero-bg:linear-gradient(120deg,#f6e9ec,#e8e2ef 55%,#dde5ee);
  --slot-bg:linear-gradient(120deg,#6b4652,#7d5564 60%,#6f5a78);
  --voet-bg:#3f2b33;--voet-ink:#eadfe2;--voet-kop:#efa6a2;--voet-muted:#b59ca4;--voet-lijn:#5a434c;--voet-tint:rgba(255,255,255,.08);
  --r-foto:28px;--r-knop:999px;
  --boom-stam:#b08878;--boom-wortel:#d9bfb5;--boom-bloesem:#f4c3c3;--boom-bloesem2:#fbe3dc;--boom-bloesem-rand:#efa6a2;--boom-hart:#b85860;
}
h1 em,h2 em{font-style:italic;color:var(--accent);font-weight:400}

/* hero: tekst op verloop, natuur rechts, klein portret dat erover valt */
.hero{position:relative;display:grid;grid-template-columns:1.05fr .95fr;min-height:calc(100vh - 190px);background:radial-gradient(900px 600px at 20% 20%,#8b5a66 0%,#6b4652 50%,#5a3c47 100%);color:#fff;overflow:hidden}
.hero-tekst{padding:clamp(3rem,7vw,6rem) clamp(1.25rem,5vw,5rem) clamp(3rem,6vw,5rem) max(1.25rem,calc((100vw - 1200px)/2 + 1.25rem));display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}
.hero .boventitel{display:flex;align-items:center;gap:.8rem;color:var(--blush)}.hero .boventitel::before{content:"";width:34px;height:1px;background:var(--blush)}
.hero h1{font-size:clamp(2.8rem,6vw,5rem);font-weight:400;margin:.2em 0 .4em;color:#fff}.hero h1 em{color:var(--blush)}
.hero-lead{font-size:1.2rem;max-width:30rem;color:#eadfe2}
.hero .knop{background:var(--blush);color:#573a44;border-color:var(--blush)}.hero .knop:hover{background:#fff}
.hero .knop-licht{background:transparent;color:#fff;border-color:rgba(255,255,255,.5)}.hero .knop-licht:hover{background:rgba(255,255,255,.12);color:#fff}
.hero-knoppen{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:2rem}
.hero-natuur{position:relative;min-height:520px}
.hero-natuur>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:55% 50%;animation:zoomuit 14s ease-out both}
@keyframes zoomuit{from{transform:scale(1.08)}to{transform:scale(1)}}
.hero-natuur::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#6b4652 0%,rgba(107,70,82,.6) 22%,rgba(107,70,82,.15) 60%,rgba(107,70,82,.25) 100%);z-index:1}
.hero-portret{position:absolute;left:-12%;bottom:5%;width:min(62%,440px);aspect-ratio:2/3;border-radius:46% 54% 48% 52% / 58% 44% 56% 42%;overflow:hidden;box-shadow:0 40px 80px -36px rgba(0,0,0,.6);z-index:3;animation:inkomen 1.4s .3s cubic-bezier(.2,.7,.2,1) both;border:6px solid rgba(248,216,208,.8)}
.hero-portret img{width:100%;height:100%;object-fit:cover;object-position:50% 0}
.hero-boom{position:absolute;right:3%;bottom:-2%;height:72%;opacity:.8;z-index:2;pointer-events:none}
.hero-boom .boom{height:100%;width:auto}.hero-boom .tak{stroke:#fff}.hero-boom .wortel{stroke:rgba(255,255,255,.7)}
.hero-tekst>*{animation:inkomen 1s cubic-bezier(.2,.7,.2,1) both}
.hero-tekst>*:nth-child(2){animation-delay:.15s}.hero-tekst>*:nth-child(3){animation-delay:.3s}.hero-tekst>*:nth-child(4){animation-delay:.45s}
@keyframes inkomen{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}

/* strook met kernwoorden */
.strook{overflow:hidden;background:linear-gradient(90deg,#f8d8d0,#e6dcea,#cfdce9);padding:1rem 0;white-space:nowrap}
.strook-in{display:inline-flex;gap:3rem;animation:schuif 40s linear infinite;font-family:var(--f-head);font-style:italic;font-size:1.3rem;color:var(--mauve)}
.strook-in span::before{content:"✿";color:var(--accent);margin-right:3rem;font-style:normal;font-size:.9rem;vertical-align:middle}
@keyframes schuif{to{transform:translateX(-50%)}}
.strook:hover .strook-in{animation-play-state:paused}

/* herken */
.herken-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:.85fr 1.15fr;gap:4rem;align-items:center}
.herken-tekst p{font-size:1.1rem}
.herken-slot{font-family:var(--f-head);font-size:1.5rem;font-style:italic;color:var(--accent);line-height:1.3}
.herken-foto{position:relative}
.herken-foto img{border-radius:28px;aspect-ratio:4/5;object-fit:cover;object-position:50% 20%}
.quote-kaart{position:absolute;right:-1.5rem;bottom:2rem;background:var(--mauve);color:#fff;padding:1.4rem 1.6rem;border-radius:22px;max-width:300px;font-family:var(--f-head);font-style:italic;font-size:1.2rem;line-height:1.35;box-shadow:0 30px 60px -30px rgba(0,0,0,.4)}

/* video */
.video{padding:0 1.25rem}
.video-kaart{max-width:1160px;margin:0 auto;position:relative;border-radius:32px;overflow:hidden;aspect-ratio:21/9;background:#000}
.video-kaart img{width:100%;height:100%;object-fit:cover;opacity:.85}
.afspelen{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1rem;color:#fff;text-decoration:none;background:linear-gradient(to top,rgba(63,43,51,.6),rgba(63,43,51,.05))}
.afspelen b{width:84px;height:84px;border-radius:50%;background:rgba(255,255,255,.92);display:grid;place-items:center;color:var(--accent);animation:puls 2.4s infinite}
@keyframes puls{0%{box-shadow:0 0 0 0 rgba(255,255,255,.55)}100%{box-shadow:0 0 0 28px rgba(255,255,255,0)}}
.afspelen span{font-family:var(--f-head);font-size:1.6rem;font-style:italic}
.afspelen small{opacity:.85;letter-spacing:.14em;text-transform:uppercase;font-size:.72rem}

/* thema's: genummerde lijst met meebewegende natuurfoto */
.themas{background:linear-gradient(180deg,var(--bg),#f1e8ef 60%,#e6e6f0)}
.themas-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start}
.themas-foto{position:sticky;top:120px;border-radius:28px;overflow:hidden;aspect-ratio:4/5}
.themas-foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .7s;transform:scale(1.04)}
.themas-foto img.aan{opacity:1;transform:none;transition:opacity .7s,transform 6s linear}
.thema-item{display:block;padding:1.6rem 0;border-top:1px solid var(--line);text-decoration:none;color:var(--head);transition:padding-left .35s}
.thema-item:hover,.thema-item.aan{padding-left:.8rem}
.thema-item:last-child{border-bottom:1px solid var(--line)}
.thema-item .nr{font-family:var(--f-head);color:var(--accent);font-size:.95rem;letter-spacing:.1em}
.thema-item h3{font-size:1.6rem;margin:.2rem 0 .4rem;transition:color .3s}.thema-item:hover h3,.thema-item.aan h3{color:var(--accent)}
.thema-item p{margin:0;color:var(--ink)}
.voorwie{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:3rem}
.voorwie div{border-radius:20px;padding:1.1rem 1.3rem;font-size:.95rem;background:rgba(255,255,255,.7)}
.voorwie strong{display:block;font-family:var(--f-head);font-size:1.1rem;color:var(--head);margin-bottom:.2rem}

/* pijlers + boom */
.groei{background:linear-gradient(180deg,#e6e6f0 0%,#e4e8ea 50%,#e4e8d8 100%)}
.groei-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:.75fr 1.25fr;gap:4rem;align-items:start}
.groei-boom{position:sticky;top:140px;height:calc(100vh - 170px);display:flex;align-items:center;justify-content:center}
.groei-boom .boom{max-height:100%;width:auto;max-width:100%}
.pijler-lijst{display:grid;gap:1rem;margin:2rem 0}
.pijler-lijst .pijler{display:grid;grid-template-columns:auto 1fr;gap:1.2rem;align-items:start;background:rgba(255,255,255,.72);border-color:transparent}
.pijler-lijst .pijler-nr{font-size:2.4rem;color:var(--accent-l);line-height:1;padding-top:.2rem}
.groei-slot{font-family:var(--f-head);font-size:1.25rem;font-style:italic;color:var(--head)}

/* natuurband */
.natuurband{position:relative;min-height:62vh;display:grid;place-items:center;text-align:center;color:#fff;overflow:hidden;isolation:isolate}
.natuurband img{position:absolute;inset:-15% 0;width:100%;height:130%;object-fit:cover;z-index:-2}
.natuurband::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(228,232,216,.9) 0%,rgba(63,43,51,.2) 35%,rgba(63,43,51,.5) 100%)}
.natuurband img{object-position:50% 60%}
.natuurband-in{max-width:760px;padding:6rem 1.25rem 4rem}
.natuurband h2{color:#fff;font-size:clamp(2rem,4.5vw,3.4rem);font-weight:400;text-shadow:0 2px 20px rgba(0,0,0,.25)}
.natuurband p{font-family:var(--f-head);font-style:italic;font-size:1.3rem;text-shadow:0 2px 12px rgba(0,0,0,.3)}

/* aanbod: zonder foto's */
.aanbod-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
.aanbod{border-radius:28px;padding:2.2rem;background:var(--surface);border:1px solid var(--line);position:relative;overflow:hidden;transition:transform .35s,box-shadow .35s;display:flex;flex-direction:column}
.aanbod::before{content:"";position:absolute;width:180px;height:180px;border-radius:50%;right:-70px;top:-70px;background:var(--tint);transition:transform .5s}
.aanbod:nth-child(2)::before{background:#e6e0ee}.aanbod:nth-child(3)::before{background:#e4e8d8}
.aanbod:hover{transform:translateY(-6px);box-shadow:0 30px 60px -35px rgba(80,40,50,.45)}.aanbod:hover::before{transform:scale(1.5)}
.aanbod>*{position:relative}.aanbod p{flex:1}
.aanbod h3{font-size:1.6rem}

/* over mij */
.voorstellen{background:linear-gradient(180deg,var(--bg),#ece6ef)}
.voorstellen-in{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:1.1fr 1fr;gap:4rem;align-items:center}
.voorstellen-foto{position:relative;max-width:460px;justify-self:center;width:100%}
.voorstellen-foto img{width:100%;aspect-ratio:2/3;object-fit:cover;object-position:50% 50%;border-radius:48% 52% 46% 54% / 56% 44% 56% 44%}
.voorstellen-foto .boom{position:absolute;width:38%;left:-10%;bottom:-4%;filter:drop-shadow(0 8px 16px rgba(80,40,50,.2))}
.handtekening{font-family:var(--f-script);font-size:2.6rem;color:var(--accent);line-height:1;margin:1.2rem 0 .2rem}

.home .slotband{margin:0;border-radius:0;padding:clamp(5rem,10vw,8rem) 1.5rem}
.slotband{color:#fff;position:relative;overflow:hidden;isolation:isolate}
.slotband h2{color:#fff}.slotband p{color:#eadfe2}.slotband .knop{background:var(--blush);color:#573a44;border-color:var(--blush)}.slotband .knop:hover{background:#fff}.slotband .slot-merk{background:#fff;border-radius:50%;padding:10px}
.slotband .slot-natuur{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 70%;opacity:.22;z-index:-1;margin:0;filter:saturate(.7)}
.home .slotband::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(107,70,82,.9),rgba(107,70,82,.55) 50%,rgba(63,43,51,.95))}
.slotband .handtekening{font-style:normal;color:var(--blush)}

.pag-foto img,.blog-foto img,.themas-foto img{object-position:50% 25%}
.pagina-over-mij .pag-foto,.pagina-contact .pag-foto,.pagina-mentaal-vastlopen .pag-foto,.pagina-relaties .pag-foto{aspect-ratio:2/3;max-width:420px;justify-self:end}
.pagina-over-mij .pag-foto img,.pagina-contact .pag-foto img,.pagina-mentaal-vastlopen .pag-foto img,.pagina-relaties .pag-foto img{object-position:50% 50%}
.themas-foto img{object-position:50% 40%}
@media (max-width:1000px){.aanbod-grid{grid-template-columns:1fr}.voorwie{grid-template-columns:1fr 1fr}.hero{grid-template-columns:1fr;min-height:0}.hero-tekst{padding-top:3rem;padding-bottom:2.5rem}.hero-natuur{min-height:420px}.hero-portret{left:6%;bottom:6%;width:min(48%,300px)}}
@media (max-width:860px){
  .herken-in,.voorstellen-in,.themas-in{grid-template-columns:1fr;gap:2rem}.themas-foto{position:relative;top:0;aspect-ratio:16/10}
  .quote-kaart{position:static;margin-top:1rem;max-width:none}
  .groei-in{grid-template-columns:1fr}.groei-boom{position:relative;top:0;height:auto}.groei-boom .boom{max-width:300px}
  .hero-boom{display:none}
}
@media (max-width:560px){.voorwie{grid-template-columns:1fr}.hero-natuur{min-height:340px}}
""" + BOOM_CSS

JS = BASIS_JS + BOOM_JS + r"""
(function(){
  // hero-boom groeit vanzelf bij laden
  var hb=document.getElementById('heroboom');if(hb){var t0=null;function st(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/3600);groeiBoom(hb,p);if(p<1)requestAnimationFrame(st)}requestAnimationFrame(st)}
  // boom groeit met scrollen door de werkwijze-sectie
  var sec=document.getElementById('groei'),svg=document.getElementById('boom');
  if(sec&&svg){function upd(){var r=sec.getBoundingClientRect();var h=r.height-innerHeight;var p=Math.max(0,Math.min(1,(-r.top+innerHeight*0.3)/(h+innerHeight*0.3)));groeiBoom(svg,p)}upd();addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);}
  // thema-foto's wisselen mee met scrollen
  var items=document.querySelectorAll('.thema-item'),fotos=document.querySelectorAll('.themas-foto img');
  if(items.length){var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var i=+e.target.dataset.i;items.forEach(function(x){x.classList.remove('aan')});fotos.forEach(function(x){x.classList.remove('aan')});e.target.classList.add('aan');fotos[i].classList.add('aan')}})},{rootMargin:'-40% 0px -40% 0px'});items.forEach(function(x){io2.observe(x)});
    items.forEach(function(x){x.addEventListener('mouseenter',function(){var i=+x.dataset.i;fotos.forEach(function(f){f.classList.remove('aan')});fotos[i].classList.add('aan')})})}
  // wortels bij over mij groeien in beeld
  var ob=document.getElementById('overboom');if(ob){var io3=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var t1=null;function g(ts){if(!t1)t1=ts;var p=Math.min(1,(ts-t1)/3000);groeiBoom(ob,p);if(p<1)requestAnimationFrame(g)}requestAnimationFrame(g);io3.disconnect()}})},{threshold:.4});io3.observe(ob)}
  // parallax natuurband
  var nb=document.querySelector('.natuurband img');if(nb&&!matchMedia('(prefers-reduced-motion: reduce)').matches){addEventListener('scroll',function(){var r=nb.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;var p=(r.top+r.height/2-innerHeight/2)/innerHeight;nb.style.transform='translateY('+(p*-50)+'px)'},{passive:true})}
})();
"""


def home():
    themas = "".join(f"""<a class="thema-item reveal" data-i="{i}" href="{t['slug']}.html"><span class="nr">0{i+1}</span><h3>{esc(t['kop'])}</h3><p>{esc(t['kort'])}</p></a>""" for i, t in enumerate(THEMAS))
    fotos = "".join(f'<img src="{A}foto/{t["foto"]}" alt="" loading="lazy" class="{"aan" if i == 0 else ""}">' for i, t in enumerate(THEMAS))
    voorwie = "".join(f'<div class="reveal vertraag-{(i%3)+1}"><strong>{esc(k)}</strong>{esc(v)}</div>' for i, (k, v) in enumerate(HOME["voorwie"]))
    pijlers = "".join(f"""<article class="pijler reveal"><span class="pijler-nr">0{i+1}</span><div><h3>{esc(p['kop'])}</h3><p>{esc(p['kort'])}</p><a class="pijl-link" href="werkwijze/{p['slug']}.html">Lees meer <span aria-hidden="true">→</span></a></div></article>""" for i, p in enumerate(PIJLERS))
    aanbod = "".join(f"""<article class="aanbod reveal vertraag-{i+1}"><h3>{esc(k)}</h3><p>{esc(t)}</p><a class="pijl-link" href="{h}">{esc(l)} <span aria-hidden="true">→</span></a></article>""" for i, (k, t, h, l) in enumerate(HOME["aanbod"]))
    herken = "".join(f"<p>{esc(x)}</p>" for x in HOME["herken"])
    woorden = ["Leer te voelen", "Durf te vertrouwen", "Rust", "Zachtheid", "Vertrouwen", "Warmte", "Professionaliteit", "Wat gevoeld mag worden, kan weer gaan stromen"]
    strook = "".join(f"<span>{esc(w)}</span>" for w in woorden) * 2
    voorst = "".join(f"<p>{esc(x)}</p>" for x in HOME["voorstellen"] if x)
    return head(HOME["seo_titel"], HOME["seo"], THEMA) + f"""<body class="home v2">
{nav('index.html')}
<main id="inhoud">
<section class="hero">
  <div class="hero-tekst">
    <p class="boventitel">{esc(TITEL)}</p>
    <h1>Leer te voelen.<br><em>Durf te vertrouwen.</em></h1>
    <p class="hero-lead">{esc(HOME['doelgroep'])}</p>
    <div class="hero-knoppen"><a class="knop" href="contact.html">Plan een kennismaking</a><a class="knop knop-licht" href="#helpen">Waarmee kan ik je helpen?</a></div>
  </div>
  <div class="hero-natuur">
    <img src="{A}foto/natuur-water.jpg" alt="" fetchpriority="high">
    <div class="hero-portret"><img src="{A}foto/portret-lach.jpg" alt="Liesbeth Postma, psychosociaal en lichaamsgericht therapeut"></div>
    <div class="hero-boom">{boom_svg('heroboom')}</div>
  </div>
</section>

<div class="strook" aria-hidden="true"><div class="strook-in">{strook}</div></div>

<section class="sectie">
  <div class="herken-in">
    <div class="herken-foto reveal"><img src="{A}foto/wilg-lach.jpg" alt="Liesbeth Postma tussen de takken van een wilg" loading="lazy"><div class="quote-kaart">“{esc(HOME['herken_slot'])}”</div></div>
    <div class="herken-tekst reveal vertraag-1"><p class="boventitel">Misschien herken je dit…</p><h2>Aan de buitenkant gaat het <em>best goed</em></h2>{herken}<p class="herken-slot">{esc(STROOM)}</p></div>
  </div>
</section>

<section class="video reveal">
  <div class="video-kaart"><img src="{A}foto/natuur-meer.jpg" alt="" loading="lazy"><a class="afspelen" href="over-mij.html" aria-label="Persoonlijk verhaal van Liesbeth (video volgt)"><b><svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></b><span>Mijn persoonlijke verhaal</span><small>Video volgt binnenkort</small></a></div>
</section>

<section class="sectie themas" id="helpen">
  <div class="themas-in">
    <div>
      <p class="boventitel reveal">Waarmee kan ik je helpen?</p>
      <h2 class="reveal">Vier thema's waarmee je bij mij <em>terechtkunt</em></h2>
      <div>{themas}</div>
    </div>
    <div class="themas-foto reveal">{fotos}</div>
  </div>
</section>

<section class="sectie groei" id="groei">
  <div class="groei-in">
    <div class="groei-boom">{boom_svg()}</div>
    <div>
      <p class="boventitel reveal">Mijn werkwijze</p>
      <h2 class="reveal">Vijf pijlers, één <em>uitgangspunt</em>: opnieuw leren voelen</h2>
      {"".join(f'<p class="reveal">{esc(x)}</p>' for x in HOME['werkwijze'])}
      <div class="pijler-lijst">{pijlers}</div>
      {"".join(f'<p class="groei-slot reveal">{esc(x)}</p>' for x in HOME['werkwijze_slot'])}
      <p class="reveal"><a class="knop" href="werkwijze.html">Meer over mijn werkwijze</a></p>
    </div>
  </div>
</section>

<section class="natuurband">
  <img src="{A}foto/natuur-heide.jpg" alt="" loading="lazy">
  <div class="natuurband-in reveal"><h2>Wat gevoeld mag worden, kan weer gaan stromen</h2><p>Stap voor stap, in jouw tempo.</p></div>
</section>

<section class="sectie">
  <div class="binnen">
    <div class="reveal" style="max-width:640px;margin-bottom:2.5rem"><p class="boventitel">Mijn aanbod</p><h2>Individueel, in een <em>opstelling</em> of in een workshop</h2></div>
    <div class="aanbod-grid">{aanbod}</div>
  </div>
</section>

<section class="sectie voorstellen">
  <div class="voorstellen-in">
    <div class="reveal">
      <p class="boventitel">Even voorstellen</p>
      <h2>Professionele kennis en <em>doorleefde ervaring</em></h2>
      {voorst}
      <p class="handtekening">Liesbeth</p>
      <a class="pijl-link" href="over-mij.html">Lees meer over mij <span aria-hidden="true">→</span></a>
    </div>
    <div class="voorstellen-foto reveal vertraag-1"><img src="{A}foto/portret-deur.jpg" alt="Liesbeth Postma" loading="lazy">{boom_svg('overboom')}</div>
  </div>
</section>

<section class="slotband reveal" style="margin-top:0">
  <img class="slot-natuur" src="{A}foto/natuur-bloemen-staand.jpg" alt="" loading="lazy">
  <div class="slotband-in">
    <img class="slot-merk" src="{A}beeldmerk.png" alt="" width="90" loading="lazy">
    <h2>Leer te voelen – durf te vertrouwen</h2>
    {"".join(f'<p style="font-style:normal;font-family:var(--f-body);font-size:1.05rem;margin-bottom:.6rem;color:#eadfe2">{esc(x)}</p>' for x in HOME['slot'])}
    <p class="handtekening">Lieve groet, Liesbeth</p>
    <a class="knop" href="contact.html">Neem contact op</a>
  </div>
</section>
</main>
{footer()}
{scripts()}
</body></html>"""
