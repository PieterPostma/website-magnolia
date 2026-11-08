
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
