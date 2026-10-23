import os

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala · Guided Learning Banner</title>
    
    <!-- Google Fonts: Plus Jakarta Sans & Outfit -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@700&display=swap" rel="stylesheet">

    <style>
        :root {
            --primary: #4F46E5;
            --primary-light: #EEF2FF;
            --coral: #FF5A36;
            --coral-hover: #E84622;
            --dark: #0F172A;
            --slate-900: #0F172A;
            --slate-800: #1E293B;
            --slate-600: #475569;
            --slate-500: #64748B;
            --slate-200: #E2E8F0;
            --slate-100: #F1F5F9;
            --slate-50: #F8FAFC;
            --surface: #FFFFFF;
            --border-color: #E2E8F0;
            --radius-card: 20px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
        }

        body {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            background-color: #F8FAFC;
            color: var(--slate-900);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
        }

        /* BANNER WRAPPER */
        .banner-container {
            width: 100%;
            max-width: 1220px;
            margin: 0 auto;
        }

        /* MAIN BANNER WRAPPER: CLEAN SURFACE, SIMPLE BORDER, NATURAL SUBTLE SHADOW */
        .bento-shell {
            background: #FFFFFF;
            border: 1px solid var(--border-color);
            border-radius: 28px;
            padding: 44px;
            box-shadow: 0 4px 25px -4px rgba(15, 23, 42, 0.04), 0 20px 40px -12px rgba(15, 23, 42, 0.06);
            position: relative;
        }

        /* BENTO GRID: 2 MAIN COLUMNS (LEFT CONTENT 1.4fr, RIGHT REEL 0.85fr) */
        .bento-grid {
            display: grid;
            grid-template-columns: 1.4fr 0.85fr;
            gap: 24px;
            align-items: stretch;
        }

        /* LEFT BENTO CLUSTER */
        .bento-left {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        /* TOP HERO TILE (ZERO SUBHEADING!) */
        .hero-headline-card {
            background: var(--slate-50);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-card);
            padding: 34px 36px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 24px;
        }

        /* CLEAN EYEBROW */
        .eyebrow-row {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .eyebrow-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #FFFFFF;
            border: 1px solid var(--border-color);
            padding: 5px 12px;
            border-radius: 9999px;
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 0.2px;
        }

        .live-dot {
            width: 7px;
            height: 7px;
            background: #10B981;
            border-radius: 50%;
        }

        .eyebrow-meta {
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--slate-500);
        }

        /* REFINED HEADLINE (NO COLORED BACKGROUND PILLS!) */
        .hero-title {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.3rem, 3.8vw, 3.3rem);
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -0.03em;
            color: var(--slate-900);
        }

        /* TEXT COLOR HIGHLIGHTS (PURE COLOR, ZERO BACKGROUND FILL) */
        .highlight-tutor {
            color: var(--primary);
        }

        .highlight-reel {
            color: var(--coral);
        }

        .highlight-click {
            color: #059669;
        }

        /* ACTION CTA ROW */
        .cta-action-row {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        .btn-primary-cta {
            background: var(--coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1rem;
            padding: 13px 26px;
            border-radius: 12px;
            border: 1px solid transparent;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 14px rgba(255, 90, 54, 0.25);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .btn-primary-cta:hover {
            background: var(--coral-hover);
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(255, 90, 54, 0.32);
        }

        .btn-secondary-cta {
            background: #FFFFFF;
            color: var(--slate-800);
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 0.95rem;
            padding: 13px 22px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s ease;
        }

        .btn-secondary-cta:hover {
            background: var(--slate-100);
            border-color: #CBD5E1;
        }

        .trial-notice {
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--slate-500);
        }

        /* LOWER BENTO TILES (2-COLUMN GRID) */
        .bento-subgrid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        /* INDIVIDUAL BENTO TILES: SIMPLE BORDERS, CLEAN PADDING */
        .bento-card {
            background: #FFFFFF;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-card);
            padding: 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 14px;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .bento-card:hover {
            border-color: #CBD5E1;
            box-shadow: 0 6px 20px -4px rgba(15, 23, 42, 0.05);
        }

        .card-top-tag {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--slate-500);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .tag-pill {
            background: var(--slate-100);
            padding: 3px 8px;
            border-radius: 6px;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            color: var(--slate-600);
        }

        .card-heading {
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--slate-900);
            line-height: 1.25;
        }

        .card-desc {
            font-size: 0.85rem;
            color: var(--slate-600);
            line-height: 1.45;
        }

        /* STAT CARD NUMBER */
        .stat-figure {
            font-family: 'Outfit', sans-serif;
            font-size: 2.8rem;
            font-weight: 800;
            line-height: 1;
            color: var(--primary);
            letter-spacing: -0.03em;
        }

        /* MITRA FORMULA PREVIEW */
        .math-code-box {
            background: var(--slate-50);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 8px 12px;
            font-family: 'Space Mono', monospace;
            font-size: 0.8rem;
            color: var(--slate-800);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .math-check {
            color: #059669;
            font-weight: 700;
        }

        /* PARENT PROOF STARS */
        .stars-row {
            color: #F59E0B;
            font-size: 0.95rem;
            letter-spacing: 2px;
        }

        /* RIGHT REEL COLUMN: TRUE 9:16 VERTICAL PROPORTIONS, SIMPLE BORDER */
        .bento-reel-card {
            background: #000000;
            border: 1px solid var(--border-color);
            border-radius: 24px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 520px;
            box-shadow: 0 8px 30px -6px rgba(15, 23, 42, 0.1);
        }

        .bento-reel-card video {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* REEL TOP HUD */
        .reel-hud-top {
            position: relative;
            z-index: 2;
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .reel-status-tag {
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #FFFFFF;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 9999px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .reel-timecode {
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #FDE047;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 6px;
        }

        /* REEL BOTTOM HUD */
        .reel-hud-bottom {
            position: relative;
            z-index: 2;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .reel-caption-pill {
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(8px);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 10px 14px;
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--slate-900);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        }

        .reel-educator-strip {
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 8px 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: #FFFFFF;
        }

        .educator-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .educator-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            overflow: hidden;
            border: 1.5px solid rgba(255, 255, 255, 0.3);
            background: #1E293B;
        }

        .educator-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .educator-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 0.85rem;
            line-height: 1.1;
        }

        .educator-sub {
            font-size: 0.7rem;
            color: #94A3B8;
        }

        .educator-rating {
            font-size: 0.75rem;
            font-weight: 700;
            color: #FDE047;
        }

        /* RESPONSIVE DESIGN */
        @media (max-width: 1024px) {
            .bento-shell {
                padding: 30px;
            }
            .bento-grid {
                grid-template-columns: 1fr;
            }
            .bento-reel-card {
                max-width: 340px;
                margin: 0 auto;
                aspect-ratio: 9 / 16;
                min-height: 480px;
            }
        }

        @media (max-width: 640px) {
            .bento-subgrid {
                grid-template-columns: 1fr;
            }
            .hero-headline-card {
                padding: 24px 20px;
            }
            .hero-title {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>

    <div class="banner-container">
        <div class="bento-shell">
            
            <div class="bento-grid">
                
                <!-- LEFT BENTO CLUSTER -->
                <div class="bento-left">
                    
                    <!-- HERO HEADLINE CARD (ZERO SUBHEADING & NO COLORED BACKGROUND PILLS) -->
                    <div class="hero-headline-card">
                        
                        <div class="eyebrow-row">
                            <div class="eyebrow-badge">
                                <span class="live-dot"></span>
                                <span>Guided Learning</span>
                            </div>
                            <span class="eyebrow-meta">Classes 1–12 · CBSE &amp; ICSE</span>
                            <span class="eyebrow-meta">★ 4.98 from 12,000+ Parents</span>
                        </div>

                        <!-- CLEAN EDITORIAL HEADLINE WITH PURE COLOR HIGHLIGHTS (ZERO BACKGROUND PILLS) -->
                        <h1 class="hero-title">
                            Where <span class="highlight-tutor">1-on-1 Tutors</span> &amp; 
                            <span class="highlight-reel">60s Reels</span> Turn Confusion 
                            Into <span class="highlight-click">Pure Confidence</span>.
                        </h1>

                        <!-- DIRECT CONVERSION ACTIONS -->
                        <div class="cta-action-row">
                            <a href="https://paathshala.app/booking" target="_blank" class="btn-primary-cta">
                                <span>Book Free 1-on-1 Class</span>
                                <span>➔</span>
                            </a>
                            <a href="/landing.html" class="btn-secondary-cta">
                                <span>See How It Works</span>
                            </a>
                            <span class="trial-notice">100% Free · No Card Needed</span>
                        </div>

                    </div>

                    <!-- 2x2 MODULAR BENTO TILES (SIMPLE BORDERS, NO SOLID SHADOWS) -->
                    <div class="bento-subgrid">
                        
                        <!-- TILE 1: 60s REELS -->
                        <div class="bento-card">
                            <div class="card-top-tag">
                                <span>Revision Engine</span>
                                <span class="tag-pill">60s</span>
                            </div>
                            <div>
                                <h3 class="card-heading">AI Breakthrough Reels</h3>
                                <p class="card-desc">Auto-clipped the instant understanding happens for 1-minute exam revision.</p>
                            </div>
                        </div>

                        <!-- TILE 2: GRADE SURGE STAT -->
                        <div class="bento-card">
                            <div class="card-top-tag">
                                <span>Documented Results</span>
                                <span class="tag-pill">+29%</span>
                            </div>
                            <div>
                                <div class="stat-figure">+29%</div>
                                <h3 class="card-heading" style="font-size:1rem; margin-top:4px;">Average Marks Surge</h3>
                                <p class="card-desc">Measured across 12,000+ students within their first 6 weeks.</p>
                            </div>
                        </div>

                        <!-- TILE 3: 24/7 MITRA AI -->
                        <div class="bento-card">
                            <div class="card-top-tag">
                                <span>Midnight Practice</span>
                                <span class="tag-pill">24/7</span>
                            </div>
                            <div>
                                <div class="math-code-box">
                                    <span>2x + 3 = 11</span>
                                    <span class="math-check">x = 4 ✓</span>
                                </div>
                                <h3 class="card-heading" style="margin-top:8px;">Mitra AI Doubt Solver</h3>
                                <p class="card-desc">Instant step-by-step logic and tailored problem sets anytime.</p>
                            </div>
                        </div>

                        <!-- TILE 4: REAL VERDICT -->
                        <div class="bento-card">
                            <div class="card-top-tag">
                                <span>Verified Review</span>
                                <div class="stars-row">★★★★★</div>
                            </div>
                            <div>
                                <h3 class="card-heading" style="font-size:1.02rem;">"62% to 91% in Physics."</h3>
                                <p class="card-desc">Rewatching the 60s class reels before exam day changed everything.</p>
                                <span style="font-size:0.75rem; font-weight:700; color:var(--slate-500); margin-top:6px; display:block;">— Priya S., Grade 10 Parent</span>
                            </div>
                        </div>

                    </div>

                </div>

                <!-- RIGHT BENTO COLUMN: EXACT 9:16 VERTICAL REEL (SIMPLE BORDER, NATURAL SHADOW) -->
                <div class="bento-reel-card">
                    
                    <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                        <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                    </video>

                    <div class="reel-hud-top">
                        <div class="reel-status-tag">
                            <span class="live-dot"></span>
                            <span>Live Breakthrough</span>
                        </div>
                        <div class="reel-timecode">0:50</div>
                    </div>

                    <div class="reel-hud-bottom">
                        <div class="reel-caption-pill">
                            💡 "Wait, so neutrons are the glue?! Now I get it!"
                        </div>

                        <div class="reel-educator-strip">
                            <div class="educator-info">
                                <div class="educator-avatar">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div>
                                    <div class="educator-name">Leah Alexander</div>
                                    <div class="educator-sub">Physics Mentor · SafeTutor</div>
                                </div>
                            </div>
                            <span class="educator-rating">★ 4.95</span>
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

print("Refined Bento banner created successfully!")
