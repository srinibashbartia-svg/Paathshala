import sys, os

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/leah_avatar.txt", "r") as f:
    avatar_b64 = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>Paathshala Guided Learning · 60-Second Concept Breakthroughs</title>
    <meta name="description" content="A dedicated expert teacher who meets your child exactly where they're stuck. Live 1-on-1 classes, 60-second concept reels, and Mitra AI.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --bg: #FAF7F2;
            --bg2: #F0EAE1;
            --fg: #18181B;
            --mut: #64748B;
            --primary: #5458F7;
            --primary-hover: #4338CA;
            --coral: #FF5A36;
            --coral-hover: #E84D29;
            --yellow: #FEF08A;
            --yellow-border: #F59E0B;
            --emerald: #10B981;
            --cyan: #38BDF8;
            --border-dark: #272727;
            --ln: rgba(39, 39, 39, 0.15);
            --vg: rgba(0, 0, 0, 0.25);
            --bar: #111827;
            box-sizing: border-box;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            background: var(--bg);
            color: var(--fg);
            font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
            overflow-x: hidden;
            line-height: 1.45;
        }}

        h1, h2, .big {{
            font-family: 'Outfit', 'Bricolage Grotesque', sans-serif;
            font-weight: 900;
            letter-spacing: -0.035em;
            line-height: 1.05;
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
            background: var(--coral);
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
            background: var(--primary);
            color: #FFFFFF;
        }}

        /* STICKY NAV */
        nav.main-nav {{
            position: sticky;
            top: 36px;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 5vw;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            background: rgba(250, 247, 242, 0.92);
            border-bottom: 2px solid var(--border-dark);
        }}
        .nav-brand {{
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: var(--fg);
        }}
        .nav-logo-box {{
            width: 38px;
            height: 38px;
            border-radius: 10px;
            background: #FFFFFF;
            border: 2px solid var(--border-dark);
            padding: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 0 var(--border-dark);
        }}
        .nav-logo-box svg {{
            width: 100%;
            height: 100%;
        }}
        .nav-brand-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.35rem;
            color: var(--fg);
        }}
        .nav-brand-title span {{
            color: var(--coral);
        }}
        .nav-links-wrap {{
            display: flex;
            align-items: center;
            gap: 24px;
        }}
        .nav-link-item {{
            color: var(--fg);
            text-decoration: none;
            font-weight: 700;
            font-size: 0.92rem;
            transition: color 0.15s;
        }}
        .nav-link-item:hover {{
            color: var(--primary);
        }}
        .btn-trial-nav {{
            background: var(--coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.92rem;
            padding: 10px 20px;
            border-radius: 14px;
            text-decoration: none;
            border: 2px solid var(--border-dark);
            box-shadow: 0 3px 0 var(--border-dark);
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .btn-trial-nav:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 0 var(--border-dark);
            background: var(--coral-hover);
        }}

        /* BUTTONS */
        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            padding: 14px 28px;
            border-radius: 16px;
            text-decoration: none;
            border: 3px solid var(--border-dark);
            box-shadow: 0 5px 0 var(--border-dark);
            cursor: pointer;
            font-size: 1.05rem;
            transition: all 0.15s ease;
        }}
        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 7px 0 var(--border-dark);
            background: var(--coral-hover);
        }}
        .btn.ghost {{
            background: #FFFFFF;
            color: var(--fg);
        }}
        .btn.ghost:hover {{
            background: var(--yellow);
        }}
        .btn.primary {{
            background: var(--primary);
        }}
        .btn.primary:hover {{
            background: var(--primary-hover);
        }}

        .hl {{
            color: var(--coral);
        }}
        .hl-indigo {{
            color: var(--primary);
        }}

        /* =========================================================================
           HERO SECTION WITH ANIMATED LAB & HIGHLIGHT REELS TICKER
           ========================================================================= */
        .hero-section {{
            padding: 60px 5vw 40px;
            position: relative;
            overflow: hidden;
            background-color: var(--bg);
            background-image: radial-gradient(#d4cfc5 1.5px, transparent 1.5px);
            background-size: 24px 24px;
        }}
        .hero-grid {{
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 4vw;
            align-items: center;
            max-width: 1240px;
            margin: 0 auto 50px;
        }}
        .pill-tag {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.82rem;
            font-weight: 800;
            padding: 5px 14px;
            border: 2px solid var(--border-dark);
            border-radius: 999px;
            margin-bottom: 20px;
            background: var(--yellow);
            color: var(--fg);
            box-shadow: 0 2px 0 var(--border-dark);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .hero-title {{
            font-size: clamp(42px, 6vw, 84px);
            margin-bottom: 18px;
        }}
        .w {{
            display: inline-block;
            overflow: hidden;
            vertical-align: top;
            padding-bottom: 0.08em;
        }}
        .w i {{
            display: inline-block;
            font-style: normal;
            transform: translateY(110%) rotate(6deg);
            animation: up 0.9s cubic-bezier(.2, .9, .2, 1) forwards;
            animation-delay: calc(var(--n) * 90ms + 0.1s);
        }}
        @keyframes up {{
            to {{ transform: none; }}
        }}
        .hero-sub {{
            margin: 18px 0 28px;
            color: var(--mut);
            font-size: clamp(16px, 1.8vw, 20px);
            max-width: 38ch;
            line-height: 1.5;
            opacity: 0;
            animation: fadeIn 0.8s 0.9s forwards;
        }}
        @keyframes fadeIn {{
            to {{ opacity: 1; }}
        }}
        .hero-actions {{
            display: flex;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
            opacity: 0;
            animation: fadeIn 0.8s 1.1s forwards;
        }}

        /* INTERACTIVE GUIDE LAB WIDGET (FROM DOWNLOADED FILE, ENHANCED) */
        .lab-card {{
            background: #FFFFFF;
            border: 3px solid var(--border-dark);
            border-radius: 28px;
            padding: 24px;
            text-align: center;
            box-shadow: 0 10px 0 var(--border-dark);
            transform: translateY(30px) scale(0.96);
            opacity: 0;
            animation: popIn 0.9s 0.8s cubic-bezier(.2, .9, .2, 1) forwards;
            position: relative;
        }}
        @keyframes popIn {{
            to {{ transform: none; opacity: 1; }}
        }}
        .lab-card p {{
            color: var(--mut);
            margin: 14px 0 18px;
            font-weight: 700;
            font-size: 0.95rem;
            min-height: 2.2em;
        }}
        .hs {{
            width: 100%;
            max-width: 380px;
            height: auto;
            display: block;
            margin: auto;
            overflow: visible;
        }}
        .a1, .a2, .q, .bl {{
            transition: opacity 0.4s;
        }}
        .a2, .bl {{
            opacity: 0;
        }}
        .glued .a1, .glued .q {{
            opacity: 0;
        }}
        .glued .a2, .glued .bl {{
            opacity: 1;
        }}
        .tch {{
            opacity: 0;
            transform: translateX(60px);
            transition: all 0.8s cubic-bezier(.3, 1.4, .4, 1);
        }}
        .glued .tch {{
            opacity: 1;
            transform: none;
        }}
        .q {{
            transform-box: fill-box;
            transform-origin: center;
            animation: wob 0.8s ease-in-out infinite alternate;
        }}
        @keyframes wob {{
            to {{ transform: rotate(-8deg); }}
        }}

        /* =========================================================================
           HIGHLIGHT REELS TICKER IN HERO
           ========================================================================= */
        .ticker-wrapper {{
            max-width: 1240px;
            margin: 20px auto 0;
            position: relative;
        }}
        .ticker-header-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
            padding: 0 4px;
        }}
        .ticker-tag-left {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.9rem;
            color: var(--fg);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .ticker-badge-live {{
            background: #EF4444;
            color: #FFFFFF;
            font-size: 0.7rem;
            padding: 2px 7px;
            border-radius: 99px;
            font-weight: 800;
            animation: pulse-red 1.6s infinite;
        }}
        @keyframes pulse-red {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        .ticker-sub-text {{
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--mut);
        }}

        .reels-track-container {{
            width: 100%;
            overflow: hidden;
            position: relative;
            padding: 8px 0 16px;
            mask-image: linear-gradient(to right, transparent, black 4%, black 96%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 4%, black 96%, transparent);
        }}
        .reels-track {{
            display: flex;
            gap: 16px;
            width: max-content;
            animation: scrollTicker 32s linear infinite;
        }}
        .reels-track:hover {{
            animation-play-state: paused;
        }}
        @keyframes scrollTicker {{
            from {{ transform: translateX(0); }}
            to {{ transform: translateX(-50%); }}
        }}

        .ticker-reel-card {{
            width: 250px;
            background: #FFFFFF;
            border: 3px solid var(--border-dark);
            border-radius: 20px;
            box-shadow: 0 6px 0 var(--border-dark);
            padding: 12px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
            flex-shrink: 0;
            text-align: left;
        }}
        .ticker-reel-card:hover {{
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 8px 0 var(--border-dark);
            background: #FFFDF9;
        }}
        .ticker-thumb-box {{
            width: 100%;
            aspect-ratio: 16 / 10;
            border-radius: 12px;
            border: 2px solid var(--border-dark);
            background: #0F172A;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
        }}
        .ticker-dur-pill {{
            position: absolute;
            bottom: 6px;
            right: 6px;
            background: rgba(0, 0, 0, 0.75);
            color: #FFFFFF;
            font-size: 0.65rem;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 6px;
        }}
        .ticker-play-circle {{
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: rgba(255, 90, 54, 0.9);
            border: 2px solid #FFFFFF;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.4);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            transition: transform 0.2s;
        }}
        .ticker-reel-card:hover .ticker-play-circle {{
            transform: translate(-50%, -50%) scale(1.15);
            background: var(--coral);
        }}
        .ticker-category-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .ticker-cat-badge {{
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 6px;
            background: var(--yellow);
            color: var(--fg);
            border: 1.5px solid var(--border-dark);
        }}
        .ticker-class-text {{
            font-size: 0.68rem;
            font-weight: 700;
            color: var(--mut);
        }}
        .ticker-card-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.88rem;
            line-height: 1.25;
            color: var(--fg);
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        .ticker-teacher-row {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.74rem;
            font-weight: 700;
            color: var(--mut);
            margin-top: auto;
            padding-top: 4px;
            border-top: 1px dashed rgba(0,0,0,0.1);
        }}

        /* =========================================================================
           CINEMATIC STICKY STORYTELLING SECTION (CUSTOM STORYLINE & VISUALS)
           ========================================================================= */
        #story {{
            height: 540vh;
            position: relative;
        }}
        .stage {{
            position: sticky;
            top: 0;
            height: 100vh;
            overflow: hidden;
            display: grid;
            place-items: center;
            background-color: var(--sb, var(--bg));
            transition: background-color 1.2s;
        }}
        .stage[data-s="0"] {{
            --sb: #0F172A;
            --cc: #5458F7;
            color: #FFFFFF;
        }}
        .stage[data-s="1"] {{
            --sb: #EEF2FF;
            --cc: #5458F7;
            color: #18181B;
        }}
        .stage[data-s="2"] {{
            --sb: #FEF3C7;
            --cc: #F59E0B;
            color: #18181B;
        }}
        .stage[data-s="3"] {{
            --sb: #E0F2FE;
            --cc: #0284C7;
            color: #18181B;
        }}
        .stage[data-s="4"] {{
            --sb: #5458F7;
            --cc: #FF5A36;
            color: #FFFFFF;
        }}

        .stage:after {{
            content: "";
            position: absolute;
            inset: 0;
            background: radial-gradient(ellipse at center, transparent 45%, var(--vg));
            pointer-events: none;
            z-index: 6;
        }}
        .prog {{
            position: absolute;
            left: 0;
            top: 0;
            height: 6px;
            background: linear-gradient(90deg, var(--coral), var(--primary), var(--emerald));
            width: calc(var(--p, 0) * 100%);
            z-index: 9;
        }}
        .lb {{
            position: absolute;
            left: 0;
            right: 0;
            height: 0;
            background: var(--bar);
            z-index: 8;
            transition: height 1s;
        }}
        .lb.t {{ top: 0; }}
        .lb.b {{ bottom: 0; }}
        .stage.cine .lb {{
            height: 5vh;
        }}

        #cur {{
            position: absolute;
            inset: 0;
            display: flex;
            z-index: 7;
            pointer-events: none;
        }}
        #cur i {{
            flex: 1;
            background: var(--cc, var(--coral));
            transform: scaleY(0);
        }}
        #cur.go i {{
            animation: curAnim 1.1s cubic-bezier(.7, 0, .3, 1) calc(var(--n) * 60ms) both;
        }}
        @keyframes curAnim {{
            0% {{ transform: scaleY(0); transform-origin: top; }}
            45% {{ transform: scaleY(1); transform-origin: top; }}
            55% {{ transform: scaleY(1); transform-origin: bottom; }}
            100% {{ transform: scaleY(0); transform-origin: bottom; }}
        }}

        .scene {{
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 0 6vw;
            opacity: 0;
            z-index: 1;
            pointer-events: none;
            clip-path: circle(0% at var(--o, 50% 50%));
            transform: scale(1.2);
            transition: clip-path 1.2s cubic-bezier(.7, 0, .2, 1), transform 1.6s cubic-bezier(.2, .8, .2, 1), opacity 0s;
        }}
        .scene.on {{
            opacity: 1;
            z-index: 3;
            pointer-events: auto;
            clip-path: circle(150% at var(--o, 50% 50%));
            transform: none;
        }}
        .scene.out {{
            opacity: 1;
            z-index: 2;
            clip-path: circle(150% at 50% 50%);
            transform: scale(0.88);
            filter: brightness(0.4) blur(6px);
            transition: transform 1.2s, filter 1.2s;
        }}
        .scene:not(.on):not(.out) * {{
            transition-duration: 0s !important;
            transition-delay: 0s !important;
        }}

        .big {{
            font-size: clamp(38px, 6.5vw, 96px);
            max-width: 18ch;
        }}
        .t2 {{
            font-size: clamp(32px, 5.5vw, 80px);
            margin-bottom: 12px;
        }}
        .mask {{
            clip-path: inset(0 100% 0 0);
            transition: clip-path 1s cubic-bezier(.7, 0, .2, 1);
        }}
        .on .mask {{
            clip-path: inset(0 0 0 0);
            transition-delay: 0.55s;
        }}
        .cap {{
            font-size: clamp(15px, 2vw, 20px);
            margin-top: 16px;
            max-width: 44ch;
            opacity: 0;
            transform: translateY(20px);
            transition: 0.8s 0.7s;
            line-height: 1.5;
        }}
        .stage[data-s="0"] .cap, .stage[data-s="4"] .cap {{
            color: #E2E8F0;
        }}
        .stage:not([data-s="0"]):not([data-s="4"]) .cap {{
            color: #475569;
        }}
        .on .cap {{
            opacity: 1;
            transform: none;
            transition-delay: 1s;
        }}

        .bgword {{
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 2vh;
            overflow: hidden;
            opacity: 0.12;
            z-index: -1;
            pointer-events: none;
        }}
        .bgword div {{
            font-family: 'Outfit', sans-serif;
            font-size: 16vh;
            font-weight: 900;
            white-space: nowrap;
            color: transparent;
            -webkit-text-stroke: 2px currentColor;
            animation: mq 28s linear infinite;
        }}
        .bgword div + div {{
            animation-direction: reverse;
        }}
        @keyframes mq {{
            to {{ transform: translateX(-50%); }}
        }}

        /* SCENE VISUALS */
        svg.sv {{
            width: min(88vw, 480px);
            height: auto;
            max-height: 40vh;
            margin: 8px 0 20px;
            overflow: visible;
        }}
        .fl {{
            font-size: 34px;
            animation: drift 3.2s ease-in-out infinite alternate;
        }}
        @keyframes drift {{
            to {{ translate: var(--dx) var(--dy); }}
        }}

        /* Whiteboard in Scene 1 */
        .wb-frame {{
            transform-box: fill-box;
            transform-origin: center;
            transform: scale(0);
            transition: transform 0.7s cubic-bezier(.3, 1.5, .4, 1) 0.6s;
        }}
        .on .wb-frame {{
            transform: none;
        }}
        .wb text {{
            font-family: 'Outfit', sans-serif;
            font-size: 26px;
            font-weight: 800;
            opacity: 0;
            transition: opacity 0.5s;
        }}
        .on .t1 {{
            opacity: 1;
            transition-delay: 1.2s;
        }}
        .on .t2 {{
            opacity: 1;
            transition-delay: 2.2s;
        }}

        /* Timeline in Scene 2 */
        svg.tg {{
            width: min(94vw, 880px);
            overflow: visible;
            margin-top: 18px;
        }}
        .tg path {{
            fill: none;
            stroke: var(--coral);
            stroke-width: 8;
            stroke-linecap: round;
            stroke-dasharray: 1;
            stroke-dashoffset: 1;
            transition: stroke-dashoffset 2.5s linear;
        }}
        .on .tg path {{
            stroke-dashoffset: 0;
        }}
        .tg circle {{
            fill: #FFFFFF;
            stroke: var(--border-dark);
            stroke-width: 3;
            transform-box: fill-box;
            transform-origin: center;
            transform: scale(0);
            transition: transform 0.6s cubic-bezier(.3, 1.8, .4, 1) calc(var(--n) * 0.8s);
        }}
        .on .tg circle {{
            transform: scale(1);
        }}
        .tg text {{
            fill: var(--fg);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 19px;
            text-anchor: middle;
            opacity: 0;
            transition: opacity 0.6s calc(var(--n) * 0.8s + 0.2s);
        }}
        .on .tg text {{
            opacity: 1;
        }}
        .tg .em {{
            font-size: 26px;
        }}

        /* 3D Cards in Scene 3 */
        .cards {{
            display: flex;
            justify-content: center;
            margin: 24px 0 10px;
            perspective: 900px;
        }}
        .tc {{
            width: clamp(140px, 22vw, 220px);
            aspect-ratio: 9 / 14;
            border-radius: 24px;
            border: 3px solid var(--border-dark);
            box-shadow: 0 8px 0 var(--border-dark);
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            color: #1A1200;
            text-align: left;
            margin: 0 calc(clamp(140px, 22vw, 220px) / -2.4);
            transform: translateY(60px);
            opacity: 0;
            transition: all 1s cubic-bezier(.2, .9, .2, 1);
            position: relative;
        }}
        .on .tc {{
            opacity: 1;
            margin: 0 10px;
            transform: rotate(var(--r)) translateY(var(--y));
        }}
        .tc u {{
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-size: 11px;
            font-weight: 900;
            background: rgba(255, 255, 255, 0.9);
            border: 1.5px solid var(--border-dark);
            border-radius: 99px;
            padding: 3px 10px;
            align-self: flex-start;
            margin-bottom: 8px;
            color: var(--border-dark);
        }}
        .tc b {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(14px, 1.8vw, 20px);
            line-height: 1.15;
            font-weight: 900;
        }}
        .tc small {{
            font-weight: 700;
            opacity: 0.8;
            margin-top: 4px;
            font-size: 0.8rem;
        }}
        .tc svg {{
            position: absolute;
            top: 14px;
            left: 0;
            width: 100%;
            padding: 0 16px;
        }}

        /* 1:1 Climax Scene 4 */
        .row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 2vw;
        }}
        .row .stat {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: clamp(70px, 16vw, 200px);
            color: var(--yellow);
            text-shadow: 0 6px 0 rgba(0,0,0,0.3);
        }}
        .row svg {{
            width: clamp(70px, 14vw, 150px);
            transform: scale(0);
            transition: transform 0.8s cubic-bezier(.3, 1.5, .4, 1) 0.9s;
        }}
        .on .row svg {{
            transform: none;
        }}

        /* MARQUEE */
        .marq {{
            overflow: hidden;
            white-space: nowrap;
            padding: 4.5vh 0;
            background: #111827;
            border-top: 3px solid #000;
            border-bottom: 3px solid #000;
            color: #FFFFFF;
        }}
        .marq div {{
            display: inline-block;
            font-family: 'Outfit', sans-serif;
            font-size: clamp(40px, 8vw, 110px);
            font-weight: 900;
            letter-spacing: -0.03em;
            animation: mq 24s linear infinite;
        }}
        .marq span {{
            color: transparent;
            -webkit-text-stroke: 2px #FFFFFF;
        }}
        .marq em {{
            color: var(--coral);
            font-style: normal;
        }}

        /* FAQS */
        .faq {{
            padding: 10vh 6vw;
            max-width: 900px;
            margin: auto;
        }}
        .faq h2 {{
            font-size: clamp(36px, 5vw, 68px);
            margin-bottom: 30px;
            text-align: center;
        }}
        details {{
            border: 3px solid var(--border-dark);
            border-radius: 16px;
            background: #FFFFFF;
            box-shadow: 0 4px 0 var(--border-dark);
            padding: 18px 24px;
            margin-bottom: 14px;
            cursor: pointer;
        }}
        summary {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(18px, 2.2vw, 24px);
            font-weight: 800;
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        summary::-webkit-details-marker {{ display: none; }}
        summary:after {{
            content: "+";
            color: var(--coral);
            font-size: 28px;
            font-weight: 800;
            transition: transform 0.2s;
        }}
        details[open] summary:after {{
            transform: rotate(45deg);
        }}
        details p {{
            color: var(--mut);
            margin-top: 14px;
            line-height: 1.55;
            font-size: 0.98rem;
        }}

        /* CTA */
        .cta {{
            text-align: center;
            padding: 14vh 6vw;
            background: linear-gradient(135deg, #FEF08A 0%, #FDE047 100%);
            border-top: 3px solid var(--border-dark);
            border-bottom: 3px solid var(--border-dark);
        }}
        .cta h2 {{
            font-size: clamp(42px, 8vw, 110px);
            margin-bottom: 30px;
            color: var(--fg);
        }}
        .cta .btn {{
            margin: 6px;
        }}

        /* FOOTER */
        footer {{
            text-align: center;
            color: var(--mut);
            padding: 40px 6vw 50px;
            font-size: 14px;
            background: #FAF7F2;
        }}
        footer a {{
            color: var(--fg);
            font-weight: 700;
            text-decoration: none;
        }}
        .footer-big-word {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: clamp(60px, 14vw, 170px);
            letter-spacing: -0.05em;
            color: rgba(0, 0, 0, 0.06);
            margin-top: 20px;
            line-height: 0.8;
            user-select: none;
        }}

        /* =========================================================================
           INTERACTIVE REEL THEATER MODAL (OPENS ON TICKER CARD CLICK)
           ========================================================================= */
        .reel-modal-overlay {{
            position: fixed;
            inset: 0;
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            padding: 20px;
        }}
        .reel-modal-overlay.active {{
            display: flex;
        }}
        .reel-modal-card {{
            background: #FAF7F2;
            border: 4px solid var(--border-dark);
            border-radius: 32px;
            box-shadow: 0 16px 0 var(--border-dark);
            max-width: 840px;
            width: 100%;
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 24px;
            padding: 24px;
            position: relative;
            animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            color: var(--fg);
            text-align: left;
        }}
        @keyframes modalPop {{
            from {{ transform: scale(0.92); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}
        .modal-close-btn {{
            position: absolute;
            top: 16px;
            right: 18px;
            font-size: 1.4rem;
            font-weight: 900;
            color: var(--border-dark);
            cursor: pointer;
            border: none;
            background: none;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .modal-close-btn:hover {{
            background: #E2E8F0;
        }}

        /* Phone player inside modal */
        .modal-phone-player {{
            width: 100%;
            aspect-ratio: 9 / 16;
            background: #0B1120;
            border: 3px solid var(--border-dark);
            border-radius: 24px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .modal-visual-scene {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            text-align: center;
            padding: 20px;
        }}
        .modal-center-play {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            cursor: pointer;
        }}
        .modal-play-btn {{
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.65);
            border: 2px solid #FFFFFF;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            transition: transform 0.2s;
        }}
        .modal-play-btn:hover {{
            transform: scale(1.1);
            background: var(--coral);
        }}
        .modal-bottom-bar {{
            position: relative;
            z-index: 10;
            padding: 14px;
            background: linear-gradient(0deg, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0) 100%);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .modal-caption {{
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            padding: 6px 10px;
            font-size: 0.78rem;
            color: #FFFFFF;
            line-height: 1.35;
        }}
        .modal-progress-wrap {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .modal-progress-bar {{
            flex: 1;
            height: 5px;
            background: rgba(255, 255, 255, 0.25);
            border-radius: 99px;
            position: relative;
            overflow: hidden;
        }}
        .modal-progress-fill {{
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 48%;
            background: var(--coral);
            border-radius: 99px;
        }}
        .modal-time-lbl {{
            font-size: 0.68rem;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 700;
        }}

        /* Modal details */
        .modal-details-col {{
            display: flex;
            flex-direction: column;
            gap: 16px;
            justify-content: center;
        }}
        .modal-category-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--coral);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.78rem;
            padding: 3px 10px;
            border-radius: 8px;
            width: fit-content;
        }}
        .modal-reel-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 1.6rem;
            line-height: 1.2;
            color: var(--fg);
        }}
        .modal-quote-box {{
            background: #FFFBEB;
            border-left: 4px solid #F59E0B;
            border-radius: 0 12px 12px 0;
            padding: 12px 16px;
            font-size: 0.95rem;
            color: #78350F;
            font-style: italic;
        }}
        .modal-teacher-card {{
            display: flex;
            align-items: center;
            gap: 12px;
            background: #FFFFFF;
            border: 2px solid var(--border-dark);
            border-radius: 16px;
            padding: 12px 16px;
            box-shadow: 0 3px 0 var(--border-dark);
        }}
        .modal-teacher-avatar {{
            width: 48px;
            height: 48px;
            border-radius: 12px;
            border: 2px solid var(--border-dark);
            overflow: hidden;
            background: #FFFFFF;
        }}
        .modal-teacher-avatar img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        @media (max-width: 860px) {{
            .hero-grid {{
                grid-template-columns: 1fr;
            }}
            .reel-modal-card {{
                grid-template-columns: 1fr;
                max-width: 420px;
            }}
            .nav-links-wrap {{
                display: none;
            }}
            .on .tc:nth-child(3) {{
                display: none;
            }}
        }}
    </style>
</head>
<body>

    <!-- TOP PROTOTYPE BAR -->
    <div class="prototype-banner">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span class="prototype-badge">Prototype #1</span>
            <span><strong>Guided Learning Landing Page</strong> (Hero Ticker + AI Predictor Storytelling Stage)</span>
        </div>
        <div class="prototype-links">
            <a href="/index.html" class="prototype-link-btn">⎇ Prototype Hub</a>
            <a href="/landing.html" class="prototype-link-btn active">Landing Page</a>
            <a href="/homepage-section.html" class="prototype-link-btn">Homepage Section</a>
            <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="prototype-link-btn">Original Reel ↗</a>
        </div>
    </div>

    <!-- SVG GLOBAL DEFINITIONS -->
    <svg width="0" height="0" style="position:absolute" aria-hidden="true">
        <defs>
            <g id="hd">
                <circle r="34" style="fill:#F2C6A0"/>
                <path d="M-35-4Q-30-48 0-46Q30-48 35-4Q20-26 0-24Q-20-26-35-4Z" fill="#18181B"/>
                <circle cx="-12" cy="2" r="3.5" fill="#18181B"/>
                <circle cx="12" cy="2" r="3.5" fill="#18181B"/>
            </g>
            <g id="stuS">
                <path d="M-62 110Q0 20 62 110Z" style="fill:#38BDF8"/>
                <use href="#hd"/>
                <path d="M-19-9l12-3M19-9l-12-3M-10 22Q0 14 10 22" stroke="#18181B" stroke-width="3" fill="none" stroke-linecap="round"/>
            </g>
            <g id="stuH">
                <path d="M-62 110Q0 20 62 110Z" style="fill:#38BDF8"/>
                <use href="#hd"/>
                <path d="M-12 14Q0 30 12 14" stroke="#18181B" stroke-width="3" fill="none" stroke-linecap="round"/>
            </g>
            <g id="tea">
                <path d="M-62 110Q0 20 62 110Z" style="fill:var(--coral)"/>
                <circle r="34" style="fill:#F2C6A0"/>
                <path d="M-36 0Q-34-50 0-48Q34-50 36 0Q22-24 0-22Q-22-24-36 0Z" fill="#3A2A1A"/>
                <circle cx="-12" cy="2" r="9" fill="none" stroke="#3A2A1A" stroke-width="2.5"/>
                <circle cx="12" cy="2" r="9" fill="none" stroke="#3A2A1A" stroke-width="2.5"/>
                <path d="M-3 2h6M-12 18Q0 30 12 18" stroke="#3A2A1A" stroke-width="3" fill="none" stroke-linecap="round"/>
            </g>
        </defs>
    </svg>

    <!-- STICKY NAVBAR -->
    <nav class="main-nav">
        <a href="/" class="nav-brand">
            <div class="nav-logo-box">
                <svg viewBox="-5.5 -2.5 45 45" fill="none">
                    <circle cx="16.827" cy="20.95" r="21.5" fill="#FFFFFF" />
                    <path d="M15.3789 1.56641C18.3485 -0.00397233 21.8239 -0.319563 25.0273 0.691406V0.692383C28.099 1.67819 30.6634 3.82668 32.1709 6.67871V6.67969C33.65 9.5688 33.9475 12.9198 33.001 16.0244L33 16.0273C32.7663 16.8763 32.3452 17.8593 31.7959 18.7578C31.2461 19.6571 30.5729 20.4651 29.8379 20.9727L29.8301 20.9785L29.8232 20.9854C29.2171 21.5856 28.6251 22.154 27.9209 22.6201L27.9131 22.626C27.417 23.0235 26.8435 23.281 26.2578 23.5615C23.8896 24.6956 21.2532 25.014 18.6572 25.3838C17.5223 25.5455 16.3713 25.7405 15.2402 25.874L15.1436 25.8857V25.9824C15.1382 26.9792 15.125 28.0164 15.1436 29.0146V29.0195C15.2326 30.5471 15.239 32.7448 14.9053 34.1934C13.8023 38.9792 8.91801 41.328 4.48145 39.2656H4.48047C3.48 38.8053 2.75252 38.2262 2.0791 37.3516L2.07324 37.3457L1.92285 37.1709C0.397689 35.3408 -0.21388 32.689 0.275391 30.3652L0.167969 30.3418L0.276367 30.3652L0.277344 30.3525C0.278271 30.3429 0.278388 30.3323 0.279297 30.3223C0.903668 26.8641 3.29994 24.1185 6.36719 22.4961C6.57023 22.3887 7.15533 22.1484 7.72852 21.9053C8.01263 21.7848 8.29222 21.6643 8.51465 21.5615C8.62571 21.5102 8.72387 21.4623 8.80176 21.4209C8.87621 21.3814 8.94258 21.3425 8.98145 21.3076L9.01953 21.2734L9.01758 21.2227C8.99171 20.3933 8.98483 19.563 8.99609 18.7334C9.00396 17.9678 8.98779 17.1376 8.97266 16.2813C8.95751 15.4242 8.94299 14.5395 8.95312 13.6621C8.97343 11.9056 9.09309 10.1855 9.5 8.77832C10.3637 5.7917 12.3812 3.2335 15.1123 1.71094L15.3789 1.56641Z" fill="#5F5AF6" stroke="black" stroke-width="0.22"/>
                    <path d="M27.142 13.0609L27.3185 13.0612C27.6183 13.0878 27.9587 13.1253 28.1817 13.3206C30.8965 15.699 31.0252 18.9068 29.2136 21.755C28.9327 22.1967 28.2947 22.2791 28.2108 22.7999C27.611 23.2069 26.9192 23.4699 26.2332 23.7481C23.4164 24.8906 20.2822 25.2101 17.2249 25.579C15.8905 25.74 14.8158 26.2706 13.4793 26.4041C11.7112 26.6422 8.30149 30.1145 6.60504 30.5874C6.60829 30.4183 6.91796 27.3761 7.84467 25.579C9.43249 22.4998 11.9016 21.1201 14.734 19.8646C15.0803 19.6812 15.3437 19.6949 15.6625 19.4302L15.5989 19.3706C15.8376 19.2941 17.1559 19.1762 17.4724 19.137C22.4276 18.5234 26.1931 17.7941 27.142 13.0609Z" fill="#E87257"/>
                </svg>
            </div>
            <span class="nav-brand-title">Paathshala <span>· Guided learning</span></span>
        </a>
        <div class="nav-links-wrap">
            <a href="#hero" class="nav-link-item">Highlight Reels</a>
            <a href="#story" class="nav-link-item">The Journey</a>
            <a href="#faq" class="nav-link-item">Parents FAQ</a>
        </div>
        <a href="https://paathshala.app/booking" class="btn-trial-nav">Book free trial</a>
    </nav>

    <!-- HERO SECTION -->
    <section class="hero-section" id="hero">
        <div class="hero-grid">
            <div>
                <span class="pill-tag">✨ Live 1-on-1 classes · Classes 1 to 12</span>
                <h1 class="hero-title" id="h1"></h1>
                <p class="hero-sub">
                    A dedicated top 1.4% educator who meets your child exactly where they're stuck — turning textbook confusion into crystal-clear "Aha!" moments.
                </p>
                <div class="hero-actions">
                    <a class="btn" href="https://paathshala.app/booking">Book free trial class ➔</a>
                    <a class="btn ghost" href="#story">Explore why it matters ↓</a>
                </div>
            </div>

            <!-- INTERACTIVE LAB CARD -->
            <div class="lab-card">
                <svg class="hs" id="nuc" viewBox="0 0 340 280" aria-hidden="true">
                    <rect x="20" y="248" width="300" height="8" rx="4" style="fill:#CBD5E1"/>
                    <g class="a1"><use href="#stuS" x="105" y="135"/></g>
                    <g class="a2"><use href="#stuH" x="105" y="135"/></g>
                    <path d="M60 248l45-18 45 18z" fill="#FFFDF9" stroke="#18181B" stroke-width="2"/>
                    <g class="q">
                        <circle cx="105" cy="45" r="32" style="fill:#FEE2E2; stroke:#EF4444; stroke-width:2;"/>
                        <text x="105" y="58" text-anchor="middle" font-family="'Outfit',sans-serif" font-size="36" font-weight="900" style="fill:#EF4444">?</text>
                    </g>
                    <g class="bl">
                        <circle cx="105" cy="45" r="32" style="fill:#FEF08A; stroke:#F59E0B; stroke-width:2;"/>
                        <text x="105" y="56" text-anchor="middle" font-size="28">💡</text>
                    </g>
                    <g class="tch">
                        <use href="#tea" x="245" y="135"/>
                        <rect x="180" y="14" width="140" height="36" rx="18" fill="#18181B"/>
                        <text x="250" y="37" text-anchor="middle" font-family="'Outfit',sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Let's try it together!</text>
                    </g>
                </svg>
                <p id="lt">Stuck on a tricky question, all alone.</p>
                <button class="btn ghost" id="glue" style="width:100%; justify-content:center; padding:12px 20px;">
                    Turn on the guide ✨
                </button>
            </div>
        </div>

        <!-- =========================================================================
             HIGHLIGHT REELS TICKER IN HERO
             ========================================================================= -->
        <div class="ticker-wrapper">
            <div class="ticker-header-row">
                <div class="ticker-tag-left">
                    <span class="ticker-badge-live">LIVE</span>
                    <span>Browse Class Highlights · Tap to preview reel</span>
                </div>
                <div class="ticker-sub-text">
                    500+ Concept Reels from real 1-on-1 sessions
                </div>
            </div>

            <div class="reels-track-container">
                <div class="reels-track" id="reelsTickerTrack">
                    <!-- REEL CARDS (DUPLICATED FOR CONTINUOUS TICKER LOOP) -->
                </div>
            </div>
        </div>
    </section>

    <!-- =========================================================================
         CINEMATIC STORYTELLING SECTION (CUSTOM STORYLINE FOR GUIDED LEARNING)
         ========================================================================= -->
    <section id="story">
        <div class="stage" id="stage" data-s="0">
            <div class="prog"></div>
            <div class="lb t"></div>
            <div class="lb b"></div>
            <div id="cur"></div>

            <!-- SCENE 0: THE MAZE OF LEARNING ALONE -->
            <div class="scene" style="--o:50% 50%">
                <div class="bgword">
                    <div>STUCK · CONFUSED · OVERWHELMED · STUCK ·</div>
                    <div>LOST IN NOTES · ENDLESS VIDEOS · NO ANSWERS ·</div>
                </div>
                <svg class="sv" viewBox="0 0 400 270" aria-hidden="true">
                    <use href="#stuS" x="200" y="115" transform="translate(-40 -23) scale(1.2)"/>
                    <text class="fl" x="40" y="70" style="--dx:14px;--dy:-10px">📚</text>
                    <text class="fl" x="320" y="60" style="--dx:-12px;--dy:12px">▶️</text>
                    <text class="fl" x="30" y="210" style="--dx:10px;--dy:12px">📝</text>
                    <text class="fl" x="330" y="210" style="--dx:-14px;--dy:-8px">💻</text>
                    <text class="fl" x="130" y="30" style="--dx:6px;--dy:-14px;fill:#EF4444;font-weight:900">?</text>
                    <text class="fl" x="245" y="40" style="--dx:-8px;--dy:-12px;fill:#EF4444;font-weight:900">?</text>
                </svg>
                <div class="big mask">Learning alone is an <span class="hl">exhausting maze.</span></div>
                <p class="cap">
                    Recorded videos, one-way lectures, endless PDFs. When a child gets stuck at 8:15 PM, a pre-recorded screen cannot see the confusion in their eyes.
                </p>
            </div>

            <!-- SCENE 1: THEN A GUIDE STEPS IN -->
            <div class="scene" style="--o:15% 85%">
                <div class="big t2 mask">Then a guide <span class="hl">steps in.</span></div>
                <svg class="sv" viewBox="0 0 420 275" aria-hidden="true">
                    <defs>
                        <clipPath id="c1"><rect x="20" y="14" width="180" height="136" rx="14"/></clipPath>
                        <clipPath id="c2"><rect x="220" y="14" width="180" height="136" rx="14"/></clipPath>
                    </defs>
                    <g class="wb-frame">
                        <rect x="20" y="14" width="180" height="136" rx="14" style="fill:#E0E7FF; stroke:#272727; stroke-width:2.5;"/>
                        <g clip-path="url(#c1)"><use href="#tea" x="110" y="62" transform="translate(110 62) scale(.72) translate(-110 -62)"/></g>
                    </g>
                    <g class="wb-frame">
                        <rect x="220" y="14" width="180" height="136" rx="14" style="fill:#E0F2FE; stroke:#272727; stroke-width:2.5;"/>
                        <g clip-path="url(#c2)"><use href="#stuH" x="310" y="62" transform="translate(310 62) scale(.72) translate(-310 -62)"/></g>
                    </g>
                    <g class="wb">
                        <rect x="20" y="164" width="380" height="100" rx="14" fill="#FFFFFF" stroke="#272727" stroke-width="2.5"/>
                        <text class="t1" x="44" y="210" fill="#18181B">2x + 3 = 11  ➔  2x = 8</text>
                        <text class="t2" x="44" y="248" fill="#10B981">x = 4  ✓ (Awesome!)</text>
                    </g>
                </svg>
                <p class="cap">One master teacher. One student. One interactive shared whiteboard where doubts vanish instantly.</p>
            </div>

            <!-- SCENE 2: THE 60-SECOND AHA! PRINCIPLE -->
            <div class="scene" style="--o:50% 100%">
                <div class="big t2 mask">From confusion to <span class="hl">"Aha!"</span> in 60s.</div>
                <svg class="tg" viewBox="0 0 800 250" aria-hidden="true">
                    <path pathLength="1" d="M40 180C150 180 150 60 270 60S400 180 530 180 670 60 760 60"/>
                    <circle cx="40" cy="180" r="30" style="--n:0"/>
                    <circle cx="270" cy="60" r="30" style="--n:1"/>
                    <circle cx="530" cy="180" r="30" style="--n:2"/>
                    <circle cx="760" cy="60" r="30" style="--n:3"/>
                    <text class="em" x="40" y="190" style="--n:0">😕</text>
                    <text class="em" x="270" y="70" style="--n:1">💡</text>
                    <text class="em" x="530" y="190" style="--n:2">✏️</text>
                    <text class="em" x="760" y="70" style="--n:3">🏆</text>
                    <text x="40" y="238" style="--n:0">Stuck</text>
                    <text x="270" y="24" style="--n:1">Visual Analogy</text>
                    <text x="530" y="238" style="--n:2">Whiteboard Practice</text>
                    <text x="735" y="24" style="--n:3">Exam Confidence</text>
                </svg>
                <p class="cap">
                    Our tutors don't read from boring slides. They craft memorable metaphors — turning complex atomic forces into "nuclear glue" and mental math into visual acrobatics.
                </p>
            </div>

            <!-- SCENE 3: NOTHING GETS LOST (PRESERVED REELS) -->
            <div class="scene" style="--o:0% 50%">
                <div class="big t2 mask">Nothing gets <span class="hl">lost.</span></div>
                <div class="cards">
                    <div class="tc" style="--r:-7deg;--y:14px;background:#BAE6FD">
                        <svg viewBox="0 0 100 70">
                            <rect width="100" height="70" rx="9" fill="#18181B"/>
                            <circle cx="50" cy="31" r="15" fill="#FFFFFF"/>
                            <path d="M45 23l14 8-14 8z" fill="#18181B"/>
                            <rect x="10" y="57" width="80" height="5" rx="2.5" fill="#FFFFFF55"/>
                            <rect x="10" y="57" width="46" height="5" rx="2.5" fill="#FF5A36"/>
                        </svg>
                        <u>Recordings</u>
                        <b>Full Class Replay</b>
                        <small>Never miss a note</small>
                    </div>

                    <div class="tc" style="--r:0deg;--y:-16px;background:#FEF08A">
                        <svg viewBox="0 0 100 70">
                            <rect width="100" height="70" rx="9" fill="#18181B"/>
                            <path d="M10 48H90" stroke="#FFFFFF66" stroke-width="4" stroke-linecap="round"/>
                            <circle cx="28" cy="48" r="5" fill="#FFFFFF"/>
                            <circle cx="80" cy="48" r="5" fill="#FFFFFF"/>
                            <path d="M58 14l5 11 12 1-9 8 3 12-11-6-11 6 3-12-9-8 12-1z" fill="#FF5A36"/>
                        </svg>
                        <u>Guided Reels</u>
                        <b>60s 'Aha!' Moments</b>
                        <small>Direct breakthroughs</small>
                    </div>

                    <div class="tc" style="--r:7deg;--y:14px;background:#BBF7D0">
                        <svg viewBox="0 0 100 70">
                            <rect width="100" height="70" rx="9" fill="#18181B"/>
                            <rect x="8" y="8" width="58" height="22" rx="9" fill="#FFFFFFCC"/>
                            <rect x="16" y="15" width="40" height="3" rx="1.5" fill="#18181B"/>
                            <rect x="16" y="21" width="26" height="3" rx="1.5" fill="#18181B"/>
                            <rect x="34" y="38" width="58" height="22" rx="9" fill="#FF5A36"/>
                            <rect x="42" y="45" width="40" height="3" rx="1.5" fill="#18181B"/>
                            <rect x="42" y="51" width="22" height="3" rx="1.5" fill="#18181B"/>
                        </svg>
                        <u>Mitra AI</u>
                        <b>Personalized Revision</b>
                        <small>24/7 AI companion</small>
                    </div>
                </div>
                <p class="cap">Every breakthrough from live class is preserved as a bite-sized video clip for your child's revision library.</p>
                <button class="btn ghost" onclick="openReelModal(0)" style="margin-top:22px">
                    Watch Leah's 'Nuclear Glue' Highlight ➔
                </button>
            </div>

            <!-- SCENE 4: 1 ON 1 WITH TOP 1.4% TUTORS -->
            <div class="scene" style="--o:100% 0%">
                <div class="row">
                    <svg viewBox="-70 -60 140 180" aria-hidden="true"><use href="#tea"/></svg>
                    <div class="big stat mask">1 : 1</div>
                    <svg viewBox="-70 -60 140 180" aria-hidden="true"><use href="#stuH"/></svg>
                </div>
                <p class="cap" style="margin-top:0">
                    A dedicated human mentor who knows your child. Not an algorithm. Not a crowd of 200 students in a silent webinar.
                </p>
                <a class="btn" href="https://paathshala.app/booking" style="margin-top:24px">
                    Book free 1-on-1 trial class ➔
                </a>
            </div>

        </div>
    </section>

    <!-- LIVE MARQUEE -->
    <div class="marq">
        <div>
            <span>Stuck. </span><em>Guided. </em><span>Growing. </span><em>Confident. </em><span>Ace exams. </span>    
            <span>Stuck. </span><em>Guided. </em><span>Growing. </span><em>Confident. </em><span>Ace exams. </span>    
            <span>Stuck. </span><em>Guided. </em><span>Growing. </span><em>Confident. </em><span>Ace exams. </span>
        </div>
    </div>

    <!-- FAQS -->
    <section class="faq" id="faq">
        <h2>Quick answers for parents</h2>
        
        <details open>
            <summary>What is Guided Learning?</summary>
            <p>
                Each student is matched 1-on-1 with an elite, vetted teacher. Every live class is backed by full recordings, AI-extracted 60-second highlight reels ("Aha!" moments), and Mitra AI for round-the-clock revision.
            </p>
        </details>

        <details>
            <summary>Are the highlight reels accessible to parents and students?</summary>
            <p>
                Yes! All 500+ Guided Learning concept reels across Math, Science, and English are 100% free to explore, revisit, and share before tests and exams.
            </p>
        </details>

        <details>
            <summary>How are Paathshala tutors selected?</summary>
            <p>
                Only 1.4% of educator applicants make the cut. Every tutor undergoes rigorous pedagogical testing, background screening, and SafeTutor child-safety verification.
            </p>
        </details>

        <details>
            <summary>How do we start?</summary>
            <p>
                Simply book a free 30-minute trial class. Your child will meet their teacher, experience the interactive whiteboard, and get their first concept gap solved on day one.
            </p>
        </details>
    </section>

    <!-- FINAL CALL TO ACTION -->
    <section class="cta">
        <h2>Give them a <span class="hl">guide.</span></h2>
        <a class="btn" href="https://paathshala.app/booking">Book free trial class ➔</a>
        <a class="btn ghost" href="#hero">Browse highlight reels ↑</a>
    </section>

    <!-- FOOTER -->
    <footer>
        <p>© 2026 Safwhigre Technologies OPC Private Limited · <a href="https://paathshala.app/">paathshala.app</a> · +91 80105 71912</p>
        <div class="footer-big-word">paathshala</div>
    </footer>

    <!-- =========================================================================
         REEL THEATER POPUP MODAL (ACTIVATED ON TICKER CLICK)
         ========================================================================= -->
    <div class="reel-modal-overlay" id="reelModal">
        <div class="reel-modal-card">
            <button class="modal-close-btn" onclick="closeReelModal()">✕</button>
            
            <!-- PHONE PLAYER -->
            <div class="modal-phone-player">
                <div class="modal-visual-scene" id="modalVisualScene">
                    <!-- Dynamic concept animation -->
                </div>
                <div class="modal-center-play" onclick="toggleModalPlay()">
                    <div class="modal-play-btn" id="modalPlayBtn">⏸</div>
                </div>
                <div class="modal-bottom-bar">
                    <div class="modal-caption" id="modalCaption">
                        "They act like nuclear glue, holding the protons together!"
                    </div>
                    <div class="modal-progress-row">
                        <div class="modal-progress-bar">
                            <div class="modal-progress-fill" id="modalProgressFill"></div>
                        </div>
                        <span class="modal-time-lbl" id="modalTimeLbl">0:24 / 0:50</span>
                    </div>
                </div>
            </div>

            <!-- DETAILS & ACTIONS -->
            <div class="modal-details-col">
                <span class="modal-category-pill" id="modalCategoryBadge">🎯 Aha Moment!</span>
                <h3 class="modal-reel-title" id="modalReelTitle">The 'Nuclear Glue' Inside an Atom</h3>
                
                <div class="modal-quote-box" id="modalQuoteBox">
                    “They act like nuclear glue, holding the protons together so they don't push each other away.”
                </div>

                <div class="modal-teacher-card">
                    <div class="modal-teacher-avatar">
                        <img src="data:image/jpeg;base64,{avatar_b64}" alt="Teacher Photo" id="modalTeacherPhoto">
                    </div>
                    <div>
                        <div style="font-family:'Outfit',sans-serif; font-weight:800; font-size:1rem;" id="modalTeacherName">Leah Alexander</div>
                        <div style="font-size:0.75rem; color:#0369A1; font-weight:700;">★ 4.95 Rating · B.Ed Verified · Kochi</div>
                    </div>
                </div>

                <a href="https://paathshala.app/booking?teacherId=d2dOWorLt4QEmqARukBjIayAknk1" target="_blank" class="btn" style="width:100%; justify-content:center;">
                    Book Free 1-on-1 Class with Tutor ➔
                </a>
            </div>

        </div>
    </div>

    <!-- SCRIPTS -->
    <script>
        // 1. Kinetic Headline Animation
        document.getElementById("h1").innerHTML = "Don't get stuck. Get guided.".split(" ").map(function(w, i) {{
            return '<span class="w"><i style="--n:' + i + '" class="' + (i > 2 ? 'hl' : '') + '">' + w + '</i></span> ';
        }}).join("");

        // 2. Interactive Guide Toggle
        var nuc = document.getElementById("nuc"),
            gb = document.getElementById("glue"),
            lt = document.getElementById("lt");
            
        gb.onclick = function() {{
            var g = nuc.classList.toggle("glued");
            gb.textContent = g ? "Turn off the guide ✕" : "Turn on the guide ✨";
            lt.textContent = g ? "With a personal guide beside them, everything clicks." : "Stuck on a tricky question, all alone.";
        }};

        // 3. Highlight Reels Data for Ticker & Modal
        const TICKER_REELS = [
            {{
                id: "nuclear-glue",
                title: "The 'Nuclear Glue' Inside an Atom",
                category: "🎯 Aha Moment!",
                grade: "Classes 8–9 · Physics",
                duration: "0:50",
                teacher: "Leah Alexander",
                emoji: "⚛️",
                quote: "“They act like nuclear glue, holding the protons together so they don't push each other away.”",
                caption: "Leah: \"Protons all repel each other. Neutrons act like nuclear glue to hold the atom core together!\"",
                visual: `<div style="font-size:4rem; animation:wob 1.8s infinite alternate;">⚛️</div><div style="color:#FEF08A; font-family:'Outfit',sans-serif; font-weight:800; font-size:1.1rem; margin-top:8px;">Nuclear Glue</div>`
            }},
            {{
                id: "empty-space",
                title: "You Are 99.999% Empty Space!",
                category: "🎯 Mind Blown",
                grade: "Class 9 · Chemistry",
                duration: "0:58",
                teacher: "Leah Alexander",
                emoji: "🌌",
                quote: "“The electrons are tiny specks of dust buzzing around the outer parking lot of the school stadium.”",
                caption: "Leah: \"If the nucleus were a marble on the pitch, electrons are specks out in the stadium parking lot!\"",
                visual: `<div style="font-size:3.5rem; animation:drift 2s infinite alternate;">🏟️</div><div style="color:#38BDF8; font-family:'Outfit',sans-serif; font-weight:800; font-size:1rem; margin-top:8px;">99.999% Vacuum</div>`
            }},
            {{
                id: "vedic-math",
                title: "Multiply Any 2-Digit in 3 Seconds",
                category: "💡 Vedic Trick",
                grade: "Classes 6–10 · Maths",
                duration: "0:42",
                teacher: "Nikita Arvey",
                emoji: "➗",
                quote: "“Cross the diagonals, add the wings, and write the product directly from left to right!”",
                caption: "Nikita: \"21 × 32: Tens = 6, Cross = (4+3)=7, Units = 2. Total = 672 in 3 seconds flat!\"",
                visual: `<div style="font-family:'Outfit',sans-serif; font-weight:900; font-size:2.8rem; color:#FEF08A;">21 × 32</div><div style="color:#34D399; font-weight:800; font-size:1.3rem;">= 672</div>`
            }},
            {{
                id: "leaf-pigments",
                title: "Why Autumn Leaves Turn Red (Pigments)",
                category: "🌿 Nature Decoded",
                grade: "Class 7 · Biology",
                duration: "0:54",
                teacher: "Soumi Sarkar",
                emoji: "🍁",
                quote: "“The orange and red were always hiding there! Green chlorophyll was just screaming louder all summer.”",
                caption: "Soumi: \"When sunlight drops, chlorophyll breaks down and hidden carotenoid sunset colors emerge!\"",
                visual: `<div style="display:flex; gap:12px; font-size:3.5rem;"><span>🍃</span>➔<span>🍁</span></div>`
            }},
            {{
                id: "magic-e",
                title: "The Secret Power of the Bossy 'E'",
                category: "🔤 Phonics Secret",
                grade: "Classes 1–3 · Reading",
                duration: "0:38",
                teacher: "Leah Alexander",
                emoji: "🔤",
                quote: "“The silent 'E' doesn't say a sound — it commands the first vowel to say its own name!”",
                caption: "Leah: \"Add an 'E' to CAP: now 'A' says its alphabet name /AY/ -> CAPE!\"",
                visual: `<div style="font-family:'Outfit',sans-serif; font-size:2.4rem; font-weight:900; color:#FFFFFF;">CAP ➔ <span style="color:#FEF08A;">CAPE</span></div>`
            }},
            {{
                id: "pythagoras-water",
                title: "Pythagoras Theorem with Water Tanks",
                category: "📐 Visual Proof",
                grade: "Class 8 · Geometry",
                duration: "0:48",
                teacher: "Tanu Riya",
                emoji: "📐",
                quote: "“The water from both leg squares fills the hypotenuse square to the exact rim!”",
                caption: "Tanu: \"a² + b² = c² visualized with liquid pouring between rotating acrylic square containers.\"",
                visual: `<div style="font-family:'Outfit',sans-serif; font-size:2.5rem; font-weight:900; color:#38BDF8;">a² + b² = c²</div>`
            }},
            {{
                id: "refraction-light",
                title: "Why Light Bends in Glass (Refraction)",
                category: "⚡ Breakthrough",
                grade: "Class 10 · Optics",
                duration: "0:45",
                teacher: "Leah Alexander",
                emoji: "⚡",
                quote: "“Think of a shopping cart hitting sand on one wheel first — it automatically pivots!”",
                caption: "Leah: \"One side of the wavefront slows down first in dense glass, pivoting the ray.\"",
                visual: `<div style="font-size:3.8rem;">🔦 ⤹ 🪟</div>`
            }}
        ];

        // Populate Ticker (duplicate items for infinite smooth scrolling)
        const track = document.getElementById("reelsTickerTrack");
        const fullList = [...TICKER_REELS, ...TICKER_REELS];
        
        fullList.forEach((item, idx) => {{
            const card = document.createElement("div");
            card.className = "ticker-reel-card";
            card.onclick = () => openReelModal(idx % TICKER_REELS.length);
            card.innerHTML = `
                <div class="ticker-thumb-box">
                    <span>${{item.emoji}}</span>
                    <div class="ticker-play-circle">▶</div>
                    <span class="ticker-dur-pill">${{item.duration}}</span>
                </div>
                <div class="ticker-category-row">
                    <span class="ticker-cat-badge">${{item.category}}</span>
                    <span class="ticker-class-text">${{item.grade.split('·')[0].trim()}}</span>
                </div>
                <h4 class="ticker-card-title">${{item.title}}</h4>
                <div class="ticker-teacher-row">
                    <span>👩‍🏫 ${{item.teacher}}</span>
                </div>
            `;
            track.appendChild(card);
        }});

        // 4. Reel Modal Controls
        let modalPlaying = true;
        let modalProgress = 40;
        let activeReelIdx = 0;

        function openReelModal(idx) {{
            activeReelIdx = idx;
            const r = TICKER_REELS[idx];
            document.getElementById("modalReelTitle").innerText = r.title;
            document.getElementById("modalCategoryBadge").innerText = r.category;
            document.getElementById("modalQuoteBox").innerText = r.quote;
            document.getElementById("modalTeacherName").innerText = r.teacher;
            document.getElementById("modalCaption").innerText = r.caption;
            document.getElementById("modalVisualScene").innerHTML = r.visual;
            
            modalProgress = 20;
            document.getElementById("reelModal").classList.add("active");
            modalPlaying = true;
            document.getElementById("modalPlayBtn").innerText = "⏸";
        }}

        function closeReelModal() {{
            document.getElementById("reelModal").classList.remove("active");
            modalPlaying = false;
        }}

        function toggleModalPlay() {{
            modalPlaying = !modalPlaying;
            document.getElementById("modalPlayBtn").innerText = modalPlaying ? "⏸" : "▶";
        }}

        setInterval(() => {{
            if (modalPlaying && document.getElementById("reelModal").classList.contains("active")) {{
                modalProgress += 2;
                if (modalProgress > 100) modalProgress = 0;
                document.getElementById("modalProgressFill").style.width = modalProgress + "%";
                const sec = Math.floor((modalProgress / 100) * 50);
                document.getElementById("modalTimeLbl").innerText = `0:${{sec < 10 ? '0' : ''}}${{sec}} / 0:50`;
            }}
        }}, 400);

        // 5. Cinematic Sticky Storytelling Scroll Engine (Matching AI Predictor Story Stage)
        var c = "", i;
        for (i = 0; i < 8; i++) c += '<i style="--n:' + i + '"></i>';
        document.getElementById("cur").innerHTML = c;

        var st = document.getElementById("story"),
            sc = [].slice.call(document.querySelectorAll(".scene")),
            stage = document.getElementById("stage"),
            cu = document.getElementById("cur"),
            cur = -1,
            to;

        function go(i) {{
            if (i === cur) return;
            var prev = cur;
            cur = i;
            clearTimeout(to);
            
            if (i < 0) {{
                sc.forEach(function(e) {{ e.classList.remove("on", "out"); }});
                stage.classList.remove("cine");
                return;
            }}
            
            stage.classList.add("cine");
            stage.dataset.s = i;
            
            var d = 0;
            if (prev >= 0) {{
                d = 450;
                cu.classList.remove("go");
                void cu.offsetWidth;
                cu.classList.add("go");
            }}
            
            to = setTimeout(function() {{
                sc.forEach(function(e, j) {{
                    e.classList.remove("out");
                    if (j === prev) {{
                        e.classList.remove("on");
                        e.classList.add("out");
                    }} else if (j !== i) {{
                        e.classList.remove("on");
                    }}
                }});
                sc[i].classList.add("on");
                setTimeout(function() {{
                    sc.forEach(function(e) {{ e.classList.remove("out"); }});
                }}, 1500);
            }}, d);
        }}

        function upd() {{
            var r = st.getBoundingClientRect(),
                p = Math.min(.999, Math.max(0, -r.top / (r.height - innerHeight)));
            stage.style.setProperty("--p", p);
            go(r.top > innerHeight * .4 ? -1 : Math.floor(p * sc.length));
        }}

        addEventListener("scroll", upd, {{ passive: true }});
        upd();
    </script>
</body>
</html>
'''

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(html_content)

print("Updated landing.html generated successfully!")
