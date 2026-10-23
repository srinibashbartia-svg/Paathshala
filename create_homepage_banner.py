import re

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/homepage-section.html", "r") as f:
    html = f.read()

# Let's replace the .guided-learning-section CSS with sleek, modern BANNER styles
banner_css = '''
        /* =========================================================================
           GUIDED LEARNING FLAGSHIP HOMEPAGE BANNER
           ========================================================================= */
        .guided-learning-banner-wrapper {
            max-width: 1220px;
            margin: 20px auto 60px;
            padding: 0 20px;
        }

        .guided-learning-banner {
            background: linear-gradient(135deg, #FAF7F2 0%, #FFFDF9 100%);
            border: 2.5px solid #18181B;
            border-radius: 28px;
            box-shadow: 7px 7px 0px #18181B;
            padding: 36px 40px;
            position: relative;
            overflow: hidden;
            display: grid;
            grid-template-columns: 1.25fr 0.85fr;
            gap: 36px;
            align-items: center;
        }

        /* BANNER AMBIENT ACCENTS */
        .banner-glow-1 {
            position: absolute;
            top: -60px;
            right: -60px;
            width: 220px;
            height: 220px;
            background: radial-gradient(circle, rgba(95, 90, 246, 0.18) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }

        .banner-glow-2 {
            position: absolute;
            bottom: -40px;
            left: 20%;
            width: 180px;
            height: 180px;
            background: radial-gradient(circle, rgba(235, 108, 80, 0.15) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }

        /* LEFT CONTENT COLUMN */
        .banner-content-col {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .banner-tag-row {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .banner-badge-primary {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #5458F7;
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.76rem;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            padding: 5px 12px;
            border-radius: 9999px;
            border: 1.5px solid #18181B;
            box-shadow: 2px 2px 0px #18181B;
        }

        .banner-badge-grade {
            background: #FFD25E;
            color: #18181B;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.74rem;
            padding: 4px 12px;
            border-radius: 9999px;
            border: 1.5px solid #18181B;
            box-shadow: 2px 2px 0px #18181B;
        }

        .banner-headline {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(1.85rem, 3.2vw, 2.75rem);
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -0.02em;
            color: #18181B;
            margin: 0;
        }

        .banner-headline span.accent-highlight {
            color: #5458F7;
            position: relative;
            display: inline-block;
        }

        .banner-simple-explainer {
            font-size: 1.05rem;
            line-height: 1.55;
            color: #475569;
            max-width: 620px;
            margin: 0;
        }

        .banner-simple-explainer strong {
            color: #18181B;
        }

        /* 4-PILLAR CONCISE FEATURE TILES */
        .banner-pillars-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin: 6px 0;
        }

        .pillar-card {
            background: #FFFFFF;
            border: 2px solid #18181B;
            border-radius: 14px;
            padding: 12px 14px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            box-shadow: 3px 3px 0px #18181B;
            transition: transform 0.15s;
        }

        .pillar-card:hover {
            transform: translate(-1.5px, -1.5px);
            box-shadow: 4.5px 4.5px 0px #18181B;
        }

        .pillar-icon-box {
            font-size: 1.35rem;
            line-height: 1;
            flex-shrink: 0;
            margin-top: 2px;
        }

        .pillar-text-group {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .pillar-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.92rem;
            color: #18181B;
        }

        .pillar-desc {
            font-size: 0.78rem;
            color: #64748B;
            line-height: 1.35;
            font-weight: 500;
        }

        /* BANNER ACTION BUTTONS */
        .banner-actions {
            display: flex;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 6px;
        }

        .btn-banner-primary {
            background: #5458F7;
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.98rem;
            padding: 12px 24px;
            border-radius: 14px;
            border: 2px solid #18181B;
            box-shadow: 4px 4px 0px #18181B;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease;
        }

        .btn-banner-primary:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px #18181B;
            background: #464AE0;
        }

        .btn-banner-secondary {
            background: #FAF7F2;
            color: #18181B;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 12px 20px;
            border-radius: 14px;
            border: 2px solid #18181B;
            box-shadow: 3px 3px 0px #18181B;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s ease;
        }

        .btn-banner-secondary:hover {
            background: #FFFFFF;
            transform: translate(-2px, -2px);
            box-shadow: 5px 5px 0px #18181B;
        }

        /* RIGHT VISUAL COLUMN (LIVE MINI CARD PREVIEW) */
        .banner-visual-col {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .banner-preview-card {
            background: #FFFFFF;
            border: 2.5px solid #18181B;
            border-radius: 20px;
            box-shadow: 6px 6px 0px #18181B;
            padding: 16px;
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .banner-reel-clip {
            width: 100%;
            height: 180px;
            border-radius: 14px;
            border: 2px solid #18181B;
            overflow: hidden;
            position: relative;
            background: #0F172A;
            box-shadow: 2px 2px 0px #18181B;
        }

        .banner-reel-clip video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .banner-clip-badge {
            position: absolute;
            top: 8px;
            left: 8px;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(4px);
            color: #FFFFFF;
            font-size: 0.68rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            gap: 5px;
            letter-spacing: 0.3px;
        }

        .banner-clip-dur {
            position: absolute;
            bottom: 8px;
            right: 8px;
            background: #EB6C50;
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 0.7rem;
            padding: 2px 7px;
            border-radius: 6px;
        }

        .banner-tutor-meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }

        .banner-tutor-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .banner-tutor-avatar {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            border: 2px solid #18181B;
            overflow: hidden;
            flex-shrink: 0;
            background: #FEF08A;
        }

        .banner-tutor-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .banner-tutor-details {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .banner-tutor-name {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.92rem;
            color: #18181B;
        }

        .banner-tutor-sub {
            font-size: 0.76rem;
            color: #64748B;
            font-weight: 600;
        }

        .banner-rating-pill {
            background: #FEF08A;
            border: 1.5px solid #18181B;
            padding: 3px 8px;
            border-radius: 8px;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.78rem;
            color: #18181B;
            box-shadow: 1.5px 1.5px 0px #18181B;
            white-space: nowrap;
        }

        /* RESPONSIVE BANNER BREAKPOINTS */
        @media (max-width: 960px) {
            .guided-learning-banner {
                grid-template-columns: 1fr;
                padding: 28px 24px;
                gap: 28px;
            }
            .banner-pillars-grid {
                grid-template-columns: 1fr;
            }
        }
'''

