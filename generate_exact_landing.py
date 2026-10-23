import sys, os

# Read Leah avatar
with open("/Users/srinibashbartia/.gemini/antigravity/scratch/leah_avatar.txt", "r") as f:
    avatar_b64 = f.read().strip()

html_code = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>Guided Learning | Paathshala</title>
    <meta name="description" content="A dedicated expert teacher who meets your child exactly where they're stuck. Live 1-on-1 classes, 60-second concept reels, and personalized guidance.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --bg: #FAF7F2;
            --bg2: #F0EAE1;
            --fg: #0A1030;
            --mut: #4D5380;
            --a: #FF5A36;        /* Paathshala Coral */
            --p: #5F5AF6;        /* Paathshala Indigo */
            --n: #38BDF8;        /* Sky Blue */
            --g: #FFC83D;        /* Warm Gold */
            --ln: rgba(10, 16, 48, 0.15);
            --vg: rgba(10, 16, 48, 0.22);
            --bar: #0A1030;
            box-sizing: border-box;
            padding-top: env(safe-area-inset-top, 0px);
            padding-bottom: env(safe-area-inset-bottom, 0px);
        }}

        @media (prefers-color-scheme: dark) {{
            :root:not([data-theme="light"]) {{
                --bg: #0A1030;
                --bg2: #151D4D;
                --fg: #FAF7F2;
                --mut: #A7ADCF;
                --a: #FF5A36;
                --p: #7C78FF;
                --n: #7FD6E8;
                --g: #FFD25E;
                --ln: rgba(255, 255, 255, 0.15);
                --vg: rgba(0, 0, 0, 0.6);
                --bar: #000000;
            }}
        }}

        :root[data-theme="dark"] {{
            --bg: #0A1030;
            --bg2: #151D4D;
            --fg: #FAF7F2;
            --mut: #A7ADCF;
            --a: #FF5A36;
            --p: #7C78FF;
            --n: #7FD6E8;
            --g: #FFD25E;
            --ln: rgba(255, 255, 255, 0.15);
            --vg: rgba(0, 0, 0, 0.6);
            --bar: #000000;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }}

        html {{
            scroll-behavior: smooth;
            scroll-padding-top: env(safe-area-inset-top, 0px);
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
            font-weight: 800;
            letter-spacing: -0.035em;
            line-height: 0.98;
        }}

        a:focus-visible, button:focus-visible, summary:focus-visible {{
            outline: 3px solid var(--a);
            outline-offset: 3px;
        }}

        /* FIXED NAV */
        nav {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 50;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: calc(12px + env(safe-area-inset-top, 0px)) 5vw 12px;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            background: color-mix(in srgb, var(--bg) 85%, transparent);
            border-bottom: 1px solid var(--ln);
        }}

        .brand-wrap {{
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: var(--fg);
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            font-weight: 800;
        }}

        .brand-emblem {{
            width: 32px;
            height: 32px;
            border-radius: 8px;
            background: #FFFFFF;
            border: 1.5px solid var(--fg);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 0 var(--fg);
        }}

        .brand-emblem svg {{
            width: 22px;
            height: 22px;
        }}

        .nav-links {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}

        .nav-link {{
            color: var(--mut);
            font-weight: 700;
            text-decoration: none;
            font-size: 14px;
            transition: color 0.15s;
        }}

        .nav-link:hover {{
            color: var(--fg);
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--a);
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            padding: 13px 26px;
            border-radius: 99px;
            text-decoration: none;
            border: 2px solid var(--fg);
            box-shadow: 0 4px 0 var(--fg);
            cursor: pointer;
            font-size: 15px;
            transition: transform 0.15s, box-shadow 0.15s;
        }}

        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 0 var(--fg);
        }}

        .btn.ghost {{
            background: transparent;
            color: var(--fg);
            border: 2px solid var(--mut);
            box-shadow: none;
        }}

        .btn.ghost:hover {{
            background: var(--bg2);
            transform: translateY(-2px);
        }}

        nav .btn {{
            padding: 8px 18px;
            font-size: 13px;
            box-shadow: 0 2px 0 var(--fg);
        }}

        .hl {{
            color: var(--a);
        }}

        /* HERO SECTION */
        .hero {{
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 105px 5vw 40px;
            position: relative;
            overflow: hidden;
        }}

        .hero:before, .hero:after {{
            content: "";
            position: absolute;
            width: 48vw;
            height: 48vw;
            border-radius: 50%;
            filter: blur(90px);
            opacity: 0.25;
            animation: float 12s ease-in-out infinite alternate;
            pointer-events: none;
        }}

        .hero:before {{
            background: var(--p);
            top: -15vw;
            left: -10vw;
        }}

        .hero:after {{
            background: var(--a);
            bottom: -20vw;
            right: -10vw;
            animation-delay: -6s;
        }}

        @keyframes float {{
            to {{
                transform: translate(8vw, 6vw) scale(1.2);
            }}
        }}

        .hero-top-grid {{
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 4vw;
            align-items: center;
            position: relative;
            z-index: 1;
            margin-bottom: 36px;
        }}

        h1 {{
            font-size: clamp(44px, 7.5vw, 100px);
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
            animation-delay: calc(var(--n) * 90ms + 0.2s);
        }}

        @keyframes up {{
            to {{ transform: none; }}
        }}

        .sub {{
            margin: 20px 0 26px;
            color: var(--mut);
            font-size: clamp(16px, 1.8vw, 20px);
            max-width: 34ch;
            opacity: 0;
            animation: fade 1s 1.2s forwards;
        }}

        @keyframes fade {{
            to {{ opacity: 1; }}
        }}

        .pill {{
            display: inline-block;
            font-size: 13px;
            font-weight: 700;
            padding: 6px 14px;
            border: 1.5px solid var(--fg);
            border-radius: 99px;
            margin-bottom: 18px;
            color: var(--fg);
            background: var(--g);
            box-shadow: 0 2px 0 var(--fg);
        }}

        .hero-btn-group {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
            opacity: 0;
            animation: fade 1s 1.3s forwards;
        }}

        /* INTERACTIVE LAB */
        .lab {{
            background: var(--bg2);
            border: 2px solid var(--fg);
            border-radius: 28px;
            padding: 24px;
            text-align: center;
            box-shadow: 0 10px 0 var(--fg);
            transform: translateY(40px) scale(0.96);
            opacity: 0;
            animation: pop 1s 1s cubic-bezier(.2, .9, .2, 1) forwards;
            position: relative;
        }}

        @keyframes pop {{
            to {{ transform: none; opacity: 1; }}
        }}

        .lab p {{
            color: var(--mut);
            font-weight: 700;
            margin: 14px 0 18px;
            min-height: 2.8em;
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
        .hero-ticker-section {{
            position: relative;
            z-index: 2;
            width: 100%;
            margin-top: 10px;
            opacity: 0;
            animation: fade 1s 1.4s forwards;
        }}

        .ticker-label-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            font-size: 0.82rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--mut);
        }}

        .ticker-label-bar span {{
            display: flex;
            align-items: center;
            gap: 6px;
            color: var(--fg);
        }}

        .live-dot {{
            width: 8px;
            height: 8px;
            background: #EF4444;
            border-radius: 50%;
            display: inline-block;
            animation: blink 1.5s infinite;
        }}

        @keyframes blink {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.3; }}
        }}

        .ticker-scroll-viewport {{
            width: 100%;
            overflow: hidden;
            position: relative;
            mask-image: linear-gradient(to right, transparent, black 4%, black 96%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 4%, black 96%, transparent);
            padding: 4px 0 12px;
        }}

        .ticker-track {{
            display: flex;
            gap: 16px;
            width: max-content;
            animation: scrollTicker 30s linear infinite;
        }}

        .ticker-track:hover {{
            animation-play-state: paused;
        }}

        @keyframes scrollTicker {{
            from {{ transform: translateX(0); }}
            to {{ transform: translateX(-50%); }}
        }}

        .reel-mini-card {{
            background: var(--bg2);
            border: 2px solid var(--fg);
            border-radius: 16px;
            box-shadow: 0 4px 0 var(--fg);
            padding: 10px 14px;
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            transition: transform 0.15s, box-shadow 0.15s;
            text-decoration: none;
            color: var(--fg);
            flex-shrink: 0;
            min-width: 260px;
        }}

        .reel-mini-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 0 var(--fg);
            background: #FFFFFF;
        }}

        .reel-thumb-icon {{
            width: 44px;
            height: 44px;
            border-radius: 10px;
            background: #0A1030;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            flex-shrink: 0;
            position: relative;
        }}

        .reel-thumb-icon .dur {{
            position: absolute;
            bottom: -4px;
            right: -4px;
            font-size: 0.6rem;
            background: var(--a);
            color: #FFFFFF;
            font-weight: 800;
            padding: 1px 4px;
            border-radius: 4px;
            font-family: 'Outfit', sans-serif;
        }}

        .reel-card-info {{
            display: flex;
            flex-direction: column;
            gap: 2px;
            overflow: hidden;
        }}

        .reel-card-tag {{
            font-size: 0.7rem;
            font-weight: 800;
            color: var(--a);
            text-transform: uppercase;
        }}

        .reel-card-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.88rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            line-height: 1.2;
        }}

        .reel-card-tutor {{
            font-size: 0.72rem;
            font-weight: 600;
            color: var(--mut);
        }}

        /* =========================================================================
           STORYTELLING SECTION (THEATRICAL FULLSCREEN STICKY SCROLLER)
           ========================================================================= */
        #story {{
            height: 520vh;
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
            --sb: color-mix(in srgb, var(--p) 18%, var(--bg));
            --cc: var(--p);
        }}

        .stage[data-s="1"] {{
            --sb: color-mix(in srgb, var(--n) 22%, var(--bg));
            --cc: var(--n);
        }}

        .stage[data-s="2"] {{
            --sb: color-mix(in srgb, var(--p) 16%, var(--bg));
            --cc: var(--p);
        }}

        .stage[data-s="3"] {{
            --sb: color-mix(in srgb, var(--g) 22%, var(--bg));
            --cc: var(--g);
        }}

        .stage[data-s="4"] {{
            --sb: color-mix(in srgb, var(--a) 22%, var(--bg));
            --cc: var(--a);
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
            height: 5px;
            background: linear-gradient(90deg, var(--a), var(--p), var(--n));
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
            background: var(--cc, var(--a));
            transform: scaleY(0);
        }}

        #cur.go i {{
            animation: cur 1.1s cubic-bezier(.7, 0, .3, 1) calc(var(--n) * 60ms) both;
        }}

        @keyframes cur {{
            0%   {{ transform: scaleY(0); transform-origin: top; }}
            45%  {{ transform: scaleY(1); transform-origin: top; }}
            55%  {{ transform: scaleY(1); transform-origin: bottom; }}
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
            font-size: clamp(40px, 8vw, 118px);
        }}

        .t2 {{
            font-size: clamp(34px, 6vw, 84px);
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
            color: var(--mut);
            font-size: clamp(15px, 2vw, 20px);
            margin-top: 16px;
            max-width: 42ch;
            opacity: 0;
            transform: translateY(20px);
            transition: 0.8s 0.7s;
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
            font-size: 18vh;
            font-weight: 800;
            white-space: nowrap;
            color: transparent;
            -webkit-text-stroke: 2px var(--fg);
            animation: mq 30s linear infinite;
        }}

        .bgword div + div {{
            animation-direction: reverse;
        }}

        @keyframes mq {{
            to {{ transform: translateX(-50%); }}
        }}

        /* SCENE SVG VISUALS */
        svg.sv {{
            width: min(88vw, 460px);
            height: auto;
            max-height: 44vh;
            margin: 8px 0 22px;
            overflow: visible;
        }}

        .fl {{
            font-size: 36px;
            animation: drift 3.2s ease-in-out infinite alternate;
        }}

        @keyframes drift {{
            to {{ translate: var(--dx) var(--dy); }}
        }}

        .tile {{
            transform-box: fill-box;
            transform-origin: center;
            transform: scale(0);
            transition: transform 0.7s cubic-bezier(.3, 1.5, .4, 1) 0.6s;
        }}

        .on .tile {{
            transform: none;
        }}

        .wb text {{
            font-family: 'Outfit', sans-serif;
            font-size: 30px;
            font-weight: 800;
            opacity: 0;
            transition: opacity 0.5s;
        }}

        .on .t1 {{
            opacity: 1;
            transition-delay: 1.3s;
        }}

        .on .t2 {{
            opacity: 1;
            transition-delay: 2.3s;
        }}

        svg.tg {{
            width: min(94vw, 900px);
            overflow: visible;
            margin-top: 18px;
        }}

        .tg path {{
            fill: none;
            stroke: var(--a);
            stroke-width: 8;
            stroke-linecap: round;
            stroke-dasharray: 1;
            stroke-dashoffset: 1;
            transition: stroke-dashoffset 2.6s linear;
        }}

        .on .tg path {{
            stroke-dashoffset: 0;
        }}

        .tg circle {{
            fill: var(--g);
            transform-box: fill-box;
            transform-origin: center;
            transform: scale(0);
            transition: transform 0.6s cubic-bezier(.3, 1.8, .4, 1) calc(var(--n) * 0.85s);
        }}

        .on .tg circle {{
            transform: scale(1);
        }}

        .tg text {{
            fill: var(--fg);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 22px;
            text-anchor: middle;
            opacity: 0;
            transition: opacity 0.6s calc(var(--n) * 0.85s + 0.2s);
        }}

        .on .tg text {{
            opacity: 1;
        }}

        .tg .em {{
            font-size: 26px;
            fill: #000000;
        }}

        .cards {{
            display: flex;
            justify-content: center;
            margin: 24px 0 8px;
            perspective: 900px;
        }}

        .tc {{
            width: clamp(120px, 24vw, 200px);
            aspect-ratio: 9 / 14;
            border-radius: 20px;
            padding: 14px;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            color: #1A1200;
            text-align: left;
            margin: 0 calc(clamp(120px, 24vw, 200px) / -2.4);
            transform: translateY(60px);
            opacity: 0;
            transition: all 1s cubic-bezier(.2, .9, .2, 1);
            position: relative;
            border: 2px solid var(--fg);
            box-shadow: 0 4px 0 var(--fg);
        }}

        .on .tc {{
            opacity: 1;
            margin: 0 8px;
            transform: rotate(var(--r)) translateY(var(--y));
        }}

        .tc u {{
            text-decoration: none;
            font-size: 11px;
            font-weight: 800;
            background: #FFFFFFB0;
            border-radius: 99px;
            padding: 3px 9px;
            align-self: flex-start;
            margin-bottom: 8px;
        }}

        .tc b {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(14px, 2vw, 19px);
            line-height: 1.1;
        }}

        .tc small {{
            font-weight: 700;
            opacity: 0.75;
            margin-top: 4px;
        }}

        .tc svg {{
            position: absolute;
            top: 12px;
            left: 0;
            width: 100%;
            padding: 0 12px;
        }}

        .row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 2vw;
        }}

        .row .stat {{
            font-size: clamp(60px, 14vw, 190px);
            color: var(--a);
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
            padding: 5vh 0;
            border-block: 1px solid var(--ln);
        }}

        .marq div {{
            display: inline-block;
            font-family: 'Outfit', sans-serif;
            font-size: clamp(50px, 11vw, 150px);
            font-weight: 800;
            letter-spacing: -0.03em;
            animation: mq 22s linear infinite;
        }}

        .marq span {{
            color: transparent;
            -webkit-text-stroke: 2px var(--fg);
        }}

        .marq em {{
            color: var(--a);
            font-style: normal;
        }}

        /* FAQS */
        .faq {{
            padding: 14vh 6vw;
            max-width: 900px;
            margin: auto;
        }}

        .faq h2 {{
            font-size: clamp(38px, 6vw, 76px);
            margin-bottom: 30px;
        }}

        details {{
            border-bottom: 1px solid var(--ln);
            padding: 20px 0;
            cursor: pointer;
        }}

        summary {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(18px, 2.4vw, 26px);
            font-weight: 700;
            list-style: none;
            display: flex;
            justify-content: space-between;
        }}

        summary:after {{
            content: "+";
            color: var(--a);
            font-size: 30px;
            transition: transform 0.3s;
        }}

        details[open] summary:after {{
            transform: rotate(45deg);
        }}

        details p {{
            color: var(--mut);
            margin-top: 12px;
            line-height: 1.5;
        }}

        .rv {{
            opacity: 0;
            transform: translateY(60px) scale(0.97);
            filter: blur(8px);
            transition: all 1s cubic-bezier(.2, .9, .2, 1);
        }}

        .rv.in {{
            opacity: 1;
            transform: none;
            filter: none;
        }}

        /* CTA */
        .cta {{
            text-align: center;
            padding: 18vh 6vw;
        }}

        .cta h2 {{
            font-size: clamp(44px, 9vw, 130px);
            margin-bottom: 34px;
        }}

        .cta .btn {{
            margin: 6px;
        }}

        footer {{
            text-align: center;
            color: var(--mut);
            padding: 30px 6vw 50px;
            font-size: 13px;
        }}

        footer a {{
            color: var(--mut);
        }}

        @media (max-width: 820px) {{
            .hero-top-grid {{
                grid-template-columns: 1fr;
                padding-top: 20px;
            }}
            .on .tc:nth-child(3) {{
                display: none;
            }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            * {{
                animation-duration: 0.01s !important;
                animation-delay: 0s !important;
                transition-duration: 0.01s !important;
                transition-delay: 0s !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- SVG DEFINITIONS -->
    <svg width="0" height="0" style="position:absolute" aria-hidden="true">
        <defs>
            <g id="hd">
                <circle r="34" style="fill:#F2C6A0"/>
                <path d="M-35-4Q-30-48 0-46Q30-48 35-4Q20-26 0-24Q-20-26-35-4Z" fill="#18181B"/>
                <circle cx="-12" cy="2" r="3.5" fill="#18181B"/>
                <circle cx="12" cy="2" r="3.5" fill="#18181B"/>
            </g>
            <g id="stuS">
                <path d="M-62 110Q0 20 62 110Z" style="fill:var(--n)"/>
                <use href="#hd"/>
                <path d="M-19-9l12-3M19-9l-12-3M-10 22Q0 14 10 22" stroke="#18181B" stroke-width="3" fill="none" stroke-linecap="round"/>
            </g>
            <g id="stuH">
                <path d="M-62 110Q0 20 62 110Z" style="fill:var(--n)"/>
                <use href="#hd"/>
                <path d="M-12 14Q0 30 12 14" stroke="#18181B" stroke-width="3" fill="none" stroke-linecap="round"/>
            </g>
            <g id="tea">
                <path d="M-62 110Q0 20 62 110Z" style="fill:var(--a)"/>
                <circle r="34" style="fill:#F2C6A0"/>
                <path d="M-36 0Q-34-50 0-48Q34-50 36 0Q22-24 0-22Q-22-24-36 0Z" fill="#3A2A1A"/>
                <circle cx="-12" cy="2" r="9" fill="none" stroke="#3A2A1A" stroke-width="2.5"/>
                <circle cx="12" cy="2" r="9" fill="none" stroke="#3A2A1A" stroke-width="2.5"/>
                <path d="M-3 2h6M-12 18Q0 30 12 18" stroke="#3A2A1A" stroke-width="3" fill="none" stroke-linecap="round"/>
            </g>
        </defs>
    </svg>

    <!-- FIXED TOP NAVBAR -->
    <nav>
        <a href="https://paathshala.app/" class="brand-wrap">
            <div class="brand-emblem">
                <svg viewBox="-5.5 -2.5 45 45" fill="none">
                    <circle cx="16.827" cy="20.95" r="21.5" fill="#FFFFFF" />
                    <path d="M15.3789 1.56641C18.3485 -0.00397233 21.8239 -0.319563 25.0273 0.691406V0.692383C28.099 1.67819 30.6634 3.82668 32.1709 6.67871V6.67969C33.65 9.5688 33.9475 12.9198 33.001 16.0244L33 16.0273C32.7663 16.8763 32.3452 17.8593 31.7959 18.7578C31.2461 19.6571 30.5729 20.4651 29.8379 20.9727L29.8301 20.9785L29.8232 20.9854C29.2171 21.5856 28.6251 22.154 27.9209 22.6201L27.9131 22.626C27.417 23.0235 26.8435 23.281 26.2578 23.5615C23.8896 24.6956 21.2532 25.014 18.6572 25.3838C17.5223 25.5455 16.3713 25.7405 15.2402 25.874L15.1436 25.8857V25.9824C15.1382 26.9792 15.125 28.0164 15.1436 29.0146V29.0195C15.2326 30.5471 15.239 32.7448 14.9053 34.1934C13.8023 38.9792 8.91801 41.328 4.48145 39.2656H4.48047C3.48 38.8053 2.75252 38.2262 2.0791 37.3516L2.07324 37.3457L1.92285 37.1709C0.397689 35.3408 -0.21388 32.689 0.275391 30.3652L0.167969 30.3418L0.276367 30.3652L0.277344 30.3525C0.278271 30.3429 0.278388 30.3323 0.279297 30.3223C0.903668 26.8641 3.29994 24.1185 6.36719 22.4961C6.57023 22.3887 7.15533 22.1484 7.72852 21.9053C8.01263 21.7848 8.29222 21.6643 8.51465 21.5615C8.62571 21.5102 8.72387 21.4623 8.80176 21.4209C8.87621 21.3814 8.94258 21.3425 8.98145 21.3076L9.01953 21.2734L9.01758 21.2227C8.99171 20.3933 8.98483 19.563 8.99609 18.7334C9.00396 17.9678 8.98779 17.1376 8.97266 16.2813C8.95751 15.4242 8.94299 14.5395 8.95312 13.6621C8.97343 11.9056 9.09309 10.1855 9.5 8.77832C10.3637 5.7917 12.3812 3.2335 15.1123 1.71094L15.3789 1.56641Z" fill="#5F5AF6" stroke="black" stroke-width="0.22"/>
                    <path d="M27.142 13.0609L27.3185 13.0612C27.6183 13.0878 27.9587 13.1253 28.1817 13.3206C30.8965 15.699 31.0252 18.9068 29.2136 21.755C28.9327 22.1967 28.2947 22.2791 28.2108 22.7999C27.611 23.2069 26.9192 23.4699 26.2332 23.7481C23.4164 24.8906 20.2822 25.2101 17.2249 25.579C15.8905 25.74 14.8158 26.2706 13.4793 26.4041C11.7112 26.6422 8.30149 30.1145 6.60504 30.5874C6.60829 30.4183 6.91796 27.3761 7.84467 25.579C9.43249 22.4998 11.9016 21.1201 14.734 19.8646C15.0803 19.6812 15.3437 19.6949 15.6625 19.4302L15.5989 19.3706C15.8376 19.2941 17.1559 19.1762 17.4724 19.137C22.4276 18.5234 26.1931 17.7941 27.142 13.0609Z" fill="#E87257"/>
                </svg>
            </div>
            <span>Paathshala <span class="hl">·</span> Guided learning</span>
        </a>
        <div class="nav-links">
            <a href="#story" class="nav-link">Why Guided?</a>
            <a href="#faq" class="nav-link">FAQ</a>
            <a class="btn" href="https://paathshala.app/booking">Book free trial</a>
        </div>
    </nav>

    <!-- HERO SECTION WITH TOP GRID & HIGHLIGHT REELS TICKER -->
    <section class="hero">
        <div class="hero-top-grid">
            <div>
                <span class="pill">Live 1-on-1 classes · Classes 1 to 12</span>
                <h1 id="h1"></h1>
                <p class="sub">A dedicated expert teacher who meets your child exactly where they're stuck.</p>
                <div class="hero-btn-group">
                    <a class="btn" href="https://paathshala.app/booking">Book free trial</a>
                    <a class="btn ghost" href="#story">Explore the journey ↓</a>
                </div>
            </div>

            <!-- INTERACTIVE LAB WIDGET -->
            <div class="lab">
                <svg class="hs" id="nuc" viewBox="0 0 340 280" aria-hidden="true">
                    <rect x="20" y="248" width="300" height="8" rx="4" style="fill:var(--mut)"/>
                    <g class="a1"><use href="#stuS" x="105" y="135"/></g>
                    <g class="a2"><use href="#stuH" x="105" y="135"/></g>
                    <path d="M60 248l45-18 45 18z" fill="var(--bg)" stroke="var(--fg)" stroke-width="2"/>
                    <g class="q">
                        <circle cx="105" cy="45" r="32" style="fill:var(--bg); stroke:var(--a); stroke-width:2;"/>
                        <text x="105" y="60" text-anchor="middle" font-family="'Outfit', sans-serif" font-size="40" font-weight="800" style="fill:var(--a)">?</text>
                    </g>
                    <g class="bl">
                        <circle cx="105" cy="45" r="32" style="fill:var(--g); stroke:var(--fg); stroke-width:2;"/>
                        <text x="105" y="58" text-anchor="middle" font-size="32">💡</text>
                    </g>
                    <g class="tch">
                        <use href="#tea" x="245" y="135"/>
                        <rect x="180" y="14" width="134" height="34" rx="17" style="fill:var(--bg); stroke:var(--fg); stroke-width:1.5;"/>
                        <text x="247" y="37" text-anchor="middle" font-family="'Outfit', sans-serif" font-size="14" font-weight="800" style="fill:var(--fg)">Let's try it together!</text>
                    </g>
                </svg>
                <p id="lt">Stuck on a question, alone.</p>
                <button class="btn" id="glue" style="width:100%; justify-content:center;">Turn on the guide ✨</button>
            </div>
        </div>

        <!-- HIGHLIGHT REELS TICKER IN HERO -->
        <div class="hero-ticker-section">
            <div class="ticker-label-bar">
                <span><i class="live-dot"></i> Live Highlight Reels from 1-on-1 Sessions</span>
                <span style="font-size:0.75rem; color:var(--mut);">Tap any reel to explore ➔</span>
            </div>
            <div class="ticker-scroll-viewport">
                <div class="ticker-track">
                    <!-- REEL 1: NUCLEAR GLUE (REFERENCE REEL) -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">⚛️<span class="dur">0:50</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🎯 Aha Moment!</span>
                            <span class="reel-card-title">The 'Nuclear Glue' Inside an Atom</span>
                            <span class="reel-card-tutor">Leah Alexander · Physics</span>
                        </div>
                    </a>

                    <!-- REEL 2: EMPTY SPACE -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r2" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">🌌<span class="dur">0:58</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🎯 Mind Blown</span>
                            <span class="reel-card-title">You Are 99.999% Empty Space!</span>
                            <span class="reel-card-tutor">Leah Alexander · Chemistry</span>
                        </div>
                    </a>

                    <!-- REEL 3: VEDIC MATH -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">➗<span class="dur">0:42</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">💡 Mental Trick</span>
                            <span class="reel-card-title">Multiply Any 2-Digit in 3 Seconds</span>
                            <span class="reel-card-tutor">Nikita Arvey · Maths</span>
                        </div>
                    </a>

                    <!-- REEL 4: AUTUMN LEAVES -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">🍁<span class="dur">0:54</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🌿 Nature Decoded</span>
                            <span class="reel-card-title">Why Autumn Leaves Turn Red</span>
                            <span class="reel-card-tutor">Soumi Sarkar · Biology</span>
                        </div>
                    </a>

                    <!-- REEL 5: MAGIC E -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">🔤<span class="dur">0:38</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🔤 Phonics Secret</span>
                            <span class="reel-card-title">The Secret Magic 'E' Rule</span>
                            <span class="reel-card-tutor">Leah Alexander · Reading</span>
                        </div>
                    </a>

                    <!-- REEL 6: PYTHAGORAS -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">📐<span class="dur">0:48</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">📐 Visual Proof</span>
                            <span class="reel-card-title">Pythagoras Theorem with Water Tanks</span>
                            <span class="reel-card-tutor">Tanu Riya · Geometry</span>
                        </div>
                    </a>

                    <!-- DUPLICATE FOR INFINITE SMOOTH LOOP -->
                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">⚛️<span class="dur">0:50</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🎯 Aha Moment!</span>
                            <span class="reel-card-title">The 'Nuclear Glue' Inside an Atom</span>
                            <span class="reel-card-tutor">Leah Alexander · Physics</span>
                        </div>
                    </a>

                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r2" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">🌌<span class="dur">0:58</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🎯 Mind Blown</span>
                            <span class="reel-card-title">You Are 99.999% Empty Space!</span>
                            <span class="reel-card-tutor">Leah Alexander · Chemistry</span>
                        </div>
                    </a>

                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">➗<span class="dur">0:42</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">💡 Mental Trick</span>
                            <span class="reel-card-title">Multiply Any 2-Digit in 3 Seconds</span>
                            <span class="reel-card-tutor">Nikita Arvey · Maths</span>
                        </div>
                    </a>

                    <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" class="reel-mini-card">
                        <div class="reel-thumb-icon">🍁<span class="dur">0:54</span></div>
                        <div class="reel-card-info">
                            <span class="reel-card-tag">🌿 Nature Decoded</span>
                            <span class="reel-card-title">Why Autumn Leaves Turn Red</span>
                            <span class="reel-card-tutor">Soumi Sarkar · Biology</span>
                        </div>
                    </a>
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

            <!-- SCENE 0: LEARNING ALONE IS A MAZE -->
            <div class="scene" style="--o:50% 50%">
                <div class="bgword">
                    <div>STUCK · STUCK · STUCK · STUCK · STUCK ·</div>
                    <div>CONFUSED · ALONE · LOST IN NOTES · STUCK ·</div>
                </div>
                <svg class="sv" viewBox="0 0 400 270" aria-hidden="true">
                    <use href="#stuS" x="200" y="115" transform="translate(-40 -23) scale(1.2)"/>
                    <text class="fl" x="40" y="70" style="--dx:14px;--dy:-10px">📚</text>
                    <text class="fl" x="320" y="60" style="--dx:-12px;--dy:12px">▶️</text>
                    <text class="fl" x="30" y="210" style="--dx:10px;--dy:12px">📝</text>
                    <text class="fl" x="330" y="210" style="--dx:-14px;--dy:-8px">💻</text>
                    <text class="fl" x="130" y="30" style="--dx:6px;--dy:-14px;fill:var(--a);font-weight:800">?</text>
                    <text class="fl" x="245" y="40" style="--dx:-8px;--dy:-12px;fill:var(--a);font-weight:800">?</text>
                </svg>
                <div class="big mask">Learning alone is a <span class="hl">maze.</span></div>
                <p class="cap">Videos, notes, recorded lectures. When doubt strikes at 8 PM, a pre-recorded screen cannot see the confusion in their eyes.</p>
            </div>

            <!-- SCENE 1: THEN A GUIDE STEPS IN -->
            <div class="scene" style="--o:15% 85%">
                <div class="big t2 mask">Then a guide <span class="hl">steps in.</span></div>
                <svg class="sv" viewBox="0 0 420 275" aria-hidden="true">
                    <defs>
                        <clipPath id="c1"><rect x="20" y="14" width="180" height="136" rx="14"/></clipPath>
                        <clipPath id="c2"><rect x="220" y="14" width="180" height="136" rx="14"/></clipPath>
                    </defs>
                    <g class="tile">
                        <rect x="20" y="14" width="180" height="136" rx="14" style="fill:var(--a);opacity:0.35"/>
                        <g clip-path="url(#c1)"><use href="#tea" x="110" y="62" transform="translate(110 62) scale(.72) translate(-110 -62)"/></g>
                    </g>
                    <g class="tile">
                        <rect x="220" y="14" width="180" height="136" rx="14" style="fill:var(--p);opacity:0.35"/>
                        <g clip-path="url(#c2)"><use href="#stuH" x="310" y="62" transform="translate(310 62) scale(.72) translate(-310 -62)"/></g>
                    </g>
                    <g class="wb">
                        <rect x="20" y="164" width="380" height="100" rx="14" fill="#FFFDF6" stroke="var(--fg)" stroke-width="2"/>
                        <text class="t1" x="44" y="212" fill="var(--fg)">2x + 3 = 11</text>
                        <text class="t2" x="44" y="250" fill="var(--a)">x = 4  ✓</text>
                    </g>
                </svg>
                <p class="cap">One master teacher, one student, one shared interactive whiteboard where confusion turns to clarity.</p>
            </div>

            <!-- SCENE 2: FROM CONFUSION TO AHA IN 60 SECONDS -->
            <div class="scene" style="--o:50% 100%">
                <div class="big t2 mask">From confusion to <span class="hl">"Aha!"</span> in 60s.</div>
                <svg class="tg" viewBox="0 0 800 250" aria-hidden="true">
                    <path pathLength="1" d="M40 180C150 180 150 60 270 60S400 180 530 180 670 60 760 60"/>
                    <circle cx="40" cy="180" r="28" style="--n:0"/>
                    <circle cx="270" cy="60" r="28" style="--n:1"/>
                    <circle cx="530" cy="180" r="28" style="--n:2"/>
                    <circle cx="760" cy="60" r="28" style="--n:3"/>
                    <text class="em" x="40" y="190" style="--n:0">😕</text>
                    <text class="em" x="270" y="70" style="--n:1">💡</text>
                    <text class="em" x="530" y="190" style="--n:2">✏️</text>
                    <text class="em" x="760" y="70" style="--n:3">🏆</text>
                    <text x="40" y="236" style="--n:0">Stuck</text>
                    <text x="270" y="26" style="--n:1">Visual Analogy</text>
                    <text x="530" y="236" style="--n:2">Live Practice</text>
                    <text x="735" y="26" style="--n:3">Mastered</text>
                </svg>
                <p class="cap">
                    Our tutors don't read dry slides. They build vivid mental anchors — like neutrons acting as "nuclear glue" holding protons together.
                </p>
            </div>

            <!-- SCENE 3: NOTHING GETS LOST -->
            <div class="scene" style="--o:0% 50%">
                <div class="big t2 mask">Nothing gets <span class="hl">lost.</span></div>
                <div class="cards">
                    <div class="tc" style="--r:-7deg;--y:14px;background:var(--n)">
                        <svg viewBox="0 0 100 70">
                            <rect width="100" height="70" rx="9" fill="#1A1200"/>
                            <circle cx="50" cy="31" r="15" fill="#FFFFFF"/>
                            <path d="M45 23l14 8-14 8z" fill="#1A1200"/>
                            <rect x="10" y="57" width="80" height="5" rx="2.5" fill="#FFFFFF55"/>
                            <rect x="10" y="57" width="46" height="5" rx="2.5" fill="#FF5A36"/>
                        </svg>
                        <u>Recording</u>
                        <b>Replay the whole class</b>
                        <small>Every session saved</small>
                    </div>

                    <div class="tc" style="--r:0deg;--y:-16px;background:var(--g)">
                        <svg viewBox="0 0 100 70">
                            <rect width="100" height="70" rx="9" fill="#1A1200"/>
                            <path d="M10 48H90" stroke="#FFFFFF66" stroke-width="4" stroke-linecap="round"/>
                            <circle cx="28" cy="48" r="5" fill="#FFFFFF"/>
                            <circle cx="80" cy="48" r="5" fill="#FFFFFF"/>
                            <path d="M58 14l5 11 12 1-9 8 3 12-11-6-11 6 3-12-9-8 12-1z" fill="#FF5A36"/>
                        </svg>
                        <u>Key moments</u>
                        <b>Jump straight to the 'Aha!'</b>
                        <small>60-second reels</small>
                    </div>

                    <div class="tc" style="--r:7deg;--y:14px;background:color-mix(in srgb, var(--p) 45%, #FFFFFF)">
                        <svg viewBox="0 0 100 70">
                            <rect width="100" height="70" rx="9" fill="#1A1200"/>
                            <rect x="8" y="8" width="58" height="22" rx="9" fill="#FFFFFFCC"/>
                            <rect x="16" y="15" width="40" height="3" rx="1.5" fill="#1A1200"/>
                            <rect x="16" y="21" width="26" height="3" rx="1.5" fill="#1A1200"/>
                            <rect x="34" y="38" width="58" height="22" rx="9" fill="#FF5A36"/>
                            <rect x="42" y="45" width="40" height="3" rx="1.5" fill="#1A1200"/>
                            <rect x="42" y="51" width="22" height="3" rx="1.5" fill="#1A1200"/>
                        </svg>
                        <u>Mitra AI</u>
                        <b>Revise anytime</b>
                        <small>Personalized AI companion</small>
                    </div>
                </div>
                <a class="btn" href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank" style="margin-top:22px">
                    See Leah's 'Nuclear Glue' Reel ➔
                </a>
            </div>

            <!-- SCENE 4: 1 : 1 CLIMAX -->
            <div class="scene" style="--o:100% 0%">
                <div class="row">
                    <svg viewBox="-70 -60 140 180" aria-hidden="true"><use href="#tea"/></svg>
                    <div class="big stat mask">1 : 1</div>
                    <svg viewBox="-70 -60 140 180" aria-hidden="true"><use href="#stuH"/></svg>
                </div>
                <p class="cap" style="margin-top:0">
                    A dedicated top 1.4% educator who knows your child. Not a webinar crowd of 200 kids, not a video.
                </p>
                <a class="btn" href="https://paathshala.app/booking" style="margin-top:24px">
                    Book free trial class ➔
                </a>
            </div>

        </div>
    </section>

    <!-- MARQUEE TICKER -->
    <div class="marq">
        <div>
            <span>Stuck. </span><em>Guided. </em><span>Growing. </span><em>Confident. </em>&nbsp;&nbsp;&nbsp;&nbsp;
            <span>Stuck. </span><em>Guided. </em><span>Growing. </span><em>Confident. </em>&nbsp;&nbsp;&nbsp;&nbsp;
            <span>Stuck. </span><em>Guided. </em><span>Growing. </span><em>Confident. </em>&nbsp;&nbsp;&nbsp;&nbsp;
        </div>
    </div>

    <!-- FAQS -->
    <section class="faq" id="faq">
        <h2 class="rv">Quick answers.</h2>
        <details class="rv" open>
            <summary>What is guided learning?</summary>
            <p>Each student is paired with a dedicated expert teacher for live 1-on-1 classes, backed by recordings, key moment reels, and an AI tutor for 24/7 revision.</p>
        </details>
        <details class="rv">
            <summary>Who is it for?</summary>
            <p>Students in classes 1 to 12 across India, with curriculum tailored to CBSE, ICSE, Cambridge, and State boards.</p>
        </details>
        <details class="rv">
            <summary>How do we start?</summary>
            <p>Book a free 30-minute trial class and meet your dedicated teacher on a shared interactive whiteboard.</p>
        </details>
    </section>

    <!-- CTA -->
    <section class="cta">
        <h2 class="rv">Give them a <span class="hl">guide.</span></h2>
        <a class="btn rv" href="https://paathshala.app/booking">Book free trial class</a>
        <a class="btn ghost rv" href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1">Explore highlight reels</a>
    </section>

    <!-- FOOTER -->
    <footer>
        © 2026 Safwhigre Technologies OPC Private Limited · <a href="https://paathshala.app/">paathshala.app</a> · +91 80105 71912
    </footer>

    <!-- INTERACTION & STICKY SCROLL SCRIPT -->
    <script>
        // 1. Kinetic H1 Text Animation
        document.getElementById("h1").innerHTML = "Don't get stuck. Get guided.".split(" ").map(function(w, i) {{
            return '<span class="w"><i style="--n:' + i + '" class="' + (i > 2 ? 'hl' : '') + '">' + w + '</i></span> ';
        }}).join("");

        // 2. Interactive Guide Lab Toggle
        var nuc = document.getElementById("nuc"),
            gb = document.getElementById("glue"),
            lt = document.getElementById("lt");

        gb.onclick = function() {{
            var g = nuc.classList.toggle("glued");
            gb.textContent = g ? "Turn off the guide ✕" : "Turn on the guide ✨";
            lt.textContent = g ? "With a personal guide beside them, it clicks." : "Stuck on a question, alone.";
        }};

        // 3. Create Curtain Slashes
        var c = "", i;
        for (i = 0; i < 8; i++) c += '<i style="--n:' + i + '"></i>';
        document.getElementById("cur").innerHTML = c;

        // 4. Sticky Story Scroll Engine
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

        // 5. Intersection Observer for Scroll Reveal
        var io = new IntersectionObserver(function(es) {{
            es.forEach(function(e) {{
                if (e.isIntersecting) e.target.classList.add("in");
            }});
        }}, {{ threshold: 0.2 }});
        document.querySelectorAll(".rv").forEach(function(e) {{ io.observe(e); }});
    </script>
</body>
</html>
'''

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(html_code)

print("Exact landing page generated successfully!")
