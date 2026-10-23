import os

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala Guided Learning · Designed Like Apple</title>
    
    <!-- SF Pro / Plus Jakarta Sans & Outfit for Apple-grade typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg-canvas: #05070E;
            --card-surface: rgba(15, 20, 32, 0.75);
            --card-border: rgba(255, 255, 255, 0.12);
            --card-border-hover: rgba(255, 255, 255, 0.25);
            --accent-purple: #5E58F7;
            --accent-purple-glow: rgba(94, 88, 247, 0.35);
            --accent-coral: #FF5A36;
            --accent-coral-glow: rgba(255, 90, 54, 0.35);
            --text-white: #FFFFFF;
            --text-silver: #A1A1AA;
            --text-muted: #71717A;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-canvas);
            color: var(--text-white);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
            overflow-x: hidden;
        }

        /* BANNER WRAPPER */
        .apple-banner-shell {
            width: 100%;
            max-width: 1220px;
            margin: 0 auto;
            position: relative;
        }

        /* AMBIENT BACKGROUND LIGHTING EFFECT (APPLE KEYNOTE GLOW) */
        .ambient-radial-glow {
            position: absolute;
            top: 20%;
            right: 15%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, var(--accent-purple-glow) 0%, rgba(255, 90, 54, 0.15) 45%, transparent 70%);
            filter: blur(80px);
            pointer-events: none;
            z-index: 0;
            border-radius: 50%;
        }

        /* MAIN CONTAINER CARD */
        .apple-banner {
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.82) 0%, rgba(10, 14, 26, 0.92) 100%);
            backdrop-filter: blur(32px);
            -webkit-backdrop-filter: blur(32px);
            border: 1px solid var(--card-border);
            border-radius: 36px;
            padding: 64px 68px;
            position: relative;
            z-index: 1;
            box-shadow: 0 24px 64px -12px rgba(0, 0, 0, 0.7), 
                        inset 0 1px 0 rgba(255, 255, 255, 0.12);
            overflow: hidden;
            transition: border-color 0.3s ease;
        }

        .apple-banner:hover {
            border-color: var(--card-border-hover);
        }

        /* SUBTLE HAIRLINE TOP HIGHLIGHT */
        .banner-hairline-glow {
            position: absolute;
            top: 0;
            left: 10%;
            right: 10%;
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.4) 50%, transparent 100%);
            pointer-events: none;
        }

        /* 2-COLUMN SYMMETRIC GRID */
        .banner-grid {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 60px;
            align-items: center;
        }

        /* LEFT: EDITORIAL COPY */
        .banner-copy-col {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        /* APPLE-STYLE MONOCHROME EYEBROW PILL */
        .apple-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 14px;
            border-radius: 9999px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(12px);
            width: fit-content;
        }

        .eyebrow-dot {
            width: 6px;
            height: 6px;
            background: #10B981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10B981;
        }

        .eyebrow-text {
            font-family: 'Outfit', sans-serif;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            color: #E4E4E7;
        }

        .eyebrow-divider {
            color: rgba(255, 255, 255, 0.2);
        }

        .eyebrow-sub {
            font-size: 0.74rem;
            color: #A1A1AA;
            font-weight: 500;
        }

        /* APPLE HEADLINE: GRADIENT METALLIC SHINE */
        .apple-headline {
            font-family: 'Outfit', -apple-system, sans-serif;
            font-size: clamp(2.6rem, 4.2vw, 3.8rem);
            font-weight: 800;
            line-height: 1.1;
            letter-spacing: -0.035em;
            color: #FFFFFF;
        }

        .headline-gradient {
            background: linear-gradient(180deg, #FFFFFF 20%, #A1A1AA 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline-block;
        }

        .headline-accent {
            background: linear-gradient(135deg, #FF6F4C 0%, #FF9E66 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline-block;
        }

        /* APPLE SUBTITLE: RESTRAINED, CONFIDENT, TIMELESS */
        .apple-subhead {
            font-size: 1.12rem;
            line-height: 1.6;
            color: #A1A1AA;
            font-weight: 400;
            max-width: 530px;
        }

        .apple-subhead strong {
            color: #F4F4F5;
            font-weight: 600;
        }

        /* APPLE SPECIFICATION PILL METRICS */
        .apple-metrics-row {
            display: flex;
            align-items: center;
            gap: 32px;
            padding: 12px 0 6px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            margin: 4px 0;
        }

        .metric-block {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .metric-num {
            font-family: 'Outfit', sans-serif;
            font-size: 1.4rem;
            font-weight: 800;
            color: #FFFFFF;
            letter-spacing: -0.02em;
        }

        .metric-label {
            font-size: 0.75rem;
            color: #71717A;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }

        /* APPLE ACTION BUTTONS */
        .apple-cta-row {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
            padding-top: 4px;
        }

        .btn-apple-primary {
            background: linear-gradient(180deg, #FFFFFF 0%, #E4E4E7 100%);
            color: #09090B;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.02rem;
            padding: 15px 30px;
            border-radius: 9999px;
            border: none;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 16px rgba(255, 255, 255, 0.15), 
                        inset 0 1px 0 rgba(255, 255, 255, 0.8);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .btn-apple-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(255, 255, 255, 0.25);
            background: #FFFFFF;
        }

        .btn-apple-secondary {
            background: rgba(255, 255, 255, 0.06);
            color: #E4E4E7;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            padding: 14px 24px;
            border-radius: 9999px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
        }

        .btn-apple-secondary:hover {
            background: rgba(255, 255, 255, 0.12);
            color: #FFFFFF;
            border-color: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }

        /* RIGHT: APPLE HARDWARE/DISPLAY SHOWCASE */
        .banner-visual-col {
            position: relative;
            display: flex;
            justify-content: center;
        }

        /* STUDIO GLASS DISPLAY FRAME */
        .studio-display {
            background: rgba(18, 22, 34, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 28px;
            padding: 14px;
            box-shadow: 0 32px 72px -16px rgba(0, 0, 0, 0.8), 
                        inset 0 1px 0 rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(24px);
            width: 100%;
            max-width: 440px;
            position: relative;
            z-index: 2;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .studio-display:hover {
            transform: translateY(-4px);
        }

        /* SCREEN BEZEL & VIDEO */
        .screen-bezel {
            border-radius: 20px;
            overflow: hidden;
            position: relative;
            background: #000000;
            border: 1px solid rgba(255, 255, 255, 0.08);
            height: 250px;
        }

        .screen-bezel video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* FLOATING HUD BADGE: LIVE BREAKTHROUGH */
        .hud-live-badge {
            position: absolute;
            top: 14px;
            left: 14px;
            background: rgba(9, 11, 17, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #FFFFFF;
            padding: 5px 11px;
            border-radius: 9999px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .hud-timecode {
            position: absolute;
            top: 14px;
            right: 14px;
            background: rgba(9, 11, 17, 0.75);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #A1A1AA;
            padding: 5px 10px;
            border-radius: 8px;
            font-family: -apple-system, monospace;
            font-size: 0.72rem;
            font-weight: 600;
        }

        /* BOTTOM SCREEN ANNOTATION */
        .hud-quote-glass {
            position: absolute;
            bottom: 14px;
            left: 14px;
            right: 14px;
            background: rgba(15, 20, 32, 0.88);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 12px;
            padding: 10px 14px;
            font-size: 0.8rem;
            color: #F4F4F5;
            font-weight: 500;
            line-height: 1.4;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.4);
        }

        .quote-icon {
            color: #FF5A36;
            font-size: 1rem;
        }

        /* DISPLAY LOWER FOOTER (EDUCATOR INFO) */
        .display-footer {
            padding: 14px 8px 4px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .educator-profile {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .educator-avatar {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            overflow: hidden;
            border: 1.5px solid rgba(255, 255, 255, 0.2);
            background: #18181B;
            flex-shrink: 0;
        }

        .educator-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .educator-text {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .educator-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 0.92rem;
            color: #FFFFFF;
        }

        .educator-sub {
            font-size: 0.74rem;
            color: #A1A1AA;
        }

        .rating-badge {
            display: flex;
            align-items: center;
            gap: 4px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 5px 10px;
            border-radius: 8px;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 0.78rem;
            color: #FDE047;
        }

        /* RESPONSIVE */
        @media (max-width: 980px) {
            .apple-banner {
                padding: 44px 30px;
            }
            .banner-grid {
                grid-template-columns: 1fr;
                gap: 48px;
            }
            .studio-display {
                max-width: 100%;
            }
        }
    </style>
</head>
<body>

    <div class="apple-banner-shell">
        
        <!-- AMBIENT PURPLE / CORAL VOLUMETRIC GLOW -->
        <div class="ambient-radial-glow"></div>

        <div class="apple-banner">
            
            <div class="banner-hairline-glow"></div>

            <div class="banner-grid">
                
                <!-- LEFT: REFINED APPLE-GRADE COPY -->
                <div class="banner-copy-col">
                    
                    <div class="apple-eyebrow">
                        <span class="eyebrow-dot"></span>
                        <span class="eyebrow-text">Guided Learning</span>
                        <span class="eyebrow-divider">|</span>
                        <span class="eyebrow-sub">Classes 1 to 12</span>
                    </div>

                    <h1 class="apple-headline">
                        <span class="headline-gradient">One educator. Total focus.</span><br>
                        <span class="headline-accent">Every breakthrough, captured.</span>
                    </h1>

                    <p class="apple-subhead">
                        Private 1-on-1 mentorship engineered for how your child actually thinks. 
                        When understanding happens, our AI automatically clips the exact 60 seconds — 
                        creating an instant, lifelong revision reel before every exam.
                    </p>

                    <!-- KEY PERFORMANCE METRICS -->
                    <div class="apple-metrics-row">
                        <div class="metric-block">
                            <span class="metric-num">Top 1.4%</span>
                            <span class="metric-label">Certified Mentors</span>
                        </div>
                        <div class="metric-block">
                            <span class="metric-num">60 Seconds</span>
                            <span class="metric-label">Aha! Video Reels</span>
                        </div>
                        <div class="metric-block">
                            <span class="metric-num">4.98 ★</span>
                            <span class="metric-label">12,000+ Verified Parents</span>
                        </div>
                    </div>

                    <!-- REFINED CALLS TO ACTION -->
                    <div class="apple-cta-row">
                        <a href="https://paathshala.app/booking" target="_blank" class="btn-apple-primary">
                            <span>Experience a Free Class</span>
                            <span>➔</span>
                        </a>
                        <a href="/landing.html" class="btn-apple-secondary">
                            <span>See How It Works</span>
                            <span>↗</span>
                        </a>
                    </div>

                </div>

                <!-- RIGHT: STUDIO DISPLAY SHOWCASE -->
                <div class="banner-visual-col">
                    <div class="studio-display">
                        
                        <div class="screen-bezel">
                            <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                                <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                            </video>

                            <div class="hud-live-badge">
                                <span class="eyebrow-dot"></span>
                                <span>Breakthrough Reel</span>
                            </div>

                            <div class="hud-timecode">
                                0:50
                            </div>

                            <div class="hud-quote-glass">
                                <span class="quote-icon">💡</span>
                                <span>"Wait, so neutrons are the glue?! Now I get it!"</span>
                            </div>
                        </div>

                        <div class="display-footer">
                            <div class="educator-profile">
                                <div class="educator-avatar">
                                    <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                                </div>
                                <div class="educator-text">
                                    <span class="educator-name">Leah Alexander</span>
                                    <span class="educator-sub">Senior Physics Mentor · SafeTutor</span>
                                </div>
                            </div>
                            <div class="rating-badge">
                                <span>★ 4.95</span>
                            </div>
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

print("Apple-grade banner generated successfully!")
