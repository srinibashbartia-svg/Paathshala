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
  Responsive, interactive Paathshala ad banner with expanding card deck.
  - Sized via cqw (1% container width).
  - Landscape layout (4:3) above 640px wide, portrait layout (4:5) below.
  - CTA brought down below the card deck with exact conversion copy.
  - Interactive expanding 9:16 vertical class reel.
*/
*{box-sizing:border-box}
html,body{margin:0}
body{background:#F8FAFC;padding:24px 16px;min-height:100vh;display:flex;align-items:center;justify-content:center}
.wrap{container-type:inline-size;width:100%;max-width:1200px;margin:0 auto}
.banner{
  --vidh:37.5cqw;
  position:relative;width:100%;aspect-ratio:4/3;overflow:hidden;
  background:#FAF8F5;color:#0F172A;
  border:1px solid #E2E8F0;border-radius:2.4cqw;box-shadow:0 0.8cqw 3cqw rgba(15,23,42,.08);
  font-family:"Plus Jakarta Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
}

/* ---------- Header (Top) ---------- */
.brand{position:absolute;top:2.2cqw;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:.7cqw;font-weight:800;font-size:1.5cqw;letter-spacing:-.02em;color:#0F172A}
.brand i{width:1.6cqw;height:1.6cqw;border-radius:.5cqw;background:#FF5A36;display:inline-block}
h1{
  position:absolute;top:5.4cqw;left:0;right:0;margin:0;text-align:center;
  font-size:4.8cqw;line-height:1.08;letter-spacing:-.04em;font-weight:800;color:#0F172A;
  padding:0 3cqw;
}

/* ---------- Interactive Card Deck (Center) ---------- */
.deck{
  position:absolute;left:0;right:0;top:18.5cqw;height:41.5cqw;
  display:flex;gap:.5cqw;padding:0 1.6cqw;align-items:flex-start;
  z-index:1;
}
.card{
  position:relative;flex:1 1 0;min-width:0;height:40cqw;overflow:hidden;cursor:pointer;
  border-radius:1.8cqw;padding:1.4cqw 1.3cqw;color:#fff;outline-offset:3px;
  border:1px solid rgba(255,255,255,0.18);
  transform:translateY(calc(var(--d,0) * 1.6cqw));
  transition:flex .6s cubic-bezier(.2,.8,.2,1),height .6s cubic-bezier(.2,.8,.2,1),transform .6s cubic-bezier(.2,.8,.2,1),box-shadow .4s;
  animation:rise .8s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 70ms + 150ms);
}
.card.on{flex-grow:3.2;z-index:2;box-shadow:0 1cqw 3.5cqw rgba(15,23,42,.25)}
@keyframes rise{from{translate:0 25cqw;opacity:0}}

.label{position:relative;z-index:2;font-size:1.05cqw;font-weight:700;opacity:.9;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.stat{position:relative;z-index:2;font-size:3.2cqw;font-weight:800;letter-spacing:-.04em;line-height:1;margin:.6cqw 0 .5cqw;white-space:nowrap;transition:font-size .5s cubic-bezier(.2,.8,.2,1)}
.card.on .stat{font-size:5.4cqw}
.more{position:relative;z-index:2;font-size:1.3cqw;line-height:1.4;font-weight:500;overflow:hidden;opacity:0;max-height:0;transform:translateY(1cqw);transition:opacity .3s,transform .5s}
.card.on .more{opacity:.95;max-height:24cqw;transform:none;transition-delay:.2s}

/* Paathshala Brand Color Palette for Cards */
.a{background:#FFD25E;color:#0F172A;border-color:rgba(15,23,42,0.12)}
.b{background:#4F46E5}
.c{background:#059669}
.e{background:#5458F7}
.f{background:#0F172A}
.g{background:#FF5A36}

/* ---------- 9:16 Vertical Video Card ---------- */
.video{background:linear-gradient(170deg,#0B1226 55%,#2A1F5C);border-color:rgba(255,255,255,0.2)}
.video video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;opacity:.55;transition:opacity .5s}
.video::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(180deg,rgba(11,18,38,.55),rgba(11,18,38,0) 35%,rgba(11,18,38,0) 60%,rgba(11,18,38,.75))}
.video.on{flex:0 0 calc(var(--vidh) * 9 / 16);height:var(--vidh)}
.video.on video{opacity:1}
.video.on .stat{font-size:2.4cqw}
.video .more h3{margin:0 0 .8cqw;font-size:1.4cqw;letter-spacing:-.02em;font-weight:800;text-shadow:0 1px 6px rgba(0,0,0,.4)}
.eq{border:1.5px solid #60A5FA;border-radius:1cqw;padding:.8cqw 1cqw;font:italic 600 1.6cqw Georgia,serif;background:rgba(11,18,38,.65);white-space:nowrap;overflow:hidden}
.so{display:inline-block;margin-top:.8cqw;border:1.5px solid #60A5FA;border-radius:1cqw;padding:.4cqw .9cqw;font-weight:800;font-size:1.2cqw;background:rgba(11,18,38,.65)}
.so em{font-style:normal;background:#FFD25E;color:#0F172A;padding:0 .4cqw;border-radius:.4cqw;margin-left:.3cqw}
.who{position:absolute;z-index:2;left:1.1cqw;right:1.1cqw;bottom:1.1cqw;padding:.7cqw .9cqw;border-radius:.9cqw;background:rgba(11,18,38,.85);font-size:1cqw;font-weight:700;opacity:0;transition:opacity .3s}
.who span{display:block;font-weight:500;opacity:.8;font-size:.85cqw}
.video.on .who{opacity:1;transition-delay:.3s}

/* ---------- CTA Section (Brought Down to Bottom) ---------- */
.cta{position:absolute;bottom:5.2cqw;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:1.2cqw;z-index:10}
.btn{
  font-family:"Plus Jakarta Sans",sans-serif;font-weight:700;font-size:1.25cqw;
  padding:1.1cqw 2.4cqw;border-radius:999px;border:1px solid #D6D6DC;
  background:#FFFFFF;color:#0F172A;white-space:nowrap;cursor:pointer;
  text-decoration:none;display:inline-flex;align-items:center;gap:.6cqw;
  transition:all 0.2s cubic-bezier(.2,.8,.2,1);
}
.btn:hover{background:#F1F5F9;transform:translateY(-1px)}
.btn.main{
  background:#FF5A36;border-color:#FF5A36;color:#FFFFFF;
  box-shadow:0 .4cqw 1.5cqw rgba(255,90,54,.35);
}
.btn.main:hover{
  background:#E84622;border-color:#E84622;
  box-shadow:0 .6cqw 2cqw rgba(255,90,54,.45);
}
.url{position:absolute;bottom:1.8cqw;left:0;right:0;text-align:center;font-size:1.05cqw;font-weight:600;color:#64748B;z-index:10}

/* ---------- Portrait Layout (Mobile) ---------- */
@container (max-width: 640px){
  .banner{--vidh:58cqw;aspect-ratio:4/5;border-radius:4cqw}
  .brand{top:3.5cqw;font-size:3.8cqw;gap:1.4cqw}
  .brand i{width:3.8cqw;height:3.8cqw;border-radius:1.2cqw}
  h1{top:9.8cqw;font-size:7.2cqw;padding:0 2cqw;line-height:1.12}

  .deck{top:28cqw;height:67cqw;gap:.8cqw;padding:0 1.6cqw}
  .a,.g{display:none}
  .card{height:65cqw;border-radius:3cqw;padding:2cqw 1.4cqw;transform:translateY(calc(var(--d,0) * 1.8cqw))}
  .card.on{flex-grow:3.4;padding:2.6cqw}
  .card:not(.on) .label{display:none}
  .label{font-size:2.4cqw}
  .stat{font-size:3.6cqw;margin:0 0 .8cqw}
  .card.on .stat{font-size:7.2cqw}
  .video.on .stat{font-size:3.6cqw}
  .more{font-size:2.7cqw}
  .video .more h3{font-size:2.8cqw;margin-bottom:1.4cqw}
  .eq{font-size:2.6cqw;padding:1.2cqw;border-radius:1.8cqw}
  .so{font-size:2.4cqw;margin-top:1.6cqw;padding:.9cqw 1.8cqw;border-radius:1.8cqw}
  .who{font-size:2cqw;left:1.8cqw;right:1.8cqw;bottom:1.8cqw;padding:1.2cqw 1.6cqw;border-radius:1.8cqw}

  .cta{bottom:11.5cqw;gap:2cqw}
  .btn{font-size:3cqw;padding:2.6cqw 4.2cqw}
  .url{bottom:4.8cqw;font-size:2.5cqw}
}

.card:focus-visible{outline:2px solid #4F46E5}
@media (prefers-reduced-motion:reduce){
  .card{animation:none;transition:none}
  .more,.stat,.video video,.who{transition:none}
}
</style>
</head>
<body>
<div class="wrap">
  <div class="banner">
    
    <!-- BRAND LOGO -->
    <div class="brand"><i></i>Paathshala</div>
    
    <!-- HEADLINE (ADJUSTED ACCORDINGLY) -->
    <h1>Where 1-on-1 Tutors &amp; 60s Reels<br>Turn Confusion Into Pure Confidence.</h1>

    <!-- EXPANDING CARDS DECK (CENTER) -->
    <div class="deck" id="deck">
      
      <!-- CARD A: CLASSES -->
      <div class="card a" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Classes</div>
        <div class="stat">1–12</div>
        <div class="more">CBSE and ICSE curriculum, taught live 1-on-1 by verified educators.</div>
      </div>

      <!-- CARD B: MITRA AI -->
      <div class="card b" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Mitra AI</div>
        <div class="stat">x=4</div>
        <div class="more">2x + 3 = 11, solved step by step. Midnight doubt solver that works anytime.</div>
      </div>

      <!-- CARD C: RATING -->
      <div class="card c" tabindex="0" role="button" aria-expanded="false">
        <div class="label">★ Rating</div>
        <div class="stat">4.98</div>
        <div class="more">Average rating from 12,000+ parents across India.</div>
      </div>

      <!-- 9:16 VERTICAL VIDEO CARD (AUTOPLAYS LEAH'S BREAKTHROUGH REEL) -->
      <div class="card video" tabindex="0" role="button" aria-expanded="false">
        <video muted loop playsinline preload="metadata" poster="reel-poster.jpg">
          <source src="reel.mp4" type="video/mp4">
          <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
        </video>
        <div class="label">Class reel</div>
        <div class="stat">0:50</div>
        <div class="more">
          <h3>Nuclear glue moment</h3>
          <div class="eq">💡 Neutrons are the glue!</div>
          <div class="so">Now I <em>get it</em></div>
        </div>
        <div class="who">Leah Alexander<span>Physics Mentor · ★ 4.95</span></div>
      </div>

      <!-- CARD E: MARKS SURGE -->
      <div class="card e" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Marks</div>
        <div class="stat">+29%</div>
        <div class="more">Average marks surge across 12,000+ students within their first 6 weeks.</div>
      </div>

      <!-- CARD F: 24/7 PRACTICE -->
      <div class="card f" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Practice</div>
        <div class="stat">24/7</div>
        <div class="more">Unlimited tailored worksheets and step-by-step doubt clearing at any hour.</div>
      </div>

      <!-- CARD G: 60s REELS -->
      <div class="card g" tabindex="0" role="button" aria-expanded="false">
        <div class="label">Revision</div>
        <div class="stat">60s</div>
        <div class="more">Auto-clipped the instant understanding happens for 1-minute exam revision.</div>
      </div>

    </div>

    <!-- CTA BROUGHT DOWN BELOW THE DECK WITH EXACT COPY -->
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
  var active=cards[3],timer=null,stopped=false;

  function vis(){return cards.filter(function(c){return c.offsetParent!==null;});}
  function render(){
    var v=vis();
    if(v.indexOf(active)<0)active=v[Math.floor(v.length/2)];
    var ai=v.indexOf(active);
    cards.forEach(function(c){
      var i=v.indexOf(c),on=c===active,vid=c.querySelector('video');
      c.classList.toggle('on',on);
      c.setAttribute('aria-expanded',on);
      c.style.setProperty('--d',i<0?0:Math.abs(i-ai));
      if(vid){
        if(on&&!reduce.matches){var p=vid.play();if(p&&p.catch)p.catch(function(){});}
        else vid.pause();
      }
    });
  }
  function set(c){active=c;render();}
  function schedule(){
    if(stopped||reduce.matches)return;
    clearTimeout(timer);
    var delay=active.classList.contains('video')?8000:3200;
    timer=setTimeout(function(){
      var v=vis();set(v[(v.indexOf(active)+1)%v.length]);schedule();
    },delay);
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

print("Interactive deck banner generated successfully!")
