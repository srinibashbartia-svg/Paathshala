import os
import shutil

scratch_dir = "/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning"
brain_dir = "/Users/srinibashbartia/.gemini/antigravity/brain/280bacfb-a77d-43c5-8fd5-6bc903a3d7fe"

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala · Guided Learning After Class</title>
    
    <!-- Paathshala Typography: Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

    <style>
        :root {
            /* Paathshala Brand Colors */
            --paathshala-violet: #5458F7;
            --paathshala-violet-dark: #3730A3;
            --paathshala-violet-deep: #2A2C85;
            --paathshala-orange: #FF5A36;
            --paathshala-orange-hover: #E04320;
            --paathshala-yellow: #FFD24A;
            --paathshala-mint: #86EFAC;
            --paathshala-mint-dark: #15803D;
            --ink: #0F172A;
            --ink-secondary: #334155;
            --white: #FFFFFF;
            --glow-cyan: #38BDF8;
            --glow-cyan-light: #BAE6FD;
            --border-card: rgba(255, 255, 255, 0.45);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
        }

        body {
            font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
            background-color: var(--paathshala-violet);
            color: var(--white);
            min-height: 100vh;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            padding: 20px;
        }

        /* -------------------------------------------------------------
           CONTAINER (SQUARE BANNER / HIGH-IMPACT HERO)
           ------------------------------------------------------------- */
        .banner-container {
            width: 100%;
            max-width: 780px;
            background-color: var(--paathshala-violet);
            border-radius: 36px;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.35);
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow: hidden;
            padding: 40px 24px 36px;
            border: 3px solid rgba(255, 255, 255, 0.2);
        }

        /* -------------------------------------------------------------
           BACKGROUND 3D RIBBONS & LIGHTING EFFECTS
           ------------------------------------------------------------- */
        .bg-curves-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }

        .bg-wave-ribbon {
            position: absolute;
            border-radius: 9999px;
            filter: blur(2px);
            opacity: 0.85;
        }

        .ribbon-1 {
            width: 700px;
            height: 350px;
            border: 32px solid rgba(255, 255, 255, 0.12);
            top: 280px;
            left: -180px;
            transform: rotate(-18deg) skewX(-10deg);
        }

        .ribbon-2 {
            width: 650px;
            height: 380px;
            border: 26px solid rgba(255, 255, 255, 0.08);
            top: 420px;
            right: -200px;
            transform: rotate(24deg);
        }

        .bg-radial-highlight {
            position: absolute;
            top: 120px;
            left: 50%;
            transform: translateX(-50%);
            width: 580px;
            height: 580px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.18) 0%, rgba(84, 88, 247, 0) 70%);
            pointer-events: none;
            z-index: 1;
        }

        /* -------------------------------------------------------------
           HEADER SECTION (MATCHING REFERENCE EXACT HIERARCHY)
           ------------------------------------------------------------- */
        .header-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            z-index: 10;
            position: relative;
            max-width: 620px;
            margin-bottom: 20px;
        }

        .brand-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
            text-decoration: none;
        }

        .brand-icon-box {
            width: 32px;
            height: 32px;
            background-color: var(--white);
            border-radius: 9px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--paathshala-violet);
            font-size: 1.15rem;
            font-weight: 900;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        .brand-name {
            font-size: 1.35rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: var(--white);
        }

        .tag-pill {
            display: inline-flex;
            align-items: center;
            padding: 5px 16px;
            border-radius: 9999px;
            border: 1.5px solid rgba(255, 255, 255, 0.6);
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(8px);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            color: var(--white);
            margin-bottom: 12px;
        }

        .main-headline {
            font-size: clamp(2.2rem, 4.2vw, 3.1rem);
            font-weight: 900;
            letter-spacing: -0.035em;
            line-height: 1.1;
            color: var(--white);
            margin-bottom: 10px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
        }

        .headline-sub {
            color: var(--paathshala-yellow);
        }

        .sub-description {
            font-size: clamp(0.95rem, 1.6vw, 1.1rem);
            font-weight: 500;
            line-height: 1.45;
            color: rgba(255, 255, 255, 0.9);
            max-width: 520px;
        }

        /* -------------------------------------------------------------
           STAGE WRAPPER (PHONE + HAND + 3D FLOATING CARDS)
           ------------------------------------------------------------- */
        .stage-container {
            position: relative;
            width: 100%;
            height: 540px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }

        /* -------------------------------------------------------------
           3D PERSPECTIVE FLOATING CARDS (5 CARDS REPRODUCING REFERENCE)
           ------------------------------------------------------------- */
        .floating-cards-layer {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 5;
        }

        .perspective-card {
            position: absolute;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(12px);
            border: 1.5px solid var(--border-card);
            border-radius: 18px;
            padding: 10px 14px;
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.22);
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--ink);
            transition: transform 0.3s ease;
            pointer-events: auto;
        }

        .perspective-card:hover {
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.3);
        }

        /* Card 1: Top-Left */
        .card-pos-1 {
            top: 30px;
            left: 20px;
            width: 195px;
            transform: rotate(-7deg) scale(0.92);
        }

        /* Card 2: Middle-Left */
        .card-pos-2 {
            top: 180px;
            left: 5px;
            width: 205px;
            transform: rotate(-10deg);
        }

        /* Card 3: Bottom-Left */
        .card-pos-3 {
            bottom: 60px;
            left: 25px;
            width: 195px;
            transform: rotate(-6deg) scale(0.95);
        }

        /* Card 4: Middle-Right */
        .card-pos-4 {
            top: 200px;
            right: 15px;
            width: 215px;
            transform: rotate(8deg);
        }

        /* Card 5: Bottom-Right */
        .card-pos-5 {
            bottom: 60px;
            right: 10px;
            width: 220px;
            transform: rotate(6deg) scale(0.96);
        }

        .card-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background-color: var(--paathshala-violet-dark);
            color: var(--white);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9rem;
            font-weight: 800;
            flex-shrink: 0;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        .avatar-orange {
            background-color: var(--paathshala-orange);
        }

        .avatar-mint {
            background-color: var(--paathshala-mint-dark);
        }

        .card-content-col {
            display: flex;
            flex-direction: column;
            gap: 3px;
            overflow: hidden;
        }

        .card-title-text {
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--ink);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .card-skeleton-bar {
            height: 5px;
            border-radius: 9999px;
            background: #CBD5E1;
            width: 80px;
        }

        .card-skeleton-bar.short {
            width: 50px;
        }

        /* -------------------------------------------------------------
           SMARTPHONE FRAME WITH HAND HOLDING IT
           ------------------------------------------------------------- */
        .phone-hand-rig {
            position: relative;
            width: 300px;
            height: 530px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 12;
            transform: rotate(3deg);
        }

        /* SMARTPHONE DEVICE */
        .phone-mockup-frame {
            position: relative;
            width: 260px;
            height: 510px;
            background-color: #0B0E14;
            border-radius: 44px;
            border: 4px solid #2B3342;
            box-shadow: 
                0 0 0 2px #1E293B,
                0 25px 60px rgba(0, 0, 0, 0.45),
                0 10px 25px rgba(0, 0, 0, 0.35);
            overflow: hidden;
            z-index: 10;
        }

        /* Dynamic Island */
        .phone-dynamic-island {
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 82px;
            height: 20px;
            background-color: #000000;
            border-radius: 14px;
            z-index: 25;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 10px;
        }

        .island-dot {
            width: 7px;
            height: 7px;
            background-color: #111827;
            border-radius: 50%;
        }

        .island-lens {
            width: 8px;
            height: 8px;
            background: radial-gradient(circle at 35% 35%, #1E3A8A, #020617);
            border-radius: 50%;
        }

        /* Video Inside Phone */
        .phone-screen {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 40px;
            overflow: hidden;
            background-color: #000;
        }

        .phone-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* Phone Screen Overlays */
        .screen-top-bar {
            position: absolute;
            top: 34px;
            left: 0;
            width: 100%;
            padding: 0 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 20;
        }

        .mentor-live-badge {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(10px);
            padding: 3px 9px;
            border-radius: 9999px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: var(--white);
            font-size: 0.65rem;
            font-weight: 700;
        }

        .dot-live-pulse {
            width: 6px;
            height: 6px;
            background-color: #EF4444;
            border-radius: 50%;
            animation: pulse-live 1.6s infinite;
        }

        @keyframes pulse-live {
            0% { transform: scale(0.9); opacity: 0.8; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.8; }
        }

        .screen-bottom-bar {
            position: absolute;
            bottom: 20px;
            left: 0;
            width: 100%;
            padding: 0 12px;
            z-index: 20;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .lesson-info-box {
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(10px);
            padding: 7px 10px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .lesson-step-badge {
            font-size: 0.58rem;
            font-weight: 800;
            color: var(--paathshala-orange);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .lesson-title-txt {
            font-size: 0.68rem;
            font-weight: 700;
            color: var(--white);
            line-height: 1.25;
            margin-top: 2px;
        }

        .controls-row {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 6px;
        }

        .btn-ctrl {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.4);
            color: var(--white);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.75rem;
            transition: background 0.2s;
        }

        .btn-ctrl:hover {
            background: rgba(255, 255, 255, 0.45);
        }

        /* -------------------------------------------------------------
           REALISTIC HAND GRAPHIC HOLDING THE PHONE
           ------------------------------------------------------------- */
        .hand-cutout-svg {
            position: absolute;
            bottom: -60px;
            left: -80px;
            width: 360px;
            height: 450px;
            pointer-events: none;
            z-index: 15;
            filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.35));
        }

        /* -------------------------------------------------------------
           THE SIGNATURE GLOWING 3D CALLOUT CARD (POPPING FORWARD)
           ------------------------------------------------------------- */
        .glowing-callout-wrapper {
            position: absolute;
            top: 130px;
            right: -55px;
            z-index: 30;
            transform: rotate(3deg);
            pointer-events: auto;
        }

        .hand-drawn-arrow {
            position: absolute;
            top: -50px;
            left: 20px;
            width: 70px;
            height: 50px;
            pointer-events: none;
        }

        .glow-card-bubble {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(240, 249, 255, 0.92));
            backdrop-filter: blur(14px);
            border: 2.5px solid var(--glow-cyan-light);
            border-radius: 20px;
            padding: 12px 18px;
            width: 240px;
            box-shadow: 
                0 0 35px rgba(56, 189, 248, 0.7),
                0 0 15px rgba(255, 255, 255, 0.8),
                0 18px 40px rgba(15, 23, 42, 0.3);
            display: flex;
            flex-direction: column;
            gap: 8px;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            cursor: pointer;
        }

        .glow-card-bubble:hover {
            transform: translateY(-4px) scale(1.03);
            box-shadow: 
                0 0 45px rgba(56, 189, 248, 0.85),
                0 0 20px rgba(255, 255, 255, 0.9),
                0 22px 50px rgba(15, 23, 42, 0.35);
        }

        .glow-header-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .glow-title-box {
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--ink);
            font-size: 0.9rem;
            font-weight: 800;
        }

        .sparkle-icon {
            color: var(--paathshala-violet);
            font-size: 1.1rem;
            animation: pulse-sparkle 2s infinite ease-in-out;
        }

        @keyframes pulse-sparkle {
            0%, 100% { transform: scale(1) rotate(0deg); }
            50% { transform: scale(1.2) rotate(15deg); }
        }

        .chevron-right {
            font-size: 1.05rem;
            font-weight: 900;
            color: var(--ink-secondary);
        }

        .glow-lines-col {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        .glow-line-bar {
            height: 6px;
            background: #BAE6FD;
            border-radius: 9999px;
            width: 100%;
        }

        .glow-line-bar.short {
            width: 65%;
            background: #E0F2FE;
        }

        .glow-sub-text {
            font-size: 0.68rem;
            font-weight: 700;
            color: #0284C7;
            margin-top: -2px;
        }

        /* -------------------------------------------------------------
           BOTTOM CTA & SYLLABUS SECTION
           ------------------------------------------------------------- */
        .bottom-action-bar {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 14px;
            z-index: 10;
            margin-top: 10px;
        }

        .btn-bottom-pill {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background-color: var(--white);
            color: var(--paathshala-violet-dark);
            padding: 13px 30px;
            border-radius: 9999px;
            font-size: 0.95rem;
            font-weight: 800;
            text-decoration: none;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
            border: 2px solid rgba(255, 255, 255, 0.8);
        }

        .btn-bottom-pill:hover {
            transform: translateY(-2px);
            background-color: var(--paathshala-yellow);
            color: var(--ink);
            box-shadow: 0 14px 30px rgba(0, 0, 0, 0.25);
        }

        .syllabus-pills-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            flex-wrap: wrap;
            opacity: 0.9;
        }

        .syllabus-chip {
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 0.05em;
            color: rgba(255, 255, 255, 0.85);
            text-transform: uppercase;
            padding: 3px 8px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* -------------------------------------------------------------
           RESPONSIVE ADJUSTMENTS
           ------------------------------------------------------------- */
        @media (max-width: 768px) {
            .perspective-card {
                display: none;
            }
            .glowing-callout-wrapper {
                right: -20px;
                top: 110px;
            }
            .stage-container {
                height: 480px;
            }
            .phone-mockup-frame {
                width: 240px;
                height: 470px;
            }
        }
    </style>
</head>
<body>

    <div class="banner-container">

        <!-- 3D BACKGROUND RIBBONS -->
        <div class="bg-curves-container">
            <div class="bg-radial-highlight"></div>
            <div class="bg-wave-ribbon ribbon-1"></div>
            <div class="bg-wave-ribbon ribbon-2"></div>
        </div>

        <!-- ================= TOP HEADER (MATCHING REFERENCE EXACT HIERARCHY) ================= -->
        <header class="header-section">
            <a href="https://paathshala.app" class="brand-badge">
                <div class="brand-icon-box">P</div>
                <div class="brand-name">Paathshala</div>
            </a>

            <div class="tag-pill">
                Skip the hesitation
            </div>

            <h1 class="main-headline">
                Start With Context.<br>
                <span class="headline-sub">We Clear Every Doubt After.</span>
            </h1>

            <p class="sub-description">
                From hesitant silence to complete concept clarity — your dedicated 1-on-1 mentor re-explains every single lesson from scratch until it clicks. 100% judgment-free.
            </p>
        </header>

        <!-- ================= CENTERPIECE STAGE ================= -->
        <div class="stage-container">

            <!-- 5 FLOATING 3D PERSPECTIVE CARDS IN BACKGROUND -->
            <div class="floating-cards-layer">
                <!-- Card 1: Top-Left -->
                <div class="perspective-card card-pos-1">
                    <div class="card-avatar">👧🏽</div>
                    <div class="card-content-col">
                        <span class="card-title-text">Class 10 CBSE Math</span>
                        <div class="card-skeleton-bar"></div>
                        <div class="card-skeleton-bar short"></div>
                    </div>
                </div>

                <!-- Card 2: Middle-Left -->
                <div class="perspective-card card-pos-2">
                    <div class="card-avatar avatar-orange">S</div>
                    <div class="card-content-col">
                        <span class="card-title-text">Hesitated to ask teacher</span>
                        <div class="card-skeleton-bar"></div>
                        <div class="card-skeleton-bar short"></div>
                    </div>
                </div>

                <!-- Card 3: Bottom-Left -->
                <div class="perspective-card card-pos-3">
                    <div class="card-avatar avatar-mint">★</div>
                    <div class="card-content-col">
                        <span class="card-title-text">0% Shyness · 1-on-1 Replay</span>
                        <div class="card-skeleton-bar"></div>
                    </div>
                </div>

                <!-- Card 4: Middle-Right -->
                <div class="perspective-card card-pos-4">
                    <div class="card-avatar avatar-orange">M</div>
                    <div class="card-content-col">
                        <span class="card-title-text">Dedicated 1-on-1 Mentor</span>
                        <div class="card-skeleton-bar"></div>
                        <div class="card-skeleton-bar short"></div>
                    </div>
                </div>

                <!-- Card 5: Bottom-Right -->
                <div class="perspective-card card-pos-5">
                    <div class="card-avatar">👦🏻</div>
                    <div class="card-content-col">
                        <span class="card-title-text">1.5k Doubts Solved Today</span>
                        <div class="card-skeleton-bar"></div>
                        <div class="card-skeleton-bar short"></div>
                    </div>
                </div>
            </div>

            <!-- SMARTPHONE DEVICE & HAND RIG -->
            <div class="phone-hand-rig">

                <!-- SMARTPHONE DEVICE MOCKUP -->
                <div class="phone-mockup-frame">
                    <!-- Dynamic Island Notch -->
                    <div class="phone-dynamic-island">
                        <div class="island-dot"></div>
                        <div class="island-lens"></div>
                    </div>

                    <!-- Video Container Inside Phone -->
                    <div class="phone-screen">
                        <video id="classReelVideo" class="phone-video" playsinline autoplay muted loop poster="reel-poster.jpg">
                            <source src="reel.mp4" type="video/mp4">
                            Your browser does not support HTML5 video.
                        </video>

                        <!-- Video Top Overlay -->
                        <div class="screen-top-bar">
                            <div class="mentor-live-badge">
                                <span>Aditi Mentor</span>
                            </div>
                            <div class="mentor-live-badge">
                                <div class="dot-live-pulse"></div>
                                <span>Live</span>
                            </div>
                        </div>

                        <!-- Video Bottom Overlay -->
                        <div class="screen-bottom-bar">
                            <div class="lesson-info-box">
                                <div class="lesson-step-badge">Step 2 of 4 · Step-by-Step</div>
                                <div class="lesson-title-txt">Quadratic Equations Made Simple</div>
                            </div>
                            <div class="controls-row">
                                <button class="btn-ctrl" id="btnPlayPause" onclick="togglePlayVideo()" title="Play/Pause">❚❚</button>
                                <button class="btn-ctrl" id="btnMuteToggle" onclick="toggleMuteVideo()" title="Mute/Unmute">🔇</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- REALISTIC HAND GRAPHIC HOLDING THE PHONE (SVG CUTOUT) -->
                <svg class="hand-cutout-svg" viewBox="0 0 380 480" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <radialGradient id="skinGrad" cx="40%" cy="50%" r="60%">
                            <stop offset="0%" stop-color="#E8B490"/>
                            <stop offset="65%" stop-color="#CE9570"/>
                            <stop offset="100%" stop-color="#B27854"/>
                        </radialGradient>
                        <linearGradient id="thumbGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#F2C2A0"/>
                            <stop offset="70%" stop-color="#D89D78"/>
                            <stop offset="100%" stop-color="#BA7E58"/>
                        </linearGradient>
                    </defs>

                    <!-- Wrist & Lower Palm -->
                    <path d="M 0 480 L 110 320 C 120 305 135 295 155 295 L 205 305 C 225 315 240 335 245 365 L 265 480 Z" fill="url(#skinGrad)" />

                    <!-- Thumb Wrapping Around Left Edge of Phone -->
                    <path d="M 125 310 C 120 280 125 240 140 215 C 148 200 162 195 174 205 C 185 215 188 235 185 260 C 182 285 175 320 165 340 Z" fill="url(#thumbGrad)" />
                    <!-- Thumb nail -->
                    <path d="M 152 208 C 158 204 166 206 170 212 C 173 218 171 226 165 230 C 159 232 153 226 150 218 Z" fill="#FDE2D2" opacity="0.85" />
                    <path d="M 153 210 C 157 207 163 208 166 213" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>

                    <!-- Dark Sleeve / Cuff at Bottom Left -->
                    <path d="M -20 480 L 80 390 L 125 435 L 50 480 Z" fill="#1E293B"/>
                    <path d="M 75 390 L 85 398 L 45 480 L 35 480 Z" fill="#0F172A"/>

                    <!-- Fingertips Peeking on the Right Side of Phone -->
                    <!-- Index finger tip -->
                    <path d="M 330 220 C 342 222 352 232 350 245 C 348 255 338 262 326 260 Z" fill="url(#skinGrad)"/>
                    <!-- Middle finger tip -->
                    <path d="M 332 270 C 345 272 355 282 352 296 C 350 306 340 312 328 310 Z" fill="url(#skinGrad)"/>
                    <!-- Ring finger tip -->
                    <path d="M 330 322 C 342 324 350 334 348 346 C 346 356 336 362 325 360 Z" fill="url(#skinGrad)"/>
                    <!-- Pinky finger tip -->
                    <path d="M 326 372 C 336 374 344 382 342 392 C 340 400 332 405 322 403 Z" fill="url(#skinGrad)"/>
                </svg>

                <!-- ================= THE GLOWING 3D CALLOUT CARD WITH ARROW ================= -->
                <div class="glowing-callout-wrapper">
                    <!-- Hand-Drawn White Arrow Pointing Down -->
                    <svg class="hand-drawn-arrow" viewBox="0 0 75 55" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M 15 8 C 35 2 55 12 52 35" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>
                        <path d="M 44 26 L 52 36 L 60 27" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>

                    <!-- The Glowing Frosted Pill Card -->
                    <div class="glow-card-bubble" onclick="togglePlayVideo()">
                        <div class="glow-header-row">
                            <div class="glow-title-box">
                                <span class="sparkle-icon">✦</span>
                                <span>Concept Clarity Summary</span>
                            </div>
                            <span class="chevron-right">›</span>
                        </div>
                        <div class="glow-lines-col">
                            <div class="glow-line-bar"></div>
                            <div class="glow-line-bar short"></div>
                        </div>
                        <div class="glow-sub-text">
                            ● 1-on-1 Mentor · 0% Hesitation
                        </div>
                    </div>
                </div>

            </div>

        </div>

        <!-- ================= BOTTOM ACTION BAR ================= -->
        <footer class="bottom-action-bar">
            <a href="https://paathshala.app" class="btn-bottom-pill">
                <span>Book Free 1-on-1 Class</span>
                <span style="font-size: 1.1rem;">➔</span>
            </a>

            <div class="syllabus-pills-row">
                <span class="syllabus-chip">CBSE</span>
                <span class="syllabus-chip">ICSE</span>
                <span class="syllabus-chip">STATE BOARDS</span>
                <span class="syllabus-chip">NCERT</span>
                <span class="syllabus-chip">IGCSE</span>
                <span class="syllabus-chip">IB FOUNDATION</span>
            </div>
        </footer>

    </div>

    <!-- SCRIPT FOR VIDEO CONTROLS -->
    <script>
        const video = document.getElementById('classReelVideo');
        const btnPlay = document.getElementById('btnPlayPause');
        const btnMute = document.getElementById('btnMuteToggle');

        function togglePlayVideo() {
            if (video.paused) {
                video.play();
                btnPlay.innerText = '❚❚';
            } else {
                video.pause();
                btnPlay.innerText = '▶';
            }
        }

        function toggleMuteVideo() {
            video.muted = !video.muted;
            btnMute.innerText = video.muted ? '🔇' : '🔊';
        }

        document.addEventListener('DOMContentLoaded', () => {
            video.play().catch(e => console.log('Autoplay muted triggered'));
        });
    </script>
</body>
</html>
'''

# Write to scratch
banner_path = os.path.join(scratch_dir, "banner.html")
homepage_path = os.path.join(scratch_dir, "homepage-section.html")

with open(banner_path, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(homepage_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Copy to brain artifacts
shutil.copyfile(banner_path, os.path.join(brain_dir, "banner.html"))
shutil.copyfile(homepage_path, os.path.join(brain_dir, "homepage-section.html"))

print("Successfully written banner and homepage files")
