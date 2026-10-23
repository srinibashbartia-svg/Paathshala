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
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --ink: #141416;
            --ink-muted: #52525B;
            --canvas: #F4EFEB;
            --card-bg: #FFFFFF;
            --coral: #FF5A36;
            --coral-hover: #E84622;
            --yellow: #FFE169;
            --lime: #C4F135;
            --purple: #5E58F7;
            --border-width: 2.5px;
            --shadow: 6px 6px 0px var(--ink);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            background-color: var(--canvas);
            color: var(--ink);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 24px;
        }

        /* BANNER CONTAINER */
        .banner-shell {
            width: 100%;
            max-width: 1180px;
            margin: 0 auto;
        }

        /* HERO BANNER CARD - WARM, EDITORIAL & SPACIOUS */
        .banner-card {
            background-color: var(--card-bg);
            border: var(--border-width) solid var(--ink);
            border-radius: 32px;
            box-shadow: 8px 8px 0px var(--ink);
            padding: 56px 60px;
            position: relative;
            overflow: hidden;
        }

        /* 2-COLUMN GRID WITH GENEROUS BREATHING ROOM */
        .banner-grid {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 56px;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        /* LEFT EDITORIAL COLUMN */
        .banner-editorial {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        /* CLEAN EYEBROW */
        .eyebrow-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .eyebrow-tag {
            font-family: 'Outfit', sans-serif;
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            padding: 4px 12px;
            border-radius: 999px;
            background: #F4F4F5;
            border: 1.5px solid var(--ink);
            color: var(--ink);
        }

        .live-dot {
            width: 7px;
            height: 7px;
            background: #10B981;
            border-radius: 50%;
            display: inline-block;
            margin-right: 4px;
        }

        /* HIGH-CRAFT TYPOGRAPHY WITH INTEGRATED PILLS (INSPIRED BY IMAGE 1) */
        .hero-title {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.4rem, 4.2vw, 3.6rem);
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -0.03em;
            color: var(--ink);
        }

        .title-line {
            display: block;
        }

        .pill-badge {
            display: inline-flex;
            align-items: center;
            padding: 2px 14px;
            border-radius: 14px;
            border: 2px solid var(--ink);
            box-shadow: 2.5px 2.5px 0px var(--ink);
            font-size: 0.8em;
            font-weight: 800;
            vertical-align: middle;
            margin: 0 4px;
            transform: translateY(-2px);
        }

        .pill-badge.yellow {
            background: var(--yellow);
            color: var(--ink);
        }

        .pill-badge.coral {
            background: var(--coral);
            color: #FFFFFF;
        }

        .pill-badge.lime {
            background: var(--lime);
            color: var(--ink);
        }

        /* SINGLE HONEST EDITORIAL PARAGRAPH */
        .hero-description {
            font-size: 1.05rem;
            line-height: 1.6;
            color: var(--ink-muted);
            max-width: 520px;
        }

        .hero-description strong {
            color: var(--ink);
            font-weight: 700;
        }

        /* ACTION BUTTONS & TRUST MARK */
        .action-row {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
            padding-top: 6px;
        }

        .btn-primary {
            background: var(--coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            padding: 15px 30px;
            border-radius: 16px;
            border: 2px solid var(--ink);
            box-shadow: 4px 4px 0px var(--ink);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease;
        }

        .btn-primary:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--ink);
            background: var(--coral-hover);
        }

        .btn-secondary {
            background: transparent;
            color: var(--ink);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.98rem;
            padding: 14px 22px;
            border-radius: 16px;
            border: 2px solid var(--ink);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s ease;
        }

        .btn-secondary:hover {
            background: #F4F4F5;
            box-shadow: 3px 3px 0px var(--ink);
            transform: translate(-1px, -1px);
        }

        .trust-line {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            color: #71717A;
            font-weight: 600;
        }

        .trust-line .stars {
            color: #F59E0B;
        }

        /* RIGHT VISUAL COLUMN: CLEAN TACTILE DEVICE SHOWCASE (INSPIRED BY IMAGE 3) */
        .banner-visual {
            position: relative;
            display: flex;
            justify-content: center;
        }

        /* MINIMALIST TACTILE STICKER (ONLY 2 CLEAN ONES, NOT A MESS) */
        .tactile-sticker {
            position: absolute;
            top: -16px;
            right: 0px;
            background: var(--yellow);
            color: var(--ink);
            border: 2px solid var(--ink);
            box-shadow: 3px 3px 0px var(--ink);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.78rem;
            padding: 6px 12px;
            border-radius: 10px;
            transform: rotate(4deg);
            z-index: 4;
            pointer-events: none;
        }

        .corner-pill {
            position: absolute;
            bottom: -12px;
            left: 8px;
            background: var(--lime);
            color: var(--ink);
            border: 2px solid var(--ink);
            box-shadow: 3px 3px 0px var(--ink);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.76rem;
            padding: 5px 12px;
            border-radius: 999px;
            transform: rotate(-3deg);
            z-index: 4;
            pointer-events: none;
        }

        /* CENTRAL CLASSROOM CARD */
        .classroom-card {
            background: #FFFFFF;
            border: var(--border-width) solid var(--ink);
            border-radius: 24px;
            box-shadow: 6px 6px 0px var(--ink);
            overflow: hidden;
            width: 100%;
            max-width: 400px;
            position: relative;
            z-index: 2;
        }

        .video-viewport {
            width: 100%;
            height: 240px;
            background: #18181B;
            position: relative;
            overflow: hidden;
        }

        .video-viewport video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .video-status-tag {
            position: absolute;
            top: 12px;
            left: 12px;
            background: rgba(20, 20, 22, 0.85);
            backdrop-filter: blur(8px);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .video-caption-bar {
            position: absolute;
            bottom: 12px;
            left: 12px;
            right: 12px;
            background: rgba(255, 255, 255, 0.95);
            border: 1.5px solid var(--ink);
            border-radius: 10px;
            padding: 8px 12px;
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--ink);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        }

        /* MENTOR FOOTER STRIP */
        .mentor-footer {
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #FAF8F5;
            border-top: 2px solid var(--ink);
        }

        .mentor-profile {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .mentor-thumb {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            border: 1.5px solid var(--ink);
            overflow: hidden;
            background: #FEF08A;
            flex-shrink: 0;
        }

        .mentor-thumb img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .mentor-meta {
            display: flex;
            flex-direction: column;
            gap: 1px;
        }

        .mentor-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.9rem;
            color: var(--ink);
        }

        .mentor-title {
            font-size: 0.75rem;
            color: var(--ink-muted);
        }

        .mentor-rating {
            font-family: 'Outfit', sans-serif;
            font-size: 0.78rem;
            font-weight: 800;
            background: #FFFFFF;
            border: 1.5px solid var(--ink);
            padding: 3px 8px;
            border-radius: 8px;
        }

        /* RESPONSIVE */
        @media (max-width: 960px) {
            .banner-card {
                padding: 40px 28px;
            }
            .banner-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            .hero-title {
                font-size: 2.3rem;
            }
            .classroom-card {
                max-width: 100%;
            }
        }
    </style>
