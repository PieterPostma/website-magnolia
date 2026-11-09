
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
  window.verstuur=function(f){var b='Naam: '+f.naam.value+'\nE-mail: '+f.email.value+'\nTelefoon: '+f.telefoon.value+'\n\n'+f.bericht.value;location.href='mailto:'+'info@liesbethpostma.nl'+'?subject='+encodeURIComponent('Kennismaken via de website')+'&body='+encodeURIComponent(b);return false;};
})();

(function(){
  // video: Google Drive-speler pas laden na klik
  var vk=document.getElementById('videokaart');
  if(vk){vk.querySelector('.afspelen').addEventListener('click',function(){var f=document.createElement('iframe');f.src='https://drive.google.com/file/d/'+vk.dataset.video+'/preview';f.allow='autoplay; fullscreen';f.allowFullscreen=true;f.title='Persoonlijk verhaal van Liesbeth';vk.innerHTML='';vk.appendChild(f)})}
  // thema-foto's wisselen mee met scrollen
  var items=document.querySelectorAll('.thema-item'),fotos=document.querySelectorAll('.themas-foto img');
  if(items.length){var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var i=+e.target.dataset.i;items.forEach(function(x){x.classList.remove('aan')});fotos.forEach(function(x){x.classList.remove('aan')});e.target.classList.add('aan');fotos[i].classList.add('aan')}})},{rootMargin:'-40% 0px -40% 0px'});items.forEach(function(x){io2.observe(x)});
    items.forEach(function(x){x.addEventListener('mouseenter',function(){var i=+x.dataset.i;fotos.forEach(function(f){f.classList.remove('aan')});fotos[i].classList.add('aan')})})}
  // parallax natuurband
  var nb=document.querySelector('.natuurband img');if(nb&&!matchMedia('(prefers-reduced-motion: reduce)').matches){addEventListener('scroll',function(){var r=nb.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;var p=(r.top+r.height/2-innerHeight/2)/innerHeight;nb.style.transform='translateY('+(p*-50)+'px)'},{passive:true})}
})();
