import os

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala · Guided Learning Banner</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">

    <style>
        :root {
            --paathshala-purple: #5458F7;
            --paathshala-coral: #FF5A36;
            --paathshala-coral-hover: #E84622;
            --paathshala-yellow: #FFD25E;
            --paathshala-lime: #A3E635;
            --paathshala-cyan: #38BDF8;
            --paathshala-dark: #18181B;
            --bg-canvas: #F6F4F0;
            --card-cream: #FFFDF9;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            background-color: var(--bg-canvas);
            color: var(--paathshala-dark);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 30px 16px;
        }

        /* BANNER CONTAINER */
        .banner-container {
            width: 100%;
            max-width: 1220px;
            margin: 0 auto;
        }

        /* MAIN BANNER CARD - SIGNATURE PAATHSHALA NEO-BRUTALIST */
        .paathshala-banner {
            background-color: var(--card-cream);
            border: 2.5px solid var(--paathshala-dark);
            border-radius: 32px;
            box-shadow: 8px 8px 0px var(--paathshala-dark);
            padding: 44px 48px;
            position: relative;
            overflow: hidden;
        }

        /* DOTTED GRAPH MATRIX TEXTURE */
        .banner-dot-matrix {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(24, 24, 27, 0.08) 1.5px, transparent 1.5px);
            background-size: 20px 20px;
            pointer-events: none;
            z-index: 0;
        }

        /* 2-COLUMN GRID: LEFT FEATURES & CTA, RIGHT 9:16 VERTICAL REEL */
        .banner-layout {
            display: grid;
            grid-template-columns: 1.28fr auto;
            gap: 48px;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        /* LEFT SIDE: TYPOGRAPHY + VISUAL FEATURE CARDS */
        .banner-left {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        /* TOP EYEBROW STRIP */
        .banner-eyebrow {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .badge-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.78rem;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 999px;
            border: 1.5px solid var(--paathshala-dark);
            box-shadow: 2px 2px 0px var(--paathshala-dark);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .badge-pill.pulse {
            background: #D1FAE5;
            color: #065F46;
        }

        .badge-pill.yellow {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
        }

        .pulse-indicator {
            width: 7px;
            height: 7px;
            background: #10B981;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 6px #10B981;
        }

        /* HEADLINE IN OUR DESIGN STYLE WITH INTEGRATED PILLS */
        .banner-headline {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.3rem, 3.8vw, 3.4rem);
            font-weight: 900;
            line-height: 1.14;
            letter-spacing: -0.03em;
            color: var(--paathshala-dark);
        }

        .inline-pill {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 1px 14px;
            border-radius: 14px;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 2.5px 2.5px 0px var(--paathshala-dark);
            font-size: 0.82em;
            vertical-align: middle;
            transform: translateY(-2px);
        }

        .inline-pill.yellow { background: var(--paathshala-yellow); }
        .inline-pill.coral { background: var(--paathshala-coral); color: #FFFFFF; }
        .inline-pill.lime { background: var(--paathshala-lime); }

        /* =========================================================================
           VISUAL ILLUSTRATION FEATURE CARDS (NO TEXT WALLS)
           ========================================================================= */
        .feature-cards-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            margin-top: 4px;
        }

        .feature-card {
            background: #FFFFFF;
            border: 2px solid var(--paathshala-dark);
            border-radius: 18px;
            box-shadow: 3.5px 3.5px 0px var(--paathshala-dark);
            padding: 16px 14px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }

        .feature-card:hover {
            transform: translate(-2px, -2px);
            box-shadow: 5px 5px 0px var(--paathshala-dark);
        }

        /* CARD ILLUSTRATION CONTAINER */
        .card-illustration {
            width: 100%;
            height: 90px;
            border-radius: 12px;
            border: 1.5px solid var(--paathshala-dark);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        .card-illustration.purple-bg { background: #EEF2FF; }
        .card-illustration.yellow-bg { background: #FEF9C3; }
        .card-illustration.green-bg { background: #ECFDF5; }

        .card-illustration svg {
            width: 100%;
            height: 100%;
        }

        /* CARD TEXT BLOCK */
        .card-text {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .card-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            color: var(--paathshala-dark);
            line-height: 1.2;
        }

        .card-benefit-tag {
            font-size: 0.74rem;
            font-weight: 700;
            color: #4B5563;
            line-height: 1.3;
        }

        /* CALL TO ACTION ROW */
        .cta-action-row {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
            padding-top: 6px;
        }

        .btn-claim {
            background: var(--paathshala-coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.05rem;
            padding: 14px 28px;
            border-radius: 16px;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 4px 4px 0px var(--paathshala-dark);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease;
        }

        .btn-claim:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--paathshala-dark);
            background: var(--paathshala-coral-hover);
        }

        .btn-tour {
            background: #FFFFFF;
            color: var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 13px 22px;
            border-radius: 16px;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 3px 3px 0px var(--paathshala-dark);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s ease;
        }

        .btn-tour:hover {
            transform: translate(-1.5px, -1.5px);
            box-shadow: 4.5px 4.5px 0px var(--paathshala-dark);
            background: #F8FAFC;
        }

        .reassurance-strip {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 0.78rem;
            color: #64748B;
            font-weight: 700;
        }

        /* =========================================================================
           RIGHT COLUMN: REAL 9:16 VERTICAL REEL IN ITS EXACT PROPORTIONS
           ========================================================================= */
        .banner-right {
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        /* 9:16 EXACT SMARTPHONE REEL CARD */
        .vertical-reel-device {
            width: 278px;
            height: 494px; /* Exact 9:16 vertical smartphone format */
            background: #000000;
            border: 2.5px solid var(--paathshala-dark);
            border-radius: 28px;
            box-shadow: 8px 8px 0px var(--paathshala-dark);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
        }

        /* AUTOPLAYING 9:16 REEL VIDEO */
        .reel-video-container {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        .reel-video-container video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* TOP OVERLAY: LIVE CLASS BADGE & TIMECODE */
        .reel-top-overlay {
            position: absolute;
            top: 14px;
            left: 14px;
            right: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 3;
        }

        .reel-live-tag {
            background: rgba(24, 24, 27, 0.85);
            backdrop-filter: blur(8px);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .reel-duration-pill {
            background: rgba(24, 24, 27, 0.85);
            backdrop-filter: blur(8px);
            color: var(--paathshala-yellow);
            font-family: 'Outfit', sans-serif;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 4px 8px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* FLOATING "AHA!" MOMENT CALLOUT BADGE */
        .reel-aha-callout {
            position: absolute;
            bottom: 78px;
            left: 12px;
            right: 12px;
            background: rgba(254, 240, 138, 0.96);
            backdrop-filter: blur(8px);
            border: 1.5px solid var(--paathshala-dark);
            border-radius: 12px;
            padding: 8px 12px;
            font-size: 0.76rem;
            font-weight: 800;
            color: var(--paathshala-dark);
            display: flex;
            align-items: center;
            gap: 7px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            z-index: 3;
        }

        /* BOTTOM OVERLAY: EDUCATOR METADATA BAR */
        .reel-bottom-bar {
            position: absolute;
            bottom: 12px;
            left: 12px;
            right: 12px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 1.5px solid var(--paathshala-dark);
            border-radius: 14px;
            padding: 8px 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 3;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }

        .reel-tutor-info {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .reel-tutor-avatar {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            border: 1.5px solid var(--paathshala-dark);
            overflow: hidden;
            background: #FEF08A;
            flex-shrink: 0;
        }

        .reel-tutor-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .reel-tutor-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.8rem;
            color: var(--paathshala-dark);
            line-height: 1.1;
        }

        .reel-tutor-tag {
            font-size: 0.68rem;
            color: #64748B;
            font-weight: 600;
        }

        .reel-rating-badge {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.72rem;
            padding: 3px 6px;
            border-radius: 6px;
            border: 1px solid var(--paathshala-dark);
        }

        /* FLOATING TACTILE CORNER STICKER */
        .floating-reel-sticker {
            position: absolute;
            top: -14px;
            right: -10px;
            background: var(--paathshala-lime);
            color: var(--paathshala-dark);
            border: 2px solid var(--paathshala-dark);
            box-shadow: 3px 3px 0px var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 0.74rem;
            padding: 5px 10px;
            border-radius: 10px;
            transform: rotate(5deg);
            z-index: 5;
            pointer-events: none;
        }

        /* RESPONSIVE DESIGN */
        @media (max-width: 990px) {
            .banner-layout {
                grid-template-columns: 1fr;
            }
            .feature-cards-grid {
                grid-template-columns: 1fr;
            }
            .vertical-reel-device {
                margin: 0 auto;
            }
        }
    </style>
</head>
<body>

    <div class="banner-container">
        <div class="paathshala-banner">
            
            <div class="banner-dot-matrix"></div>

            <div class="banner-layout">
                
                <!-- LEFT SIDE: HEADLINE + VISUAL FEATURE CARDS (NO TEXT WALLS) -->
                <div class="banner-left">
                    
                    <div class="banner-eyebrow">
                        <div class="badge-pill pulse">
                            <span class="pulse-indicator"></span>
                            <span>Guided Learning</span>
                        </div>
                        <div class="badge-pill yellow">
                            <span>★ 4.98 Rating · 12,000+ Students</span>
                        </div>
                        <span style="font-size: 0.8rem; font-weight: 700; color: #64748B;">Classes 1 to 12 · CBSE & ICSE</span>
                    </div>

                    <!-- HERO HEADLINE -->
                    <h1 class="banner-headline">
                        Where <span class="inline-pill yellow">1-on-1 Mentors 🧑‍🏫</span><br>
                        &amp; <span class="inline-pill coral">60s Reels ⚡</span> make concepts<br>
                        finally <span class="inline-pill lime">CLICK 💡</span>
                    </h1>

                    <!-- 3 VISUAL ILLUSTRATION FEATURE CARDS (COMMUNICATES INSTANTLY VIA GRAPHICS) -->
                    <div class="feature-cards-grid">
                        
                        <!-- CARD 1: 1-ON-1 MENTORSHIP ILLUSTRATION -->
                        <div class="feature-card">
                            <div class="card-illustration purple-bg">
                                <svg viewBox="0 0 160 90" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <!-- Teacher avatar -->
                                    <circle cx="45" cy="40" r="18" fill="#5458F7" stroke="#18181B" stroke-width="2"/>
                                    <circle cx="45" cy="34" r="7" fill="#FEF08A"/>
                                    <path d="M33 54C33 47.3726 38.3726 42 45 42C51.6274 42 57 47.3726 57 54" stroke="#FEF08A" stroke-width="2"/>
                                    <text x="45" y="72" font-family="Outfit" font-size="8" font-weight="900" fill="#18181B" text-anchor="middle">TOP 1.4%</text>

                                    <!-- Connecting Learning Link with Live Sparkle -->
                                    <path d="M68 40H92" stroke="#18181B" stroke-width="2.5" stroke-dasharray="4 4"/>
                                    <circle cx="80" cy="40" r="9" fill="#FFD25E" stroke="#18181B" stroke-width="1.5"/>
                                    <text x="80" y="43" font-family="Outfit" font-size="9" font-weight="900" fill="#18181B" text-anchor="middle">1:1</text>

                                    <!-- Student avatar -->
                                    <circle cx="115" cy="40" r="18" fill="#FF5A36" stroke="#18181B" stroke-width="2"/>
                                    <circle cx="115" cy="34" r="7" fill="#FFFFFF"/>
                                    <path d="M103 54C103 47.3726 108.373 42 115 42C121.627 42 127 47.3726 127 54" stroke="#FFFFFF" stroke-width="2"/>
                                    <text x="115" y="72" font-family="Outfit" font-size="8" font-weight="900" fill="#18181B" text-anchor="middle">STUDENT</text>
                                </svg>
                            </div>
                            <div class="card-text">
                                <span class="card-title">1-on-1 Mentorship</span>
                                <span class="card-benefit-tag">Taught at your child's exact speed until it clicks.</span>
                            </div>
                        </div>

                        <!-- CARD 2: 60-SEC REEL CLIPPING ILLUSTRATION -->
                        <div class="feature-card">
                            <div class="card-illustration yellow-bg">
                                <svg viewBox="0 0 160 90" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <!-- Filmstrip Reel frame -->
                                    <rect x="35" y="15" width="90" height="58" rx="8" fill="#FFFFFF" stroke="#18181B" stroke-width="2"/>
                                    <line x1="35" y1="28" x2="125" y2="28" stroke="#18181B" stroke-width="1.5"/>
                                    <circle cx="43" cy="21" r="2.5" fill="#18181B"/>
                                    <circle cx="51" cy="21" r="2.5" fill="#18181B"/>
                                    <circle cx="59" cy="21" r="2.5" fill="#18181B"/>
                                    
                                    <!-- Glowing Lightbulb (Aha Moment) -->
                                    <circle cx="80" cy="46" r="12" fill="#FFE066" stroke="#18181B" stroke-width="2"/>
                                    <path d="M76 56H84" stroke="#18181B" stroke-width="2" stroke-linecap="round"/>
                                    <text x="80" y="50" font-family="Outfit" font-size="12" text-anchor="middle">💡</text>

                                    <!-- 60s Timer Badge -->
                                    <rect x="95" y="44" width="24" height="13" rx="4" fill="#FF5A36" stroke="#18181B" stroke-width="1.5"/>
                                    <text x="107" y="53" font-family="Outfit" font-size="8" font-weight="900" fill="#FFFFFF" text-anchor="middle">:60s</text>
                                </svg>
                            </div>
                            <div class="card-text">
                                <span class="card-title">60-Sec "Aha!" Reels</span>
                                <span class="card-benefit-tag">AI auto-clips breakthrough moments for instant exam recap.</span>
                            </div>
                        </div>

                        <!-- CARD 3: 24/7 MITRA AI DOUBT SOLVING ILLUSTRATION -->
                        <div class="feature-card">
                            <div class="card-illustration green-bg">
                                <svg viewBox="0 0 160 90" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <!-- Blackboard / Note Card -->
                                    <rect x="36" y="16" width="88" height="56" rx="8" fill="#18181B" stroke="#18181B" stroke-width="2"/>
                                    <!-- Math Step -->
                                    <text x="46" y="36" font-family="monospace" font-size="9" font-weight="700" fill="#E2E8F0">2x + 3 = 11</text>
                                    <text x="46" y="50" font-family="monospace" font-size="9" font-weight="800" fill="#A3E635">x = 4 ✓</text>
                                    
                                    <!-- Cute Mitra AI Bot Face Tag -->
                                    <rect x="88" y="32" width="28" height="24" rx="6" fill="#38BDF8" stroke="#18181B" stroke-width="1.5"/>
                                    <circle cx="96" cy="42" r="2" fill="#18181B"/>
                                    <circle cx="108" cy="42" r="2" fill="#18181B"/>
                                    <path d="M99 48C101 50 103 50 105 48" stroke="#18181B" stroke-width="1.5" stroke-linecap="round"/>
                                    <rect x="100" y="28" width="4" height="4" fill="#FFD25E"/>
                                </svg>
                            </div>
                            <div class="card-text">
                                <span class="card-title">24/7 Mitra AI Practice</span>
                                <span class="card-benefit-tag">Unlimited step-by-step doubt clearing & practice sheets.</span>
                            </div>
                        </div>

                    </div>

                    <!-- HIGH-CONVERTING SALES ACTION BUTTONS -->
                    <div class="cta-action-row">
                        <a href="https://paathshala.app/booking" target="_blank" class="btn-claim">
                            <span>Book Free 1-on-1 Class</span>
                            <span style="font-size:1.15rem;">➔</span>
                        </a>
                        <a href="/landing.html" class="btn-tour">
                            <span>See How It Works</span>
                            <span>⚡</span>
                        </a>
                    </div>

                    <div class="reassurance-strip">
                        <span>🛡️ 100% Free 45-Min Class</span>
                        <span>•</span>
                        <span>🚫 No Credit Card Needed</span>
                        <span>•</span>
                        <span>📈 94% Grade Boost</span>
                    </div>

                </div>

                <!-- RIGHT SIDE: REAL 9:16 VERTICAL REEL IN ITS EXACT PROPORTIONS -->
                <div class="banner-right">
                    
                    <div class="floating-reel-sticker">
                        <span>⚡ LIVE CLASS REEL</span>
                    </div>

                    <div class="vertical-reel-device">
                        
                        <!-- 9:16 AUTOPLAYING VIDEO -->
                        <div class="reel-video-container">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                        </div>

                        <!-- TOP STATUS BADGE -->
                        <div class="reel-top-overlay">
                            <div class="reel-live-tag">
                                <span class="pulse-indicator"></span>
                                <span>Real Class Breakthrough</span>
                            </div>
                            <div class="reel-duration-pill">0:50</div>
                        </div>

                        <!-- FLOATING "AHA!" MOMENT CALLOUT BADGE -->
                        <div class="reel-aha-callout">
                            <span>💡</span>
                            <span>"Wait, so neutrons are the glue?! Now I get it!"</span>
                        </div>

                        <!-- BOTTOM TEACHER CARD OVERLAY -->
                        <div class="reel-bottom-bar">
                            <div class="reel-tutor-info">
                                <div class="reel-tutor-avatar">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div>
                                    <div class="reel-tutor-name">Leah Alexander</div>
                                    <div class="reel-tutor-tag">Top 1.4% Physics Mentor</div>
                                </div>
                            </div>
                            <div class="reel-rating-badge">★ 4.95</div>
                        </div>

                    </div>

                </div>

            </div>

        </div>
    </div>

</body>
</html>
'''

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/homepage-section.html", "w") as f:
    f.write(html_code)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/banner.html", "w") as f:
    f.write(html_code)

print("Illustrated 9:16 Reel Banner created successfully!")
