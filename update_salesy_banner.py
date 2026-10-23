import re

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/homepage-section.html", "r") as f:
    html = f.read()

# Define high-impact, design-forward, salesy CSS for the banner
salesy_banner_css = '''
        /* =========================================================================
           HIGH-CONVERTING DESIGN-FORWARD GUIDED LEARNING HOMEPAGE BANNER
           ========================================================================= */
        .guided-learning-banner-wrapper {
            max-width: 1240px;
            margin: 24px auto 60px;
            padding: 0 20px;
        }

        .guided-learning-banner {
            background: linear-gradient(135deg, #4844E7 0%, #5F5AF6 60%, #4338CA 100%);
            border: 2.5px solid #18181B;
            border-radius: 28px;
            box-shadow: 8px 8px 0px #18181B;
            position: relative;
            overflow: hidden;
            color: #FFFFFF;
        }

        /* INTEGRATED DOTTED GRAPH CANVAS */
        .banner-grid-overlay {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(255, 255, 255, 0.22) 1.5px, transparent 1.5px);
            background-size: 20px 20px;
            pointer-events: none;
            z-index: 1;
        }

        /* INTEGRATED MINI MARQUEE STRIP (FILLED TEXT) */
        .banner-top-ticker {
            background: rgba(17, 24, 39, 0.45);
            backdrop-filter: blur(8px);
            border-bottom: 1.5px solid rgba(255, 255, 255, 0.15);
            padding: 8px 0;
            overflow: hidden;
            white-space: nowrap;
            position: relative;
            z-index: 2;
        }

        .banner-ticker-content {
            display: inline-block;
            font-family: 'Outfit', sans-serif;
            font-size: 0.88rem;
            font-weight: 900;
            letter-spacing: 0.5px;
            animation: banner-ticker 26s linear infinite;
        }

        @keyframes banner-ticker {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        .banner-ticker-content span {
            color: #FFFFFF;
            margin: 0 10px;
        }

        .banner-ticker-content em {
            color: #FFD25E;
            font-style: normal;
            margin: 0 10px;
        }

        .banner-ticker-content .coral-word {
            color: #FF725E;
            font-weight: 900;
            margin: 0 10px;
        }

        /* MAIN BANNER TWO-COLUMN BODY */
        .banner-main-grid {
            display: grid;
            grid-template-columns: 1.28fr 0.82fr;
            gap: 40px;
            align-items: center;
            padding: 38px 44px;
            position: relative;
            z-index: 2;
        }

        /* LEFT: SALES COPY & VALUE STACK */
        .banner-sales-col {
            display: flex;
            flex-direction: column;
            gap: 18px;
        }

        .banner-trust-pills {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .badge-live-pulse {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(255, 255, 255, 0.18);
            backdrop-filter: blur(6px);
            border: 1.5px solid rgba(255, 255, 255, 0.4);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.74rem;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            padding: 4px 12px;
            border-radius: 9999px;
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            background: #10B981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10B981;
            animation: pulse-green 1.5s infinite;
        }

        @keyframes pulse-green {
            0% { transform: scale(0.9); opacity: 0.8; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.8; }
        }

        .badge-stat-rating {
            background: #FFD25E;
            color: #18181B;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.74rem;
            padding: 4px 12px;
            border-radius: 9999px;
            border: 1.5px solid #18181B;
            box-shadow: 2px 2px 0px #18181B;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .badge-board-coverage {
            background: #FFFFFF;
            color: #18181B;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.74rem;
            padding: 4px 12px;
            border-radius: 9999px;
            border: 1.5px solid #18181B;
            box-shadow: 2px 2px 0px #18181B;
        }

        .banner-sales-headline {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2rem, 3.4vw, 3rem);
            font-weight: 900;
            line-height: 1.12;
            letter-spacing: -0.025em;
            color: #FFFFFF;
            margin: 0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
        }

        .banner-sales-headline span.gold-hl {
            color: #FFD25E;
            position: relative;
        }

        .banner-sales-subtext {
            font-size: 1.08rem;
            line-height: 1.55;
            color: #E0E7FF;
            max-width: 630px;
            margin: 0;
        }

        .banner-sales-subtext strong {
            color: #FFFFFF;
            font-weight: 700;
        }

        /* 4 HIGH-CONVERSION SALES VALUE CARDS */
        .banner-sales-cards-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin: 4px 0;
        }

        .sales-benefit-card {
            background: rgba(255, 255, 255, 0.96);
            border: 2px solid #18181B;
            border-radius: 16px;
            padding: 13px 15px;
            display: flex;
            align-items: flex-start;
            gap: 11px;
            box-shadow: 3.5px 3.5px 0px #18181B;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
            color: #18181B;
        }

        .sales-benefit-card:hover {
            transform: translate(-2px, -2px);
            box-shadow: 5px 5px 0px #18181B;
            background: #FFFFFF;
        }

        .sales-card-icon {
            font-size: 1.45rem;
            line-height: 1;
            flex-shrink: 0;
            background: #FEF3C7;
            border: 1.5px solid #18181B;
            border-radius: 10px;
            padding: 6px;
            box-shadow: 1.5px 1.5px 0px #18181B;
        }

        .sales-card-icon.coral-bg {
            background: #FFE4E6;
        }

        .sales-card-icon.blue-bg {
            background: #DBEAFE;
        }

        .sales-card-icon.green-bg {
            background: #D1FAE5;
        }

        .sales-card-text {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .sales-card-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            color: #18181B;
            line-height: 1.2;
        }

        .sales-card-desc {
            font-size: 0.8rem;
            color: #475569;
            line-height: 1.35;
            font-weight: 500;
        }

        /* SALES CTAS & RISK REVERSAL */
        .banner-sales-cta-row {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
            margin-top: 6px;
        }

        .btn-sales-primary {
            background: #FF5A36;
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.05rem;
            padding: 14px 28px;
            border-radius: 16px;
            border: 2px solid #18181B;
            box-shadow: 4px 4px 0px #18181B;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.15s ease;
        }

        .btn-sales-primary:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px #18181B;
            background: #E84D29;
            color: #FFFFFF;
        }

        .btn-sales-secondary {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.96rem;
            padding: 13px 22px;
            border-radius: 16px;
            border: 2px solid rgba(255, 255, 255, 0.6);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s ease;
        }

        .btn-sales-secondary:hover {
            background: #FFFFFF;
            color: #18181B;
            border-color: #18181B;
            box-shadow: 4px 4px 0px #18181B;
            transform: translate(-2px, -2px);
        }

        .banner-reassurance-strip {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
            font-size: 0.78rem;
            color: #E0E7FF;
            font-weight: 600;
            margin-top: -4px;
        }

        .banner-reassurance-strip span {
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        /* RIGHT: INTERACTIVE HIGH-DESIGN LIVE HUD CARD */
        .banner-showcase-col {
            position: relative;
            z-index: 2;
        }

        .showcase-hud-card {
            background: #FFFFFF;
            border: 2.5px solid #18181B;
            border-radius: 22px;
            box-shadow: 7px 7px 0px #18181B;
            padding: 16px;
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 12px;
            color: #18181B;
        }

        .hud-video-frame {
            width: 100%;
            height: 200px;
            border-radius: 14px;
            border: 2px solid #18181B;
            overflow: hidden;
            position: relative;
            background: #0F172A;
            box-shadow: 2px 2px 0px #18181B;
        }

        .hud-video-frame video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .hud-live-tag {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(6px);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 4px 9px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .hud-aha-pill {
            position: absolute;
            bottom: 10px;
            left: 10px;
            right: 10px;
            background: rgba(254, 240, 138, 0.95);
            backdrop-filter: blur(8px);
            border: 1.5px solid #18181B;
            border-radius: 10px;
            padding: 6px 10px;
            font-size: 0.76rem;
            font-weight: 800;
            color: #18181B;
            display: flex;
            align-items: center;
            gap: 7px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            animation: bounce-subtle 3s infinite ease-in-out;
        }

        @keyframes bounce-subtle {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-3px); }
        }

        .hud-student-quote {
            background: #F8FAFC;
            border: 1.5px dashed #CBD5E1;
            border-radius: 12px;
            padding: 8px 12px;
            font-size: 0.78rem;
            color: #334155;
            font-style: italic;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .hud-tutor-meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            padding-top: 2px;
        }

        .hud-tutor-identity {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .hud-tutor-photo {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            border: 2px solid #18181B;
            overflow: hidden;
            flex-shrink: 0;
            background: #FEF08A;
        }

        .hud-tutor-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .hud-tutor-text {
            display: flex;
            flex-direction: column;
            gap: 1px;
        }

        .hud-tutor-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            color: #18181B;
        }

        .hud-tutor-qualification {
            font-size: 0.74rem;
            color: #64748B;
            font-weight: 600;
        }

        .hud-verified-tag {
            background: #D1FAE5;
            color: #065F46;
            border: 1.5px solid #10B981;
            padding: 3px 8px;
            border-radius: 8px;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.74rem;
            white-space: nowrap;
        }

        /* RESPONSIVE DESIGN */
        @media (max-width: 990px) {
            .banner-main-grid {
                grid-template-columns: 1fr;
                padding: 28px 22px;
                gap: 30px;
            }
            .banner-sales-cards-grid {
                grid-template-columns: 1fr;
            }
            .guided-learning-banner-wrapper {
                padding: 0 14px;
            }
        }
'''

