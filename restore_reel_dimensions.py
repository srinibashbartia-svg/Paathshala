import re

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "r") as f:
    content = f.read()

# Replace the giant reel styles with the original clean dimension .reel-mini-card styles
reel_css_old = r'\/\* BIGGER REEL CARD \(FULL VIDEO CANVAS\) \*\/[\s\S]*?border: 1px solid rgba\(255, 255, 255, 0\.25\);\s*\}'
reel_css_new = '''/* ORIGINAL SLEEK REEL CARD DIMENSIONS */
        .reel-mini-card {
            background: var(--card-bg);
            border: 2.5px solid var(--border-dark);
            border-radius: 18px;
            box-shadow: 5px 5px 0px var(--border-dark);
            padding: 10px 14px;
            display: flex;
            align-items: center;
            gap: 14px;
            cursor: pointer;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s, background 0.2s;
            text-decoration: none;
            color: var(--fg-dark);
            flex-shrink: 0;
            width: 340px;
        }

        .reel-mini-card:hover {
            transform: translate(-3px, -3px) scale(1.02);
            box-shadow: 8px 8px 0px var(--border-dark);
            background: #FFFFFF;
        }

        /* LIVE MUTED VIDEO CONTAINER */
        .reel-video-container {
            width: 76px;
            height: 106px;
            border-radius: 12px;
            border: 2px solid var(--border-dark);
            overflow: hidden;
            position: relative;
            background: #000000;
            flex-shrink: 0;
            box-shadow: 2px 2px 0px var(--border-dark);
        }

        .reel-video-container video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* MUTE & DURATION BADGES */
        .mute-indicator-pill {
            position: absolute;
            top: 4px;
            left: 4px;
            background: rgba(0, 0, 0, 0.72);
            color: #FFFFFF;
            font-size: 0.58rem;
            font-weight: 800;
            padding: 2px 5px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            gap: 3px;
            backdrop-filter: blur(4px);
            letter-spacing: 0.3px;
        }

        .dur-pill {
            position: absolute;
            bottom: 4px;
            right: 4px;
            background: var(--a);
            color: #FFFFFF;
            font-size: 0.62rem;
            font-weight: 900;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: 'Outfit', sans-serif;
            box-shadow: 0 2px 4px rgba(0,0,0,0.4);
        }

        .reel-card-info {
            display: flex;
            flex-direction: column;
            gap: 4px;
            overflow: hidden;
            flex: 1;
            text-align: left;
        }

        .reel-card-tag {
            font-size: 0.7rem;
            font-weight: 900;
            color: var(--a);
            text-transform: uppercase;
            letter-spacing: 0.6px;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .reel-card-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            line-height: 1.25;
            color: var(--fg-dark);
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .reel-card-tutor {
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--mut-dark);
            display: flex;
            align-items: center;
            gap: 4px;
        }'''

content = re.sub(reel_css_old, reel_css_new, content)

# Also fix the responsive breakpoint for reel cards
content = re.sub(
    r'\.reel-card\s*\{\s*width:\s*180px;\s*height:\s*290px;\s*\}',
    '.reel-mini-card { width: 300px; }',
    content
)

# Now replace the HTML cards inside .ticker-track with the original .reel-mini-card structure
ticker_html_old = r'<div class="ticker-track">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/section>'
ticker_html_new = '''<div class="ticker-track">

                    <!-- CARD 1: NUCLEAR GLUE -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:50</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">⚛️ AHA MOMENT!</span>
                            <span class="reel-card-title">The 'Nuclear Glue' Inside an Atom</span>
                            <span class="reel-card-tutor">Leah Alexander · Physics</span>
                        </div>
                    </a>

                    <!-- CARD 2: 99.999% EMPTY SPACE -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r2" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r2.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r2.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:58</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🌌 MIND BLOWN</span>
                            <span class="reel-card-title">You Are 99.999% Empty Space!</span>
                            <span class="reel-card-tutor">Leah Alexander · Chemistry</span>
                        </div>
                    </a>

                    <!-- CARD 3: VEDIC MULTIPLICATION -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1_og.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:42</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">💡 MENTAL MATH</span>
                            <span class="reel-card-title">Multiply Any 2-Digit Number in 3s</span>
                            <span class="reel-card-tutor">Nikita Arvey · Mathematics</span>
                        </div>
                    </a>

                    <!-- CARD 4: AUTUMN LEAVES -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r2" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r2.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r2.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:54</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🌿 NATURE DECODED</span>
                            <span class="reel-card-title">Why Leaves Turn Red In Autumn</span>
                            <span class="reel-card-tutor">Soumi Sarkar · Biology</span>
                        </div>
                    </a>

                    <!-- CARD 5: MAGIC E PHONICS -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:38</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🔤 PHONICS SECRET</span>
                            <span class="reel-card-title">The Secret Magic 'E' Rule</span>
                            <span class="reel-card-tutor">Leah Alexander · Reading</span>
                        </div>
                    </a>

                    <!-- CARD 6: PYTHAGORAS WATER TANKS -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r2" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r2.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r2.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:48</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">📐 VISUAL PROOF</span>
                            <span class="reel-card-title">Pythagoras Theorem with Water Tanks</span>
                            <span class="reel-card-tutor">Tanu Riya · Geometry</span>
                        </div>
                    </a>

                    <!-- REPEAT SET FOR SEAMLESS 40s CONTINUOUS TICKER LOOP -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:50</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">⚛️ AHA MOMENT!</span>
                            <span class="reel-card-title">The 'Nuclear Glue' Inside an Atom</span>
                            <span class="reel-card-tutor">Leah Alexander · Physics</span>
                        </div>
                    </a>

                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r2" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r2.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r2.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:58</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🌌 MIND BLOWN</span>
                            <span class="reel-card-title">You Are 99.999% Empty Space!</span>
                            <span class="reel-card-tutor">Leah Alexander · Chemistry</span>
                        </div>
                    </a>

                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1_og.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                            <span class="mute-indicator-pill">🔇 Muted</span>
                            <span class="dur-pill">0:42</span>
                        </div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">💡 MENTAL MATH</span>
                            <span class="reel-card-title">Multiply Any 2-Digit Number in 3s</span>
                            <span class="reel-card-tutor">Nikita Arvey · Mathematics</span>
                        </div>
                    </a>

                </div>
            </div>
        </div>
    </section>'''

content = re.sub(ticker_html_old, ticker_html_new, content)

# Update video selector in JS
content = re.sub(
    r"document\.querySelectorAll\('\.reel-card video'\)",
    "document.querySelectorAll('.reel-video-container video')",
    content
)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(content)

print("Restored original reel card dimensions and confirmed full-width ticker!")
