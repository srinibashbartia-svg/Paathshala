import re

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "r") as f:
    content = f.read()

# 1. Update Hero CSS to center align heading and content, remove lab CSS, and make ticker stretch full width with no fade
# Replace .hero and related hero styles
hero_css_old = r'\/\* HERO SECTION \*\/[\s\S]*?\/\* =========================================================================\s*HIGHLIGHT REELS TICKER'
hero_css_new = '''/* HERO SECTION */
        .hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 120px 0 35px;
            position: relative;
            overflow: hidden;
            background: transparent;
            text-align: center;
        }

        .hero:before, .hero:after {
            content: "";
            position: absolute;
            width: 50vw;
            height: 50vw;
            border-radius: 50%;
            filter: blur(100px);
            opacity: 0.35;
            animation: float 14s ease-in-out infinite alternate;
            pointer-events: none;
        }

        .hero:before {
            background: #7C6CFF;
            top: -15vw;
            left: -10vw;
        }

        .hero:after {
            background: #E76F51;
            bottom: -20vw;
            right: -10vw;
            animation-delay: -7s;
        }

        @keyframes float {
            to { transform: translate(6vw, 6vw) scale(1.15); }
        }

        .hero-center-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            max-width: 960px;
            margin: 0 auto 40px;
            padding: 0 5vw;
            position: relative;
            z-index: 1;
        }

        h1 {
            font-size: clamp(42px, 6.8vw, 88px);
            color: #FFFFFF;
            text-align: center;
            margin: 0 auto;
            line-height: 1.05;
        }

        .w {
            display: inline-block;
            overflow: hidden;
            vertical-align: top;
            padding-bottom: 0.08em;
        }

        .w i {
            display: inline-block;
            font-style: normal;
            transform: translateY(110%) rotate(6deg);
            animation: heroUp 0.85s cubic-bezier(.2, .9, .2, 1) forwards;
            animation-delay: calc(var(--n) * 80ms + 0.15s);
        }

        @keyframes heroUp {
            to { transform: none; }
        }

        .sub {
            margin: 20px auto 28px;
            color: var(--mut);
            font-size: clamp(16px, 1.9vw, 21px);
            max-width: 560px;
            text-align: center;
            opacity: 0;
            animation: fade 0.8s 1.1s forwards;
            line-height: 1.55;
        }

        @keyframes fade {
            to { opacity: 1; }
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 13.5px;
            font-weight: 800;
            padding: 7px 18px;
            border: 2px solid var(--border-dark);
            border-radius: 99px;
            margin-bottom: 20px;
            color: var(--border-dark);
            background: var(--g);
            box-shadow: 2px 2px 0px var(--border-dark);
        }

        .hero-btn-group {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
            opacity: 0;
            animation: fade 0.8s 1.2s forwards;
            margin-top: 4px;
        }

        /* =========================================================================
           HIGHLIGHT REELS TICKER'''

content = re.sub(hero_css_old, hero_css_new, content)

# 2. Update Ticker CSS: full viewport width stretch, NO FADING MASK
ticker_css_old = r'\.hero-ticker-section\s*\{[\s\S]*?@keyframes scrollTicker\s*\{[\s\S]*?\}'
ticker_css_new = '''.hero-ticker-section {
            position: relative;
            z-index: 2;
            width: 100vw;
            margin-top: 15px;
            opacity: 0;
            animation: fade 0.8s 1.3s forwards;
            overflow: hidden;
        }

        .ticker-label-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 100vw;
            padding: 0 5vw;
            margin-bottom: 16px;
            font-size: 0.88rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            color: #FFFFFF;
        }

        .ticker-label-bar span {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .live-dot {
            width: 10px;
            height: 10px;
            background: #EF4444;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 12px #EF4444;
            animation: blink 1.4s infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }

        /* FULL WIDTH PANNING VIEWPORT: NO MASK / NO FADING */
        .ticker-scroll-viewport {
            width: 100vw;
            overflow: hidden;
            position: relative;
            padding: 10px 0 24px;
            /* No mask-image so reels never fade at padding edges */
        }

        .ticker-track {
            display: flex;
            gap: 22px;
            width: max-content;
            animation: scrollTicker 45s linear infinite;
        }

        .ticker-track:hover {
            animation-play-state: paused;
        }

        @keyframes scrollTicker {
            from { transform: translateX(0); }
            to { transform: translateX(-50%); }
        }'''

content = re.sub(ticker_css_old, ticker_css_new, content)

# 3. Replace the HTML structure in .hero: Remove .lab and wrap heading in .hero-center-content
hero_html_old = r'<section class="hero">\s*<div class="hero-top-grid">[\s\S]*?<\/div>\s*<\/div>\s*<!-- =========================================================================\s*HIGHLIGHT REELS TICKER'
hero_html_new = '''<section class="hero">
        <div class="hero-center-content">
            <span class="pill">Live 1-on-1 classes · Classes 1 to 12</span>
            <h1 id="h1"></h1>
            <p class="sub">A dedicated expert teacher who meets your child exactly where they're stuck.</p>
            <div class="hero-btn-group">
                <a class="btn" href="https://paathshala.app/booking">Book free trial ➔</a>
                <a class="btn ghost" href="#story">Explore the journey ↓</a>
            </div>
        </div>

        <!-- =========================================================================
             HIGHLIGHT REELS TICKER'''

content = re.sub(hero_html_old, hero_html_new, content)

# 4. Remove .lab JS logic
js_lab_old = r'\/\/ 2\. Interactive Guide Lab Toggle[\s\S]*?Stuck on a question, alone\.";\s*\};'
content = re.sub(js_lab_old, '', content)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(content)

print("Successfully centered hero heading and stretched highlight reels full width without fading!")
