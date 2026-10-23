import os

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Paathshala · Guided Learning Banner</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Outfit:wght@600;700;800;900&display=swap">
<style>
/*
  Compact, widescreen Paathshala ad banner with interactive outlined card deck.
  - Video removed as requested.
  - Decreased banner height (aspect-ratio 16/7.5) to look like a true sleek banner.
  - Card height halved (19cqw vs previous 40cqw).
  - Every card clearly outlined with a crisp 1.5px border.
  - CTA positioned at the bottom with exact copy.
*/
*{box-sizing:border-box}
html,body{margin:0}
body{background:#F1F5F9;padding:24px 16px;min-height:100vh;display:flex;align-items:center;justify-content:center}
.wrap{container-type:inline-size;width:100%;max-width:1200px;margin:0 auto}

.banner{
  position:relative;width:100%;aspect-ratio:16/7.6;overflow:hidden;
  background:#FAF8F5;color:#0F172A;
  border:1px solid #E2E8F0;border-radius:2cqw;box-shadow:0 0.6cqw 2.5cqw rgba(15,23,42,.07);
  font-family:"Plus Jakarta Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
}

/* ---------- Header (Top) ---------- */
.brand{position:absolute;top:1.8cqw;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:.6cqw;font-weight:800;font-size:1.3cqw;letter-spacing:-.02em;color:#0F172A}
.brand i{width:1.3cqw;height:1.3cqw;border-radius:.4cqw;background:#FF5A36;display:inline-block}
h1{
  position:absolute;top:4.2cqw;left:0;right:0;margin:0;text-align:center;
  font-size:3.2cqw;line-height:1.1;letter-spacing:-.03em;font-weight:800;color:#0F172A;
  padding:0 4cqw;
}

/* ---------- Compact Outlined Card Deck (Half Height) ---------- */
.deck{
  position:absolute;left:0;right:0;top:13.2cqw;height:21cqw;
  display:flex;gap:.6cqw;padding:0 1.8cqw;align-items:flex-start;
  z-index:1;
}

.card{
  position:relative;flex:1 1 0;min-width:0;height:19.5cqw;overflow:hidden;cursor:pointer;
  border-radius:1.4cqw;padding:1.1cqw 1.2cqw;color:#fff;outline-offset:2px;
  border:1.5px solid rgba(15,23,42,0.2);
  transform:translateY(calc(var(--d,0) * 0.8cqw));
  transition:flex .5s cubic-bezier(.2,.8,.2,1),height .5s cubic-bezier(.2,.8,.2,1),transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .3s,border-color .3s;
  animation:rise .7s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 60ms + 100ms);
  box-shadow:0 2px 8px rgba(15,23,42,.06);
}

.card.on{
  flex-grow:2.8;z-index:2;
  border-color:#0F172A;
  box-shadow:0 0.8cqw 2.5cqw rgba(15,23,42,.22);
}

@keyframes rise{from{translate:0 15cqw;opacity:0}}

.label{position:relative;z-index:2;font-size:0.95cqw;font-weight:700;opacity:.9;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.stat{position:relative;z-index:2;font-size:2.4cqw;font-weight:800;letter-spacing:-.03em;line-height:1;margin:.5cqw 0 .4cqw;white-space:nowrap;transition:font-size .4s cubic-bezier(.2,.8,.2,1)}
.card.on .stat{font-size:3.6cqw}
.more{position:relative;z-index:2;font-size:1.05cqw;line-height:1.35;font-weight:500;overflow:hidden;opacity:0;max-height:0;transform:translateY(.6cqw);transition:opacity .25s,transform .4s}
.card.on .more{opacity:.95;max-height:12cqw;transform:none;transition-delay:.15s}

/* Outlined Card Themes */
.a{background:#FFD25E;color:#0F172A;border-color:#D97706}
.b{background:#4F46E5;border-color:#3730A3}
.c{background:#059669;border-color:#047857}
.e{background:#5458F7;border-color:#3B3DC9}
.f{background:#0F172A;border-color:#334155}
.g{background:#FF5A36;border-color:#C23817}

/* ---------- CTA Section (Brought Down to Bottom) ---------- */
.cta{position:absolute;bottom:4.2cqw;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:1.1cqw;z-index:10}
.btn{
  font-family:"Plus Jakarta Sans",sans-serif;font-weight:700;font-size:1.15cqw;
  padding:0.9cqw 2.1cqw;border-radius:999px;border:1px solid #D6D6DC;
  background:#FFFFFF;color:#0F172A;white-space:nowrap;cursor:pointer;
  text-decoration:none;display:inline-flex;align-items:center;gap:.5cqw;
  transition:all 0.2s cubic-bezier(.2,.8,.2,1);
}
.btn:hover{background:#F1F5F9;transform:translateY(-1px)}
.btn.main{
  background:#FF5A36;border-color:#FF5A36;color:#FFFFFF;
  box-shadow:0 .3cqw 1.2cqw rgba(255,90,54,.32);
}
.btn.main:hover{
  background:#E84622;border-color:#E84622;
  box-shadow:0 .5cqw 1.6cqw rgba(255,90,54,.42);
}
.url{position:absolute;bottom:1.4cqw;left:0;right:0;text-align:center;font-size:0.95cqw;font-weight:600;color:#64748B;z-index:10}

/* ---------- Mobile Layout ---------- */
@container (max-width: 680px){
  .banner{aspect-ratio:4/4.8;border-radius:3cqw}
  .brand{top:3.2cqw;font-size:3.4cqw;gap:1.2cqw}
  .brand i{width:3.2cqw;height:3.2cqw;border-radius:1cqw}
  h1{top:8.5cqw;font-size:5.8cqw;padding:0 2cqw;line-height:1.15}

  .deck{top:24cqw;height:48cqw;gap:.7cqw;padding:0 1.4cqw}
  .a,.g{display:none}
  .card{height:46cqw;border-radius:2.4cqw;padding:1.8cqw 1.4cqw;transform:translateY(calc(var(--d,0) * 1.2cqw))}
  .card.on{flex-grow:3;padding:2.2cqw}
  .card:not(.on) .label{display:none}
  .label{font-size:2.2cqw}
  .stat{font-size:3.2cqw;margin:0 0 .6cqw}
  .card.on .stat{font-size:5.4cqw}
  .more{font-size:2.2cqw}

  .cta{bottom:9cqw;gap:1.6cqw}
  .btn{font-size:2.8cqw;padding:2.2cqw 3.8cqw}
  .url{bottom:3.4cqw;font-size:2.2cqw}
}

.card:focus-visible{outline:2.5px solid #4F46E5}
@media (prefers-reduced-motion:reduce){
  .card{animation:none;transition:none}
  .more,.stat{transition:none}
}
</style>
</head>
<body>
<div class="wrap">
  <div class="banner">
    
    <!-- BRAND LOGO -->
    <div class="brand"><i></i>Paathshala</div>
    
    <!-- HEADLINE -->
    <h1>Where 1-on-1 Tutors &amp; 60s Reels<br>Turn Confusion Into Pure Confidence.</h1>

    <!-- 6 COMPACT OUTLINED CARDS (HALF HEIGHT, NO VIDEO) -->
    <div class="deck" id="deck">
      
      <!-- CARD A: CLASSES -->
      <div class="card a" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Classes</div>
        <div class="stat">1–12</div>
        <div class="more">CBSE &amp; ICSE, taught live 1-on-1 by verified educators.</div>
      </div>

      <!-- CARD B: MITRA AI -->
      <div class="card b" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Mitra AI</div>
        <div class="stat">x=4</div>
        <div class="more">2x + 3 = 11, solved step by step. Midnight doubt solver anytime.</div>
      </div>

      <!-- CARD C: RATING -->
      <div class="card c" tabindex="0" role="button" aria-expanded="false">
        <div class="label">★ Rating</div>
        <div class="stat">4.98</div>
        <div class="more">Average rating from 12,000+ parents across India.</div>
      </div>

      <!-- CARD E: MARKS SURGE -->
      <div class="card e" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Marks</div>
        <div class="stat">+29%</div>
        <div class="more">Average marks surge across students in their first 6 weeks.</div>
      </div>

      <!-- CARD F: 24/7 PRACTICE -->
      <div class="card f" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Practice</div>
        <div class="stat">24/7</div>
        <div class="more">Unlimited tailored worksheets and step-by-step doubt clearing.</div>
      </div>

      <!-- CARD G: 60s REELS -->
      <div class="card g" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Revision</div>
        <div class="stat">60s</div>
        <div class="more">Auto-clipped the instant understanding happens for 1-minute recap.</div>
      </div>

    </div>

    <!-- CTA BROUGHT DOWN TO THE BOTTOM WITH EXACT COPY -->
    <div class="cta">
      <a href="https://paathshala.app/booking" target="_blank" class="btn main">
        <span>Book Free 1-on-1 Class</span>
        <span>➔</span>
      </a>
      <a href="/landing.html" class="btn">
        <span>See How It Works</span>
      </a>
    </div>

    <!-- TRUST NOTICE -->
    <div class="url">paathshala.app · 100% free · No card needed · CBSE &amp; ICSE Grades 1–12</div>

  </div>
</div>

<script>
(function(){
  var deck=document.getElementById('deck');
  var cards=[].slice.call(deck.children);
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)');
  var active=cards[1],timer=null,stopped=false;

  function vis(){return cards.filter(function(c){return c.offsetParent!==null;});}
  function render(){
    var v=vis();
    if(v.indexOf(active)<0)active=v[Math.floor(v.length/2)];
    var ai=v.indexOf(active);
    cards.forEach(function(c){
      var i=v.indexOf(c),on=c===active;
      c.classList.toggle('on',on);
      c.setAttribute('aria-expanded',on);
      c.style.setProperty('--d',i<0?0:Math.abs(i-ai));
    });
  }
  function set(c){active=c;render();}
  function schedule(){
    if(stopped||reduce.matches)return;
    clearTimeout(timer);
    timer=setTimeout(function(){
      var v=vis();set(v[(v.indexOf(active)+1)%v.length]);schedule();
    },3000);
  }
  function pause(){clearTimeout(timer);}

  cards.forEach(function(c,i){
    c.style.setProperty('--i',i);
    c.addEventListener('pointerenter',function(e){if(e.pointerType==='mouse')set(c);});
    c.addEventListener('click',function(){stopped=true;pause();set(c);});
    c.addEventListener('focus',function(){set(c);});
    c.addEventListener('keydown',function(e){
      if(e.key==='Enter'||e.key===' '){e.preventDefault();stopped=true;pause();set(c);}
    });
  });
  deck.addEventListener('pointerenter',pause);
  deck.addEventListener('pointerleave',schedule);
  deck.addEventListener('focusin',pause);
  deck.addEventListener('focusout',schedule);
  window.addEventListener('resize',render);

  render();
  schedule();
})();
</script>
</body>
</html>
'''

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/homepage-section.html", "w") as f:
    f.write(html_code)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/banner.html", "w") as f:
    f.write(html_code)

print("Compact banner generated successfully!")
