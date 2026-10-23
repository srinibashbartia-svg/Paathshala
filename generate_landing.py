import sys, os

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/leah_avatar.txt", "r") as f:
    avatar_b64 = f.read().strip()

landing_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala Guided Learning · 60-Second Concept Breakthroughs</title>
    <meta name="description" content="Master complex concepts in 60 seconds with Guided Learning AI. Real 1-on-1 class highlights turned into instant visual breakthroughs by India's top 1.4% tutors.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Kalam:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-indigo: #5458F7;
            --bg-dark: #3F43D4;
            --primary: #4F46E5;
            --primary-hover: #4338CA;
            --coral: #FF5A36;
            --coral-hover: #E84D29;
            --cream-canvas: #FAF7F2;
            --cream-card: #FFFFFF;
            --accent-yellow: #FEF3C7;
            --accent-yellow-border: #F59E0B;
            --emerald: #10B981;
            --text-main: #18181B;
            --text-muted: #64748B;
            --border-dark: #272727;
            --border-light: rgba(255, 255, 255, 0.2);
            --radius-pill: 9999px;
            --radius-card: 24px;
            --radius-canvas: 20px;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }}

        html, body {{
            width: 100%;
            min-height: 100vh;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-indigo);
            background-image: radial-gradient(rgba(255, 255, 255, 0.22) 1.5px, transparent 1.5px);
            background-size: 24px 24px;
            background-attachment: fixed;
            color: #FFFFFF;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }}

        /* TOP PROTOTYPE TOOLBAR */
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
            background: #FF5A36;
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
            background: #4F46E5;
            color: #FFFFFF;
        }}

        /* DEDICATED STICKY HEADER (MATCHING AI PREDICTOR NAV) */
        header.career-nav-header {{
            position: sticky;
            top: 36px;
            z-index: 1000;
            background: rgba(84, 88, 247, 0.94);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.18);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
            width: 100%;
            height: 72px;
        }}
        .career-nav-container {{
            max-width: 1240px;
            margin: 0 auto;
            padding: 0 24px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
        }}
        .career-nav-brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: #FFFFFF;
        }}
        .career-nav-logo-box {{
            width: 40px;
            height: 40px;
            border-radius: 12px;
            background: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 5px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }}
        .career-nav-logo-box svg {{
            width: 100%;
            height: 100%;
        }}
        .career-nav-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.45rem;
            letter-spacing: -0.02em;
            color: #FFFFFF;
        }}
        .career-nav-title span {{
            font-size: 0.82rem;
            font-weight: 700;
            background: rgba(255, 255, 255, 0.2);
            padding: 3px 8px;
            border-radius: 8px;
            margin-left: 8px;
            vertical-align: middle;
            color: #FEF08A;
        }}
        .career-nav-links {{
            display: flex;
            align-items: center;
            gap: 24px;
        }}
        .career-nav-link {{
            color: rgba(255, 255, 255, 0.88);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            transition: color 0.15s;
        }}
        .career-nav-link:hover {{
            color: #FFFFFF;
        }}
        .btn-coral-nav-cta {{
            background: var(--coral);
            color: #FFFFFF;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 10px 20px;
            border-radius: 14px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: 2px solid #272727;
            box-shadow: 0 4px 0 #272727;
            transition: all 0.15s ease;
        }}
        .btn-coral-nav-cta:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 0 #272727;
            background: var(--coral-hover);
        }}

        /* HERO SECTION (INSPIRATION FROM AI PREDICTOR HERO) */
        .career-hero-layout {{
            max-width: 1240px;
            margin: 0 auto;
            padding: 48px 24px 64px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 36px;
        }}
        .hero-tag-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            padding: 6px 16px;
            border-radius: 9999px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            font-size: 0.85rem;
            font-weight: 700;
            color: #FEF08A;
        }}
        .career-hero-center-header h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.4rem, 4.5vw, 4.4rem);
            font-weight: 900;
            letter-spacing: -0.03em;
            line-height: 1.08;
            color: #FFFFFF;
            max-width: 960px;
            margin: 12px 0 16px;
        }}
        .career-hero-center-header h1 span.hl {{
            background: linear-gradient(135deg, #FDE047 0%, #FF5A36 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline-block;
        }}
        .career-hero-center-header p.sub {{
            font-size: clamp(1rem, 1.8vw, 1.25rem);
            line-height: 1.5;
            color: rgba(255, 255, 255, 0.9);
            max-width: 760px;
            margin: 0 auto;
        }}
        .hero-stats-row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 8px;
        }}
        .hero-stat-badge {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 0, 0, 0.22);
            padding: 6px 14px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            font-size: 0.85rem;
            font-weight: 600;
        }}
        .hero-stat-badge strong {{
            color: #FDE047;
            font-weight: 800;
        }}

        /* EDITORIAL REEL CANVAS (MATCHING PREDICTOR QUIZ CANVAS AESTHETIC) */
        .predictor-wrapper {{
            width: 100%;
            max-width: 1140px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }}
        .editorial-quiz-canvas {{
            background: var(--cream-canvas);
            border: 3px solid #272727;
            border-radius: 28px;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.35), 0 8px 0 #272727;
            padding: 24px 28px;
            box-sizing: border-box;
            width: 100%;
            position: relative;
            color: #18181B;
            text-align: left;
        }}
        .editorial-canvas-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 14px;
            border-bottom: 2px dashed #E2E8F0;
        }}
        .editorial-mark-left {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.88rem;
            letter-spacing: 0.04em;
            color: #272727;
            text-transform: uppercase;
        }}
        .editorial-mark-star {{
            color: var(--coral);
            font-size: 1.1rem;
        }}
        .editorial-mark-right {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            color: #64748B;
        }}
        .live-pulse-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #10B981;
            box-shadow: 0 0 0 rgba(16, 185, 129, 0.4);
            animation: pulse-green 1.6s infinite;
        }}
        @keyframes pulse-green {{
            0% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
            70% {{ box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
        }}

        /* FILTER CHIPS (GRADE & SUBJECTS) */
        .canvas-filter-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 24px;
        }}
        .grade-chips-group, .subject-chips-group {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .filter-chip {{
            background: #FFFFFF;
            border: 2px solid #272727;
            border-radius: 12px;
            padding: 6px 14px;
            font-size: 0.82rem;
            font-weight: 700;
            color: #272727;
            cursor: pointer;
            box-shadow: 0 2px 0 #272727;
            transition: all 0.15s ease;
        }}
        .filter-chip:hover {{
            transform: translateY(-1px);
            box-shadow: 0 3px 0 #272727;
            background: #F8FAFC;
        }}
        .filter-chip.active {{
            background: #5458F7;
            color: #FFFFFF;
            box-shadow: 0 3px 0 #272727;
        }}
        .filter-chip.category-active {{
            background: #FEF08A;
            color: #272727;
        }}

        /* THEATER LAYOUT */
        .reel-theater-grid {{
            display: grid;
            grid-template-columns: minmax(320px, 380px) 1fr;
            gap: 28px;
            align-items: start;
        }}

        /* PHONE / VERTICAL REEL PLAYER */
        .reel-player-column {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .reel-device-card {{
            width: 100%;
            aspect-ratio: 9 / 16;
            max-height: 600px;
            background: #0B1120;
            border: 4px solid #272727;
            border-radius: 32px;
            box-shadow: 0 10px 0 #272727;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            user-select: none;
        }}
        .reel-video-canvas {{
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            background: #0F172A;
        }}

        /* SIMULATED ANIMATED CONCEPT VISUALIZATION INSIDE PLAYER */
        .reel-concept-visual {{
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            pointer-events: none;
        }}
        .atom-scene {{
            width: 220px;
            height: 220px;
            position: relative;
            animation: slow-rotate 24s linear infinite;
        }}
        @keyframes slow-rotate {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        .nucleus-core {{
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 74px;
            height: 74px;
            border-radius: 50%;
            background: radial-gradient(circle, #EF4444 30%, #3B82F6 70%);
            box-shadow: 0 0 30px rgba(239, 68, 68, 0.6);
            display: flex;
            align-items: center;
            justify-content: center;
            animation: nucleus-pulse 2s ease-in-out infinite alternate;
        }}
        @keyframes nucleus-pulse {{
            from {{ transform: translate(-50%, -50%) scale(0.95); filter: drop-shadow(0 0 12px #EF4444); }}
            to {{ transform: translate(-50%, -50%) scale(1.05); filter: drop-shadow(0 0 24px #3B82F6); }}
        }}
        .electron-orbit {{
            position: absolute;
            inset: 0;
            border: 2px dashed rgba(255, 255, 255, 0.3);
            border-radius: 50%;
        }}
        .electron-orbit.orbit-2 {{
            transform: rotate(60deg);
        }}
        .electron-orbit.orbit-3 {{
            transform: rotate(120deg);
        }}
        .electron-dot {{
            position: absolute;
            width: 14px;
            height: 14px;
            background: #38BDF8;
            border-radius: 50%;
            box-shadow: 0 0 10px #38BDF8;
            top: -7px;
            left: 50%;
            margin-left: -7px;
        }}

        /* OVERLAY CONTROLS ON REEL PLAYER */
        .reel-player-top {{
            position: relative;
            z-index: 10;
            padding: 18px 16px 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(180deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0) 100%);
        }}
        .reel-brand-tag {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(8px);
            padding: 3px 10px;
            border-radius: 9999px;
            font-size: 0.72rem;
            font-weight: 800;
            color: #FFFFFF;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .reel-sound-btn {{
            background: rgba(0, 0, 0, 0.5);
            border: 2px solid rgba(255, 255, 255, 0.4);
            color: #FFFFFF;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .reel-sound-btn:hover {{
            background: rgba(0,0,0,0.8);
            transform: scale(1.05);
        }}

        .reel-player-center {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            cursor: pointer;
        }}
        .big-play-btn {{
            width: 64px;
            height: 64px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.65);
            border: 3px solid #FFFFFF;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            transition: all 0.2s;
        }}
        .big-play-btn:hover {{
            transform: scale(1.1);
            background: #FF5A36;
        }}

        .reel-player-bottom {{
            position: relative;
            z-index: 10;
            padding: 16px;
            background: linear-gradient(0deg, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.4) 70%, rgba(0,0,0,0) 100%);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .reel-caption-bubble {{
            background: rgba(15, 23, 42, 0.85);
            border: 1.5px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 8px 12px;
            backdrop-filter: blur(8px);
        }}
        .reel-caption-text {{
            font-size: 0.82rem;
            line-height: 1.4;
            color: #F8FAFC;
            font-weight: 600;
        }}
        .reel-caption-text span.speaker {{
            color: #FDE047;
            font-weight: 800;
        }}
        .reel-progress-wrap {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .reel-progress-bar {{
            flex: 1;
            height: 6px;
            background: rgba(255, 255, 255, 0.25);
            border-radius: 9999px;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }}
        .reel-progress-fill {{
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 64%;
            background: #FF5A36;
            border-radius: 9999px;
            transition: width 0.1s linear;
        }}
        .reel-time-lbl {{
            font-size: 0.72rem;
            font-weight: 700;
            color: rgba(255, 255, 255, 0.8);
            font-variant-numeric: tabular-nums;
        }}

        .reel-side-actions {{
            position: absolute;
            right: 12px;
            bottom: 90px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            align-items: center;
            z-index: 15;
        }}
        .reel-action-btn {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
            background: rgba(0, 0, 0, 0.5);
            border: 2px solid rgba(255, 255, 255, 0.3);
            width: 44px;
            height: 44px;
            border-radius: 50%;
            color: #FFFFFF;
            font-size: 1.1rem;
            cursor: pointer;
            justify-content: center;
            transition: all 0.2s;
        }}
        .reel-action-btn:hover {{
            transform: scale(1.1);
            background: rgba(255, 90, 54, 0.9);
        }}
        .reel-action-count {{
            font-size: 0.65rem;
            font-weight: 800;
            color: #FFFFFF;
            text-shadow: 0 1px 3px rgba(0,0,0,0.8);
        }}

        /* DETAILS COLUMN */
        .reel-details-col {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .neo-card {{
            background: #FFFFFF;
            border: 3px solid #272727;
            border-radius: 20px;
            box-shadow: 0 6px 0 #272727;
            padding: 20px;
        }}
        .reel-header-card {{
            background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
        }}
        .meta-pill-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 10px;
        }}
        .tag-pill {{
            background: #FFFFFF;
            border: 2px solid #272727;
            border-radius: 8px;
            padding: 3px 10px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.78rem;
            font-weight: 800;
            color: #272727;
            box-shadow: 0 2px 0 #272727;
        }}
        .tag-pill.aha {{
            background: #FF5A36;
            color: #FFFFFF;
        }}
        .reel-title-main {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.7rem;
            line-height: 1.2;
            color: #0F172A;
            margin-bottom: 12px;
        }}
        .reel-quote-card {{
            background: rgba(255, 255, 255, 0.85);
            border-left: 5px solid #272727;
            border-radius: 0 12px 12px 0;
            padding: 12px 16px;
            font-size: 0.98rem;
            line-height: 1.5;
            color: #1E293B;
            font-style: italic;
            margin-bottom: 10px;
        }}
        .reel-quote-card strong {{
            color: #0F172A;
            font-style: normal;
        }}
        .reel-subtitle-desc {{
            font-size: 0.88rem;
            color: #475569;
            line-height: 1.45;
        }}

        /* TEACHER SPOTLIGHT CARD */
        .teacher-spotlight-card {{
            background: linear-gradient(135deg, #E0F2FE 0%, #BAE6FD 100%);
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}
        .teacher-header-row {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}
        .teacher-avatar-box {{
            width: 64px;
            height: 64px;
            border-radius: 16px;
            border: 3px solid #272727;
            box-shadow: 0 4px 0 #272727;
            overflow: hidden;
            background: #FFFFFF;
            flex-shrink: 0;
        }}
        .teacher-avatar-box img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .teacher-name-box h3 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.25rem;
            color: #0F172A;
            margin-bottom: 4px;
        }}
        .teacher-creds-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            font-size: 0.78rem;
            font-weight: 700;
            color: #0369A1;
        }}
        .badge-verified {{
            background: #FFFFFF;
            border: 2px solid #272727;
            border-radius: 6px;
            padding: 2px 6px;
            font-size: 0.72rem;
            font-weight: 800;
            color: #272727;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .btn-book-teacher {{
            background: #10B981;
            color: #FFFFFF;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1rem;
            padding: 12px 18px;
            border-radius: 14px;
            border: 3px solid #272727;
            box-shadow: 0 4px 0 #272727;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .btn-book-teacher:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 0 #272727;
            background: #059669;
        }}

        /* INTERACTIVE 1-QUESTION COMPREHENSION CHECK */
        .quiz-check-card {{
            background: #F8FAFC;
            border: 3px solid #272727;
            border-radius: 20px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .quiz-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .quiz-tag {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.8rem;
            color: #4F46E5;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}
        .quiz-xp {{
            background: #FEF08A;
            border: 1.5px solid #272727;
            border-radius: 8px;
            padding: 2px 8px;
            font-size: 0.72rem;
            font-weight: 800;
            color: #272727;
        }}
        .quiz-question {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.98rem;
            color: #0F172A;
            line-height: 1.35;
        }}
        .quiz-options-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}
        .quiz-opt-btn {{
            background: #FFFFFF;
            border: 2px solid #CBD5E1;
            border-radius: 12px;
            padding: 8px 10px;
            font-size: 0.82rem;
            font-weight: 700;
            color: #334155;
            cursor: pointer;
            text-align: left;
            transition: all 0.15s;
        }}
        .quiz-opt-btn:hover {{
            border-color: #272727;
            background: #F1F5F9;
        }}
        .quiz-opt-btn.correct {{
            background: #DCFCE7;
            border-color: #10B981;
            color: #15803D;
        }}
        .quiz-opt-btn.wrong {{
            background: #FEE2E2;
            border-color: #EF4444;
            color: #B91C1C;
        }}
        .quiz-feedback-banner {{
            display: none;
            background: #DCFCE7;
            border: 2px solid #16A34A;
            border-radius: 12px;
            padding: 8px 12px;
            font-size: 0.82rem;
            font-weight: 700;
            color: #166534;
            align-items: center;
            gap: 8px;
        }}

        /* RELATED REELS ROW */
        .related-reels-row {{
            display: flex;
            gap: 12px;
            overflow-x: auto;
            padding: 4px 2px 10px;
            scroll-snap-type: x mandatory;
        }}
        .related-reel-card {{
            width: 140px;
            min-width: 140px;
            background: #FFFFFF;
            border: 3px solid #272727;
            border-radius: 16px;
            box-shadow: 0 4px 0 #272727;
            padding: 8px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            cursor: pointer;
            scroll-snap-align: start;
            transition: all 0.15s;
        }}
        .related-reel-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 0 #272727;
        }}
        .related-reel-card.active {{
            background: #FEF08A;
            border-color: #272727;
        }}
        .related-thumb {{
            width: 100%;
            aspect-ratio: 9 / 16;
            border-radius: 10px;
            border: 2px solid #272727;
            background: #1E293B;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .related-thumb-icon {{
            font-size: 1.8rem;
        }}
        .related-title {{
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
        .related-meta {{
            font-size: 0.68rem;
            font-weight: 700;
            color: #64748B;
            display: flex;
            justify-content: space-between;
        }}

        /* CINEMATIC STORY SECTION (INSPIRATION FROM #story IN PREDICTOR) */
        section.story-section {{
            max-width: 1140px;
            margin: 60px auto 40px;
            padding: 0 24px;
        }}
        .story-header-box {{
            text-align: center;
            margin-bottom: 40px;
        }}
        .story-tag {{
            background: rgba(255, 255, 255, 0.2);
            padding: 4px 14px;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 800;
            color: #FEF08A;
            text-transform: uppercase;
        }}
        .story-header-box h2 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: clamp(2rem, 3.5vw, 3rem);
            margin: 12px 0 10px;
        }}
        .story-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
        }}
        .story-card {{
            background: #FFFFFF;
            border: 3px solid #272727;
            border-radius: 24px;
            box-shadow: 0 8px 0 #272727;
            padding: 26px;
            color: #18181B;
            display: flex;
            flex-direction: column;
            gap: 12px;
            position: relative;
        }}
        .story-step-num {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 900;
            color: #CBD5E1;
            line-height: 1;
        }}
        .story-card h3 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.3rem;
            color: #0F172A;
        }}
        .story-card p {{
            font-size: 0.92rem;
            line-height: 1.55;
            color: #475569;
        }}
        .story-visual-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 10px;
            background: #F1F5F9;
            font-size: 0.8rem;
            font-weight: 700;
            color: #1E293B;
            width: fit-content;
            margin-top: auto;
        }}

        /* MARQUEE BANNER */
        .marq-wrap {{
            overflow: hidden;
            white-space: nowrap;
            background: #272727;
            border-top: 3px solid #000000;
            border-bottom: 3px solid #000000;
            padding: 14px 0;
            margin: 60px 0;
            box-shadow: 0 8px 0 rgba(0, 0, 0, 0.2);
        }}
        .marq-content {{
            display: inline-block;
            animation: marq 22s linear infinite;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.3rem;
            color: #FFFFFF;
            letter-spacing: 0.04em;
        }}
        .marq-content span {{ color: #FDE047; }}
        .marq-content em {{ font-style: normal; color: #FF5A36; }}
        @keyframes marq {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }}
        }}

        /* SUBJECT CURATED GRID */
        .curated-library-section {{
            max-width: 1140px;
            margin: 0 auto 60px;
            padding: 0 24px;
        }}
        .library-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 20px;
            margin-top: 24px;
        }}
        .lib-reel-item {{
            background: #FFFFFF;
            border: 3px solid #272727;
            border-radius: 20px;
            box-shadow: 0 6px 0 #272727;
            padding: 14px;
            color: #18181B;
            cursor: pointer;
            transition: all 0.15s;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .lib-reel-item:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 0 #272727;
        }}
        .lib-thumb-box {{
            width: 100%;
            aspect-ratio: 16 / 9;
            background: #0F172A;
            border-radius: 12px;
            border: 2px solid #272727;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
        }}
        .lib-dur-badge {{
            position: absolute;
            bottom: 8px;
            right: 8px;
            background: rgba(0, 0, 0, 0.75);
            color: #FFFFFF;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 6px;
        }}
        .lib-sub-tag {{
            font-size: 0.72rem;
            font-weight: 800;
            color: #4F46E5;
            text-transform: uppercase;
        }}
        .lib-reel-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.95rem;
            line-height: 1.3;
            color: #0F172A;
        }}
        .lib-teacher-snippet {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.78rem;
            color: #64748B;
            font-weight: 600;
            margin-top: auto;
        }}

        /* FAQ ACCORDION */
        .faq-section {{
            max-width: 860px;
            margin: 60px auto;
            padding: 0 24px;
        }}
        .faq-title {{
            text-align: center;
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 900;
            margin-bottom: 24px;
        }}
        .faq-item {{
            background: #FFFFFF;
            border: 3px solid #272727;
            border-radius: 16px;
            box-shadow: 0 4px 0 #272727;
            margin-bottom: 12px;
            overflow: hidden;
        }}
        .faq-item summary {{
            padding: 16px 20px;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            color: #0F172A;
            cursor: pointer;
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .faq-item summary::-webkit-details-marker {{ display: none; }}
        .faq-item summary::after {{
            content: "+";
            font-size: 1.4rem;
            font-weight: 800;
            color: #FF5A36;
        }}
        .faq-item[open] summary::after {{
            content: "−";
        }}
        .faq-item p {{
            padding: 0 20px 18px 20px;
            font-size: 0.92rem;
            line-height: 1.55;
            color: #475569;
        }}

        /* BOTTOM CTA */
        .bottom-cta-banner {{
            max-width: 1140px;
            margin: 60px auto 40px;
            padding: 44px 28px;
            background: linear-gradient(135deg, #FF5A36 0%, #F97316 100%);
            border: 4px solid #272727;
            border-radius: 32px;
            box-shadow: 0 12px 0 #272727;
            text-align: center;
            box-sizing: border-box;
        }}
        .bottom-cta-banner h2 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: clamp(1.8rem, 3.5vw, 2.8rem);
            color: #FFFFFF;
            margin-bottom: 12px;
        }}
        .bottom-cta-banner p {{
            font-size: 1.05rem;
            color: #FEF3C7;
            max-width: 650px;
            margin: 0 auto 28px;
            line-height: 1.5;
        }}
        .cta-buttons-wrap {{
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
        }}
        .btn-cta-main {{
            background: #FFFFFF;
            color: #272727;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            padding: 14px 28px;
            border-radius: 16px;
            border: 3px solid #272727;
            box-shadow: 0 4px 0 #272727;
            transition: all 0.15s ease;
        }}
        .btn-cta-main:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 0 #272727;
            background: #FEF08A;
        }}
        .btn-cta-ghost {{
            background: transparent;
            color: #FFFFFF;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            padding: 14px 28px;
            border-radius: 16px;
            border: 3px solid #FFFFFF;
            box-shadow: 0 4px 0 rgba(0,0,0,0.3);
            transition: all 0.15s ease;
        }}
        .btn-cta-ghost:hover {{
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
        }}

        /* FOOTER (MATCHING PAATHSHALA SIGNATURE FOOTER) */
        footer.landing-footer {{
            background: #111827;
            color: #E2E8F0;
            padding: 50px 24px 20px;
            margin-top: 80px;
            border-top: 3px solid #272727;
            position: relative;
            overflow: hidden;
        }}
        .footer-container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .footer-grid {{
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1.2fr;
            gap: 40px;
            margin-bottom: 40px;
        }}
        .footer-brand h4 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.5rem;
            color: #FFFFFF;
            margin-bottom: 12px;
        }}
        .footer-desc {{
            font-size: 0.88rem;
            color: #94A3B8;
            line-height: 1.55;
            max-width: 360px;
        }}
        .footer-col h5 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1rem;
            color: #FFFFFF;
            margin-bottom: 14px;
        }}
        .footer-links {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .footer-links a {{
            color: #94A3B8;
            text-decoration: none;
            font-size: 0.85rem;
            transition: color 0.15s;
        }}
        .footer-links a:hover {{
            color: #FFFFFF;
        }}
        .footer-big-text-wrap {{
            width: 100%;
            height: 120px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.15;
            user-select: none;
            pointer-events: none;
            margin-top: 20px;
        }}
        .footer-big-text {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: clamp(60px, 12vw, 150px);
            color: #FFFFFF;
            letter-spacing: -0.05em;
        }}

        /* BOOKING MODAL */
        .modal-overlay {{
            position: fixed;
            inset: 0;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(8px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            padding: 20px;
        }}
        .modal-overlay.active {{
            display: flex;
        }}
        .modal-card {{
            background: #FFFFFF;
            border: 4px solid #272727;
            border-radius: 28px;
            box-shadow: 0 16px 0 #272727;
            padding: 28px;
            max-width: 480px;
            width: 100%;
            color: #18181B;
            position: relative;
            animation: popIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        @keyframes popIn {{
            from {{ transform: scale(0.95); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}
        .modal-close-btn {{
            position: absolute;
            top: 20px;
            right: 20px;
            font-size: 1.4rem;
            font-weight: 800;
            color: #272727;
            cursor: pointer;
            border: none;
            background: none;
        }}

        @media (max-width: 900px) {{
            .reel-theater-grid {{
                grid-template-columns: 1fr;
            }}
            .reel-player-column {{
                max-width: 400px;
                margin: 0 auto;
                width: 100%;
            }}
            .footer-grid {{
                grid-template-columns: 1fr 1fr;
            }}
            .career-nav-links {{
                display: none;
            }}
        }}
        @media (max-width: 600px) {{
            .editorial-quiz-canvas {{
                padding: 16px;
                border-radius: 20px;
            }}
            .quiz-options-grid {{
                grid-template-columns: 1fr;
            }}
            .footer-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>

    <!-- TOP PROTOTYPE BAR -->
    <div class="prototype-banner">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span class="prototype-badge">Prototype #1</span>
            <span><strong>Guided Learning Landing Page</strong> (Inspired by AI Predictor Bhavishya Page)</span>
        </div>
        <div class="prototype-links">
            <a href="/index.html" class="prototype-link-btn">⎇ Prototype Hub</a>
            <a href="/landing.html" class="prototype-link-btn active">Landing Page</a>
            <a href="/homepage-section.html" class="prototype-link-btn">Homepage Section</a>
            <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="prototype-link-btn">Original Reel ↗</a>
        </div>
    </div>

    <!-- STICKY HEADER (MATCHING BHAVISHYA PREDICTOR NAV) -->
    <header class="career-nav-header" id="careerNavHeader">
        <div class="career-nav-container">
            <a href="/" class="career-nav-brand">
                <div class="career-nav-logo-box">
                    <svg viewBox="-5.5 -2.5 45 45" fill="none">
                        <circle cx="16.827" cy="20.95" r="21.5" fill="#FFFFFF" />
                        <path d="M15.3789 1.56641C18.3485 -0.00397233 21.8239 -0.319563 25.0273 0.691406V0.692383C28.099 1.67819 30.6634 3.82668 32.1709 6.67871V6.67969C33.65 9.5688 33.9475 12.9198 33.001 16.0244L33 16.0273C32.7663 16.8763 32.3452 17.8593 31.7959 18.7578C31.2461 19.6571 30.5729 20.4651 29.8379 20.9727L29.8301 20.9785L29.8232 20.9854C29.2171 21.5856 28.6251 22.154 27.9209 22.6201L27.9131 22.626C27.417 23.0235 26.8435 23.281 26.2578 23.5615C23.8896 24.6956 21.2532 25.014 18.6572 25.3838C17.5223 25.5455 16.3713 25.7405 15.2402 25.874L15.1436 25.8857V25.9824C15.1382 26.9792 15.125 28.0164 15.1436 29.0146V29.0195C15.2326 30.5471 15.239 32.7448 14.9053 34.1934C13.8023 38.9792 8.91801 41.328 4.48145 39.2656H4.48047C3.48 38.8053 2.75252 38.2262 2.0791 37.3516L2.07324 37.3457L1.92285 37.1709C0.397689 35.3408 -0.21388 32.689 0.275391 30.3652L0.167969 30.3418L0.276367 30.3652L0.277344 30.3525C0.278271 30.3429 0.278388 30.3323 0.279297 30.3223C0.903668 26.8641 3.29994 24.1185 6.36719 22.4961C6.57023 22.3887 7.15533 22.1484 7.72852 21.9053C8.01263 21.7848 8.29222 21.6643 8.51465 21.5615C8.62571 21.5102 8.72387 21.4623 8.80176 21.4209C8.87621 21.3814 8.94258 21.3425 8.98145 21.3076L9.01953 21.2734L9.01758 21.2227C8.99171 20.3933 8.98483 19.563 8.99609 18.7334C9.00396 17.9678 8.98779 17.1376 8.97266 16.2813C8.95751 15.4242 8.94299 14.5395 8.95312 13.6621C8.97343 11.9056 9.09309 10.1855 9.5 8.77832C10.3637 5.7917 12.3812 3.2335 15.1123 1.71094L15.3789 1.56641Z" fill="#5F5AF6" stroke="black" stroke-width="0.22"/>
                        <path d="M27.142 13.0609L27.3185 13.0612C27.6183 13.0878 27.9587 13.1253 28.1817 13.3206C30.8965 15.699 31.0252 18.9068 29.2136 21.755C28.9327 22.1967 28.2947 22.2791 28.2108 22.7999C27.611 23.2069 26.9192 23.4699 26.2332 23.7481C23.4164 24.8906 20.2822 25.2101 17.2249 25.579C15.8905 25.74 14.8158 26.2706 13.4793 26.4041C11.7112 26.6422 8.30149 30.1145 6.60504 30.5874C6.60829 30.4183 6.91796 27.3761 7.84467 25.579C9.43249 22.4998 11.9016 21.1201 14.734 19.8646C15.0803 19.6812 15.3437 19.6949 15.6625 19.4302L15.5989 19.3706C15.8376 19.2941 17.1559 19.1762 17.4724 19.137C22.4276 18.5234 26.1931 17.7941 27.142 13.0609Z" fill="#E87257"/>
                    </svg>
                </div>
                <span class="career-nav-title">Paathshala <span>Guided Learning</span></span>
            </a>
            <nav class="career-nav-links">
                <a href="#theaterSection" class="career-nav-link">Reel Theater</a>
                <a href="#storySection" class="career-nav-link">Why Guided Learning</a>
                <a href="#librarySection" class="career-nav-link">Explore Subjects</a>
                <a href="#faqSection" class="career-nav-link">Parent FAQs</a>
            </nav>
            <div>
                <a href="#theaterSection" class="btn-coral-nav-cta">
                    <span>Watch Free Reels</span>
                    <span>➔</span>
                </a>
            </div>
        </div>
    </header>

    <!-- HERO SECTION -->
    <section class="career-hero-layout" id="hero">
        <div class="hero-tag-pill">
            <span>✨ AI-POWERED CONCEPT COMPANION</span>
            <span>·</span>
            <span>CLASSES 1 TO 12</span>
        </div>
        <div class="career-hero-center-header">
            <h1>
                Know every concept in <span class="hl">60 seconds</span> with Guided Learning
            </h1>
            <p class="sub">
                No boring 45-minute lectures. Real 1-on-1 moments turned into instant "Aha!" breakthroughs by India's top 1.4% verified tutors.
            </p>
            <div class="hero-stats-row">
                <div class="hero-stat-badge">
                    <span>🎬 <strong>500+</strong> Concept Reels</span>
                </div>
                <div class="hero-stat-badge">
                    <span>🎯 <strong>98.4%</strong> Retention Score</span>
                </div>
                <div class="hero-stat-badge">
                    <span>👩‍🏫 Top <strong>1.4%</strong> Verified Tutors</span>
                </div>
                <div class="hero-stat-badge">
                    <span>🆓 <strong>100% Free</strong> Forever</span>
                </div>
            </div>
        </div>

        <!-- EDITORIAL REEL CANVAS -->
        <div class="predictor-wrapper" id="theaterSection">
            <div class="editorial-quiz-canvas">
                <div class="editorial-canvas-header">
                    <div class="editorial-mark-left">
                        <span class="editorial-mark-star">✦</span>
                        <span>PAATHSHALA GUIDED LEARNING · CONCEPT RADAR</span>
                    </div>
                    <div class="editorial-mark-right">
                        <div class="live-pulse-dot"></div>
                        <span>LIVE CLASS CLIP · LEAH ALEXANDER</span>
                    </div>
                </div>

                <!-- FILTER CHIPS BAR -->
                <div class="canvas-filter-bar">
                    <div class="grade-chips-group">
                        <button class="filter-chip active" onclick="setGradeFilter(this, 'all')">All Grades</button>
                        <button class="filter-chip" onclick="setGradeFilter(this, 'foundational')">Classes 1–5 (Foundations)</button>
                        <button class="filter-chip" onclick="setGradeFilter(this, 'middle')">Classes 6–8 (Middle)</button>
                        <button class="filter-chip" onclick="setGradeFilter(this, 'board')">Classes 9–12 (Board Prep)</button>
                    </div>
                    <div class="subject-chips-group">
                        <button class="filter-chip category-active" onclick="setSubjectFilter(this, 'physics')">⚛️ Physics</button>
                        <button class="filter-chip" onclick="setSubjectFilter(this, 'chemistry')">🧪 Chemistry</button>
                        <button class="filter-chip" onclick="setSubjectFilter(this, 'math')">📐 Math Tricks</button>
                        <button class="filter-chip" onclick="setSubjectFilter(this, 'phonics')">🔤 Phonics</button>
                    </div>
                </div>

                <!-- MAIN THEATER GRID -->
                <div class="reel-theater-grid">
                    
                    <!-- LEFT COLUMN: 9:16 PHONE REEL PLAYER -->
                    <div class="reel-player-column">
                        <div class="reel-device-card" id="mainReelPlayer">
                            
                            <!-- SIMULATED LIVE CONCEPT CANVAS -->
                            <div class="reel-concept-visual" id="reelVisualScene">
                                <div class="atom-scene" id="atomVisualScene">
                                    <div class="electron-orbit">
                                        <div class="electron-dot"></div>
                                    </div>
                                    <div class="electron-orbit orbit-2">
                                        <div class="electron-dot" style="top:auto; bottom:-7px;"></div>
                                    </div>
                                    <div class="electron-orbit orbit-3">
                                        <div class="electron-dot" style="left:0; top:50%;"></div>
                                    </div>
                                    <div class="nucleus-core">
                                        <span style="font-size: 1.8rem;">⚛️</span>
                                    </div>
                                </div>
                            </div>

                            <!-- TOP REEL BAR -->
                            <div class="reel-player-top">
                                <div class="reel-brand-tag">
                                    <span>✦ Paathshala Highlight</span>
                                </div>
                                <button class="reel-sound-btn" id="soundToggleBtn" onclick="toggleReelAudio()" title="Toggle Sound">
                                    🔊
                                </button>
                            </div>

                            <!-- CENTER BIG PLAY/PAUSE TRIGGER -->
                            <div class="reel-player-center" onclick="toggleReelPlayback()">
                                <div class="big-play-btn" id="centerPlayIcon">⏸</div>
                            </div>

                            <!-- FLOATING SIDE ACTIONS -->
                            <div class="reel-side-actions">
                                <button class="reel-action-btn" id="likeBtn" onclick="likeReel()">
                                    ❤️
                                </button>
                                <span class="reel-action-count" id="likeCount">1.4k</span>

                                <button class="reel-action-btn" onclick="shareReel()">
                                    🔗
                                </button>
                                <span class="reel-action-count">Share</span>

                                <button class="reel-action-btn" onclick="openBookingModal()">
                                    📅
                                </button>
                                <span class="reel-action-count">Tutor</span>
                            </div>

                            <!-- BOTTOM BAR & SUBTITLES -->
                            <div class="reel-player-bottom">
                                <div class="reel-caption-bubble">
                                    <div class="reel-caption-text" id="liveSubtitle">
                                        <span class="speaker">Leah:</span> "They act like nuclear glue, holding the protons together so they don't push each other away."
                                    </div>
                                </div>

                                <div class="reel-progress-wrap">
                                    <div class="reel-progress-bar" onclick="seekReel(event)">
                                        <div class="reel-progress-fill" id="reelProgressFill" style="width: 48%;"></div>
                                    </div>
                                    <div class="reel-time-lbl" id="reelTimeLabel">0:24 / 0:50</div>
                                </div>
                            </div>

                        </div>
                    </div>

                    <!-- RIGHT COLUMN: REEL INTELLIGENCE & TUTOR DETAILS -->
                    <div class="reel-details-col">
                        
                        <!-- REEL INFO CARD -->
                        <div class="neo-card reel-header-card">
                            <div class="meta-pill-row">
                                <span class="tag-pill aha" id="activeCategoryTag">🎯 Aha Moment!</span>
                                <span class="tag-pill" id="activeGradeTag">Class 8–9 · Atomic Structure</span>
                                <span class="tag-pill" id="activeDurationTag">⏱ 50 Seconds</span>
                            </div>
                            <h2 class="reel-title-main" id="activeReelTitle">The 'Nuclear Glue' Inside an Atom</h2>
                            <blockquote class="reel-quote-card">
                                <strong>Core Takeaway:</strong>
                                <span id="activeQuoteText">“They act like nuclear glue, holding the protons together so they don't push each other away.”</span>
                            </blockquote>
                            <p class="reel-subtitle-desc" id="activeReelDesc">
                                A live breakthrough moment from an actual 1-on-1 class on Paathshala. Learn the crucial role of neutrons in atomic stability.
                            </p>
                        </div>

                        <!-- TEACHER SPOTLIGHT CARD -->
                        <div class="neo-card teacher-spotlight-card">
                            <div class="teacher-header-row">
                                <div class="teacher-avatar-box">
                                    <img src="data:image/jpeg;base64,{avatar_b64}" alt="Leah Alexander" id="activeTeacherPhoto">
                                </div>
                                <div class="teacher-name-box">
                                    <h3 id="activeTeacherName">Leah Alexander</h3>
                                    <div class="teacher-creds-row">
                                        <span class="badge-verified">✓ Paathshala Verified</span>
                                        <span>★ 4.95 (148 reviews)</span>
                                        <span>· Kochi, Kerala</span>
                                    </div>
                                </div>
                            </div>
                            <button class="btn-book-teacher" onclick="openBookingModal()">
                                <span>📅</span>
                                <span id="btnBookTeacherLabel">Book a 1-on-1 Class with Leah Alexander</span>
                            </button>
                        </div>

                        <!-- INTERACTIVE 1-QUESTION COMPREHENSION CHECK -->
                        <div class="quiz-check-card">
                            <div class="quiz-header">
                                <span class="quiz-tag">⚡ 30-Sec Comprehension Check</span>
                                <span class="quiz-xp">+50 Concept XP</span>
                            </div>
                            <h4 class="quiz-question" id="quizQuestionText">
                                Why don't the positively charged protons in a nucleus repel each other and fly apart?
                            </h4>
                            <div class="quiz-options-grid" id="quizOptionsContainer">
                                <button class="quiz-opt-btn" onclick="checkAnswer(this, false)">A) Gravity pulls them together</button>
                                <button class="quiz-opt-btn" onclick="checkAnswer(this, true)">B) Neutrons provide strong nuclear glue</button>
                                <button class="quiz-opt-btn" onclick="checkAnswer(this, false)">C) Electrons hold them from outside</button>
                                <button class="quiz-opt-btn" onclick="checkAnswer(this, false)">D) They have opposite charges</button>
                            </div>
                            <div class="quiz-feedback-banner" id="quizFeedbackBanner">
                                <span>🎉</span>
                                <span id="quizFeedbackText">Brilliant! You just mastered Atomic Stability in under 60 seconds!</span>
                            </div>
                        </div>

                        <!-- MORE CLASS HIGHLIGHTS ROW -->
                        <div>
                            <h4 style="font-family:'Outfit',sans-serif; font-weight:800; font-size:1.05rem; margin-bottom:10px; color:#18181B;">
                                🎬 More highlights from this topic & tutor:
                            </h4>
                            <div class="related-reels-row">
                                
                                <div class="related-reel-card active" onclick="switchReel(0)">
                                    <div class="related-thumb">
                                        <span class="related-thumb-icon">⚛️</span>
                                    </div>
                                    <div class="related-title">The 'Nuclear Glue' Inside an Atom</div>
                                    <div class="related-meta">
                                        <span>50s</span>
                                        <span>Leah A.</span>
                                    </div>
                                </div>

                                <div class="related-reel-card" onclick="switchReel(1)">
                                    <div class="related-thumb">
                                        <span class="related-thumb-icon">🌌</span>
                                    </div>
                                    <div class="related-title">You Are 99.999% Empty Space!</div>
                                    <div class="related-meta">
                                        <span>58s</span>
                                        <span>Leah A.</span>
                                    </div>
                                </div>

                                <div class="related-reel-card" onclick="switchReel(2)">
                                    <div class="related-thumb">
                                        <span class="related-thumb-icon">➗</span>
                                    </div>
                                    <div class="related-title">Multiply Any 2-Digit Number in 3s</div>
                                    <div class="related-meta">
                                        <span>42s</span>
                                        <span>Nikita A.</span>
                                    </div>
                                </div>

                                <div class="related-reel-card" onclick="switchReel(3)">
                                    <div class="related-thumb">
                                        <span class="related-thumb-icon">🌿</span>
                                    </div>
                                    <div class="related-title">Why Leaves Turn Red in Autumn</div>
                                    <div class="related-meta">
                                        <span>54s</span>
                                        <span>Soumi S.</span>
                                    </div>
                                </div>

                                <div class="related-reel-card" onclick="switchReel(4)">
                                    <div class="related-thumb">
                                        <span class="related-thumb-icon">🔤</span>
                                    </div>
                                    <div class="related-title">The Secret Power of the Bossy 'E'</div>
                                    <div class="related-meta">
                                        <span>38s</span>
                                        <span>Leah A.</span>
                                    </div>
                                </div>

                            </div>
                        </div>

                    </div>

                </div>

            </div>
        </div>
    </section>

    <!-- CINEMATIC STORY SECTION (MATCHING #story FROM BHAVISHYA PREDICTOR) -->
    <section class="story-section" id="storySection">
        <div class="story-header-box">
            <span class="story-tag">THE COGNITIVE REVOLUTION</span>
            <h2>Why 60-second Guided Learning works</h2>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
                Cognitive psychology shows that human working memory peaks when complex concepts are stripped down to intuitive visual metaphors.
            </p>
        </div>

        <div class="story-grid">
            
            <div class="story-card">
                <div class="story-step-num">01</div>
                <h3>The 45-Minute Lecture Trap</h3>
                <p>
                    Students zone out after the first 7 minutes. Traditional classroom lecturing floods working memory with irrelevant filler words, causing 70% retention loss within 24 hours.
                </p>
                <div class="story-visual-badge">
                    <span>⚠️ 70% Forgotten by Next Day</span>
                </div>
            </div>

            <div class="story-card">
                <div class="story-step-num">02</div>
                <h3>The 60-Second "Aha!" Moment</h3>
                <p>
                    Our AI scans real 1-on-1 tutoring transcripts and detects the exact minute where confusion turns into mastery — using concrete metaphors like "nuclear glue" or "stadium parking lots".
                </p>
                <div class="story-visual-badge">
                    <span>💡 Visual Metaphors Stick Forever</span>
                </div>
            </div>

            <div class="story-card">
                <div class="story-step-num">03</div>
                <h3>Stopwatch Efficiency</h3>
                <p>
                    A single 50-second reel covers what would otherwise take 3 dense textbook pages to digest. Students review 10 critical exam concepts in the time it takes to brew tea.
                </p>
                <div class="story-visual-badge">
                    <span>⏱ 10 Concepts in 10 Minutes</span>
                </div>
            </div>

            <div class="story-card">
                <div class="story-step-num">04</div>
                <h3>Knowledge Graph Mapping</h3>
                <p>
                    Every watched reel connects directly to the student's personalized syllabus map. Watch atomic structure today, and Mitra AI unlocks chemical bonding tomorrow.
                </p>
                <div class="story-visual-badge">
                    <span>🗺 Dynamic Syllabus Progress</span>
                </div>
            </div>

            <div class="story-card">
                <div class="story-step-num">05</div>
                <h3>India's Top 1.4% Tutors</h3>
                <p>
                    Every reel is delivered by our rigorously vetted, background-checked master educators. Loved a clip? You can book that exact teacher for a full 1-on-1 interactive class.
                </p>
                <div class="story-visual-badge">
                    <span>🎓 Direct 1-on-1 Booking</span>
                </div>
            </div>

            <div class="story-card" style="background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);">
                <div class="story-step-num" style="color: #D97706;">06</div>
                <h3 style="color: #92400E;">Active Recall Micro-Quizzes</h3>
                <p style="color: #78350F;">
                    Immediately following each reel, students test their recall in 30 seconds. This cements neural pathways and converts short-term curiosity into permanent exam readiness.
                </p>
                <div class="story-visual-badge" style="background: #FFFFFF; color: #92400E;">
                    <span>🏆 +50 XP Concept Mastery</span>
                </div>
            </div>

        </div>
    </section>

    <!-- LIVE MARQUEE -->
    <div class="marq-wrap">
        <div class="marq-content">
            <span>Watch it. </span><em>✦ Grasp it. </em><span>✦ Remember it. </span><em>✦ Master it. </em><span>✦ Ace your exams. </span>    
            <span>Watch it. </span><em>✦ Grasp it. </em><span>✦ Remember it. </span><em>✦ Master it. </em><span>✦ Ace your exams. </span>    
            <span>Watch it. </span><em>✦ Grasp it. </em><span>✦ Remember it. </span><em>✦ Master it. </em><span>✦ Ace your exams. </span>
        </div>
    </div>

    <!-- CURATED SUBJECT REEL LIBRARY -->
    <section class="curated-library-section" id="librarySection">
        <div style="text-align: center; margin-bottom: 24px;">
            <div class="hero-tag-pill" style="background: rgba(255,255,255,0.18);">EXPLORE BY SUBJECT</div>
            <h2 style="font-family:'Outfit',sans-serif; font-size: 2.6rem; font-weight:900; margin-top: 10px;">
                Curated Concept Library
            </h2>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1rem;">
                Browse hundreds of micro-highlights taught by our certified CBSE, ICSE & Cambridge educators.
            </p>
        </div>

        <div class="library-grid">
            
            <div class="lib-reel-item" onclick="switchReel(0)">
                <div class="lib-thumb-box">
                    <span>⚛️</span>
                    <span class="lib-dur-badge">0:50</span>
                </div>
                <span class="lib-sub-tag">Physics · Class 9</span>
                <h4 class="lib-reel-title">The 'Nuclear Glue' Inside an Atom</h4>
                <div class="lib-teacher-snippet">
                    <span>👩‍🏫 Leah Alexander</span>
                    <span>· 4.95 ★</span>
                </div>
            </div>

            <div class="lib-reel-item" onclick="switchReel(1)">
                <div class="lib-thumb-box">
                    <span>🌌</span>
                    <span class="lib-dur-badge">0:58</span>
                </div>
                <span class="lib-sub-tag">Chemistry · Class 9</span>
                <h4 class="lib-reel-title">You Are 99.999% Empty Space!</h4>
                <div class="lib-teacher-snippet">
                    <span>👩‍🏫 Leah Alexander</span>
                    <span>· 4.95 ★</span>
                </div>
            </div>

            <div class="lib-reel-item" onclick="switchReel(2)">
                <div class="lib-thumb-box">
                    <span>➗</span>
                    <span class="lib-dur-badge">0:42</span>
                </div>
                <span class="lib-sub-tag">Mathematics · Class 6–8</span>
                <h4 class="lib-reel-title">Multiply Any 2-Digit Number in 3 Seconds</h4>
                <div class="lib-teacher-snippet">
                    <span>👩‍🏫 Nikita Arvey</span>
                    <span>· 4.99 ★</span>
                </div>
            </div>

            <div class="lib-reel-item" onclick="switchReel(3)">
                <div class="lib-thumb-box">
                    <span>🌿</span>
                    <span class="lib-dur-badge">0:54</span>
                </div>
                <span class="lib-sub-tag">Biology · Class 7</span>
                <h4 class="lib-reel-title">Why Autumn Leaves Turn Red (Hidden Pigments)</h4>
                <div class="lib-teacher-snippet">
                    <span>👩‍🏫 Soumi Sarkar</span>
                    <span>· 4.98 ★</span>
                </div>
            </div>

            <div class="lib-reel-item" onclick="switchReel(4)">
                <div class="lib-thumb-box">
                    <span>🔤</span>
                    <span class="lib-dur-badge">0:38</span>
                </div>
                <span class="lib-sub-tag">Phonics · Classes 1–3</span>
                <h4 class="lib-reel-title">The Secret Power of the Bossy 'E'</h4>
                <div class="lib-teacher-snippet">
                    <span>👩‍🏫 Leah Alexander</span>
                    <span>· 4.95 ★</span>
                </div>
            </div>

            <div class="lib-reel-item" onclick="switchReel(2)">
                <div class="lib-thumb-box">
                    <span>📐</span>
                    <span class="lib-dur-badge">0:48</span>
                </div>
                <span class="lib-sub-tag">Geometry · Class 8</span>
                <h4 class="lib-reel-title">Pythagoras Theorem Visualized with Water</h4>
                <div class="lib-teacher-snippet">
                    <span>👩‍🏫 Tanu Riya</span>
                    <span>· 4.97 ★</span>
                </div>
            </div>

        </div>
    </section>

    <!-- PARENT & STUDENT FAQS -->
    <section class="faq-section" id="faqSection">
        <h2 class="faq-title">Quick Answers for Parents</h2>
        
        <details class="faq-item" open>
            <summary>Are Guided Learning reels completely free?</summary>
            <p>
                Yes! All 500+ Guided Learning concept reels, animations, transcripts, and micro-quizzes are 100% free to explore without any subscription or credit card requirement.
            </p>
        </details>

        <details class="faq-item">
            <summary>Can I book the exact tutor who appears in the reel?</summary>
            <p>
                Absolutely. Every reel features an active, verified Paathshala teacher. Simply click "Book a 1-on-1 Class" on the reel to reserve a free 30-minute trial session directly with them.
            </p>
        </details>

        <details class="faq-item">
            <summary>Which education boards and classes are covered?</summary>
            <p>
                Reels are organized across CBSE, ICSE, Cambridge, and State Boards for students from Class 1 through Class 12, covering Mathematics, Physics, Chemistry, Biology, Social Science, and English Phonics.
            </p>
        </details>

        <details class="faq-item">
            <summary>How does Mitra AI choose which reels my child needs?</summary>
            <p>
                When your child takes classes or practices quizzes on Paathshala, Mitra AI tracks concept gaps and serves targeted 60-second reels right before their exams or live sessions to fill missing foundations.
            </p>
        </details>
    </section>

    <!-- BOTTOM CTA BANNER -->
    <div class="bottom-cta-banner">
        <h2>Give your child clarity in 60 seconds.</h2>
        <p>
            Experience how our top 1.4% tutors transform learning from a chore into a superpower. Start with a free reel or book a live 1-on-1 trial class today.
        </p>
        <div class="cta-buttons-wrap">
            <a href="#theaterSection" class="btn-cta-main">Watch Concept Reels Free ➔</a>
            <button class="btn-cta-ghost" onclick="openBookingModal()">Book Free 1-on-1 Trial</button>
        </div>
    </div>

    <!-- SIGNATURE PAATHSHALA FOOTER -->
    <footer class="landing-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h4>Paathshala Guided Learning</h4>
                    <p class="footer-desc">
                        Empowering students across India with bite-sized concept clarity, live interactive 1-on-1 classes, and dedicated top 1.4% verified tutors.
                    </p>
                </div>
                <div class="footer-col">
                    <h5>Features</h5>
                    <ul class="footer-links">
                        <li><a href="#theaterSection">Reel Theater</a></li>
                        <li><a href="#storySection">Why Guided Learning</a></li>
                        <li><a href="#librarySection">Subject Library</a></li>
                        <li><a href="/ai-career-predictor">Bhavishya AI Predictor</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h5>Quick Links</h5>
                    <ul class="footer-links">
                        <li><a href="/">Paathshala Home</a></li>
                        <li><a href="/user-profile?publicId=alchemist-589748">Leah Alexander Profile</a></li>
                        <li><a href="/classes">Classes & Pricing</a></li>
                        <li><a href="/about-us">About Us</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h5>Contact & Support</h5>
                    <ul class="footer-links">
                        <li><a href="mailto:paathshalasupport@safwhigre.com">paathshalasupport@safwhigre.com</a></li>
                        <li><a href="tel:+918010571912">+91 80105 71912</a></li>
                        <li><span style="color:#94A3B8; font-size:0.8rem;">Mon–Sat: 9 AM – 9 PM IST</span></li>
                    </ul>
                </div>
            </div>
            <p style="text-align:center; font-size:0.8rem; color:#64748B; padding-top:20px; border-top:1px solid rgba(255,255,255,0.1);">
                © 2026 Safwhigre Technologies OPC Private Limited · Paathshala · All Rights Reserved.
            </p>
        </div>
        <div class="footer-big-text-wrap">
            <div class="footer-big-text">paathshala</div>
        </div>
    </footer>

    <!-- BOOKING SIMULATION MODAL -->
    <div class="modal-overlay" id="bookingModal">
        <div class="modal-card">
            <button class="modal-close-btn" onclick="closeBookingModal()">✕</button>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px;">
                <div style="width:48px; height:48px; border-radius:12px; border:2px solid #272727; overflow:hidden;">
                    <img src="data:image/jpeg;base64,{avatar_b64}" style="width:100%; height:100%; object-fit:cover;" id="modalTutorImg">
                </div>
                <div>
                    <h3 style="font-family:'Outfit',sans-serif; font-size:1.2rem;" id="modalTutorName">Book Class with Leah Alexander</h3>
                    <p style="font-size:0.8rem; color:#64748B;">★ 4.95 Rating · SafeTutor Verified</p>
                </div>
            </div>
            
            <p style="font-size:0.9rem; color:#475569; margin-bottom:16px;">
                Experience a complete 1-on-1 session with this tutor. 100% free with zero payment details required.
            </p>

            <div style="background:#F1F5F9; border-radius:12px; padding:12px; margin-bottom:16px;">
                <div style="font-size:0.75rem; font-weight:800; color:#475569; text-transform:uppercase; margin-bottom:6px;">Available Slots:</div>
                <div style="display:flex; gap:6px; flex-wrap:wrap;">
                    <span style="background:#FFFFFF; border:1.5px solid #272727; border-radius:8px; padding:4px 10px; font-size:0.8rem; font-weight:700;">Today, 5:00 PM</span>
                    <span style="background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:8px; padding:4px 10px; font-size:0.8rem; font-weight:700;">Today, 6:30 PM</span>
                    <span style="background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:8px; padding:4px 10px; font-size:0.8rem; font-weight:700;">Tomorrow, 4:00 PM</span>
                </div>
            </div>

            <a href="https://paathshala.app/booking?teacherId=d2dOWorLt4QEmqARukBjIayAknk1" target="_blank" class="btn-book-teacher" style="width:100%; box-sizing:border-box;">
                Confirm Free Booking on Paathshala ➔
            </a>
        </div>
    </div>

    <!-- CLIENT INTERACTIVITY JAVASCRIPT -->
    <script>
        const REELS_DATA = [
            {{
                id: "6acca1a0fa97e5183b039237-r1",
                title: "The 'Nuclear Glue' Inside an Atom",
                category: "🎯 Aha Moment!",
                grade: "Class 8–9 · Atomic Structure",
                duration: "⏱ 50 Seconds",
                quote: "“They act like nuclear glue, holding the protons together so they don't push each other away.”",
                desc: "A live breakthrough moment from an actual 1-on-1 class on Paathshala. Learn the crucial role of neutrons in atomic stability.",
                teacher: "Leah Alexander",
                teacherRole: "Paathshala Certified · B.Ed Calicut",
                teacherAvatar: "data:image/jpeg;base64,{avatar_b64}",
                teacherRating: "★ 4.95 (148 reviews)",
                subtitles: [
                    "Protons have a positive electrical charge...",
                    "So naturally, like charges repel each other violently!",
                    "Why doesn't the nucleus instantly explode apart?",
                    "Meet the neutrons: they act like nuclear glue, holding the protons together!"
                ],
                visualHtml: `
                    <div class="atom-scene">
                        <div class="electron-orbit"><div class="electron-dot"></div></div>
                        <div class="electron-orbit orbit-2"><div class="electron-dot" style="top:auto; bottom:-7px;"></div></div>
                        <div class="electron-orbit orbit-3"><div class="electron-dot" style="left:0; top:50%;"></div></div>
                        <div class="nucleus-core"><span style="font-size: 1.8rem;">⚛️</span></div>
                    </div>
                `,
                quizQuestion: "Why don't the positively charged protons in a nucleus repel each other and fly apart?",
                quizOptions: [
                    {{ text: "A) Gravity pulls them together", correct: false }},
                    {{ text: "B) Neutrons provide strong nuclear glue", correct: true }},
                    {{ text: "C) Electrons hold them from outside", correct: false }},
                    {{ text: "D) They have opposite charges", correct: false }}
                ],
                quizSuccessText: "Brilliant! You just mastered Atomic Stability in under 60 seconds!"
            }},
            {{
                id: "6acca1a0fa97e5183b039237-r2",
                title: "You Are 99.999% Empty Space!",
                category: "🎯 Aha Moment!",
                grade: "Class 9 · Atomic Scale",
                duration: "⏱ 58 Seconds",
                quote: "“The electrons are tiny specks of dust buzzing around the outer parking lot of the school stadium.”",
                desc: "A mind-bending analogy that reveals why you, your chair, and your smartphone are almost entirely empty space.",
                teacher: "Leah Alexander",
                teacherRole: "Paathshala Certified · B.Ed Calicut",
                teacherAvatar: "data:image/jpeg;base64,{avatar_b64}",
                teacherRating: "★ 4.95 (148 reviews)",
                subtitles: [
                    "If you enlarged the nucleus to the size of a marble in the center of a cricket stadium...",
                    "The electrons would be microscopic specks of dust in the outer parking lot!",
                    "Everything in between is 99.999% vacuum.",
                    "You feel solid only because electromagnetic fields push back!"
                ],
                visualHtml: `
                    <div style="display:flex; flex-direction:column; align-items:center; gap:16px;">
                        <div style="font-size:3.5rem; animation: float 3s ease-in-out infinite;">🏟️</div>
                        <div style="background:rgba(255,255,255,0.15); padding:8px 16px; border-radius:12px; font-weight:800; font-size:1.1rem; color:#FEF08A;">
                            99.999% VACUUM
                        </div>
                    </div>
                `,
                quizQuestion: "If the nucleus was the size of a marble in a stadium, where are the electrons?",
                quizOptions: [
                    {{ text: "A) Right on the pitch", correct: false }},
                    {{ text: "B) Out in the stadium parking lot", correct: true }},
                    {{ text: "C) Glued to the marble", correct: false }},
                    {{ text: "D) Swimming inside the nucleus", correct: false }}
                ],
                quizSuccessText: "Mind blown! You grasped the atomic scale analogy perfectly!"
            }},
            {{
                id: "math-vedic-01",
                title: "Multiply Any 2-Digit Number in 3 Seconds",
                category: "💡 Mental Trick",
                grade: "Classes 6–10 · Mental Math",
                duration: "⏱ 42 Seconds",
                quote: "“Cross the diagonals, add the wings, and write the product directly from left to right!”",
                desc: "Vedic multiplication shortcut that eliminates paper scratchwork during high-stakes exams.",
                teacher: "Nikita Arvey",
                teacherRole: "Maths & Olympiad Coach · 4.99 ★",
                teacherAvatar: "data:image/jpeg;base64,{avatar_b64}",
                teacherRating: "★ 4.99 (210 reviews)",
                subtitles: [
                    "Say you want to multiply 21 × 32 in your head.",
                    "Step 1: Multiply tens digits: 2 × 3 = 6.",
                    "Step 2: Cross-multiply: (2×2) + (1×3) = 7.",
                    "Step 3: Multiply units digits: 1 × 2 = 2. Answer: 672!"
                ],
                visualHtml: `
                    <div style="text-align:center;">
                        <div style="font-family:'Outfit',sans-serif; font-weight:900; font-size:3.2rem; color:#FEF08A; letter-spacing:4px;">
                            21 × 32
                        </div>
                        <div style="font-size:1.4rem; color:#38BDF8; font-weight:800; margin-top:8px;">
                            = 672
                        </div>
                    </div>
                `,
                quizQuestion: "In the 2-digit mental trick (21 × 32), what was the middle cross step?",
                quizOptions: [
                    {{ text: "A) 2 + 1 + 3 + 2 = 8", correct: false }},
                    {{ text: "B) (2×2) + (1×3) = 7", correct: true }},
                    {{ text: "C) 21 + 32 = 53", correct: false }},
                    {{ text: "D) 2 × 3 × 1 = 6", correct: false }}
                ],
                quizSuccessText: "Speed demon! You just learned mental calculation like a topper!"
            }},
            {{
                id: "bio-pigments-01",
                title: "Why Autumn Leaves Turn Red (Hidden Pigments)",
                category: "🌿 Nature Decoded",
                grade: "Class 7–8 · Plant Biology",
                duration: "⏱ 54 Seconds",
                quote: "“The orange and red were always hiding there! Green chlorophyll was just screaming louder all summer.”",
                desc: "Why tree leaves undergo dramatic color changes when sunlight hours decrease in winter.",
                teacher: "Soumi Sarkar",
                teacherRole: "Biology Specialist · 4.98 ★",
                teacherAvatar: "data:image/jpeg;base64,{avatar_b64}",
                teacherRating: "★ 4.98 (182 reviews)",
                subtitles: [
                    "Why do leaves suddenly turn golden and red in autumn?",
                    "Did the tree make new red paint? No!",
                    "Carotenoids and anthocyanins were inside the leaf all spring and summer.",
                    "When chlorophyll breaks down, the hidden sunset colors finally shine!"
                ],
                visualHtml: `
                    <div style="display:flex; gap:14px; font-size:3.5rem;">
                        <span>🍃</span>
                        <span style="font-size:2rem; align-self:center;">➔</span>
                        <span>🍁</span>
                    </div>
                `,
                quizQuestion: "Were the yellow and red pigments created only in autumn?",
                quizOptions: [
                    {{ text: "A) Yes, cold air creates red sap", correct: false }},
                    {{ text: "B) No, they were always present beneath green chlorophyll", correct: true }},
                    {{ text: "C) Insects paint the leaves", correct: false }},
                    {{ text: "D) Roots pump food upward", correct: false }}
                ],
                quizSuccessText: "Spot on! You understand hidden leaf pigments like a pro!"
            }},
            {{
                id: "phonics-bossy-e",
                title: "The Secret Power of the Bossy 'E'",
                category: "🔤 Phonics Secret",
                grade: "Classes 1–3 · Early Reading",
                duration: "⏱ 38 Seconds",
                quote: "“The silent 'E' at the end doesn't say a sound — it commands the first vowel to say its own name!”",
                desc: "Turn 'CAP' into 'CAPE' and 'PIN' into 'PINE' with the ultimate magic 'E' pronunciation rule.",
                teacher: "Leah Alexander",
                teacherRole: "Primary Educator & Jolly Phonics Certified",
                teacherAvatar: "data:image/jpeg;base64,{avatar_b64}",
                teacherRating: "★ 4.95 (148 reviews)",
                subtitles: [
                    "Notice the word C-A-P: short vowel sound /a/ as in 'cap'.",
                    "Add an 'E' at the end: C-A-P-E.",
                    "The magic 'E' is silent, but it kicks the 'A'!",
                    "Now 'A' says its full alphabet name: /AY/ -> 'Cape'!"
                ],
                visualHtml: `
                    <div style="text-align:center;">
                        <div style="font-family:'Outfit',sans-serif; font-size:2.8rem; font-weight:900; color:#FFFFFF;">
                            CAP ➔ <span style="color:#FEF08A;">CAPE</span>
                        </div>
                        <div style="font-size:1.1rem; color:#A7F3D0; font-weight:800; margin-top:8px;">
                            Magic 'E' Rule
                        </div>
                    </div>
                `,
                quizQuestion: "What does the magic silent 'E' do to the first vowel in 'PIN'?",
                quizOptions: [
                    {{ text: "A) Makes it sound like /eh/", correct: false }},
                    {{ text: "B) Makes 'I' say its alphabet name ('PINE')", correct: true }},
                    {{ text: "C) Adds a double consonant", correct: false }},
                    {{ text: "D) Nothing at all", correct: false }}
                ],
                quizSuccessText: "Superstar! Your phonics foundation is rock solid!"
            }}
        ];

        let currentReelIdx = 0;
        let isPlaying = true;
        let isMuted = false;
        let progress = 48;
        let playInterval;

        function updateReelUI() {{
            const r = REELS_DATA[currentReelIdx];
            document.getElementById('activeReelTitle').innerText = r.title;
            document.getElementById('activeCategoryTag').innerText = r.category;
            document.getElementById('activeGradeTag').innerText = r.grade;
            document.getElementById('activeDurationTag').innerText = r.duration;
            document.getElementById('activeQuoteText').innerText = r.quote;
            document.getElementById('activeReelDesc').innerText = r.desc;
            document.getElementById('activeTeacherName').innerText = r.teacher;
            document.getElementById('btnBookTeacherLabel').innerText = "Book a 1-on-1 Class with " + r.teacher;
            document.getElementById('modalTutorName').innerText = "Book Class with " + r.teacher;
            
            // Visual Scene
            document.getElementById('reelVisualScene').innerHTML = r.visualHtml;
            
            // Subtitles
            document.getElementById('liveSubtitle').innerHTML = `<span class="speaker">${{r.teacher.split(' ')[0]}}:</span> "${{r.subtitles[0]}}"`;

            // Quiz
            document.getElementById('quizQuestionText').innerText = r.quizQuestion;
            const optContainer = document.getElementById('quizOptionsContainer');
            optContainer.innerHTML = '';
            r.quizOptions.forEach(opt => {{
                const btn = document.createElement('button');
                btn.className = 'quiz-opt-btn';
                btn.innerText = opt.text;
                btn.onclick = function() {{ checkAnswer(this, opt.correct); }};
                optContainer.appendChild(btn);
            }});
            document.getElementById('quizFeedbackBanner').style.display = 'none';

            // Active related card
            document.querySelectorAll('.related-reel-card').forEach((el, idx) => {{
                el.classList.toggle('active', idx === currentReelIdx);
            }});
        }}

        function switchReel(idx) {{
            currentReelIdx = idx;
            progress = 10;
            updateReelUI();
            startPlaybackLoop();
        }}

        function toggleReelPlayback() {{
            isPlaying = !isPlaying;
            document.getElementById('centerPlayIcon').innerText = isPlaying ? '⏸' : '▶';
        }}

        function toggleReelAudio() {{
            isMuted = !isMuted;
            document.getElementById('soundToggleBtn').innerText = isMuted ? '🔇' : '🔊';
        }}

        function seekReel(e) {{
            const rect = e.currentTarget.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            progress = Math.min(100, Math.max(0, (clickX / rect.width) * 100));
            document.getElementById('reelProgressFill').style.width = progress + '%';
        }}

        function checkAnswer(btn, isCorrect) {{
            const siblings = btn.parentElement.querySelectorAll('.quiz-opt-btn');
            siblings.forEach(b => b.disabled = true);
            if (isCorrect) {{
                btn.classList.add('correct');
                const banner = document.getElementById('quizFeedbackBanner');
                banner.style.display = 'flex';
                banner.querySelector('#quizFeedbackText').innerText = REELS_DATA[currentReelIdx].quizSuccessText;
            }} else {{
                btn.classList.add('wrong');
                siblings.forEach(b => {{
                    if (b.innerText.includes("B)") || b.innerText.includes("parking lot") || b.innerText.includes("alphabet name")) {{
                        b.classList.add('correct');
                    }}
                }});
            }}
        }}

        function likeReel() {{
            const countEl = document.getElementById('likeCount');
            const heart = document.getElementById('likeBtn');
            heart.style.transform = 'scale(1.3)';
            setTimeout(() => {{ heart.style.transform = 'scale(1)'; }}, 200);
            countEl.innerText = "1.5k";
        }}

        function shareReel() {{
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(window.location.href);
                alert("✨ Reel link copied to clipboard! Share it with your friends or classmates.");
            }} else {{
                alert("Share link: " + window.location.href);
            }}
        }}

        function openBookingModal() {{
            document.getElementById('bookingModal').classList.add('active');
        }}

        function closeBookingModal() {{
            document.getElementById('bookingModal').classList.remove('active');
        }}

        function setGradeFilter(btn, grade) {{
            btn.parentElement.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            if (grade === 'foundational') switchReel(4);
            else if (grade === 'middle') switchReel(2);
            else if (grade === 'board') switchReel(0);
        }}

        function setSubjectFilter(btn, subj) {{
            btn.parentElement.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('category-active'));
            btn.classList.add('category-active');
            if (subj === 'physics') switchReel(0);
            else if (subj === 'chemistry') switchReel(1);
            else if (subj === 'math') switchReel(2);
            else if (subj === 'phonics') switchReel(4);
        }}

        function startPlaybackLoop() {{
            clearInterval(playInterval);
            playInterval = setInterval(() => {{
                if (isPlaying) {{
                    progress += 1.5;
                    if (progress >= 100) {{
                        progress = 0;
                    }}
                    document.getElementById('reelProgressFill').style.width = progress + '%';
                    const currentSec = Math.floor((progress / 100) * 50);
                    document.getElementById('reelTimeLabel').innerText = `0:${{currentSec < 10 ? '0' : ''}}${{currentSec}} / 0:50`;
                    
                    const subIdx = Math.floor((progress / 100) * REELS_DATA[currentReelIdx].subtitles.length);
                    const subText = REELS_DATA[currentReelIdx].subtitles[Math.min(subIdx, REELS_DATA[currentReelIdx].subtitles.length - 1)];
                    document.getElementById('liveSubtitle').innerHTML = `<span class="speaker">${{REELS_DATA[currentReelIdx].teacher.split(' ')[0]}}:</span> "${{subText}}"`;
                }}
            }}, 400);
        }}

        startPlaybackLoop();
    </script>
</body>
</html>
'''

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(landing_html)

print("Generated landing.html successfully!")