# 1. Inject or update the CSS in homepage-section.html
css_pattern = r'\/\* =========================================================================\s*FLAGSHIP GUIDED LEARNING HOMEPAGE SECTION[\s\S]*?\/\* RESPONSIVE ADJUSTMENTS'
html = re.sub(css_pattern, banner_css + '\n        /* RESPONSIVE ADJUSTMENTS', html)

# 2. Build the Banner Markup that clearly and concisely explains what it is without missing anything
banner_markup = '''    <!-- =========================================================================
         FLAGSHIP GUIDED LEARNING HOMEPAGE BANNER
         ========================================================================= -->
    <div class="guided-learning-banner-wrapper" id="guidedLearningSection">
        <div class="guided-learning-banner">
            
            <div class="banner-glow-1"></div>
            <div class="banner-glow-2"></div>

            <!-- LEFT: EXPLAINER & 4 ESSENTIAL PILLARS -->
            <div class="banner-content-col">
                
                <div class="banner-tag-row">
                    <span class="banner-badge-primary">✨ New Feature · Guided Learning</span>
                    <span class="banner-badge-grade">Classes 1 to 12 · CBSE & ICSE</span>
                </div>

                <h2 class="banner-headline">
                    Don't let them get stuck.<br>
                    Give them a <span class="accent-highlight">personal guide.</span>
                </h2>

                <p class="banner-simple-explainer">
                    <strong>What is Guided Learning?</strong> Not a crowded batch, not a pre-recorded video. 
                    It is <strong>dedicated 1-on-1 live teaching</strong> tailored to where your child gets stuck, 
                    backed by <strong>60-second video breakthrough moments</strong> and <strong>24/7 AI practice</strong>.
                </p>

                <!-- THE 4 COMPLETE PILLARS (NOTHING MISSED, VERY CONCISE) -->
                <div class="banner-pillars-grid">
                    
                    <div class="pillar-card">
                        <div class="pillar-icon-box">🧑‍🏫</div>
                        <div class="pillar-text-group">
                            <span class="pillar-title">Live 1-on-1 Mentorship</span>
                            <span class="pillar-desc">Top 1.4% dedicated tutor teaching live at your child's exact learning pace.</span>
                        </div>
                    </div>

                    <div class="pillar-card">
                        <div class="pillar-icon-box">🎯</div>
                        <div class="pillar-text-group">
                            <span class="pillar-title">60-Second "Aha!" Reels</span>
                            <span class="pillar-desc">Key breakthrough moments clipped from real classes for 1-minute visual recap.</span>
                        </div>
                    </div>

                    <div class="pillar-card">
                        <div class="pillar-icon-box">🤖</div>
                        <div class="pillar-text-group">
                            <span class="pillar-title">24/7 Mitra AI Tutor</span>
                            <span class="pillar-desc">Ask doubts, solve practice questions, and revise anytime between live classes.</span>
                        </div>
                    </div>

                    <div class="pillar-card">
                        <div class="pillar-icon-box">📹</div>
                        <div class="pillar-text-group">
                            <span class="pillar-title">Zero Knowledge Lost</span>
                            <span class="pillar-desc">Every full session recorded and annotated whiteboard saved forever.</span>
                        </div>
                    </div>

                </div>

                <!-- ACTIONS -->
                <div class="banner-actions">
                    <a href="/landing.html" class="btn-banner-primary">
                        <span>Explore Guided Learning</span>
                        <span>➔</span>
                    </a>
                    <a href="https://paathshala.app/booking" target="_blank" class="btn-banner-secondary">
                        <span>Book Free 1-on-1 Class</span>
                    </a>
                </div>

            </div>

            <!-- RIGHT: LIVE INTERACTIVE PREVIEW CARD -->
            <div class="banner-visual-col">
                <div class="banner-preview-card">
                    
                    <div class="banner-reel-clip">
                        <video autoplay loop muted playsinline preload="auto" poster="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg">
                            <source src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/reels/6acca1a0fa97e5183b039237-r1.mp4" type="video/mp4">
                        </video>
                        <div class="banner-clip-badge">
                            <span>● Live Class Highlight</span>
                        </div>
                        <span class="banner-clip-dur">0:50</span>
                    </div>

                    <div class="banner-tutor-meta">
                        <div class="banner-tutor-info">
                            <div class="banner-tutor-avatar">
                                <img src="https://storage.googleapis.com/paathshala-storage/recordings/6acca1a0fa97e5183b039237/thumbnails/reel_6acca1a0fa97e5183b039237-r1.jpg" alt="Leah Alexander">
                            </div>
                            <div class="banner-tutor-details">
                                <span class="banner-tutor-name">Leah Alexander</span>
                                <span class="banner-tutor-sub">Senior Physics Educator · Top 1.4%</span>
                            </div>
                        </div>
                        <div class="banner-rating-pill">★ 4.95</div>
                    </div>

                    <a href="https://paathshala.app/user-profile?publicId=alchemist-589748" target="_blank" style="text-decoration:none; font-size:0.8rem; font-weight:800; color:#5458F7; text-align:center; padding-top:4px; display:block;">
                        View Teacher Profile & 1-on-1 Schedule ➔
                    </a>

                </div>
            </div>

        </div>
    </div>'''

# Replace the old section markup
markup_pattern = r'<section class="guided-learning-section dotted-paper-bg" id="guidedLearningSection">[\s\S]*?<\/section>'
html = re.sub(markup_pattern, banner_markup, html)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/homepage-section.html", "w") as f:
    f.write(html)

print("Homepage section updated to a concise, complete Guided Learning banner!")
