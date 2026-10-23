import sys, os

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/leah_avatar.txt", "r") as f:
    avatar_b64 = f.read().strip()

homepage_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala Home · Featuring Guided Learning Section</title>
    <meta name="description" content="Paathshala 1-on-1 live tutoring with India's top 1.4% tutors. Now featuring 60-second Guided Learning concept reels.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-cream: #FFFDF9;
            --primary: #5F5AF6;
            --primary-hover: #4B45E8;
            --coral: #EB6C50;
            --coral-hover: #D75A3E;
            --dark: #18181B;
            --text-main: #18181B;
            --text-muted: #64748B;
            --border-dark: #272727;
            --radius-card: 20px;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-cream);
            color: var(--text-main);
            overflow-x: hidden;
            line-height: 1.5;
        }}

        .dotted-paper-bg {{
            background-image: radial-gradient(#d4cfc5 1.5px, transparent 1.5px);
            background-size: 24px 24px;
        }}

        /* TOP PROTOTYPE BAR */
        .prototype-banner {{
            background: #111827;
            color: #E2E8F0;
            padding: 8px 16px;
            font-size: 0.8rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.12);
            position: sticky;
            top: 0;
            z-index: 9999;
        }}
        .prototype-badge {{
            background: #10B981;
            color: #FFFFFF;
            padding: 2px 8px;
            border-radius: 6px;
            font-weight: 800;
            font-size: 0.7rem;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }}
        .prototype-links {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .prototype-link-btn {{
            color: #93C5FD;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.78rem;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 8px;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.08);
            transition: all 0.2s;
        }}
        .prototype-link-btn:hover {{
            background: rgba(255, 255, 255, 0.2);
            color: #FFFFFF;
        }}
        .prototype-link-btn.active {{
            background: #10B981;
            color: #FFFFFF;
        }}

        /* VIEW SWITCHER IN TOOLBAR */
        .view-mode-toggle {{
            display: inline-flex;
            background: rgba(255, 255, 255, 0.12);
            border-radius: 8px;
            padding: 2px;
            gap: 2px;
        }}
        .mode-btn {{
            background: none;
            border: none;
            color: #CBD5E1;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .mode-btn.active {{
            background: #FFFFFF;
            color: #0F172A;
        }}

        /* PAATHSHALA HOMEPAGE HEADER */
        header.homepage-header {{
            background: rgba(255, 253, 249, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 2px solid #272727;
            position: sticky;
            top: 36px;
            z-index: 1000;
            height: 70px;
        }}
        .nav-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .nav-logo {{
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: #272727;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.45rem;
        }}
        .nav-logo-box {{
            width: 38px;
            height: 38px;
            border: 2px solid #272727;
            border-radius: 10px;
            padding: 4px;
            background: #FFFFFF;
        }}
        .nav-links {{
            display: flex;
            align-items: center;
            gap: 24px;
            list-style: none;
        }}
        .nav-links a {{
            color: #272727;
            text-decoration: none;
            font-weight: 700;
            font-size: 0.92rem;
            transition: color 0.15s;
        }}
        .nav-links a:hover {{
            color: var(--primary);
        }}
        .btn-trial-nav {{
            background: var(--coral);
            color: #FFFFFF;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.92rem;
            padding: 9px 18px;
            border-radius: 12px;
            border: 2px solid #272727;
            box-shadow: 0 3px 0 #272727;
            transition: all 0.15s;
        }}
        .btn-trial-nav:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 0 #272727;
        }}

        /* CONDENSED HOMEPAGE HERO (FOR CONTEXT) */
        .hero-context-preview {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 24px 30px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 16px;
        }}
        .hero-tag-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #FEF08A;
            border: 2px solid #272727;
            border-radius: 9999px;
            padding: 4px 14px;
            font-weight: 800;
            font-size: 0.8rem;
            box-shadow: 0 2px 0 #272727;
        }}
        .hero-title-main {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.2rem, 4vw, 3.8rem);
            font-weight: 900;
            line-height: 1.1;
            letter-spacing: -0.02em;
            max-width: 900px;
        }}
        .hero-title-main span.coral {{
            color: var(--coral);
        }}

        /* =========================================================================
           FLAGSHIP GUIDED LEARNING HOMEPAGE SECTION
           ========================================================================= */
        section.guided-learning-section {{
            padding: 60px 0 80px;
            border-top: 3px solid #272727;
            border-bottom: 3px solid #272727;
            position: relative;
            background-color: #FAF8F5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }}
        .section-header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        .section-tag {{
            font-family: 'Outfit', sans-serif;
            font-size: 0.82rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #5F5AF6;
            background: #EDE9FE;
            border: 2px solid #272727;
            border-radius: 9999px;
            padding: 4px 14px;
            display: inline-block;
            box-shadow: 0 2px 0 #272727;
            margin-bottom: 12px;
        }}
        .section-title {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2rem, 3.4vw, 2.9rem);
            font-weight: 900;
            letter-spacing: -0.02em;
            color: #18181B;
            line-height: 1.15;
        }}
        .section-desc {{
            color: var(--text-muted);
            margin-top: 12px;
            font-size: 1.05rem;
            max-width: 680px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.5;
        }}

        /* SECTION TABS FOR GRADE SELECTION */
        .grade-tabs-bar {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 36px;
        }}
        .grade-tab-btn {{
            background: #FFFFFF;
            border: 2px solid #272727;
            border-radius: 12px;
            padding: 8px 18px;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.92rem;
            color: #272727;
            cursor: pointer;
            box-shadow: 0 3px 0 #272727;
            transition: all 0.15s ease;
        }}
        .grade-tab-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 0 #272727;
            background: #F8FAFC;
        }}
        .grade-tab-btn.active {{
            background: #5F5AF6;
            color: #FFFFFF;
            box-shadow: 0 4px 0 #272727;
        }}

        /* MAIN TWO-COLUMN SECTION CARD */
        .section-main-card {{
            background: #FFFFFF;
            border: 3px solid #272727;
            border-radius: 32px;
            box-shadow: 0 12px 0 #272727;
            padding: 36px;
            display: grid;
            grid-template-columns: 360px 1fr;
            gap: 36px;
            align-items: center;
        }}

        /* SMARTPHONE PHONE MOCKUP FOR REEL PLAYBACK */
        .phone-mockup-wrapper {{
            display: flex;
            justify-content: center;
        }}
        .phone-frame {{
            width: 320px;
            aspect-ratio: 9 / 18;
            background: #0F172A;
            border: 4px solid #272727;
            border-radius: 36px;
            box-shadow: 0 10px 0 #272727;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            user-select: none;
        }}
        .phone-notch {{
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 90px;
            height: 18px;
            background: #272727;
            border-radius: 10px;
            z-index: 20;
        }}
        .phone-video-screen {{
            position: absolute;
            inset: 0;
            background: #0B1120;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        /* SIMULATED ANIMATED VISUAL IN PHONE SCREEN */
        .phone-visual-scene {{
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            text-align: center;
        }}

        /* PHONE OVERLAYS */
        .phone-top-bar {{
            position: relative;
            z-index: 10;
            padding: 34px 14px 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(180deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%);
        }}
        .phone-live-tag {{
            background: rgba(235, 108, 80, 0.9);
            color: #FFFFFF;
            font-size: 0.68rem;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            text-transform: uppercase;
        }}
        .phone-sound-btn {{
            background: rgba(0, 0, 0, 0.6);
            border: 1.5px solid rgba(255, 255, 255, 0.4);
            color: #FFFFFF;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.8rem;
        }}

        .phone-center-play {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            cursor: pointer;
        }}
        .phone-play-btn {{
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.65);
            border: 2px solid #FFFFFF;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            transition: all 0.2s;
        }}
        .phone-play-btn:hover {{
            background: #EB6C50;
            transform: scale(1.1);
        }}

        .phone-bottom-bar {{
            position: relative;
            z-index: 10;
            padding: 14px;
            background: linear-gradient(0deg, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.4) 70%, rgba(0,0,0,0) 100%);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .phone-caption {{
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 6px 10px;
            font-size: 0.78rem;
            color: #FFFFFF;
            line-height: 1.35;
        }}
        .phone-caption strong {{
            color: #FEF08A;
        }}
        .phone-progress-row {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .phone-progress-bar {{
            flex: 1;
            height: 5px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 9999px;
            overflow: hidden;
            position: relative;
        }}
        .phone-progress-fill {{
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 55%;
            background: #EB6C50;
            border-radius: 9999px;
        }}
        .phone-time-text {{
            font-size: 0.68rem;
            font-weight: 700;
            color: rgba(255, 255, 255, 0.75);
        }}

        /* RIGHT DETAILS & PLAYLIST COLUMN */
        .section-content-col {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .selected-reel-header {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .selected-pill-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .badge-pill {{
            font-family: 'Outfit', sans-serif;
            font-size: 0.75rem;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 8px;
            border: 2px solid #272727;
            box-shadow: 0 2px 0 #272727;
        }}
        .badge-pill.aha {{
            background: #EB6C50;
            color: #FFFFFF;
        }}
        .badge-pill.grade {{
            background: #FEF08A;
            color: #272727;
        }}
        .selected-reel-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.75rem;
            line-height: 1.2;
            color: #0F172A;
        }}
        .selected-reel-quote {{
            background: #FFFBEB;
            border-left: 4px solid #F59E0B;
            border-radius: 0 12px 12px 0;
            padding: 10px 14px;
            font-size: 0.95rem;
            line-height: 1.45;
            color: #78350F;
            font-style: italic;
        }}

        /* INTERACTIVE PLAYLIST CAROUSEL */
        .playlist-title-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 6px;
        }}
        .playlist-title-row h4 {{
            font-family: 'Outfit', sans-serif;
            font-size: 0.98rem;
            font-weight: 800;
            color: #18181B;
        }}
        .playlist-row {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }}
        .playlist-item-card {{
            background: #F8FAFC;
            border: 2px solid #272727;
            border-radius: 14px;
            box-shadow: 0 3px 0 #272727;
            padding: 10px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .playlist-item-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 0 #272727;
            background: #F1F5F9;
        }}
        .playlist-item-card.active {{
            background: #FEF08A;
            border-color: #272727;
            box-shadow: 0 4px 0 #272727;
        }}
        .playlist-thumb-box {{
            width: 100%;
            aspect-ratio: 16 / 10;
            background: #1E293B;
            border-radius: 8px;
            border: 1.5px solid #272727;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            position: relative;
        }}
        .playlist-dur {{
            position: absolute;
            bottom: 4px;
            right: 4px;
            background: rgba(0, 0, 0, 0.7);
            color: #FFFFFF;
            font-size: 0.65rem;
            font-weight: 800;
            padding: 1px 4px;
            border-radius: 4px;
        }}
        .playlist-item-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.78rem;
            line-height: 1.25;
            color: #0F172A;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        .playlist-item-teacher {{
            font-size: 0.7rem;
            font-weight: 700;
            color: #64748B;
        }}

        /* TEACHER COMPONENT & DUAL CTAS */
        .section-teacher-strip {{
            background: #F0FDF4;
            border: 2px solid #272727;
            border-radius: 16px;
            box-shadow: 0 3px 0 #272727;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .strip-teacher-left {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .strip-teacher-avatar {{
            width: 44px;
            height: 44px;
            border-radius: 12px;
            border: 2px solid #272727;
            overflow: hidden;
            background: #FFFFFF;
        }}
        .strip-teacher-avatar img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .strip-teacher-name {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            color: #0F172A;
        }}
        .strip-teacher-sub {{
            font-size: 0.74rem;
            color: #15803D;
            font-weight: 700;
        }}

        /* ACTION BUTTONS */
        .section-actions-row {{
            display: flex;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
        }}
        .btn-book-from-section {{
            background: #10B981;
            color: #FFFFFF;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 12px 20px;
            border-radius: 12px;
            border: 2px solid #272727;
            box-shadow: 0 4px 0 #272727;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease;
        }}
        .btn-book-from-section:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 0 #272727;
            background: #059669;
        }}
        .btn-explore-landing {{
            background: #FFFFFF;
            color: #272727;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 12px 20px;
            border-radius: 12px;
            border: 2px solid #272727;
            box-shadow: 0 4px 0 #272727;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.15s ease;
        }}
        .btn-explore-landing:hover {{
            background: #FEF08A;
            transform: translateY(-2px);
            box-shadow: 0 6px 0 #272727;
        }}

        /* TRUST STRIP BELOW SECTION */
        .trust-strip-row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 28px;
            flex-wrap: wrap;
            margin-top: 32px;
            font-size: 0.85rem;
            font-weight: 700;
            color: #475569;
        }}
        .trust-item {{
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        /* OTHER HOMEPAGE SECTIONS FOR CONTEXT */
        .context-academics-section {{
            padding: 60px 0;
            text-align: center;
        }}
        .academics-card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        .academic-preview-card {{
            background: #FFFFFF;
            border: 3px solid #272727;
            border-radius: 20px;
            box-shadow: 0 6px 0 #272727;
            padding: 24px;
            text-align: left;
        }}
        .academic-preview-card h3 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.2rem;
            margin-bottom: 8px;
        }}

        @media (max-width: 960px) {{
            .section-main-card {{
                grid-template-columns: 1fr;
            }}
            .phone-mockup-wrapper {{
                margin-bottom: 10px;
            }}
            .playlist-row {{
                grid-template-columns: 1fr 1fr;
            }}
            .nav-links {{
                display: none;
            }}
        }}
        @media (max-width: 600px) {{
            .playlist-row {{
                grid-template-columns: 1fr;
            }}
            .section-main-card {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body class="dotted-paper-bg">

    <!-- TOP PROTOTYPE BAR -->
    <div class="prototype-banner">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span class="prototype-badge">Prototype #2</span>
            <span><strong>Homepage Guided Learning Section</strong> (Embedded into Paathshala.app flow)</span>
        </div>
        <div class="prototype-links">
            <div class="view-mode-toggle">
                <button class="mode-btn active" onclick="setViewMode('flow')">Full Page Flow</button>
                <button class="mode-btn" onclick="setViewMode('isolated')">Section Only</button>
            </div>
            <a href="/index.html" class="prototype-link-btn">⎇ Prototype Hub</a>
            <a href="/landing.html" class="prototype-link-btn">Landing Page</a>
            <a href="/homepage-section.html" class="prototype-link-btn active">Homepage Section</a>
            <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="prototype-link-btn">Original Reel ↗</a>
        </div>
    </div>

    <!-- HOMEPAGE HEADER (STANDARD PAATHSHALA NAVBAR) -->
    <header class="homepage-header" id="pageHeader">
        <div class="nav-container">
            <a href="/" class="nav-logo">
                <div class="nav-logo-box">
                    <svg viewBox="-5.5 -2.5 45 45" fill="none" style="width:100%; height:100%;">
                        <circle cx="16.827" cy="20.95" r="21.5" fill="#FFFFFF" />
                        <path d="M15.3789 1.56641C18.3485 -0.00397233 21.8239 -0.319563 25.0273 0.691406V0.692383C28.099 1.67819 30.6634 3.82668 32.1709 6.67871V6.67969C33.65 9.5688 33.9475 12.9198 33.001 16.0244L33 16.0273C32.7663 16.8763 32.3452 17.8593 31.7959 18.7578C31.2461 19.6571 30.5729 20.4651 29.8379 20.9727L29.8301 20.9785L29.8232 20.9854C29.2171 21.5856 28.6251 22.154 27.9209 22.6201L27.9131 22.626C27.417 23.0235 26.8435 23.281 26.2578 23.5615C23.8896 24.6956 21.2532 25.014 18.6572 25.3838C17.5223 25.5455 16.3713 25.7405 15.2402 25.874L15.1436 25.8857V25.9824C15.1382 26.9792 15.125 28.0164 15.1436 29.0146V29.0195C15.2326 30.5471 15.239 32.7448 14.9053 34.1934C13.8023 38.9792 8.91801 41.328 4.48145 39.2656H4.48047C3.48 38.8053 2.75252 38.2262 2.0791 37.3516L2.07324 37.3457L1.92285 37.1709C0.397689 35.3408 -0.21388 32.689 0.275391 30.3652L0.167969 30.3418L0.276367 30.3652L0.277344 30.3525C0.278271 30.3429 0.278388 30.3323 0.279297 30.3223C0.903668 26.8641 3.29994 24.1185 6.36719 22.4961C6.57023 22.3887 7.15533 22.1484 7.72852 21.9053C8.01263 21.7848 8.29222 21.6643 8.51465 21.5615C8.62571 21.5102 8.72387 21.4623 8.80176 21.4209C8.87621 21.3814 8.94258 21.3425 8.98145 21.3076L9.01953 21.2734L9.01758 21.2227C8.99171 20.3933 8.98483 19.563 8.99609 18.7334C9.00396 17.9678 8.98779 17.1376 8.97266 16.2813C8.95751 15.4242 8.94299 14.5395 8.95312 13.6621C8.97343 11.9056 9.09309 10.1855 9.5 8.77832C10.3637 5.7917 12.3812 3.2335 15.1123 1.71094L15.3789 1.56641Z" fill="#5F5AF6" stroke="black" stroke-width="0.22"/>
                        <path d="M27.142 13.0609L27.3185 13.0612C27.6183 13.0878 27.9587 13.1253 28.1817 13.3206C30.8965 15.699 31.0252 18.9068 29.2136 21.755C28.9327 22.1967 28.2947 22.2791 28.2108 22.7999C27.611 23.2069 26.9192 23.4699 26.2332 23.7481C23.4164 24.8906 20.2822 25.2101 17.2249 25.579C15.8905 25.74 14.8158 26.2706 13.4793 26.4041C11.7112 26.6422 8.30149 30.1145 6.60504 30.5874C6.60829 30.4183 6.91796 27.3761 7.84467 25.579C9.43249 22.4998 11.9016 21.1201 14.734 19.8646C15.0803 19.6812 15.3437 19.6949 15.6625 19.4302L15.5989 19.3706C15.8376 19.2941 17.1559 19.1762 17.4724 19.137C22.4276 18.5234 26.1931 17.7941 27.142 13.0609Z" fill="#E87257"/>
                    </svg>
                </div>
                <span>Paathshala</span>
            </a>
            <ul class="nav-links">
                <li><a href="#guidedLearningSection">✨ Guided Learning</a></li>
                <li><a href="/classes">Find Tutors</a></li>
                <li><a href="/ai-career-predictor">Bhavishya Predictor</a></li>
                <li><a href="/pricing">Pricing</a></li>
            </ul>
            <a href="https://paathshala.app/free-trial" target="_blank" class="btn-trial-nav">Book Free Trial</a>
        </div>
    </header>

    <!-- SURROUNDING HOMEPAGE HERO (FOR PAGE FLOW PERSPECTIVE) -->
    <div id="homepageHeroPreview" class="hero-context-preview">
        <div class="hero-tag-badge">
            <span>🇮🇳 INDIA'S MOST LOVED 1-ON-1 ONLINE SCHOOL</span>
        </div>
        <h1 class="hero-title-main">
            Where your child falls in love with learning, <span class="coral">one concept at a time.</span>
        </h1>
        <p style="color: #64748B; font-size: 1.1rem; max-width: 650px;">
            Personalized 1-on-1 tutoring designed for ICSE, CBSE, and Cambridge students. Taught exclusively by the top 1.4% educators in India.
        </p>
    </div>

    <!-- =========================================================================
         FLAGSHIP GUIDED LEARNING HOMEPAGE SECTION
         ========================================================================= -->
    <section class="guided-learning-section dotted-paper-bg" id="guidedLearningSection">
        <div class="container">
            
            <div class="section-header">
                <p class="section-tag">✨ NEW: GUIDED LEARNING REELS</p>
                <h2 class="section-title">60-Second "Aha!" Moments From Real Classes</h2>
                <p class="section-desc">
                    Experience how our top 1.4% tutors transform complex textbook theories into simple, visual breakthroughs in under 60 seconds. Pick a class to preview live highlights:
                </p>
            </div>

            <!-- GRADE LEVEL SELECTOR TABS -->
            <div class="grade-tabs-bar">
                <button class="grade-tab-btn active" onclick="setSectionGrade(this, 'all')">🌟 All Highlights</button>
                <button class="grade-tab-btn" onclick="setSectionGrade(this, 'primary')">Primary (Classes 1–5)</button>
                <button class="grade-tab-btn" onclick="setSectionGrade(this, 'middle')">Middle School (Classes 6–8)</button>
                <button class="grade-tab-btn" onclick="setSectionGrade(this, 'secondary')">High School (Classes 9–12)</button>
            </div>

            <!-- TWO COLUMN SECTION CARD -->
            <div class="section-main-card">
                
                <!-- LEFT: SMARTPHONE MOCKUP -->
                <div class="phone-mockup-wrapper">
                    <div class="phone-frame">
                        <div class="phone-notch"></div>
                        
                        <!-- SCREEN VISUAL CANVAS -->
                        <div class="phone-video-screen">
                            <div class="phone-visual-scene" id="phoneVisual">
                                <div style="font-size: 4rem; animation: pulse 2s infinite;">⚛️</div>
                                <div style="color: #FEF08A; font-family:'Outfit',sans-serif; font-weight:800; font-size:1.1rem; margin-top:8px;">
                                    Nuclear Glue
                                </div>
                            </div>
                        </div>

                        <!-- PHONE TOP CONTROLS -->
                        <div class="phone-top-bar">
                            <span class="phone-live-tag">Live Reel Clip</span>
                            <button class="phone-sound-btn" onclick="togglePhoneAudio(this)">🔊</button>
                        </div>

                        <!-- PHONE CENTER PLAY BUTTON -->
                        <div class="phone-center-play" onclick="togglePhonePlay()">
                            <div class="phone-play-btn" id="phonePlayIcon">⏸</div>
                        </div>

                        <!-- PHONE BOTTOM CONTROLS & SUBTITLES -->
                        <div class="phone-bottom-bar">
                            <div class="phone-caption" id="phoneSubtitle">
                                <strong>Leah:</strong> "They act like nuclear glue, holding the protons together so they don't push each other away."
                            </div>
                            <div class="phone-progress-row">
                                <div class="phone-progress-bar">
                                    <div class="phone-progress-fill" id="phoneFill"></div>
                                </div>
                                <span class="phone-time-text" id="phoneTimer">0:24 / 0:50</span>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- RIGHT: REEL DETAILS & INTERACTIVE PLAYLIST -->
                <div class="section-content-col">
                    
                    <div class="selected-reel-header">
                        <div class="selected-pill-row">
                            <span class="badge-pill aha" id="secBadgeCategory">🎯 Aha Moment!</span>
                            <span class="badge-pill grade" id="secBadgeGrade">Class 8–9 · Physics</span>
                            <span class="badge-pill" id="secBadgeDuration">⏱ 50 Seconds</span>
                        </div>
                        <h3 class="selected-reel-title" id="secReelTitle">The 'Nuclear Glue' Inside an Atom</h3>
                        <div class="selected-reel-quote" id="secReelQuote">
                            “They act like nuclear glue, holding the protons together so they don't push each other away.”
                        </div>
                    </div>

                    <!-- PLAYLIST ROW -->
                    <div class="playlist-title-row">
                        <h4>Tap to preview other class moments:</h4>
                        <span style="font-size:0.75rem; color:#64748B; font-weight:700;">3 of 150+ Reels</span>
                    </div>

                    <div class="playlist-row" id="sectionPlaylistContainer">
                        
                        <div class="playlist-item-card active" onclick="selectSectionReel(0)">
                            <div class="playlist-thumb-box">
                                <span>⚛️</span>
                                <span class="playlist-dur">0:50</span>
                            </div>
                            <div class="playlist-item-title">The 'Nuclear Glue' Inside an Atom</div>
                            <div class="playlist-item-teacher">Leah Alexander · 4.95 ★</div>
                        </div>

                        <div class="playlist-item-card" onclick="selectSectionReel(1)">
                            <div class="playlist-thumb-box">
                                <span>🌌</span>
                                <span class="playlist-dur">0:58</span>
                            </div>
                            <div class="playlist-item-title">You Are 99.999% Empty Space!</div>
                            <div class="playlist-item-teacher">Leah Alexander · 4.95 ★</div>
                        </div>

                        <div class="playlist-item-card" onclick="selectSectionReel(2)">
                            <div class="playlist-thumb-box">
                                <span>➗</span>
                                <span class="playlist-dur">0:42</span>
                            </div>
                            <div class="playlist-item-title">Multiply Any 2-Digit in 3 Seconds</div>
                            <div class="playlist-item-teacher">Nikita Arvey · 4.99 ★</div>
                        </div>

                    </div>

                    <!-- TEACHER PROFILE STRIP -->
                    <div class="section-teacher-strip">
                        <div class="strip-teacher-left">
                            <div class="strip-teacher-avatar">
                                <img src="data:image/jpeg;base64,{avatar_b64}" alt="Teacher" id="secTeacherImg">
                            </div>
                            <div>
                                <div class="strip-teacher-name" id="secTeacherName">Leah Alexander</div>
                                <div class="strip-teacher-sub" id="secTeacherSub">✓ SafeTutor Certified · 148 Verified Reviews</div>
                            </div>
                        </div>
                        <div style="font-size: 0.85rem; font-weight: 800; color: #0369A1;">
                            ★ 4.95 Parent Rating
                        </div>
                    </div>

                    <!-- DUAL CALL TO ACTION -->
                    <div class="section-actions-row">
                        <a href="https://paathshala.app/booking?teacherId=d2dOWorLt4QEmqARukBjIayAknk1" target="_blank" class="btn-book-from-section" id="btnBookTeacherSection">
                            <span>📅</span>
                            <span>Book Free Class with Leah</span>
                        </a>
                        <a href="/landing.html" class="btn-explore-landing">
                            <span>Explore 150+ Concept Reels</span>
                            <span>➔</span>
                        </a>
                    </div>

                </div>

            </div>

            <!-- TRUST STRIP -->
            <div class="trust-strip-row">
                <div class="trust-item">
                    <span>🎬</span>
                    <span>100% Extracted from real 1-on-1 classes</span>
                </div>
                <div class="trust-item">
                    <span>⚡</span>
                    <span>Curated by Paathshala Mitra AI</span>
                </div>
                <div class="trust-item">
                    <span>👩‍🏫</span>
                    <span>Taught exclusively by Top 1.4% Tutors</span>
                </div>
                <div class="trust-item">
                    <span>🆓</span>
                    <span>Completely free with zero ads</span>
                </div>
            </div>

        </div>
    </section>

    <!-- SURROUNDING HOMEPAGE CONTENT (ACADEMICS & MORE FOR FLOW) -->
    <section class="context-academics-section container" id="homepageAcademicsPreview">
        <p class="section-tag">CURRICULUM</p>
        <h2 class="section-title">All Boards & Subjects Covered</h2>
        <div class="academics-card-grid">
            <div class="academic-preview-card">
                <h3>Classes 1 to 5 (Foundations)</h3>
                <p style="color:#64748B; font-size:0.9rem;">Building reading fluency with Phonics, Singapore Math problem-solving, and foundational Science.</p>
            </div>
            <div class="academic-preview-card">
                <h3>Classes 6 to 8 (Middle School)</h3>
                <p style="color:#64748B; font-size:0.9rem;">Mastering algebraic thinking, conceptual Physics, and Chemistry lab preparations with Olympiad coaches.</p>
            </div>
            <div class="academic-preview-card">
                <h3>Classes 9 to 12 (Board & Prep)</h3>
                <p style="color:#64748B; font-size:0.9rem;">CBSE, ICSE & IGCSE board mastery, previous year paper walk-throughs, and competitive edge.</p>
            </div>
        </div>
    </section>

    <!-- JAVASCRIPT FOR HOMEPAGE SECTION -->
    <script>
        const SECTION_REELS = [
            {{
                title: "The 'Nuclear Glue' Inside an Atom",
                category: "🎯 Aha Moment!",
                grade: "Class 8–9 · Physics",
                duration: "⏱ 50 Seconds",
                quote: "“They act like nuclear glue, holding the protons together so they don't push each other away.”",
                teacher: "Leah Alexander",
                teacherRating: "★ 4.95 (148 reviews)",
                sub: "✓ SafeTutor Certified · 148 Verified Reviews",
                teacherBtn: "Book Free Class with Leah",
                bookingUrl: "https://paathshala.app/booking?teacherId=d2dOWorLt4QEmqARukBjIayAknk1",
                emoji: "⚛️",
                conceptTag: "Nuclear Glue",
                subtitle: "Leah: \"They act like nuclear glue, holding the protons together so they don't push each other away.\""
            }},
            {{
                title: "You Are 99.999% Empty Space!",
                category: "🎯 Aha Moment!",
                grade: "Class 9 · Chemistry",
                duration: "⏱ 58 Seconds",
                quote: "“The electrons are tiny specks of dust buzzing around the outer parking lot of the school.”",
                teacher: "Leah Alexander",
                teacherRating: "★ 4.95 (148 reviews)",
                sub: "✓ SafeTutor Certified · 148 Verified Reviews",
                teacherBtn: "Book Free Class with Leah",
                bookingUrl: "https://paathshala.app/booking?teacherId=d2dOWorLt4QEmqARukBjIayAknk1",
                emoji: "🌌",
                conceptTag: "Atomic Scale",
                subtitle: "Leah: \"The electrons are tiny specks of dust buzzing around the outer parking lot of the school.\""
            }},
            {{
                title: "Multiply Any 2-Digit in 3 Seconds",
                category: "💡 Mental Trick",
                grade: "Classes 6–10 · Mental Math",
                duration: "⏱ 42 Seconds",
                quote: "“Cross the diagonals, add the wings, and write the product directly from left to right!”",
                teacher: "Nikita Arvey",
                teacherRating: "★ 4.99 (210 reviews)",
                sub: "✓ Maths & Olympiad Gold Medalist · 210 Reviews",
                teacherBtn: "Book Free Class with Nikita",
                bookingUrl: "https://paathshala.app/classes",
                emoji: "➗",
                conceptTag: "Vedic Math",
                subtitle: "Nikita: \"Cross the diagonals, add the wings, and write the product directly from left to right!\""
            }}
        ];

        let currentSecIdx = 0;
        let phonePlaying = true;
        let phoneProgress = 48;
        let phoneTimerInterval;

        function selectSectionReel(idx) {{
            currentSecIdx = idx;
            const item = SECTION_REELS[idx];
            document.getElementById('secReelTitle').innerText = item.title;
            document.getElementById('secBadgeCategory').innerText = item.category;
            document.getElementById('secBadgeGrade').innerText = item.grade;
            document.getElementById('secBadgeDuration').innerText = item.duration;
            document.getElementById('secReelQuote').innerText = item.quote;
            document.getElementById('secTeacherName').innerText = item.teacher;
            document.getElementById('secTeacherSub').innerText = item.sub;
            document.getElementById('btnBookTeacherSection').querySelector('span:nth-child(2)').innerText = item.teacherBtn;
            document.getElementById('btnBookTeacherSection').href = item.bookingUrl;

            // Visual
            document.getElementById('phoneVisual').innerHTML = `
                <div style="font-size: 4rem; animation: pulse 2s infinite;">${{item.emoji}}</div>
                <div style="color: #FEF08A; font-family:'Outfit',sans-serif; font-weight:800; font-size:1.1rem; margin-top:8px;">
                    ${{item.conceptTag}}
                </div>
            `;
            document.getElementById('phoneSubtitle').innerHTML = item.subtitle;

            // Playlist Active
            document.querySelectorAll('.playlist-item-card').forEach((el, i) => {{
                el.classList.toggle('active', i === idx);
            }});

            phoneProgress = 15;
        }}

        function togglePhonePlay() {{
            phonePlaying = !phonePlaying;
            document.getElementById('phonePlayIcon').innerText = phonePlaying ? '⏸' : '▶';
        }}

        function togglePhoneAudio(btn) {{
            btn.innerText = (btn.innerText === '🔊') ? '🔇' : '🔊';
        }}

        function setSectionGrade(btn, grade) {{
            btn.parentElement.querySelectorAll('.grade-tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            if (grade === 'secondary') selectSectionReel(0);
            else if (grade === 'middle') selectSectionReel(2);
            else if (grade === 'primary') selectSectionReel(1);
        }}

        function setViewMode(mode) {{
            const hero = document.getElementById('homepageHeroPreview');
            const academics = document.getElementById('homepageAcademicsPreview');
            const btns = document.querySelectorAll('.mode-btn');
            
            if (mode === 'isolated') {{
                hero.style.display = 'none';
                academics.style.display = 'none';
                btns[0].classList.remove('active');
                btns[1].classList.add('active');
            }} else {{
                hero.style.display = 'flex';
                academics.style.display = 'block';
                btns[0].classList.add('active');
                btns[1].classList.remove('active');
            }}
        }}

        // Phone loop
        setInterval(() => {{
            if (phonePlaying) {{
                phoneProgress += 1.6;
                if (phoneProgress >= 100) phoneProgress = 0;
                document.getElementById('phoneFill').style.width = phoneProgress + '%';
                const cur = Math.floor((phoneProgress / 100) * 50);
                document.getElementById('phoneTimer').innerText = `0:${{cur < 10 ? '0' : ''}}${{cur}} / 0:50`;
            }}
        }}, 400);
    </script>
</body>
</html>
'''

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/homepage-section.html", "w") as f:
    f.write(homepage_html)

print("Generated homepage-section.html successfully!")
