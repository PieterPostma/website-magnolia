
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
  window.verstuur=function(f){var b='Naam: '+f.naam.value+'\nE-mail: '+f.email.value+'\nTelefoon: '+f.telefoon.value+'\n\n'+f.bericht.value;location.href='mailto:'+'liesbeth@magnolia-elst.nl'+'?subject='+encodeURIComponent('Kennismaken via de website')+'&body='+encodeURIComponent(b);return false;};
})();

window.groeiBoom=function(svg,p){
  var takken=svg.querySelectorAll('.tak'),w=svg.querySelectorAll('.wortel'),bl=svg.querySelectorAll('.bloesem');
  var n=takken.length;
  w.forEach(function(el){el.style.strokeDashoffset=1-Math.max(0,Math.min(1,p/0.18))});
  takken.forEach(function(el,i){var s=0.1+i*(0.55/n),e=s+0.22;el.style.strokeDashoffset=1-Math.max(0,Math.min(1,(p-s)/(e-s)))});
  bl.forEach(function(el,i){var s=0.62+i*(0.3/bl.length);var v=Math.max(0,Math.min(1,(p-s)/0.1));el.style.opacity=v;el.style.transform='scale('+(0.2+0.8*v)+')'});
  svg.classList.toggle('klaar',p>0.98);
  return p>0.98;
};

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
