import os

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala · Avant-Garde Bento Guided Learning Banner</title>
    
    <!-- Google Fonts: Outfit (Avant-garde geometric display) & Space Mono / Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@600;700;800&family=Space+Mono:wght@700&display=swap" rel="stylesheet">

    <style>
        :root {
            --p-purple: #5458F7;
            --p-purple-light: #EEF0FF;
            --p-coral: #FF5A36;
            --p-coral-hover: #E84622;
            --p-yellow: #FFD25E;
            --p-lime: #A3E635;
            --p-cyan: #38BDF8;
            --p-ink: #141416;
            --bg-canvas: #F4EFEB;
            --card-cream: #FFFDF9;
            --border-thick: 2.5px solid var(--p-ink);
            --shadow-hard: 6px 6px 0px var(--p-ink);
            --shadow-hero: 9px 9px 0px var(--p-ink);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            background-color: var(--bg-canvas);
            color: var(--p-ink);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 36px 16px;
        }

        /* BANNER CONTAINER */
        .bento-shell {
            width: 100%;
            max-width: 1240px;
            margin: 0 auto;
        }

        /* AVANT-GARDE BENTO GRID LAYOUT */
        .bento-grid {
            display: grid;
            grid-template-columns: 1.45fr 0.85fr;
            gap: 20px;
            align-items: stretch;
        }

        /* LEFT BENTO SUB-GRID (4 ASYMMETRIC TILES) */
        .bento-left-cluster {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        /* COMMON AVANT-GARDE TILE ATTRIBUTES */
        .bento-tile {
            background: var(--card-cream);
            border: var(--border-thick);
            border-radius: 26px;
            box-shadow: var(--shadow-hard);
            padding: 24px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease;
        }

        .bento-tile:hover {
            transform: translate(-3px, -3px);
            box-shadow: 9px 9px 0px var(--p-ink);
        }

        /* AVANT-GARDE INDEX NOTATION (e.g., [ 01 ], [ 02 ]) */
        .tile-meta-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.8px;
            color: #52525B;
        }

        .index-pill {
            background: #FFFFFF;
            border: 1.5px solid var(--p-ink);
            padding: 2px 8px;
            border-radius: 6px;
            box-shadow: 1.5px 1.5px 0px var(--p-ink);
        }

        /* =========================================================================
           TILE 1: MAIN AVANT-GARDE HERO HEADLINE & CTA (NO SUBHEADING!)
           ========================================================================= */
        .tile-hero-headline {
            grid-column: span 2;
            background: #FFFFFF;
            padding: 34px 36px;
            min-height: 250px;
            justify-content: space-between;
        }

        .hero-top-strip {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .category-tag {
            background: var(--p-yellow);
            color: var(--p-ink);
            font-family: 'Space Mono', monospace;
            font-size: 0.74rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 999px;
            border: 1.5px solid var(--p-ink);
            box-shadow: 2px 2px 0px var(--p-ink);
            text-transform: uppercase;
        }

        .live-tag {
            background: #DCFCE7;
            color: #166534;
            font-family: 'Space Mono', monospace;
            font-size: 0.74rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 999px;
            border: 1.5px solid var(--p-ink);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .live-pulse {
            width: 7px;
            height: 7px;
            background: #16A34A;
            border-radius: 50%;
            box-shadow: 0 0 6px #16A34A;
        }

        /* AVANT-GARDE MONUMENTAL HEADLINE (NO SUBHEADING AT ALL!) */
        .avant-headline {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.4rem, 4.2vw, 3.6rem);
            font-weight: 900;
            line-height: 1.08;
            letter-spacing: -0.04em;
            text-transform: uppercase;
            color: var(--p-ink);
            margin-bottom: 24px;
        }

        .avant-pill {
            display: inline-flex;
            align-items: center;
            padding: 2px 14px;
            border-radius: 14px;
            border: 2px solid var(--p-ink);
            box-shadow: 3px 3px 0px var(--p-ink);
            font-size: 0.78em;
            vertical-align: middle;
            margin: 0 4px;
            transform: translateY(-3px);
            text-transform: none;
            letter-spacing: -0.01em;
        }

        .avant-pill.coral { background: var(--p-coral); color: #FFFFFF; }
        .avant-pill.yellow { background: var(--p-yellow); color: var(--p-ink); }
        .avant-pill.lime { background: var(--p-lime); color: var(--p-ink); }

        /* DIRECT CTA ACTION ROW */
        .hero-cta-strip {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        .btn-avant-coral {
            background: var(--p-coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.05rem;
            padding: 14px 28px;
            border-radius: 16px;
            border: 2px solid var(--p-ink);
            box-shadow: 4px 4px 0px var(--p-ink);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.15s ease;
        }

        .btn-avant-coral:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--p-ink);
            background: var(--p-coral-hover);
        }

        .badge-zero-cost {
            background: var(--p-lime);
            color: var(--p-ink);
            font-family: 'Space Mono', monospace;
            font-size: 0.8rem;
            font-weight: 700;
            padding: 8px 14px;
            border-radius: 12px;
            border: 2px solid var(--p-ink);
            box-shadow: 2.5px 2.5px 0px var(--p-ink);
        }

        /* =========================================================================
           TILE 2: THE 60-SECOND REVELATIONS TILE
           ========================================================================= */
        .tile-sixty-reels {
            background: var(--p-purple-light);
        }

        .sixty-graphic-hud {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #FFFFFF;
            border: 2px solid var(--p-ink);
            border-radius: 14px;
            padding: 10px 14px;
            box-shadow: 2.5px 2.5px 0px var(--p-ink);
            margin: 10px 0;
        }

        .hud-timer {
            font-family: 'Space Mono', monospace;
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--p-purple);
        }

        .hud-icon {
            font-size: 1.3rem;
        }

        .tile-copy-punch {
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.2rem;
            line-height: 1.18;
            color: var(--p-ink);
        }

        .tile-caption {
            font-size: 0.78rem;
            font-weight: 700;
            color: #52525B;
            margin-top: 4px;
        }

        /* =========================================================================
           TILE 3: THE 94% GRADE SURGE STAT TILE
           ========================================================================= */
        .tile-grade-surge {
            background: var(--p-yellow);
        }

        .huge-stat-num {
            font-family: 'Outfit', sans-serif;
            font-size: 3.4rem;
            font-weight: 900;
            line-height: 0.95;
            letter-spacing: -0.05em;
            color: var(--p-ink);
            margin: 6px 0 4px;
        }

        .stat-badge-sub {
            background: var(--p-ink);
            color: #FFFFFF;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 6px;
            width: fit-content;
            margin-bottom: 8px;
        }

        /* =========================================================================
           TILE 4: 24/7 MITRA AI NIGHT-OWL TILE
           ========================================================================= */
        .tile-mitra-ai {
            background: #18181B;
            color: #FFFFFF;
        }

        .tile-mitra-ai .tile-meta-header {
            color: #A1A1AA;
        }

        .tile-mitra-ai .index-pill {
            background: #27272A;
            border-color: #52525B;
            color: #E4E4E7;
            box-shadow: none;
        }

        .code-chalkboard {
            background: #09090B;
            border: 1.5px solid #3F3F46;
            border-radius: 12px;
            padding: 10px 12px;
            font-family: 'Space Mono', monospace;
            font-size: 0.82rem;
            color: #38BDF8;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 8px 0;
        }

        .step-check {
            color: var(--p-lime);
            font-weight: 700;
        }

        .mitra-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.15rem;
            color: #FFFFFF;
        }

        /* =========================================================================
           TILE 5: VERIFIED PARENT OUTCOME TILE
           ========================================================================= */
        .tile-parent-proof {
            background: #FFFFFF;
        }

        .proof-stars {
            color: #F59E0B;
            font-size: 1rem;
            letter-spacing: 2px;
            margin-bottom: 6px;
        }

        .proof-quote {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1rem;
            line-height: 1.25;
            color: var(--p-ink);
            margin-bottom: 8px;
        }

        .proof-author-tag {
            font-size: 0.74rem;
            font-weight: 700;
            color: #71717A;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* =========================================================================
           RIGHT BENTO COLUMN: HERO 9:16 VERTICAL REEL (EXACT PROPORTIONS)
           ========================================================================= */
        .bento-reel-column {
            position: relative;
        }

        .reel-avant-card {
            background: #000000;
            border: var(--border-thick);
            border-radius: 28px;
            box-shadow: var(--shadow-hero);
            height: 100%;
            min-height: 520px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* AUTOPLAYING 9:16 VIDEO IN EXACT PROPORTIONS */
        .reel-avant-card video {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* REEL FLOATING TOP BAR */
        .reel-hud-top {
            position: relative;
            z-index: 3;
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .avant-live-badge {
            background: rgba(20, 20, 22, 0.9);
            backdrop-filter: blur(10px);
            border: 1.5px solid rgba(255, 255, 255, 0.25);
            color: #FFFFFF;
            font-family: 'Space Mono', monospace;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .avant-time-pill {
            background: var(--p-yellow);
            color: var(--p-ink);
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 6px;
            border: 1px solid var(--p-ink);
        }

        /* REEL FLOATING BOTTOM STACK */
        .reel-hud-bottom {
            position: relative;
            z-index: 3;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .avant-quote-pill {
            background: rgba(255, 255, 255, 0.96);
            border: 2px solid var(--p-ink);
            border-radius: 14px;
            padding: 10px 14px;
            font-size: 0.8rem;
            font-weight: 800;
            color: var(--p-ink);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.35);
        }

        .avant-mentor-pill {
            background: rgba(20, 20, 22, 0.92);
            backdrop-filter: blur(10px);
            border: 1.5px solid rgba(255, 255, 255, 0.25);
            border-radius: 14px;
            padding: 9px 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: #FFFFFF;
        }

        .mentor-cell {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .mentor-cell-img {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            border: 1.5px solid #FFFFFF;
            overflow: hidden;
            background: #FEF08A;
        }

        .mentor-cell-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .mentor-meta-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.82rem;
            line-height: 1.1;
        }

        .mentor-meta-spec {
            font-size: 0.68rem;
            color: #A1A1AA;
        }

        /* FLOATING AVANT-GARDE TAPE BADGE */
        .avant-tape-sticker {
            position: absolute;
            top: -12px;
            right: 18px;
            background: var(--p-lime);
            color: var(--p-ink);
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 8px;
            border: 2px solid var(--p-ink);
            box-shadow: 3px 3px 0px var(--p-ink);
            transform: rotate(3deg);
            z-index: 5;
            pointer-events: none;
        }

        /* RESPONSIVE LAYOUT */
        @media (max-width: 1024px) {
            .bento-grid {
                grid-template-columns: 1fr;
            }
            .reel-avant-card {
                min-height: 480px;
                max-width: 340px;
                margin: 0 auto;
                aspect-ratio: 9 / 16;
            }
        }

        @media (max-width: 640px) {
            .bento-left-cluster {
                grid-template-columns: 1fr;
            }
            .tile-hero-headline {
                grid-column: span 1;
                padding: 24px 20px;
            }
            .avant-headline {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>

    <div class="bento-shell">
        <div class="bento-grid">
            
            <!-- LEFT ASYMMETRIC BENTO CLUSTER (5 TILES) -->
            <div class="bento-left-cluster">
                
                <!-- TILE 1: AVANT-GARDE HERO HEADLINE & CTA (ZERO SUBHEADING!) -->
                <div class="bento-tile tile-hero-headline">
                    <div>
                        <div class="hero-top-strip">
                            <span class="category-tag">CBSE · ICSE · GRADES 1–12</span>
                            <div class="live-tag">
                                <span class="live-pulse"></span>
                                <span>GUIDED LEARNING</span>
                            </div>
                        </div>

                        <!-- BOLD AVANT-GARDE HEADLINE (NO SUBHEAD UNDER IT) -->
                        <h1 class="avant-headline">
                            ONE-ON-ONE <span class="avant-pill coral">TUTORS 🧑‍🏫</span><br>
                            SIXTY-SECOND <span class="avant-pill yellow">REELS ⚡</span><br>
                            CONCEPTS THAT <span class="avant-pill lime">CLICK 💡</span>
                        </h1>
                    </div>

                    <!-- DIRECT CONVERSION ACTION STRIP -->
                    <div class="hero-cta-strip">
                        <a href="https://paathshala.app/booking" target="_blank" class="btn-avant-coral">
                            <span>Claim Free 1-on-1 Class</span>
                            <span>➔</span>
                        </a>
                        <span class="badge-zero-cost">₹0 FREE PASS · NO CARD</span>
                    </div>
                </div>

                <!-- TILE 2: 60-SEC REVELATIONS -->
                <div class="bento-tile tile-sixty-reels">
                    <div class="tile-meta-header">
                        <span class="index-pill">[ 01 ]</span>
                        <span>REVISION ENGINE</span>
                    </div>

                    <div>
                        <div class="sixty-graphic-hud">
                            <span class="hud-timer">00:60s</span>
                            <span class="hud-icon">✂️⚡</span>
                        </div>
                        <div class="tile-copy-punch">
                            AI Breakthrough Reels.
                        </div>
                        <div class="tile-caption">
                            Auto-clipped the instant understanding happens.
                        </div>
                    </div>
                </div>

                <!-- TILE 3: +29% / 94% GRADE SURGE STAT -->
                <div class="bento-tile tile-grade-surge">
                    <div class="tile-meta-header">
                        <span class="index-pill">[ 02 ]</span>
                        <span>PROVEN OUTCOME</span>
                    </div>

                    <div>
                        <div class="stat-badge-sub">EXAM SURGE</div>
                        <div class="huge-stat-num">+29%</div>
                        <div class="tile-copy-punch" style="font-size:1.05rem;">
                            Average Marks Jump.
                        </div>
                        <div class="tile-caption">
                            Documented across 12,000+ students in 6 weeks.
                        </div>
                    </div>
                </div>

                <!-- TILE 4: 24/7 MITRA AI NIGHT-OWL DOUBT SOLVER -->
                <div class="bento-tile tile-mitra-ai">
                    <div class="tile-meta-header">
                        <span class="index-pill">[ 03 ]</span>
                        <span>24/7 MITRA AI</span>
                    </div>

                    <div>
                        <div class="code-chalkboard">
                            <span>2x + 3 = 11</span>
                            <span class="step-check">x = 4 ✓</span>
                        </div>
                        <div class="mitra-title">
                            Midnight Doubt Solver.
                        </div>
                        <div class="tile-caption" style="color:#A1A1AA;">
                            Instant step-by-step math &amp; science logic.
                        </div>
                    </div>
                </div>

                <!-- TILE 5: REAL PARENT VERDICT -->
                <div class="bento-tile tile-parent-proof">
                    <div class="tile-meta-header">
                        <span class="index-pill">[ 04 ]</span>
                        <span>VERIFIED VERDICT</span>
                    </div>

                    <div>
                        <div class="proof-stars">★★★★★</div>
                        <div class="proof-quote">
                            "62% to 91% in Physics."
                        </div>
                        <div class="proof-author-tag">
                            <span>Priya Sharma</span>
                            <span>•</span>
                            <span>Grade 10 Parent</span>
                        </div>
                    </div>
                </div>

            </div>

            <!-- RIGHT BENTO COLUMN: HERO 9:16 VERTICAL REEL -->
            <div class="bento-reel-column">
                
                <div class="avant-tape-sticker">
                    <span>★ LIVE CLASSROOM REEL</span>
                </div>

                <div class="reel-avant-card">
                    
                    <!-- 9:16 VIDEO -->
                    <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                        <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                    </video>

                    <!-- TOP HUD -->
                    <div class="reel-hud-top">
                        <div class="avant-live-badge">
                            <span class="live-pulse"></span>
                            <span>BREAKTHROUGH</span>
                        </div>
                        <div class="avant-time-pill">0:50</div>
                    </div>

                    <!-- BOTTOM HUD -->
                    <div class="reel-hud-bottom">
                        <div class="avant-quote-pill">
                            💡 "Wait, so neutrons are the glue?! Now I get it!"
                        </div>

                        <div class="avant-mentor-pill">
                            <div class="mentor-cell">
                                <div class="mentor-cell-img">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div>
                                    <div class="mentor-meta-name">Leah Alexander</div>
                                    <div class="mentor-meta-spec">Senior Physics Mentor</div>
                                </div>
                            </div>
                            <span style="font-family:'Space Mono'; font-weight:700; font-size:0.75rem; color:#FEF08A;">★ 4.95</span>
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

print("Avant-Garde Bento Banner generated successfully!")