# Replace banner CSS
css_pattern = r'\/\* =========================================================================\s*GUIDED LEARNING FLAGSHIP HOMEPAGE BANNER[\s\S]*?\/\* RESPONSIVE ADJUSTMENTS'
html = re.sub(css_pattern, salesy_banner_css + '\n        /* RESPONSIVE ADJUSTMENTS', html)

# Define the new Salesy + Design-forward banner markup with the filled text ticker integrated!
salesy_banner_markup = '''    <!-- =========================================================================
         FLAGSHIP SALESY + DESIGN-FORWARD GUIDED LEARNING HOMEPAGE BANNER
         ========================================================================= -->
    <div class="guided-learning-banner-wrapper" id="guidedLearningSection">
        <div class="guided-learning-banner">
            
            <div class="banner-grid-overlay"></div>

            <!-- FILLED MARQUEE TICKER INTEGRATED ON BANNER -->
            <div class="banner-top-ticker">
                <div class="banner-ticker-content">
                    <span>Stuck.</span><em>Guided.</em><span class="coral-word">Growing.</span><span>Confident.</span>&nbsp;&nbsp;✦&nbsp;&nbsp;
                    <span>Stuck.</span><em>Guided.</em><span class="coral-word">Growing.</span><span>Confident.</span>&nbsp;&nbsp;✦&nbsp;&nbsp;
                    <span>Stuck.</span><em>Guided.</em><span class="coral-word">Growing.</span><span>Confident.</span>&nbsp;&nbsp;✦&nbsp;&nbsp;
                    <span>Stuck.</span><em>Guided.</em><span class="coral-word">Growing.</span><span>Confident.</span>&nbsp;&nbsp;✦&nbsp;&nbsp;
                    <span>Stuck.</span><em>Guided.</em><span class="coral-word">Growing.</span><span>Confident.</span>&nbsp;&nbsp;✦&nbsp;&nbsp;
                    <span>Stuck.</span><em>Guided.</em><span class="coral-word">Growing.</span><span>Confident.</span>&nbsp;&nbsp;✦&nbsp;&nbsp;
                </div>
            </div>

            <!-- TWO-COLUMN MAIN BANNER STACK -->
            <div class="banner-main-grid">
                
                <!-- LEFT COLUMN: POWERFUL SALES COPY & VALUE PROPOSITION -->
                <div class="banner-sales-col">
                    
                    <div class="banner-trust-pills">
                        <div class="badge-live-pulse">
                            <span class="pulse-dot"></span>
                            <span>140+ Live Classes Today</span>
                        </div>
                        <div class="badge-stat-rating">
                            <span>★ 4.98 / 5.0</span>
                            <span style="font-weight:600; opacity:0.85;">(12,400+ Parents)</span>
                        </div>
                        <div class="badge-board-coverage">
                            <span>CBSE · ICSE · Classes 1–12</span>
                        </div>
                    </div>

                    <h2 class="banner-sales-headline">
                        Turn <span class="gold-hl">"I don't get it"</span> into<br>pure confidence in 1 class.
                    </h2>

                    <p class="banner-sales-subtext">
                        Why force your child through 60-minute recorded lectures when the breakthrough happens in 60 seconds? 
                        Paathshala matches them with a <strong>dedicated top 1.4% educator</strong> who teaches 1-on-1 at their exact speed, 
                        backed by <strong>instant video reels</strong> of key concepts and <strong>24/7 AI practice</strong>.
                    </p>

                    <!-- 4 SALES-DRIVEN TRANSFORMATION BENEFIT CARDS -->
                    <div class="banner-sales-cards-grid">
                        
                        <div class="sales-benefit-card">
                            <div class="sales-card-icon coral-bg">⚡</div>
                            <div class="sales-card-text">
                                <span class="sales-card-title">60-Sec "Aha!" Highlights</span>
                                <span class="sales-card-desc">AI automatically clips the exact moment the concept clicked for 1-minute exam revision.</span>
                            </div>
                        </div>

                        <div class="sales-benefit-card">
                            <div class="sales-card-icon">🧑‍🏫</div>
                            <div class="sales-card-text">
                                <span class="sales-card-title">Top 1.4% Private Mentor</span>
                                <span class="sales-card-desc">Only 1 in 70 teachers qualify. 100% personal focus — never moving on until they get it.</span>
                            </div>
                        </div>

                        <div class="sales-benefit-card">
                            <div class="sales-card-icon blue-bg">🤖</div>
                            <div class="sales-card-text">
                                <span class="sales-card-title">24/7 Mitra AI Doubt Solver</span>
                                <span class="sales-card-desc">Instant step-by-step doubt clearing and homework practice worksheets anytime.</span>
                            </div>
                        </div>

                        <div class="sales-benefit-card">
                            <div class="sales-card-icon green-bg">📈</div>
                            <div class="sales-card-text">
                                <span class="sales-card-title">Guaranteed Grade Jump</span>
                                <span class="sales-card-desc">Every whiteboard note and lesson saved forever. 94% of students report grade jumps in 6 weeks.</span>
                            </div>
                        </div>

                    </div>

                    <!-- DIRECT SALES CTA & ZERO-RISK REASSURANCE -->
                    <div class="banner-sales-cta-row">
                        <a href="https://paathshala.app/booking" target="_blank" class="btn-sales-primary">
                            <span>Claim Free 1-on-1 Class</span>
                            <span style="font-size:1.15rem;">➔</span>
                        </a>
                        <a href="/landing.html" class="btn-sales-secondary">
                            <span>See How It Works</span>
                            <span>⚡</span>
                        </a>
                    </div>

                    <div class="banner-reassurance-strip">
                        <span>🛡️ 100% Free 45-Min Trial</span>
                        <span>•</span>
                        <span>🚫 No Credit Card Needed</span>
                        <span>•</span>
                        <span>🎯 Math, Science, English, Coding</span>
                    </div>

                </div>

                <!-- RIGHT COLUMN: INTERACTIVE CLASSROOM BREAKTHROUGH HUD -->
                <div class="banner-showcase-col">
                    <div class="showcase-hud-card">
                        
                        <div class="hud-video-frame">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                            
                            <div class="hud-live-tag">
                                <span class="pulse-dot"></span>
                                <span>Real Class Highlight · 0:50</span>
                            </div>

                            <div class="hud-aha-pill">
                                <span>💡</span>
                                <span>Aha! Moment: "Nuclear glue holds protons together"</span>
                            </div>
                        </div>

                        <div class="hud-student-quote">
                            <span>💬</span>
                            <span>"Wait, so neutrons are the glue?! I finally get why they don't repel!" — Aarav, Class 9</span>
                        </div>

                        <div class="hud-tutor-meta">
                            <div class="hud-tutor-identity">
                                <div class="hud-tutor-photo">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div class="hud-tutor-text">
                                    <span class="hud-tutor-name">Leah Alexander</span>
                                    <span class="hud-tutor-qualification">Senior Physics Educator · 4.95 ★</span>
                                </div>
                            </div>
                            <span class="hud-verified-tag">✓ Top 1.4%</span>
                        </div>

                        <a href="https://paathshala.app/user-profile?publicId=alchemist-589748" target="_blank" style="text-decoration:none; font-size:0.82rem; font-weight:800; color:#4844E7; text-align:center; padding-top:4px; display:block;">
                            Meet Leah & Book Her Schedule ➔
                        </a>

                    </div>
                </div>

            </div>

        </div>
    </div>'''

# Replace banner HTML
markup_pattern = r'<div class="guided-learning-banner-wrapper" id="guidedLearningSection">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>'
html = re.sub(markup_pattern, salesy_banner_markup, html)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/homepage-section.html", "w") as f:
    f.write(html)

print("Salesy + Design-forward Homepage banner updated successfully!")