</head>
<body>

    <!-- =========================================================================
         SIMPLIFIED, HUMAN-CRAFTED GUIDED LEARNING HOMEPAGE BANNER
         ========================================================================= -->
    <div class="banner-shell">
        <div class="banner-card">
            
            <div class="banner-grid">
                
                <!-- LEFT EDITORIAL COLUMN -->
                <div class="banner-editorial">
                    
                    <div class="eyebrow-row">
                        <span class="eyebrow-tag"><span class="live-dot"></span>Guided Learning</span>
                        <span style="font-size: 0.8rem; font-weight: 700; color: #71717A;">Classes 1–12 · CBSE & ICSE</span>
                    </div>

                    <!-- HERO HEADLINE (TASTEFUL PILLS INSPIRED BY IMAGE 1) -->
                    <h1 class="hero-title">
                        <span class="title-line">Where <span class="pill-badge yellow">1-on-1 Tutors</span></span>
                        <span class="title-line">&amp; <span class="pill-badge coral">60s Reels ⚡</span></span>
                        <span class="title-line">make concepts <span class="pill-badge lime">click 💡</span></span>
                    </h1>

                    <!-- CONCISE, HONEST DESCRIPTION -->
                    <p class="hero-description">
                        No boring 60-minute recorded lectures. Your child gets matched with a <strong>dedicated top 1.4% mentor</strong> at their own pace — with every breakthrough moment <strong>auto-clipped into a 60-second recap</strong> so they never forget.
                    </p>

                    <!-- DIRECT ACTIONS -->
                    <div class="action-row">
                        <a href="https://paathshala.app/booking" target="_blank" class="btn-primary">
                            <span>Book Free Trial Class</span>
                            <span>➔</span>
                        </a>
                        <a href="/landing.html" class="btn-secondary">
                            <span>See How It Works</span>
                        </a>
                    </div>

                    <!-- SUBTLE SOCIAL PROOF -->
                    <div class="trust-line">
                        <span class="stars">★★★★★</span>
                        <span><strong>4.98 / 5.0</strong> from 12,000+ parents · 100% Free Trial (₹0)</span>
                    </div>

                </div>

                <!-- RIGHT SHOWCASE COLUMN (CLEAN, TACTILE & HUMAN) -->
                <div class="banner-visual">
                    
                    <!-- TWO TASTEFUL TACTILE STICKERS -->
                    <div class="tactile-sticker">
                        <span>⚡ 60-SEC BREAKTHROUGH</span>
                    </div>

                    <div class="corner-pill">
                        <span>✓ TOP 1.4% MENTOR</span>
                    </div>

                    <!-- CLEAN VIDEO HUD CARD -->
                    <div class="classroom-card">
                        
                        <div class="video-viewport">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>

                            <div class="video-status-tag">
                                <span class="live-dot"></span>
                                <span>Class Highlight · 0:50</span>
                            </div>

                            <div class="video-caption-bar">
                                💡 "Wait, so neutrons are the glue?! Now I get it!"
                            </div>
                        </div>

                        <div class="mentor-footer">
                            <div class="mentor-profile">
                                <div class="mentor-thumb">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div class="mentor-meta">
                                    <span class="mentor-name">Leah Alexander</span>
                                    <span class="mentor-title">Physics Educator · SafeTutor Certified</span>
                                </div>
                            </div>
                            <span class="mentor-rating">★ 4.95</span>
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

print("Simplified, human-designed banner created successfully!")
