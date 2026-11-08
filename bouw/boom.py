# -*- coding: utf-8 -*-
"""Groeiende magnolia als SVG + scroll-gestuurde animatie (gedeeld, per versie anders ingekleurd)."""

# takken: (pad, volgorde) – bloesems: (x, y, schaal, vertraging)
TAKKEN = [
    "M200 560 C204 500 196 440 200 380 C203 340 198 300 200 250",             # stam
    "M200 400 C170 380 140 360 118 318 C108 300 100 285 96 262",             # links laag
    "M200 360 C235 335 262 318 282 282 C292 262 300 245 306 222",            # rechts midden
    "M200 300 C180 270 160 250 150 215 C145 198 142 185 140 168",            # links hoog
    "M200 250 C210 220 225 195 245 170 C255 157 262 145 266 128",            # rechts hoog
    "M200 250 C196 215 192 180 194 140 C195 120 196 105 200 86",             # top
    "M118 318 C105 305 92 300 76 296",                                        # zijtakje
    "M282 282 C300 280 316 284 332 292",                                      # zijtakje
    "M150 215 C135 210 122 212 112 218",                                      # zijtakje
    "M245 170 C258 168 270 172 278 182",                                      # zijtakje
]
BLOESEMS = [
    (96, 262, 1.0), (76, 296, .7), (306, 222, 1.0), (332, 292, .7), (140, 168, .95), (112, 218, .65),
    (266, 128, .95), (278, 182, .65), (200, 86, 1.1), (160, 250, .6), (240, 215, .6), (190, 160, .55), (215, 120, .6),
]
WORTELS = [
    "M200 560 C180 575 150 580 120 596", "M200 560 C220 578 250 582 285 598", "M200 560 C195 580 190 600 192 622",
    "M200 560 C170 566 140 566 112 572", "M200 560 C232 568 262 566 294 574",
]


def bloesem(x, y, s, i):
    """Vijfbladige magnoliabloesem."""
    bl = "".join(f'<ellipse rx="7" ry="13" cy="-11" transform="rotate({k*72})" class="pet"/>' for k in range(5))
    return f'<g transform="translate({x} {y}) scale({s})"><g class="bloesem" style="--i:{i}">{bl}<circle r="3.2" class="hart"/></g></g>'


def boom_svg(idd="boom", wortels=True):
    takken = "".join(f'<path d="{p}" class="tak" style="--i:{i}" pathLength="1"/>' for i, p in enumerate(TAKKEN))
    w = "".join(f'<path d="{p}" class="wortel" style="--i:{i}" pathLength="1"/>' for i, p in enumerate(WORTELS)) if wortels else ""
    bl = "".join(bloesem(x, y, s, i) for i, (x, y, s) in enumerate(BLOESEMS))
    return f'''<svg class="boom" id="{idd}" viewBox="40 60 320 580" aria-hidden="true" focusable="false">
<g class="wortels">{w}</g>
<g class="takken">{takken}</g>
<g class="bloesems">{bl}</g>
</svg>'''


BOOM_CSS = r"""
.boom{width:100%;height:auto;overflow:visible}
.boom .tak{fill:none;stroke:var(--boom-stam,#b08878);stroke-width:7;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1}
.boom .tak:nth-child(n+2){stroke-width:4.5}
.boom .tak:nth-child(n+7){stroke-width:3}
.boom .wortel{fill:none;stroke:var(--boom-wortel,#d9bfb5);stroke-width:3.5;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1}
.boom .bloesem{opacity:0;transform-box:fill-box;transform-origin:center;transition:opacity .4s}
.boom .pet{fill:var(--boom-bloesem,#f4c3c3);stroke:var(--boom-bloesem-rand,#efa6a2);stroke-width:.6;opacity:.9}
.boom .bloesem .pet:nth-child(odd){fill:var(--boom-bloesem2,#f8d8d0)}
.boom .hart{fill:var(--boom-hart,#b85860)}
.boom.klaar .bloesem{animation:wieg 6s ease-in-out infinite;animation-delay:calc(var(--i) * -.7s)}
@keyframes wieg{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
"""

# JS: groeiBoom(svgEl, progress 0..1). Takken groeien na elkaar, bloesems volgen, wortels als eerste.
BOOM_JS = r"""
window.groeiBoom=function(svg,p){
  var takken=svg.querySelectorAll('.tak'),w=svg.querySelectorAll('.wortel'),bl=svg.querySelectorAll('.bloesem');
  var n=takken.length;
  w.forEach(function(el){el.style.strokeDashoffset=1-Math.max(0,Math.min(1,p/0.18))});
  takken.forEach(function(el,i){var s=0.1+i*(0.55/n),e=s+0.22;el.style.strokeDashoffset=1-Math.max(0,Math.min(1,(p-s)/(e-s)))});
  bl.forEach(function(el,i){var s=0.62+i*(0.3/bl.length);var v=Math.max(0,Math.min(1,(p-s)/0.1));el.style.opacity=v;el.style.transform='scale('+(0.2+0.8*v)+')'});
  svg.classList.toggle('klaar',p>0.98);
  return p>0.98;
};
"""
