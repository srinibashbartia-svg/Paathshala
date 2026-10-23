import os

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala · Guided Learning High-Converting Banner</title>
    
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
            --bg-canvas: #F4EFEB;
            --card-cream: #FFFDF9;
            --border: 2.5px solid var(--paathshala-dark);
            --shadow-card: 6px 6px 0px var(--paathshala-dark);
            --shadow-hover: 9px 9px 0px var(--paathshala-dark);
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
            padding: 40px 16px;
        }

        /* BANNER SHELL */
        .banner-shell {
            width: 100%;
            max-width: 1280px;
            margin: 0 auto;
        }

        /* MAIN BANNER CONTAINER */
        .banner-card {
            background-color: var(--card-cream);
            border: var(--border);
            border-radius: 36px;
            box-shadow: 10px 10px 0px var(--paathshala-dark);
            padding: 48px 44px;
            position: relative;
            overflow: hidden;
        }

        /* DOT MATRIX TEXTURE */
        .banner-pattern {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(24, 24, 27, 0.07) 1.5px, transparent 1.5px);
            background-size: 22px 22px;
            pointer-events: none;
            z-index: 0;
        }

        /* BANNER HEADER */
        .banner-header {
            position: relative;
            z-index: 2;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 24px;
            margin-bottom: 36px;
            flex-wrap: wrap;
        }

        .header-content {
            max-width: 720px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .eyebrow-pill-group {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .eyebrow-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.76rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            padding: 5px 12px;
            border-radius: 999px;
            border: 1.5px solid var(--paathshala-dark);
            box-shadow: 2px 2px 0px var(--paathshala-dark);
            background: #FFFFFF;
        }

        .eyebrow-pill.green {
            background: #DCFCE7;
            color: #166534;
        }

        .pulse-dot {
            width: 7px;
            height: 7px;
            background: #16A34A;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 6px #16A34A;
        }

        .banner-title {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.2rem, 3.8vw, 3.2rem);
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -0.03em;
            color: var(--paathshala-dark);
        }

        .highlight-pill {
            display: inline-flex;
            align-items: center;
            padding: 1px 12px;
            border-radius: 12px;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 2.5px 2.5px 0px var(--paathshala-dark);
            font-size: 0.85em;
            vertical-align: middle;
            margin: 0 4px;
            transform: translateY(-2px);
        }

        .highlight-pill.yellow { background: var(--paathshala-yellow); }
        .highlight-pill.coral { background: var(--paathshala-coral); color: #FFFFFF; }
        .highlight-pill.lime { background: var(--paathshala-lime); }

        .banner-subtitle {
            font-size: 1.02rem;
            color: #52525B;
            line-height: 1.5;
            font-weight: 500;
        }

        /* HEADER CTA BUTTON */
        .header-cta-block {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 8px;
        }

        .btn-main {
            background: var(--paathshala-coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            padding: 15px 32px;
            border-radius: 16px;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 4px 4px 0px var(--paathshala-dark);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.15s ease;
        }

        .btn-main:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--paathshala-dark);
            background: var(--paathshala-coral-hover);
        }

        .header-guarantee {
            font-size: 0.78rem;
            font-weight: 700;
            color: #71717A;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* =========================================================================
           4 HIGH-CONVERTING STORY / REEL CARDS (INSPIRED BY REFERENCE IMAGES)
           ========================================================================= */
        .cards-row {
            position: relative;
            z-index: 2;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }

        /* COMMON STORY CARD STYLING */
        .story-card {
            aspect-ratio: 9 / 15.5;
            border-radius: 24px;
            border: var(--border);
            box-shadow: var(--shadow-card);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 20px;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease;
        }

        .story-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-hover);
        }

        /* CARD 1: THE REAL LIVE CLASS REEL (9:16 VIDEO IN OUR STYLE) */
        .card-reel {
            background: #000000;
            color: #FFFFFF;
            padding: 0;
        }

        .card-reel video {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .reel-overlay-top {
            position: relative;
            z-index: 3;
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .reel-tag {
            background: rgba(24, 24, 27, 0.88);
            backdrop-filter: blur(8px);
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .reel-time {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.72rem;
            padding: 3px 8px;
            border-radius: 6px;
            border: 1px solid var(--paathshala-dark);
        }

        .reel-overlay-bottom {
            position: relative;
            z-index: 3;
            padding: 14px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .reel-caption-pill {
            background: rgba(255, 255, 255, 0.96);
            border: 1.5px solid var(--paathshala-dark);
            border-radius: 12px;
            padding: 9px 12px;
            font-size: 0.78rem;
            font-weight: 800;
            color: var(--paathshala-dark);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        }

        .reel-author-badge {
            background: rgba(24, 24, 27, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 8px 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: #FFFFFF;
        }

        .reel-author-info {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .reel-avatar {
            width: 28px;
            height: 28px;
            border-radius: 6px;
            border: 1px solid #FFFFFF;
            overflow: hidden;
            background: #FEF08A;
        }

        .reel-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .reel-name {
            font-family: 'Outfit', sans-serif;
            font-size: 0.78rem;
            font-weight: 800;
            line-height: 1.1;
        }

        .reel-subject {
            font-size: 0.68rem;
            color: #A1A1AA;
        }

        /* CARD 2: KINETIC 60-SEC RECAP (INSPIRED BY THE SHAVER / REPEAT TYPOGRAPHY IN IMAGE 1) */
        .card-kinetic {
            background: var(--paathshala-purple);
            color: #FFFFFF;
        }

        .kinetic-bg-text {
            position: absolute;
            inset: 0;
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 900;
            line-height: 1.05;
            color: rgba(255, 255, 255, 0.12);
            pointer-events: none;
            padding: 16px;
            word-break: break-all;
            user-select: none;
        }

        .kinetic-top-badge {
            background: #FFFFFF;
            color: var(--paathshala-dark);
            border: 1.5px solid var(--paathshala-dark);
            box-shadow: 2px 2px 0px var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 999px;
            width: fit-content;
            position: relative;
            z-index: 2;
        }

        .kinetic-center-graphic {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 12px;
        }

        .big-aha-sticker {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
            border: 2.5px solid var(--paathshala-dark);
            box-shadow: 4px 4px 0px var(--paathshala-dark);
            border-radius: 20px;
            padding: 16px;
            width: 84px;
            height: 84px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.4rem;
            transform: rotate(-4deg);
        }

        .kinetic-hook-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.45rem;
            font-weight: 900;
            line-height: 1.15;
            color: #FFFFFF;
            text-transform: uppercase;
        }

        .kinetic-bottom-pill {
            background: var(--paathshala-lime);
            color: var(--paathshala-dark);
            border: 1.5px solid var(--paathshala-dark);
            box-shadow: 2px 2px 0px var(--paathshala-dark);
            border-radius: 12px;
            padding: 8px 12px;
            font-size: 0.75rem;
            font-weight: 800;
            line-height: 1.3;
            text-align: center;
            position: relative;
            z-index: 2;
        }

        /* CARD 3: SOCIAL PROOF / PARENT REVIEW (INSPIRED BY THE DEUX / BURN REVIEW CARDS IN IMAGE 1) */
        .card-review {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
        }

        .review-stars-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .gold-stars {
            font-size: 1.1rem;
            color: #D97706;
            letter-spacing: 2px;
        }

        .marks-jump-tag {
            background: var(--paathshala-dark);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 6px;
        }

        .quote-bubble {
            background: #FFFFFF;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 3px 3px 0px var(--paathshala-dark);
            border-radius: 16px;
            padding: 16px 14px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .quote-lead {
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            font-weight: 900;
            line-height: 1.2;
            color: var(--paathshala-dark);
        }

        .quote-body {
            font-size: 0.82rem;
            color: #4B5563;
            line-height: 1.45;
            font-weight: 600;
        }

        .review-parent-meta {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--paathshala-dark);
        }

        .parent-avatar-circle {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #E0E7FF;
            border: 1.5px solid var(--paathshala-dark);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.75rem;
        }

        /* CARD 4: THE 100% FREE TRIAL CLAIM TICKET (INSPIRED BY THE PROMO / FESTIVE CARDS IN IMAGE 1) */
        .card-promo {
            background: var(--paathshala-coral);
            color: #FFFFFF;
        }

        .promo-ticket-top {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .promo-pill-light {
            background: rgba(255, 255, 255, 0.25);
            border: 1.5px solid rgba(255, 255, 255, 0.5);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 999px;
            width: fit-content;
            letter-spacing: 0.6px;
            text-transform: uppercase;
        }

        .promo-huge-price {
            font-family: 'Outfit', sans-serif;
            font-size: 2.5rem;
            font-weight: 900;
            line-height: 1.05;
            color: #FFFFFF;
            letter-spacing: -0.03em;
        }

        .promo-huge-sub {
            font-size: 0.82rem;
            font-weight: 700;
            color: #FFE4E6;
        }

        .ticket-feature-list {
            background: #FFFFFF;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 3px 3px 0px var(--paathshala-dark);
            border-radius: 14px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            color: var(--paathshala-dark);
            font-size: 0.75rem;
            font-weight: 800;
        }

        .ticket-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .ticket-check {
            color: #10B981;
            font-weight: 900;
        }

        .btn-ticket-claim {
            background: var(--paathshala-yellow);
            color: var(--paathshala-dark);
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 0.95rem;
            padding: 12px;
            border-radius: 12px;
            border: 2px solid var(--paathshala-dark);
            box-shadow: 3px 3px 0px var(--paathshala-dark);
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: all 0.15s ease;
        }

        .btn-ticket-claim:hover {
            transform: translate(-1.5px, -1.5px);
            box-shadow: 4.5px 4.5px 0px var(--paathshala-dark);
            background: #FDE047;
        }

        /* RESPONSIVE DESIGN */
        @media (max-width: 1080px) {
            .cards-row {
                grid-template-columns: repeat(2, 1fr);
            }
            .banner-card {
                padding: 36px 28px;
            }
        }

        @media (max-width: 640px) {
            .cards-row {
                grid-template-columns: 1fr;
            }
            .story-card {
                aspect-ratio: auto;
                min-height: 420px;
            }
        }
    </style>
</head>
<body>

    <div class="banner-shell">
        <div class="banner-card">
            
            <div class="banner-pattern"></div>

            <!-- BANNER HEADER -->
            <div class="banner-header">
                
                <div class="header-content">
                    <div class="eyebrow-pill-group">
                        <div class="eyebrow-pill green">
                            <span class="pulse-dot"></span>
                            <span>Guided Learning Experience</span>
                        </div>
                        <div class="eyebrow-pill">
                            <span>★ 4.98 Rating · 12,000+ Students</span>
                        </div>
                        <span style="font-size: 0.8rem; font-weight: 700; color: #71717A;">Classes 1 to 12 · CBSE &amp; ICSE</span>
                    </div>

                    <h2 class="banner-title">
                        Where <span class="highlight-pill yellow">1-on-1 Mentors 🧑‍🏫</span> &amp; 
                        <span class="highlight-pill coral">60s Reels ⚡</span> make concepts 
                        finally <span class="highlight-pill lime">CLICK 💡</span>
                    </h2>

                    <p class="banner-subtitle">
                        Private classes matched to your child's exact learning pace. Every breakthrough auto-clipped into a 60-second recap for instant exam recall.
                    </p>
                </div>

                <div class="header-cta-block">
                    <a href="https://paathshala.app/booking" target="_blank" class="btn-main">
                        <span>Book Free 1-on-1 Class</span>
                        <span style="font-size:1.15rem;">➔</span>
                    </a>
                    <div class="header-guarantee">
                        <span>🛡️ 100% Free Trial</span>
                        <span>•</span>
                        <span>No Card Required</span>
                    </div>
                </div>

            </div>

            <!-- 4 HIGH-CONVERTING STORY / REEL CARDS IN OUR DESIGN STYLE -->
            <div class="cards-row">
                
                <!-- CARD 1: REAL 9:16 CLASSROOM REEL -->
                <div class="story-card card-reel">
                    <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                        <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                    </video>

                    <div class="reel-overlay-top">
                        <div class="reel-tag">
                            <span class="pulse-dot"></span>
                            <span>Live Breakthrough</span>
                        </div>
                        <div class="reel-time">0:50</div>
                    </div>

                    <div class="reel-overlay-bottom">
                        <div class="reel-caption-pill">
                            💡 "Wait, so neutrons are the glue?! Now I get it!"
                        </div>
                        <div class="reel-author-badge">
                            <div class="reel-author-info">
                                <div class="reel-avatar">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div>
                                    <div class="reel-name">Leah Alexander</div>
                                    <div class="reel-subject">Physics · SafeTutor</div>
                                </div>
                            </div>
                            <span style="font-family:'Outfit'; font-weight:800; font-size:0.75rem; color:#FEF08A;">★ 4.95</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 2: KINETIC 60-SEC RECAP (INSPIRED BY IMAGE 1) -->
                <div class="story-card card-kinetic">
                    <div class="kinetic-bg-text">
                        60S 60S 60S 60S 60S 60S 60S 60S 60S
                    </div>

                    <div class="kinetic-top-badge">
                        <span>⚡ NEVER FORGET AGAIN</span>
                    </div>

                    <div class="kinetic-center-graphic">
                        <div class="big-aha-sticker">
                            <span>💡</span>
                        </div>
                        <h3 class="kinetic-hook-title">
                            No More 60-Min Boring Lectures.
                        </h3>
                    </div>

                    <div class="kinetic-bottom-pill">
                        <span>✂️ Breakthroughs auto-clipped into 60s reels for 1-minute exam revision.</span>
                    </div>
                </div>

                <!-- CARD 3: SOCIAL PROOF / PARENT REVIEW (INSPIRED BY IMAGE 1) -->
                <div class="story-card card-review">
                    <div class="review-stars-row">
                        <div class="gold-stars">★★★★★</div>
                        <div class="marks-jump-tag">+29% MARKS BOOST</div>
                    </div>

                    <div class="quote-bubble">
                        <div class="quote-lead">"Doesn't feel like tuition. It actually clicked."</div>
                        <div class="quote-body">
                            "Arjun jumped from 62% in Physics to 91% in his CBSE term exams. Rewatching the 60s class reels before test day changed everything."
                        </div>
                    </div>

                    <div class="review-parent-meta">
                        <div class="parent-avatar-circle">👩‍💼</div>
                        <div>
                            <div>Priya Sharma</div>
                            <div style="font-size:0.68rem; font-weight:600; color:#52525B;">Grade 10 Parent · Bengaluru</div>
                        </div>
                    </div>
                </div>

                <!-- CARD 4: 100% FREE CLASS CLAIM TICKET (INSPIRED BY IMAGE 1) -->
                <div class="story-card card-promo">
                    <div class="promo-ticket-top">
                        <div class="promo-pill-light">EXCLUSIVE PASS</div>
                        <div class="promo-huge-price">₹0 FREE</div>
                        <div class="promo-huge-sub">1-on-1 Class with Top 1.4% Mentor</div>
                    </div>

                    <div class="ticket-feature-list">
                        <div class="ticket-item">
                            <span class="ticket-check">✓</span>
                            <span>Live 45-Min Private Session</span>
                        </div>
                        <div class="ticket-item">
                            <span class="ticket-check">✓</span>
                            <span>Instant 60s Breakthrough Reel</span>
                        </div>
                        <div class="ticket-item">
                            <span class="ticket-check">✓</span>
                            <span>No Credit Card Required</span>
                        </div>
                    </div>

                    <a href="https://paathshala.app/booking" target="_blank" class="btn-ticket-claim">
                        <span>Claim Free Class</span>
                        <span>➔</span>
                    </a>
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

print("High-converting story banner generated successfully!")
