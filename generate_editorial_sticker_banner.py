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
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,700;9..144,900&display=swap" rel="stylesheet">

    <style>
        :root {
            --paathshala-purple: #5458F7;
            --paathshala-purple-dark: #3E42D4;
            --paathshala-coral: #FF5A36;
            --paathshala-coral-hover: #E44723;
            --paathshala-yellow: #FFD25E;
            --paathshala-lime: #A3E635;
            --paathshala-pink: #F472B6;
            --paathshala-cyan: #38BDF8;
            --paathshala-dark: #18181B;
            --canvas-bg: #F5F3EF;
            --card-cream: #FFFDF9;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--canvas-bg);
            color: var(--paathshala-dark);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px 16px;
        }

        /* BANNER CONTAINER */
        .guided-banner-container {
            width: 100%;
            max-width: 1240px;
            margin: 0 auto;
        }

        /* MAIN BANNER CARD - WARM EDITORIAL NEO-BRUTALIST */
        .guided-banner {
            background-color: var(--card-cream);
            border: 3px solid var(--paathshala-dark);
            border-radius: 32px;
            box-shadow: 10px 10px 0px var(--paathshala-dark);
            position: relative;
            overflow: hidden;
            padding: 44px 50px 40px;
        }

        /* DOTTED GRAPH CANVAS TEXTURE */
        .banner-dots-texture {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(24, 24, 27, 0.08) 1.5px, transparent 1.5px);
            background-size: 22px 22px;
            pointer-events: none;
            z-index: 0;
        }

        /* ROTATING CIRCULAR STAMP BADGE (INSPIRED BY IMAGE 2) */
        .circular-stamp {
            position: absolute;
            top: 26px;
            right: 32px;
            width: 88px;
            height: 88px;
            z-index: 3;
            animation: rotate-stamp 20s linear infinite;
            pointer-events: none;
        }

        @keyframes rotate-stamp {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .stamp-center-icon {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 1.4rem;
        }

        /* TWO-COLUMN LAYOUT */
        .banner-grid {
            display: grid;
            grid-template-columns: 1.22fr 0.9fr;
            gap: 44px;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        /* LEFT CONTENT: HEADLINE WITH EMBEDDED COLOR PILLS (INSPIRED BY IMAGE 1) */
        .banner-content {
            display: flex;
            flex-direction: column;
            gap: 22px;
        }

        .category-pill-row {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .tag-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.8rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding: 5px 14px;
            border-radius: 999px;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 2px 2px 0px var(--paathshala-dark);
        }

        .tag-pill.live-pulse {
            background: #D1FAE5;
            color: #065F46;
        }

        .tag-pill.rating {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
        }

        .tag-pill.board {
            background: #FFFFFF;
            color: var(--paathshala-dark);
        }

        .pulse-circle {
            width: 8px;
            height: 8px;
            background: #10B981;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 6px #10B981;
            animation: pulse-ring 1.5s infinite;
        }

        @keyframes pulse-ring {
            0%, 100% { transform: scale(0.9); opacity: 0.8; }
            50% { transform: scale(1.3); opacity: 1; }
        }

        /* COMPOSITE HEADLINE WITH INTEGRATED COLORFUL PILLS (IMAGE 1 STYLE) */
        .headline-composite {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.3rem, 4.1vw, 3.7rem);
            font-weight: 900;
            line-height: 1.14;
            letter-spacing: -0.03em;
            color: var(--paathshala-dark);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .headline-row {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px 14px;
        }

        /* INLINE COLORFUL PILLS INSIDE HEADLINE */
        .inline-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 2px 16px;
            border-radius: 16px;
            border: 2.5px solid var(--paathshala-dark);
            box-shadow: 3.5px 3.5px 0px var(--paathshala-dark);
            font-size: 0.76em;
            font-weight: 900;
            vertical-align: middle;
            transform: translateY(-2px);
            white-space: nowrap;
        }

        .inline-pill.coral {
            background: var(--paathshala-coral);
            color: #FFFFFF;
            transform: translateY(-2px) rotate(-1.5deg);
        }

        .inline-pill.yellow {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
            transform: translateY(-2px) rotate(1.2deg);
        }

        .inline-pill.purple {
            background: var(--paathshala-purple);
            color: #FFFFFF;
            transform: translateY(-2px) rotate(-1deg);
        }

        .inline-pill.lime {
            background: var(--paathshala-lime);
            color: var(--paathshala-dark);
            transform: translateY(-2px) rotate(1.5deg);
        }

        /* PERSUASIVE VALUE PARAGRAPH */
        .banner-subtext {
            font-size: 1.05rem;
            line-height: 1.55;
            color: #4B5563;
            max-width: 580px;
        }

        .banner-subtext strong {
            color: var(--paathshala-dark);
            font-weight: 800;
        }

        /* WINDING PATH STRIP (INSPIRED BY IMAGE 2 - THE CURVED JOURNEY RIBBON) */
        .journey-ribbon-bar {
            background: #EEF2FF;
            border: 2px dashed #6366F1;
            border-radius: 16px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 0.85rem;
            font-weight: 700;
            color: #3730A3;
            overflow-x: auto;
        }

        .journey-step {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
        }

        .journey-step-badge {
            background: var(--paathshala-purple);
            color: #FFFFFF;
            font-size: 0.7rem;
            font-weight: 900;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }

        .journey-arrow {
            color: #818CF8;
            font-weight: 900;
        }

        /* 4 TRANSFORMATION VALUE TILES */
        .value-tiles-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        .value-tile {
            background: #FFFFFF;
            border: 2px solid var(--paathshala-dark);
            border-radius: 14px;
            padding: 10px 13px;
            box-shadow: 3px 3px 0px var(--paathshala-dark);
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.15s ease;
        }

        .value-tile:hover {
            transform: translate(-1.5px, -1.5px);
            box-shadow: 4.5px 4.5px 0px var(--paathshala-dark);
        }

        .tile-icon {
            font-size: 1.25rem;
            flex-shrink: 0;
            width: 34px;
            height: 34px;
            border-radius: 9px;
            border: 1.5px solid var(--paathshala-dark);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 1px 1px 0px var(--paathshala-dark);
        }

        .tile-icon.coral-bg { background: #FFE4E6; }
        .tile-icon.yellow-bg { background: #FEF3C7; }
        .tile-icon.lime-bg { background: #DCFCE7; }
        .tile-icon.purple-bg { background: #EDE9FE; }

        .tile-text {
            display: flex;
            flex-direction: column;
            gap: 1px;
        }

        .tile-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.88rem;
            color: var(--paathshala-dark);
            line-height: 1.2;
        }

        .tile-desc {
            font-size: 0.74rem;
            color: #64748B;
            font-weight: 600;
            line-height: 1.2;
        }

        /* SALES ACTION BUTTONS & RISK REVERSAL */
        .cta-action-row {
            display: flex;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 4px;
        }

        .btn-claim-free {
            background: var(--paathshala-coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.05rem;
            padding: 14px 28px;
            border-radius: 16px;
            border: 2.5px solid var(--paathshala-dark);
            box-shadow: 4px 4px 0px var(--paathshala-dark);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 9px;
            transition: all 0.15s ease;
        }

        .btn-claim-free:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--paathshala-dark);
            background: var(--paathshala-coral-hover);
        }

        .btn-watch-tour {
            background: #FFFFFF;
            color: var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 13px 22px;
            border-radius: 16px;
            border: 2.5px solid var(--paathshala-dark);
            box-shadow: 4px 4px 0px var(--paathshala-dark);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s ease;
        }

        .btn-watch-tour:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--paathshala-dark);
            background: #F8FAFC;
        }

        .reassurance-strip {
            display: flex;
            align-items: center;
            gap: 14px;
            font-size: 0.78rem;
            color: #6B7280;
            font-weight: 700;
        }

        .reassurance-strip span {
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        /* RIGHT SIDE: PLAYFUL STICKER PACK HUD (INSPIRED BY IMAGE 3) */
        .banner-visual {
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        /* FLOATING STICKERS POPPING AROUND THE DEVICE (IMAGE 3 STYLE) */
        .sticker {
            position: absolute;
            z-index: 5;
            border: 2.5px solid var(--paathshala-dark);
            box-shadow: 3.5px 3.5px 0px var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 12px;
            pointer-events: none;
            animation: float-sticker 3.5s ease-in-out infinite alternate;
        }

        @keyframes float-sticker {
            0% { transform: translateY(0) rotate(var(--rot, 0deg)); }
            100% { transform: translateY(-6px) rotate(var(--rot, 0deg)); }
        }

        /* TOP-LEFT STICKER: BLUE TICKET (IMAGE 3) */
        .sticker-ticket {
            top: -18px;
            left: -12px;
            background: var(--paathshala-cyan);
            color: var(--paathshala-dark);
            font-size: 0.8rem;
            --rot: -4deg;
        }

        /* TOP-RIGHT STICKER: GREEN GROWTH ARROW (IMAGE 3) */
        .sticker-arrow {
            top: -22px;
            right: 18px;
            background: var(--paathshala-lime);
            color: var(--paathshala-dark);
            font-size: 0.8rem;
            --rot: 5deg;
            animation-delay: 0.4s;
        }

        /* BOTTOM-RIGHT STICKER: CORAL LIGHTBULB (IMAGE 3) */
        .sticker-bulb {
            bottom: -16px;
            right: -10px;
            background: var(--paathshala-coral);
            color: #FFFFFF;
            font-size: 0.82rem;
            --rot: -3deg;
            animation-delay: 0.8s;
            box-shadow: 4px 4px 0px var(--paathshala-dark);
        }

        /* BOTTOM-LEFT STICKER: PINK WAVY/SCALLOPED BADGE (IMAGE 3) */
        .sticker-pink-badge {
            bottom: 22px;
            left: -20px;
            background: var(--paathshala-pink);
            color: var(--paathshala-dark);
            font-size: 0.78rem;
            border-radius: 999px;
            --rot: 6deg;
            animation-delay: 1.2s;
        }

        /* CENTRAL CLASSROOM HUD DEVICE CARD */
        .hud-card {
            background: #FFFFFF;
            border: 3px solid var(--paathshala-dark);
            border-radius: 24px;
            box-shadow: 8px 8px 0px var(--paathshala-dark);
            padding: 16px;
            width: 100%;
            max-width: 420px;
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .hud-video-box {
            width: 100%;
            height: 220px;
            border-radius: 16px;
            border: 2px solid var(--paathshala-dark);
            overflow: hidden;
            position: relative;
            background: #0F172A;
            box-shadow: 2px 2px 0px var(--paathshala-dark);
        }

        .hud-video-box video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .hud-live-tag {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(15, 23, 42, 0.88);
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

        .hud-aha-moment-pill {
            position: absolute;
            bottom: 10px;
            left: 10px;
            right: 10px;
            background: rgba(254, 240, 138, 0.96);
            backdrop-filter: blur(8px);
            border: 1.5px solid var(--paathshala-dark);
            border-radius: 10px;
            padding: 6px 10px;
            font-size: 0.76rem;
            font-weight: 800;
            color: var(--paathshala-dark);
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }

        .hud-student-feedback {
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
            line-height: 1.3;
        }

        .hud-mentor-strip {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            padding-top: 2px;
        }

        .hud-mentor-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .hud-mentor-avatar {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            border: 2px solid var(--paathshala-dark);
            overflow: hidden;
            flex-shrink: 0;
            background: #FEF08A;
        }

        .hud-mentor-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .hud-mentor-details {
            display: flex;
            flex-direction: column;
            gap: 1px;
        }

        .hud-mentor-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.94rem;
            color: var(--paathshala-dark);
        }

        .hud-mentor-role {
            font-size: 0.74rem;
            color: #64748B;
            font-weight: 600;
        }

        .hud-badge-verified {
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

        .hud-schedule-link {
            text-decoration: none;
            font-size: 0.82rem;
            font-weight: 800;
            color: var(--paathshala-purple);
            text-align: center;
            padding-top: 2px;
            display: block;
            transition: color 0.15s ease;
        }

        .hud-schedule-link:hover {
            color: var(--paathshala-purple-dark);
            text-decoration: underline;
        }

        /* RESPONSIVE DESIGN */
        @media (max-width: 980px) {
            .guided-banner {
                padding: 32px 24px;
            }
            .banner-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            .circular-stamp {
                display: none;
            }
            .headline-composite {
                font-size: 2.2rem;
            }
            .value-tiles-grid {
                grid-template-columns: 1fr;
            }
            .hud-card {
                max-width: 100%;
            }
        }
    </style>
</head>
<body>

    <!-- =========================================================================
         STANDALONE GUIDED LEARNING HOMEPAGE BANNER (INSPIRED BY USER IMAGES)
         ========================================================================= -->
    <div class="guided-banner-container">
        <div class="guided-banner">
            
            <!-- SUBTLE DOTS TEXTURE -->
            <div class="banner-dots-texture"></div>

            <!-- ROTATING CIRCULAR STAMP BADGE (IMAGE 2 STYLE) -->
            <div class="circular-stamp">
                <svg viewBox="0 0 100 100" width="100%" height="100%">
                    <path id="stampCurve" d="M 50, 50 m -37, 0 a 37,37 0 1,1 74,0 a 37,37 0 1,1 -74,0" fill="none"/>
                    <text font-family="Outfit" font-size="9.5" font-weight="900" fill="#18181B" letter-spacing="2">
                        <textPath href="#stampCurve" startOffset="0%">
                            ★ PAATHSHALA ★ GUIDED LEARNING ★
                        </textPath>
                    </text>
                </svg>
                <div class="stamp-center-icon">⚡</div>
            </div>

            <div class="banner-grid">
                
                <!-- LEFT CONTENT: COMPOSITE HEADLINE WITH INTEGRATED COLORFUL PILLS (IMAGE 1) -->
                <div class="banner-content">
                    
                    <!-- TOP TRUST TAGS -->
                    <div class="category-pill-row">
                        <div class="tag-pill live-pulse">
                            <span class="pulse-circle"></span>
                            <span>140+ Live Classes Today</span>
                        </div>
                        <div class="tag-pill rating">
                            <span>★ 4.98 / 5.0 (12,400+ Parents)</span>
                        </div>
                        <div class="tag-pill board">
                            <span>Classes 1–12 · CBSE & ICSE</span>
                        </div>
                    </div>

                    <!-- COMPOSITE HEADLINE WITH EMBEDDED COLORFUL PILLS (IMAGE 1 STYLE) -->
                    <h1 class="headline-composite">
                        <div class="headline-row">
                            <span>WHERE</span>
                            <span class="inline-pill coral">1-on-1 Tutors 🧑‍🏫</span>
                        </div>
                        <div class="headline-row">
                            <span class="inline-pill yellow">60s Reels ⚡</span>
                            <span>AND</span>
                            <span class="inline-pill purple">Mitra AI 🤖</span>
                        </div>
                        <div class="headline-row">
                            <span>MAKE LEARNING</span>
                            <span class="inline-pill lime">CLICK 💡</span>
                        </div>
                    </h1>

                    <!-- PERSUASIVE VALUE PARAGRAPH -->
                    <p class="banner-subtext">
                        Why force your child through boring 60-minute recorded lectures? 
                        Paathshala pairs them with a <strong>dedicated top 1.4% mentor</strong> at their exact pace, 
                        auto-clipped with <strong>60-second video highlights</strong> so concepts stick forever.
                    </p>

                    <!-- CURVED JOURNEY RIBBON (INSPIRED BY IMAGE 2) -->
                    <div class="journey-ribbon-bar">
                        <span style="font-weight:900; color:#18181B; margin-right:4px;">THE JOURNEY:</span>
                        <div class="journey-step">
                            <span class="journey-step-badge">1</span>
                            <span>Stuck on Concept</span>
                        </div>
                        <span class="journey-arrow">➔</span>
                        <div class="journey-step">
                            <span class="journey-step-badge">2</span>
                            <span>1-on-1 Breakthrough</span>
                        </div>
                        <span class="journey-arrow">➔</span>
                        <div class="journey-step">
                            <span class="journey-step-badge">3</span>
                            <span>60s Reel Saved</span>
                        </div>
                        <span class="journey-arrow">➔</span>
                        <div class="journey-step">
                            <span class="journey-step-badge">4</span>
                            <span style="color:#059669; font-weight:800;">100% Confident ✓</span>
                        </div>
                    </div>

                    <!-- 4 TRANSFORMATION VALUE TILES -->
                    <div class="value-tiles-grid">
                        <div class="value-tile">
                            <div class="tile-icon coral-bg">⚡</div>
                            <div class="tile-text">
                                <span class="tile-title">60-Sec "Aha!" Reels</span>
                                <span class="tile-desc">AI clips breakthrough seconds for fast exam recap.</span>
                            </div>
                        </div>

                        <div class="value-tile">
                            <div class="tile-icon yellow-bg">🧑‍🏫</div>
                            <div class="tile-text">
                                <span class="tile-title">Top 1.4% Private Tutor</span>
                                <span class="tile-desc">100% personal focus at your child's speed.</span>
                            </div>
                        </div>

                        <div class="value-tile">
                            <div class="tile-icon lime-bg">🤖</div>
                            <div class="tile-text">
                                <span class="tile-title">24/7 Mitra AI Practice</span>
                                <span class="tile-desc">Instant doubt solving & homework worksheets.</span>
                            </div>
                        </div>

                        <div class="value-tile">
                            <div class="tile-icon purple-bg">📈</div>
                            <div class="tile-text">
                                <span class="tile-title">Guaranteed Grade Boost</span>
                                <span class="tile-desc">94% report grade jumps within 6 weeks.</span>
                            </div>
                        </div>
                    </div>

                    <!-- HIGH-CONVERTING SALES CTA ROW -->
                    <div class="cta-action-row">
                        <a href="https://paathshala.app/booking" target="_blank" class="btn-claim-free">
                            <span>Claim Free 1-on-1 Class</span>
                            <span style="font-size:1.15rem;">➔</span>
                        </a>
                        <a href="/landing.html" class="btn-watch-tour">
                            <span>See How It Works</span>
                            <span>⚡</span>
                        </a>
                    </div>

                    <!-- RISK-FREE REASSURANCE -->
                    <div class="reassurance-strip">
                        <span>🛡️ 100% Free 45-Min Trial</span>
                        <span>•</span>
                        <span>🚫 No Credit Card Needed</span>
                        <span>•</span>
                        <span>🎯 Math, Science, Coding</span>
                    </div>

                </div>

                <!-- RIGHT SIDE: PLAYFUL STICKER PACK HUD (INSPIRED BY IMAGE 3) -->
                <div class="banner-visual">
                    
                    <!-- POPPING GRAPHIC STICKERS (IMAGE 3 STYLE) -->
                    <div class="sticker sticker-ticket">
                        <span>✦ WELCOME TO GUIDED LEARNING ✦</span>
                    </div>

                    <div class="sticker sticker-arrow">
                        <span>↗ +28% MARKS BOOST</span>
                    </div>

                    <div class="sticker sticker-pink-badge">
                        <span>YOU GOT THIS! 🌸</span>
                    </div>

                    <div class="sticker sticker-bulb">
                        <span>💡 "AHA!" MOMENT</span>
                    </div>

                    <!-- CENTRAL CLASSROOM HUD DEVICE CARD -->
                    <div class="hud-card">
                        
                        <div class="hud-video-box">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>
                            
                            <div class="hud-live-tag">
                                <span class="pulse-circle"></span>
                                <span>Real Class Highlight · 0:50</span>
                            </div>

                            <div class="hud-aha-moment-pill">
                                <span>💡</span>
                                <span>Concept Click: "Nuclear glue holds protons together"</span>
                            </div>
                        </div>

                        <div class="hud-student-feedback">
                            <span>💬</span>
                            <span>"Wait, so neutrons are the glue?! I finally get why they don't repel!" — Aarav, Class 9</span>
                        </div>

                        <div class="hud-mentor-strip">
                            <div class="hud-mentor-info">
                                <div class="hud-mentor-avatar">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div class="hud-mentor-details">
                                    <span class="hud-mentor-name">Leah Alexander</span>
                                    <span class="hud-mentor-role">Senior Physics Mentor · 4.95 ★</span>
                                </div>
                            </div>
                            <span class="hud-badge-verified">✓ Top 1.4%</span>
                        </div>

                        <a href="https://paathshala.app/user-profile?publicId=alchemist-589748" target="_blank" class="hud-schedule-link">
                            Meet Leah & Book Her Schedule ➔
                        </a>

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

print("Editorial Sticker Banner created successfully!")
