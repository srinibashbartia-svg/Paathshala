#!/usr/bin/env python3
"""
generate_packaging_banner.py
Redesigns the Paathshala Guided Learning Hero Banner with:
1. Exact Worm Mascot anatomy matching media_1792552882621_ebe33cd4.png:
   - Mathematically smooth tubular bodies with uniform thickness and perfect rounded caps
   - Curved cylindrical segment stripes cleanly masked within the body contours
   - Expressive round cartoon eyes with specular highlight reflections
   - Signature floating golden star (★)
   - Paathshala Violet (#5458F7), Paathshala Orange (#FF5A36), Paathshala Yellow (#FFD24A)
2. Three distinct high-fidelity Worm Action Poses with an instant interactive switcher:
   - Pose 1: Rocket Surfer / Co-Pilot (Leaning forward, holding star-wand, fluttering headband ribbons & cape)
   - Pose 2: Looping Corkscrew (Directly recreating the top-left loop from the reference image around the rocket)
   - Pose 3: Super-Mentor Glider (Streamlined horizontal flight pose with goggles)
3. Full environment:
   - Supersonic Pencil Rocket with stabilizer fins, exhaust cloud puffs, and comic speed lines
   - Student Worm on mountain peak in Paathshala Orange with "Aha!" star
   - Cozy Sleeping Worm coiled in flat spiral on cloud with closed eyes and 'z Z Z'
   - Mountain peaks with snow caps and pine trees
   - Floating doubt drone / satellite beaming solved formula
   - Packaging header with Paathshala stripes ribbon
   - Left visual specification sheet with micro-comparison cards and authentic barcode
   - Cloud title container with problem & solution headlines
"""

import os
import shutil

BANNER_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala · Guided Learning After Class</title>
    
    <!-- Paathshala Typography: Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&display=swap" rel="stylesheet">

    <style>
        :root {
            /* Paathshala Brand Palette (Strictly No Gradients) */
            --paathshala-violet: #5458F7;
            --paathshala-violet-dark: #3730A3;
            --paathshala-orange: #FF5A36;
            --paathshala-orange-dark: #D94420;
            --paathshala-yellow: #FFD24A;
            --paathshala-mint: #86EFAC;
            --ink: #0F172A;
            --white: #FFFFFF;
            --cream: #FFFDF0;
            --bg-canvas: #090D16;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
        }

        body {
            font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
            background-color: var(--bg-canvas);
            color: var(--ink);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 32px 16px 80px;
            gap: 36px;
        }

        .banner-wrapper {
            width: 100%;
            max-width: 1260px;
            margin: 0 auto;
        }

        /* -------------------------------------------------------------
           INTERACTIVE WORM POSE CONTROLS BAR (AT TOP)
           ------------------------------------------------------------- */
        .character-pose-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #1E293B;
            border: 3px solid var(--ink);
            border-radius: 20px;
            padding: 10px 18px;
            margin-bottom: 16px;
            box-shadow: 4px 4px 0px var(--ink);
            flex-wrap: wrap;
            gap: 12px;
        }

        .pose-bar-label {
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--white);
            font-size: 0.85rem;
            font-weight: 900;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .pose-bar-tag {
            background-color: var(--paathshala-orange);
            color: var(--white);
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 0.68rem;
            border: 1.5px solid var(--ink);
        }

        .pose-buttons-row {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .btn-pose-toggle {
            background-color: #334155;
            color: var(--white);
            border: 2px solid var(--ink);
            border-radius: 9999px;
            padding: 7px 16px;
            font-family: inherit;
            font-size: 0.78rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.15s ease;
            box-shadow: 2px 2px 0px var(--ink);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn-pose-toggle:hover {
            background-color: #475569;
            transform: translateY(-1px);
        }

        .btn-pose-toggle.active {
            background-color: var(--paathshala-yellow);
            color: var(--ink);
            box-shadow: 3px 3px 0px var(--ink);
            transform: translateY(-1px);
        }

        /* -------------------------------------------------------------
           MAIN BANNER CONTAINER: SOLID VIOLET & SOLID ACCENTS
           ------------------------------------------------------------- */
        .paathshala-banner {
            position: relative;
            width: 100%;
            background-color: var(--paathshala-violet);
            border: 4px solid var(--ink);
            border-radius: 28px;
            box-shadow: 8px 8px 0px var(--ink);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* -------------------------------------------------------------
           TOP PACKAGING HEADER (BRAND + STRIPES RIBBON)
           ------------------------------------------------------------- */
        .banner-top-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 30px;
            border-bottom: 3.5px solid var(--ink);
            background-color: var(--cream);
            position: relative;
            z-index: 10;
        }

        .brand-logo-area {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--ink);
        }

        .brand-logo-mark {
            width: 34px;
            height: 34px;
            background-color: var(--paathshala-orange);
            border: 2.5px solid var(--ink);
            border-radius: 10px;
            box-shadow: 2.5px 2.5px 0px var(--ink);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
            color: var(--white);
            font-weight: 900;
        }

        .brand-logo-text {
            font-size: 1.35rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            text-transform: uppercase;
        }

        .brand-subline {
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            color: var(--paathshala-violet);
            padding: 5px 14px;
            background-color: #EEF2FF;
            border: 2px solid var(--ink);
            border-radius: 9999px;
            box-shadow: 2px 2px 0px var(--ink);
        }

        /* PAATHSHALA SIGNATURE STRIPES ELEMENT */
        .stripes-badge-top {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 6px 14px;
            border-radius: 9999px;
            border: 2.5px solid var(--ink);
            background: repeating-linear-gradient(
                -45deg,
                var(--paathshala-orange),
                var(--paathshala-orange) 8px,
                var(--paathshala-yellow) 8px,
                var(--paathshala-yellow) 16px
            );
            box-shadow: 2.5px 2.5px 0px var(--ink);
        }

        .stripes-label {
            font-size: 0.72rem;
            font-weight: 900;
            letter-spacing: 0.04em;
            color: var(--ink);
            background-color: var(--white);
            padding: 3px 10px;
            border-radius: 9999px;
            border: 1.5px solid var(--ink);
            white-space: nowrap;
        }

        /* -------------------------------------------------------------
           MAIN BANNER GRID: LEFT VISUAL SPEC SHEET + RIGHT ILLUSTRATION
           ------------------------------------------------------------- */
        .banner-body {
            display: grid;
            grid-template-columns: 320px 1fr;
            min-height: 610px;
            position: relative;
        }

        /* -------------------------------------------------------------
           LEFT COLUMN: REDUCED WORDING + VISUAL STORYTELLING
           ------------------------------------------------------------- */
        .spec-sidebar {
            background-color: var(--cream);
            border-right: 3.5px solid var(--ink);
            padding: 22px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 16px;
            position: relative;
            z-index: 5;
        }

        .spec-header-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .spec-badge {
            font-size: 0.68rem;
            font-weight: 900;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: var(--white);
            background-color: var(--ink);
            padding: 4px 10px;
            border-radius: 6px;
        }

        .spec-ver {
            font-size: 0.68rem;
            font-weight: 800;
            color: #64748B;
        }

        /* VISUAL COMPARISON CARDS: BEFORE VS AFTER */
        .visual-comparison-box {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        /* CARD 1: IN CLASS (PROBLEM) */
        .visual-card-problem {
            background-color: #FEE2E2;
            border: 2.5px solid var(--ink);
            border-radius: 14px;
            padding: 10px 12px;
            box-shadow: 3px 3px 0px var(--ink);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .visual-thumb {
            width: 58px;
            height: 58px;
            flex-shrink: 0;
            background-color: var(--white);
            border: 2px solid var(--ink);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .visual-info {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .visual-label-red {
            font-size: 0.64rem;
            font-weight: 900;
            color: #DC2626;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .visual-title {
            font-size: 0.85rem;
            font-weight: 900;
            color: var(--ink);
            line-height: 1.15;
        }

        .visual-desc {
            font-size: 0.68rem;
            font-weight: 700;
            color: #64748B;
            line-height: 1.25;
        }

        /* CARD 2: AFTER CLASS WITH MENTOR (SOLUTION) */
        .visual-card-solution {
            background-color: #EEF2FF;
            border: 2.5px solid var(--ink);
            border-radius: 14px;
            padding: 10px 12px;
            box-shadow: 3px 3px 0px var(--ink);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .visual-thumb-violet {
            width: 58px;
            height: 58px;
            flex-shrink: 0;
            background-color: #E0E7FF;
            border: 2px solid var(--ink);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .visual-label-violet {
            font-size: 0.64rem;
            font-weight: 900;
            color: var(--paathshala-violet);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* VISUAL KEY METRICS */
        .visual-pills-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }

        .metric-pill {
            background-color: var(--white);
            border: 2px solid var(--ink);
            border-radius: 10px;
            padding: 8px 10px;
            box-shadow: 2px 2px 0px var(--ink);
            display: flex;
            flex-direction: column;
            gap: 1px;
        }

        .metric-pill-head {
            font-size: 0.62rem;
            font-weight: 800;
            text-transform: uppercase;
            color: #64748B;
            letter-spacing: 0.04em;
        }

        .metric-pill-body {
            font-size: 0.78rem;
            font-weight: 900;
            color: var(--ink);
        }

        /* BIG STAT CALLOUT */
        .spec-big-callout {
            background-color: var(--paathshala-orange);
            border: 2.5px solid var(--ink);
            border-radius: 14px;
            padding: 10px 14px;
            box-shadow: 3px 3px 0px var(--ink);
            color: var(--white);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .spec-big-num {
            font-size: 1.25rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            line-height: 1.1;
        }

        .spec-big-desc {
            font-size: 0.68rem;
            font-weight: 800;
            letter-spacing: 0.04em;
            opacity: 0.95;
            text-transform: uppercase;
        }

        .spec-badge-free {
            background-color: var(--paathshala-yellow);
            color: var(--ink);
            font-size: 0.75rem;
            font-weight: 900;
            padding: 4px 10px;
            border-radius: 8px;
            border: 2px solid var(--ink);
            box-shadow: 2px 2px 0px var(--ink);
        }

        /* AUTHENTIC BARCODE */
        .spec-barcode-box {
            background-color: var(--white);
            border: 2.5px solid var(--ink);
            border-radius: 10px;
            padding: 6px 8px;
            box-shadow: 3px 3px 0px var(--ink);
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .barcode-bars {
            width: 100%;
            height: 38px;
            display: block;
        }

        .barcode-digits {
            font-family: monospace;
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 3px;
            color: var(--ink);
            margin-top: 2px;
        }

        /* -------------------------------------------------------------
           RIGHT COLUMN: MAIN COMIC ILLUSTRATION WORLD
           ------------------------------------------------------------- */
        .illustration-stage {
            position: relative;
            background-color: var(--paathshala-violet);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 24px 28px 24px;
        }

        .scene-svg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none;
        }

        /* STICKER ROW AT TOP RIGHT */
        .stage-stickers-layer {
            position: relative;
            z-index: 4;
            display: flex;
            justify-content: flex-end;
            gap: 12px;
            align-items: flex-start;
        }

        .sticker-badge {
            background-color: var(--white);
            border: 2.5px solid var(--ink);
            border-radius: 9999px;
            padding: 7px 16px;
            font-size: 0.78rem;
            font-weight: 900;
            letter-spacing: 0.02em;
            color: var(--ink);
            box-shadow: 3.5px 3.5px 0px var(--ink);
            display: flex;
            align-items: center;
            gap: 6px;
            transform: rotate(-2deg);
            white-space: nowrap;
        }

        .sticker-badge.orange {
            background-color: var(--paathshala-orange);
            color: var(--white);
            transform: rotate(2deg);
        }

        .sticker-badge.yellow {
            background-color: var(--paathshala-yellow);
            color: var(--ink);
            transform: rotate(-1.5deg);
        }

        .sticker-badge.mint {
            background-color: var(--paathshala-mint);
            color: var(--ink);
            transform: rotate(3deg);
        }

        /* -------------------------------------------------------------
           BOTTOM TITLE CLOUD (PROBLEM & SOLUTION HEADLINE)
           ------------------------------------------------------------- */
        .stage-bottom-deck {
            position: relative;
            z-index: 4;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: auto;
        }

        .cloud-title-container {
            position: relative;
            background-color: var(--white);
            border: 4px solid var(--ink);
            border-radius: 36px;
            padding: 20px 36px 16px;
            box-shadow: 6px 6px 0px var(--ink);
            text-align: center;
            max-width: 760px;
            width: 100%;
        }

        /* COMIC CLOUD BUBBLE EARS */
        .cloud-title-container::before {
            content: '';
            position: absolute;
            top: -24px;
            left: 50px;
            width: 58px;
            height: 58px;
            background-color: var(--white);
            border: 4px solid var(--ink);
            border-radius: 50%;
            border-bottom-color: var(--white);
            z-index: 2;
        }

        .cloud-title-container::after {
            content: '';
            position: absolute;
            top: -30px;
            right: 75px;
            width: 70px;
            height: 70px;
            background-color: var(--white);
            border: 4px solid var(--ink);
            border-radius: 50%;
            border-bottom-color: var(--white);
            z-index: 2;
        }

        .cloud-inner-fix {
            position: relative;
            z-index: 3;
        }

        .problem-line {
            display: block;
            font-size: clamp(1.15rem, 2vw, 1.75rem);
            font-weight: 900;
            color: var(--paathshala-orange);
            letter-spacing: -0.03em;
            line-height: 1.1;
            margin-bottom: 2px;
            text-transform: uppercase;
        }

        .solution-line {
            display: block;
            font-size: clamp(1.8rem, 3.8vw, 3.2rem);
            font-weight: 900;
            color: var(--ink);
            letter-spacing: -0.05em;
            line-height: 1.05;
            text-transform: uppercase;
        }

        .subtitle-pill-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
            flex-wrap: wrap;
        }

        .cloud-subtitle-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.82rem;
            font-weight: 800;
            color: var(--paathshala-violet);
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }

        .dot-divider {
            color: #CBD5E1;
            font-weight: 900;
        }

        /* HIGH-CONVERTING CTA BUTTON */
        .cta-bottom-bar {
            margin-top: 14px;
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .btn-cta-packaging {
            background-color: var(--paathshala-orange);
            color: var(--white);
            font-size: 1.05rem;
            font-weight: 900;
            letter-spacing: -0.01em;
            padding: 13px 34px;
            border-radius: 9999px;
            border: 3.5px solid var(--ink);
            box-shadow: 4px 4px 0px var(--ink);
            text-decoration: none;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-cta-packaging:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px var(--ink);
            background-color: #E04B28;
        }

        .cta-trust-note {
            font-size: 0.8rem;
            font-weight: 800;
            color: var(--white);
            letter-spacing: 0.02em;
            background-color: rgba(15, 23, 42, 0.45);
            padding: 6px 14px;
            border-radius: 9999px;
            border: 1.5px solid rgba(255, 255, 255, 0.3);
        }

        /* WORM VARIATION DISPLAY LOGIC */
        .worm-variation {
            display: none;
        }
        .worm-variation.active {
            display: inline;
        }

        /* -------------------------------------------------------------
           LOWER SECTION: WORM CHARACTER DESIGN SHEET & POSES
           ------------------------------------------------------------- */
        .character-sheet-card {
            background-color: var(--cream);
            border: 4px solid var(--ink);
            border-radius: 24px;
            padding: 28px 32px;
            box-shadow: 8px 8px 0px var(--ink);
            width: 100%;
            max-width: 1260px;
        }

        .sheet-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 3px solid var(--ink);
            padding-bottom: 16px;
            margin-bottom: 24px;
            flex-wrap: wrap;
            gap: 12px;
        }

        .sheet-title {
            font-size: 1.4rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            text-transform: uppercase;
        }

        .sheet-desc {
            font-size: 0.85rem;
            font-weight: 700;
            color: #64748B;
        }

        .variations-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }

        .variation-card {
            background-color: var(--white);
            border: 3px solid var(--ink);
            border-radius: 18px;
            padding: 18px;
            box-shadow: 4px 4px 0px var(--ink);
            display: flex;
            flex-direction: column;
            gap: 12px;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .variation-card:hover {
            transform: translateY(-2px);
            box-shadow: 6px 6px 0px var(--ink);
        }

        .variation-card.current-active {
            border-color: var(--paathshala-orange);
            background-color: #FFF8F6;
            outline: 3px solid var(--paathshala-orange);
        }

        .variation-preview-box {
            width: 100%;
            height: 180px;
            background-color: var(--paathshala-violet);
            border: 2px solid var(--ink);
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }

        .variation-info-box {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .variation-pill-badge {
            align-self: flex-start;
            font-size: 0.65rem;
            font-weight: 900;
            padding: 3px 8px;
            border-radius: 6px;
            border: 1.5px solid var(--ink);
            text-transform: uppercase;
        }

        .variation-pill-badge.orange {
            background-color: var(--paathshala-orange);
            color: var(--white);
        }

        .variation-pill-badge.yellow {
            background-color: var(--paathshala-yellow);
            color: var(--ink);
        }

        .variation-name {
            font-size: 1.05rem;
            font-weight: 900;
            color: var(--ink);
        }

        .variation-details {
            font-size: 0.76rem;
            font-weight: 700;
            color: #64748B;
            line-height: 1.35;
        }

        @media (max-width: 960px) {
            .banner-body {
                grid-template-columns: 1fr;
            }
            .spec-sidebar {
                border-right: none;
                border-bottom: 3.5px solid var(--ink);
            }
            .cloud-title-container::before,
            .cloud-title-container::after {
                display: none;
            }
        }
    </style>
</head>
<body>

<div class="banner-wrapper">

    <!-- ================= INTERACTIVE WORM POSE SWITCHER ================= -->
    <div class="character-pose-bar">
        <div class="pose-bar-label">
            <span>🐛 WORM MASCOT ACTION POSE:</span>
            <span class="pose-bar-tag">CLICK TO TEST POSE</span>
        </div>
        <div class="pose-buttons-row">
            <button class="btn-pose-toggle active" onclick="switchWormPose('v1', this)">
                <span>★</span> Pose 1: Rocket Surfer
            </button>
            <button class="btn-pose-toggle" onclick="switchWormPose('v2', this)">
                <span>⚡</span> Pose 2: Looping Corkscrew
            </button>
            <button class="btn-pose-toggle" onclick="switchWormPose('v3', this)">
                <span>🚀</span> Pose 3: Super-Mentor Glider
            </button>
        </div>
    </div>

    <!-- ================= MAIN PACKAGING BANNER ================= -->
    <div class="paathshala-banner">

        <!-- TOP PACKAGING HEADER -->
        <header class="banner-top-header">
            <a href="https://paathshala.app" class="brand-logo-area">
                <div class="brand-logo-mark">P</div>
                <div class="brand-logo-text">PAATHSHALA</div>
            </a>
            
            <div class="brand-subline">— AFTER-CLASS GUIDED LEARNING —</div>

            <div class="stripes-badge-top">
                <span class="stripes-label">/// 100% PRIVATE /// ZERO HESITATION ///</span>
            </div>
        </header>

        <!-- MAIN BANNER GRID -->
        <div class="banner-body">

            <!-- LEFT COLUMN: VISUAL STORYTELLING (REDUCED WORDING) -->
            <aside class="spec-sidebar">
                <div class="spec-header-row">
                    <span class="spec-badge">HOW IT WORKS</span>
                    <span class="spec-ver">STEP-BY-STEP</span>
                </div>

                <!-- VISUAL 1: THE IN-CLASS PROBLEM -->
                <div class="visual-comparison-box">
                    <div class="visual-card-problem">
                        <div class="visual-thumb">
                            <!-- SVG: Confused striped worm in class with '?' -->
                            <svg width="46" height="46" viewBox="0 0 50 50" fill="none">
                                <rect x="4" y="38" width="42" height="4" rx="1.5" fill="#CBD5E1" stroke="#0F172A" stroke-width="2"/>
                                <!-- Exact worm capsule body -->
                                <path d="M16 38 C16 26 22 18 30 18 C36 18 38 24 36 30 C34 35 30 38 22 38" 
                                      stroke="#5458F7" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
                                <circle cx="20" cy="27" r="2.2" fill="#3730A3"/>
                                <circle cx="28" cy="20" r="2.2" fill="#3730A3"/>
                                <circle cx="35" cy="28" r="2.2" fill="#3730A3"/>
                                <!-- Worm Head & Eyes -->
                                <circle cx="16" cy="20" r="5.5" fill="#5458F7" stroke="#0F172A" stroke-width="1.8"/>
                                <circle cx="14" cy="19" r="2" fill="#FFFFFF"/>
                                <circle cx="14" cy="19" r="1" fill="#0F172A"/>
                                <circle cx="18" cy="19" r="2" fill="#FFFFFF"/>
                                <circle cx="18" cy="19" r="1" fill="#0F172A"/>
                                <text x="32" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="13" fill="#DC2626">?</text>
                            </svg>
                        </div>
                        <div class="visual-info">
                            <span class="visual-label-red">1. In Class</span>
                            <div class="visual-title">Too Shy to Ask</div>
                            <div class="visual-desc">Awkward in front of 40 kids. Doubts pile up.</div>
                        </div>
                    </div>

                    <!-- VISUAL 2: THE AFTER-CLASS SOLUTION -->
                    <div class="visual-card-solution">
                        <div class="visual-thumb-violet">
                            <!-- SVG: 1-on-1 Mentor Worm guiding student with star -->
                            <svg width="46" height="46" viewBox="0 0 50 50" fill="none">
                                <rect x="4" y="38" width="42" height="4" rx="1.5" fill="#86EFAC" stroke="#0F172A" stroke-width="2"/>
                                <!-- Mentor Worm (Violet) -->
                                <path d="M12 38 C12 24 16 16 22 16" stroke="#5458F7" stroke-width="6" stroke-linecap="round"/>
                                <circle cx="15" cy="26" r="2" fill="#3730A3"/>
                                <!-- Student Worm (Orange) -->
                                <path d="M38 38 C38 26 34 22 28 22" stroke="#FF5A36" stroke-width="6" stroke-linecap="round"/>
                                <circle cx="35" cy="29" r="2" fill="#D94420"/>
                                <!-- Mentor Eyes -->
                                <circle cx="21" cy="15" r="4" fill="#5458F7" stroke="#0F172A" stroke-width="1.5"/>
                                <circle cx="20" cy="15" r="1.5" fill="#FFFFFF"/>
                                <circle cx="20" cy="15" r="0.8" fill="#0F172A"/>
                                <!-- Student Eyes looking up happily -->
                                <circle cx="29" cy="21" r="4" fill="#FF5A36" stroke="#0F172A" stroke-width="1.5"/>
                                <circle cx="28" cy="20" r="1.5" fill="#FFFFFF"/>
                                <circle cx="28" cy="20" r="0.8" fill="#0F172A"/>
                                <!-- Floating Star (Aha!) -->
                                <polygon points="25,5 26.5,8.5 30,9 27.5,11.5 28,15 25,13 22,15 22.5,11.5 20,9 23.5,8.5" fill="#FFD24A" stroke="#0F172A" stroke-width="1.2"/>
                            </svg>
                        </div>
                        <div class="visual-info">
                            <span class="visual-label-violet">2. After Class</span>
                            <div class="visual-title">1-on-1 Mentor</div>
                            <div class="visual-desc">Explains patient step-by-step until it clicks.</div>
                        </div>
                    </div>
                </div>

                <!-- QUICK VISUAL SPEC CHIPS -->
                <div class="visual-pills-grid">
                    <div class="metric-pill">
                        <span class="metric-pill-head">Syllabus</span>
                        <span class="metric-pill-body">CBSE · ICSE (1-12)</span>
                    </div>
                    <div class="metric-pill">
                        <span class="metric-pill-head">Pace</span>
                        <span class="metric-pill-body">100% Child's Speed</span>
                    </div>
                    <div class="metric-pill">
                        <span class="metric-pill-head">Hesitation</span>
                        <span class="metric-pill-body">0% Awkwardness</span>
                    </div>
                    <div class="metric-pill">
                        <span class="metric-pill-head">Clarity</span>
                        <span class="metric-pill-body">Instant "Aha!"</span>
                    </div>
                </div>

                <!-- BIG CALLOUT STAT -->
                <div class="spec-big-callout">
                    <div>
                        <div class="spec-big-num">1-ON-1 TRIAL</div>
                        <div class="spec-big-desc">Zero credit card needed</div>
                    </div>
                    <span class="spec-badge-free">100% FREE</span>
                </div>

                <!-- AUTHENTIC BARCODE -->
                <div class="spec-barcode-box">
                    <svg class="barcode-bars" viewBox="0 0 200 36" preserveAspectRatio="none">
                        <rect x="0" y="0" width="3" height="36" fill="#0F172A"/>
                        <rect x="5" y="0" width="2" height="36" fill="#0F172A"/>
                        <rect x="10" y="0" width="5" height="36" fill="#0F172A"/>
                        <rect x="18" y="0" width="2" height="36" fill="#0F172A"/>
                        <rect x="23" y="0" width="4" height="36" fill="#0F172A"/>
                        <rect x="30" y="0" width="6" height="36" fill="#0F172A"/>
                        <rect x="39" y="0" width="2" height="36" fill="#0F172A"/>
                        <rect x="44" y="0" width="4" height="36" fill="#0F172A"/>
                        <rect x="51" y="0" width="7" height="36" fill="#0F172A"/>
                        <rect x="61" y="0" width="3" height="36" fill="#0F172A"/>
                        <rect x="67" y="0" width="2" height="36" fill="#0F172A"/>
                        <rect x="72" y="0" width="5" height="36" fill="#0F172A"/>
                        <rect x="80" y="0" width="3" height="36" fill="#0F172A"/>
                        <rect x="86" y="0" width="6" height="36" fill="#0F172A"/>
                        <rect x="95" y="0" width="2" height="36" fill="#0F172A"/>
                        <rect x="100" y="0" width="4" height="36" fill="#0F172A"/>
                        <rect x="107" y="0" width="7" height="36" fill="#0F172A"/>
                        <rect x="117" y="0" width="2" height="36" fill="#0F172A"/>
                        <rect x="122" y="0" width="5" height="36" fill="#0F172A"/>
                        <rect x="130" y="0" width="3" height="36" fill="#0F172A"/>
                        <rect x="136" y="0" width="6" height="36" fill="#0F172A"/>
                        <rect x="145" y="0" width="3" height="36" fill="#0F172A"/>
                        <rect x="151" y="0" width="4" height="36" fill="#0F172A"/>
                        <rect x="158" y="0" width="7" height="36" fill="#0F172A"/>
                        <rect x="168" y="0" width="2" height="36" fill="#0F172A"/>
                        <rect x="173" y="0" width="5" height="36" fill="#0F172A"/>
                        <rect x="181" y="0" width="3" height="36" fill="#0F172A"/>
                        <rect x="187" y="0" width="6" height="36" fill="#0F172A"/>
                        <rect x="196" y="0" width="4" height="36" fill="#0F172A"/>
                    </svg>
                    <span class="barcode-digits">8 901234 567890</span>
                </div>
            </aside>

            <!-- RIGHT COLUMN: COMIC ILLUSTRATION WORLD -->
            <main class="illustration-stage">

                <!-- TOP STICKER ROW -->
                <div class="stage-stickers-layer">
                    <div class="sticker-badge yellow">
                        <span>★</span> ZERO SHYNESS
                    </div>
                    <div class="sticker-badge orange">
                        NO AWKWARD QUESTIONS
                    </div>
                    <div class="sticker-badge mint">
                        <span>💡</span> INSTANT "AHA!"
                    </div>
                </div>

                <!-- FULLSTAGE SVG: MOUNTAINS, WORM MASCOTS, ROCKET PENCIL, DOODLES -->
                <svg class="scene-svg" viewBox="0 0 920 610" fill="none" xmlns="http://www.w3.org/2000/svg">
                    
                    <!-- ================= RETRO COMIC STARS & CRESCENT MOON ================= -->
                    <!-- Crescent Moon -->
                    <path d="M840 50 C820 50 805 65 805 85 C805 105 820 120 840 120 C830 110 825 95 825 85 C825 75 830 60 840 50 Z" 
                          fill="#FFD24A" stroke="#0F172A" stroke-width="3"/>
                    
                    <!-- 4-point Sparkle Stars (Yellow & White) -->
                    <g transform="translate(710, 70)">
                        <path d="M0 -14 C1 -4 4 -1 14 0 C4 1 1 4 0 14 C-1 4 -4 1 -14 0 C-4 -1 -1 -4 0 -14 Z" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>
                    </g>
                    <g transform="translate(770, 150)">
                        <path d="M0 -10 C1 -3 3 -1 10 0 C3 1 1 3 0 10 C-1 3 -3 1 -10 0 C-3 -1 -1 -3 0 -10 Z" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                    </g>
                    <g transform="translate(190, 45)">
                        <path d="M0 -11 C1 -3 3 -1 11 0 C3 1 1 3 0 11 C-1 3 -3 1 -11 0 C-3 -1 -1 -3 0 -11 Z" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>
                    </g>
                    <g transform="translate(90, 100)">
                        <path d="M0 -8 C1 -2 2 -1 8 0 C2 1 1 2 0 8 C-1 2 -2 1 -8 0 C-2 -1 -1 -2 0 -8 Z" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                    </g>

                    <!-- Geometric Floating Doodles -->
                    <polygon points="120,60 135,52 145,65 130,73" fill="#86EFAC" stroke="#0F172A" stroke-width="2.5"/>
                    <line x1="120" y1="60" x2="130" y2="73" stroke="#0F172A" stroke-width="2"/>
                    <line x1="135" y1="52" x2="145" y2="75" stroke="#0F172A" stroke-width="2"/>

                    <polygon points="780,105 795,97 805,110 790,118" fill="#FF5A36" stroke="#0F172A" stroke-width="2.5"/>

                    <!-- Friendly Paathshala Doubt Drone / Satellite Beaming Solved Formula -->
                    <g transform="translate(670, 105)">
                        <polygon points="-15,18 15,18 45,95 -45,95" fill="#FFD24A" opacity="0.4" stroke="#0F172A" stroke-width="2" stroke-dasharray="4 3"/>
                        <rect x="-44" y="65" width="88" height="22" rx="6" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <text x="0" y="80" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="10.5" fill="#0F172A" text-anchor="middle">2x+3=11 ➔ x=4 ✓</text>
                        <!-- UFO Dome -->
                        <ellipse cx="0" cy="8" rx="14" ry="12" fill="#86EFAC" stroke="#0F172A" stroke-width="2.5"/>
                        <circle cx="0" cy="6" r="3.5" fill="#0F172A"/>
                        <circle cx="-1" cy="5" r="1" fill="#FFFFFF"/>
                        <!-- Disc Saucer in Paathshala Orange -->
                        <ellipse cx="0" cy="18" rx="28" ry="8" fill="#FF5A36" stroke="#0F172A" stroke-width="3"/>
                        <circle cx="-16" cy="18" r="2" fill="#FFFFFF"/>
                        <circle cx="-8" cy="19" r="2" fill="#FFFFFF"/>
                        <circle cx="0" cy="20" r="2" fill="#FFFFFF"/>
                        <circle cx="8" cy="19" r="2" fill="#FFFFFF"/>
                        <circle cx="16" cy="18" r="2" fill="#FFFFFF"/>
                    </g>

                    <!-- ================= MOUNTAIN PEAKS AT BOTTOM ================= -->
                    <!-- Left Mountain (Mint Green with snow cap) -->
                    <polygon points="10,610 180,290 340,610" fill="#86EFAC" stroke="#0F172A" stroke-width="3.5"/>
                    <polygon points="180,290 145,355 160,365 175,350 190,368 205,355 215,362" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>

                    <!-- Right Mountain 1 (Paathshala Orange with snow cap & flag) -->
                    <polygon points="560,610 730,260 900,610" fill="#FF5A36" stroke="#0F172A" stroke-width="3.5"/>
                    <polygon points="730,260 695,325 710,335 730,320 745,338 760,325 770,332" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>
                    <line x1="730" y1="260" x2="730" y2="215" stroke="#0F172A" stroke-width="3"/>
                    <polygon points="730,215 762,228 730,242" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>

                    <!-- Far Right Mountain 2 (Warm Coral) -->
                    <polygon points="730,610 840,320 940,610" fill="#E04B28" stroke="#0F172A" stroke-width="3.5"/>
                    <polygon points="840,320 815,365 830,372 845,360 860,375 870,368" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>

                    <!-- Shrub / Pine trees on slope -->
                    <circle cx="650" cy="400" r="14" fill="#2F8F5B" stroke="#0F172A" stroke-width="2.5"/>
                    <circle cx="666" cy="395" r="16" fill="#2F8F5B" stroke="#0F172A" stroke-width="2.5"/>
                    <circle cx="682" cy="402" r="12" fill="#2F8F5B" stroke="#0F172A" stroke-width="2.5"/>

                    <!-- ================= THE STUDENT WORM (ON THE MOUNTAIN SUMMIT) ================= -->
                    <!-- Exact anatomy from reference: curved capsule body with alternating stripes, round cartoon eyes -->
                    <g transform="translate(180, 260)">
                        <!-- Floating Golden Star above head -->
                        <g transform="translate(0, -68)">
                            <polygon points="0,-12 3.5,-3.5 12,0 3.5,3.5 0,12 -3.5,3.5 -12,0 -3.5,-3.5" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>
                        </g>

                        <!-- "Aha!" Speech Pill -->
                        <g transform="translate(26, -56)">
                            <rect x="0" y="0" width="54" height="22" rx="7" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2" filter="drop-shadow(2px 2px 0px #0F172A)"/>
                            <text x="27" y="15" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="12" fill="#FF5A36" text-anchor="middle">Aha! ★</text>
                        </g>

                        <!-- Student Worm Mask (Smooth wavy S-tube in Paathshala Orange with Coral Stripes) -->
                        <defs>
                            <mask id="student-worm-mask">
                                <path d="M 0 32 C -8 18, 10 4, 2 -12 C -4 -24, 6 -34, 4 -46" 
                                      fill="none" stroke="#FFFFFF" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
                            </mask>
                        </defs>

                        <!-- Outer Ink Outline of Student Worm -->
                        <path d="M 0 32 C -8 18, 10 4, 2 -12 C -4 -24, 6 -34, 4 -46" 
                              fill="none" stroke="#0F172A" stroke-width="41" stroke-linecap="round" stroke-linejoin="round"/>

                        <!-- Masked Student Body -->
                        <g mask="url(#student-worm-mask)">
                            <rect x="-40" y="-80" width="80" height="130" fill="#FF5A36"/>
                            <!-- Transverse Dark Coral Stripes -->
                            <path d="M -22 22 Q 0 26 22 22" stroke="#D94420" stroke-width="12" stroke-linecap="round"/>
                            <path d="M -20 6 Q 0 10 20 6" stroke="#D94420" stroke-width="12" stroke-linecap="round"/>
                            <path d="M -18 -10 Q 0 -6 18 -10" stroke="#D94420" stroke-width="12" stroke-linecap="round"/>
                            <path d="M -16 -26 Q 0 -22 16 -26" stroke="#D94420" stroke-width="12" stroke-linecap="round"/>
                        </g>

                        <!-- Student Eyes looking happily up at flying Mentor -->
                        <circle cx="-1" cy="-48" r="6" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="0.5" cy="-49" r="3" fill="#0F172A"/>
                        <circle cx="-0.5" cy="-50.5" r="1.2" fill="#FFFFFF"/>

                        <circle cx="10" cy="-47" r="5.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="11.5" cy="-48" r="2.8" fill="#0F172A"/>
                        <circle cx="10.5" cy="-49.5" r="1.1" fill="#FFFFFF"/>

                        <!-- Happy open mouth -->
                        <path d="M 2 -38 Q 6 -32 10 -38 Z" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>

                        <!-- Cheering Waving Hands -->
                        <path d="M -12 -12 Q -26 -24 -20 -36" stroke="#0F172A" stroke-width="3" stroke-linecap="round" fill="none"/>
                        <path d="M 14 -12 Q 28 -24 22 -36" stroke="#0F172A" stroke-width="3" stroke-linecap="round" fill="none"/>
                    </g>

                    <!-- ================= THE SUPERSONIC ROCKET PENCIL & HERO MENTOR WORM ================= -->
                    <g transform="translate(400, 175) rotate(-9)">

                        <!-- 1. Puffy white exhaust clouds trailing behind rocket -->
                        <g transform="translate(-175, 42)">
                            <circle cx="0" cy="0" r="25" fill="#FFFFFF" stroke="#0F172A" stroke-width="3.5"/>
                            <circle cx="-22" cy="-12" r="17" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>
                            <circle cx="-36" cy="6" r="15" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>
                            <circle cx="-16" cy="20" r="19" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>
                            <circle cx="16" cy="-14" r="16" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>
                            <circle cx="-58" cy="-8" r="8" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="-72" cy="8" r="5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                            <!-- Retro Comic Speed Lines -->
                            <line x1="-85" y1="2" x2="-125" y2="2" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round"/>
                            <line x1="-80" y1="-14" x2="-110" y2="-14" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
                            <line x1="-76" y1="18" x2="-112" y2="18" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
                        </g>

                        <!-- 2. The Supersonic Pencil Rocket Vehicle -->
                        <!-- Red Rubber Eraser at back -->
                        <rect x="-150" y="24" width="26" height="36" rx="4" fill="#FF5A36" stroke="#0F172A" stroke-width="3.5"/>
                        <!-- Ferrule Metal Band -->
                        <rect x="-124" y="22" width="16" height="40" rx="2" fill="#E2E8F0" stroke="#0F172A" stroke-width="3.5"/>
                        <line x1="-116" y1="23" x2="-116" y2="61" stroke="#0F172A" stroke-width="2"/>
                        <!-- Hexagonal Pencil Body in Paathshala Yellow -->
                        <rect x="-108" y="21" width="220" height="42" rx="3" fill="#FFD24A" stroke="#0F172A" stroke-width="3.5"/>
                        <line x1="-108" y1="35" x2="112" y2="35" stroke="#0F172A" stroke-width="2"/>
                        <line x1="-108" y1="49" x2="112" y2="49" stroke="#0F172A" stroke-width="2"/>
                        <!-- Text on pencil -->
                        <text x="0" y="46" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="12" fill="#0F172A" letter-spacing="3" text-anchor="middle">PAATHSHALA · GUIDED JET</text>
                        <!-- Wood Cone -->
                        <polygon points="112,21 172,42 112,63" fill="#FDE68A" stroke="#0F172A" stroke-width="3.5"/>
                        <!-- Graphite Tip -->
                        <polygon points="152,35 172,42 152,49" fill="#0F172A" stroke="#0F172A" stroke-width="1"/>
                        <!-- Stabilizer Fins in Paathshala Orange -->
                        <polygon points="-90,21 -60,-4 -25,21" fill="#FF5A36" stroke="#0F172A" stroke-width="3.5"/>
                        <polygon points="-90,63 -60,88 -25,63" fill="#FF5A36" stroke="#0F172A" stroke-width="3.5"/>

                        <!-- 3. DYNAMIC HERO WORM MASCOT: TOGGLABLE VARIATIONS -->
                        
                        <!-- VARIATION 1: ROCKET SURFER (ACTIVE BY DEFAULT) -->
                        <g class="worm-variation active" id="worm-v1">
                            <defs>
                                <mask id="v1-worm-body-mask">
                                    <path d="M -60 20 C -45 8, -35 -14, -14 -16 C 6 -18, 22 -14, 32 -38" 
                                          fill="none" stroke="#FFFFFF" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>
                                </mask>
                            </defs>
                            <!-- Cape in Paathshala Orange -->
                            <path d="M -8 -16 C -50 -32 -85 -18 -115 8 C -90 2 -65 -12 -28 -6 Z" 
                                  fill="#FF5A36" stroke="#0F172A" stroke-width="3.5" stroke-linejoin="round"/>
                            <path d="M -22 -10 C -60 -18 -85 -6 -100 6" stroke="#0F172A" stroke-width="2" fill="none"/>
                            <!-- Black Outer Ink Border -->
                            <path d="M -60 20 C -45 8, -35 -14, -14 -16 C 6 -18, 22 -14, 32 -38" 
                                  fill="none" stroke="#0F172A" stroke-width="47" stroke-linecap="round" stroke-linejoin="round"/>
                            <!-- Masked Body: Violet + Indigo Stripes -->
                            <g mask="url(#v1-worm-body-mask)">
                                <rect x="-140" y="-120" width="240" height="200" fill="#5458F7"/>
                                <path d="M -72 6 Q -60 18 -48 30" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
                                <path d="M -48 -6 Q -36 8 -24 22" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
                                <path d="M -24 -26 Q -14 -12 -4 2" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
                                <path d="M 2 -32 Q 12 -18 22 -4" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
                                <path d="M 16 -48 Q 28 -34 38 -20" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
                            </g>
                            <!-- Golden Star above head -->
                            <g transform="translate(32, -72)">
                                <polygon points="0,-13 4,-4 13,0 4,4 0,13 -4,4 -13,0 -4,-4" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>
                            </g>
                            <!-- Headband with streaming ribbons -->
                            <path d="M 16 -40 C -2 -48 -18 -38 -32 -50 C -22 -40 -10 -42 12 -34" 
                                  fill="#FF5A36" stroke="#0F172A" stroke-width="2.5" stroke-linejoin="round"/>
                            <path d="M 18 -36 C 4 -40 -6 -28 -18 -34 C -8 -28 2 -32 16 -30" 
                                  fill="#FF5A36" stroke="#0F172A" stroke-width="2" stroke-linejoin="round"/>
                            <path d="M 14 -44 C 22 -36 34 -34 46 -42" stroke="#FF5A36" stroke-width="8" stroke-linecap="round"/>
                            <path d="M 14 -44 C 22 -36 34 -34 46 -42" stroke="#0F172A" stroke-width="2" fill="none"/>
                            <!-- Round Cartoon Eyes -->
                            <circle cx="28" cy="-44" r="8" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="30" cy="-44" r="4.5" fill="#0F172A"/>
                            <circle cx="28.5" cy="-46.5" r="1.6" fill="#FFFFFF"/>
                            <circle cx="42" cy="-42" r="7.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="44" cy="-42" r="4.2" fill="#0F172A"/>
                            <circle cx="42.5" cy="-44.5" r="1.5" fill="#FFFFFF"/>
                            <!-- Smile -->
                            <path d="M 28 -28 Q 36 -22 42 -28" stroke="#0F172A" stroke-width="3" fill="none" stroke-linecap="round"/>
                            <!-- Steering hand & Star Wand -->
                            <circle cx="-16" cy="14" r="6" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
                            <path d="M 28 -14 Q 48 -10 62 -18" stroke="#5458F7" stroke-width="9" stroke-linecap="round" fill="none"/>
                            <path d="M 28 -14 Q 48 -10 62 -18" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>
                            <circle cx="62" cy="-18" r="5.5" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
                            <line x1="62" y1="-18" x2="88" y2="-28" stroke="#FFD24A" stroke-width="4.5" stroke-linecap="round"/>
                            <g transform="translate(92, -30)">
                                <path d="M 0 -8 C 1 -2 3 -1 8 0 C 3 1 1 3 0 8 C -1 3 -3 1 -8 0 C -3 -1 -1 -3 0 -8 Z" fill="#FFD24A" stroke="#0F172A" stroke-width="1.8"/>
                            </g>
                        </g>

                        <!-- VARIATION 2: LOOPING CORKSCREW (BASED ON REFERENCE TOP-LEFT LOOP) -->
                        <g class="worm-variation" id="worm-v2">
                            <defs>
                                <mask id="v2-worm-body-mask">
                                    <path d="M -55 24 C -50 -10, -25 -45, 5 -45 C 35 -45, 45 -15, 20 -2 C 0 8, -25 0, -20 -30 C -15 -55, 10 -65, 35 -60" 
                                          fill="none" stroke="#FFFFFF" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
                                </mask>
                            </defs>
                            <path d="M -15 -25 C -55 -45 -85 -25 -110 5 C -85 -5 -60 -15 -25 -12 Z" 
                                  fill="#FF5A36" stroke="#0F172A" stroke-width="3.5" stroke-linejoin="round"/>
                            <path d="M -55 24 C -50 -10, -25 -45, 5 -45 C 35 -45, 45 -15, 20 -2 C 0 8, -25 0, -20 -30 C -15 -55, 10 -65, 35 -60" 
                                  fill="none" stroke="#0F172A" stroke-width="45" stroke-linecap="round" stroke-linejoin="round"/>
                            <g mask="url(#v2-worm-body-mask)">
                                <rect x="-130" y="-120" width="230" height="200" fill="#5458F7"/>
                                <path d="M -60 10 Q -45 15 -35 25" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M -45 -25 Q -30 -20 -20 -10" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M -10 -55 Q 5 -45 15 -35" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M 35 -30 Q 25 -20 15 -10" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M 10 5 Q 0 -5 -10 -15" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M -30 -35 Q -15 -35 0 -45" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M 0 -70 Q 15 -60 30 -55" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                            </g>
                            <g transform="translate(35, -92)">
                                <polygon points="0,-13 4,-4 13,0 4,4 0,13 -4,4 -13,0 -4,-4" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>
                            </g>
                            <path d="M 18 -66 C 0 -74 -12 -65 -26 -75" stroke="#FF5A36" stroke-width="6" stroke-linecap="round" fill="none"/>
                            <path d="M 18 -66 C 0 -74 -12 -65 -26 -75" stroke="#0F172A" stroke-width="2" stroke-linecap="round" fill="none"/>
                            <rect x="20" y="-72" width="28" height="8" rx="3" fill="#FF5A36" stroke="#0F172A" stroke-width="2"/>
                            <circle cx="30" cy="-62" r="7.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="32" cy="-62" r="4.2" fill="#0F172A"/>
                            <circle cx="30.5" cy="-64.5" r="1.5" fill="#FFFFFF"/>
                            <circle cx="43" cy="-60" r="7" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="45" cy="-60" r="3.9" fill="#0F172A"/>
                            <circle cx="43.5" cy="-62.5" r="1.4" fill="#FFFFFF"/>
                            <path d="M 32 -48 Q 38 -42 44 -48 Z" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>
                            <path d="M 40 -35 Q 58 -40 68 -55" stroke="#5458F7" stroke-width="8" stroke-linecap="round" fill="none"/>
                            <path d="M 40 -35 Q 58 -40 68 -55" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>
                            <circle cx="68" cy="-55" r="5" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
                        </g>

                        <!-- VARIATION 3: SUPER-MENTOR GLIDER -->
                        <g class="worm-variation" id="worm-v3">
                            <defs>
                                <mask id="v3-worm-body-mask">
                                    <path d="M -70 20 C -45 28, -25 5, 5 10 C 35 15, 55 -5, 65 -25" 
                                          fill="none" stroke="#FFFFFF" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
                                </mask>
                            </defs>
                            <path d="M 0 5 C -45 -18 -85 -10 -120 5 C -90 -2 -65 -10 -25 -2 Z" 
                                  fill="#FF5A36" stroke="#0F172A" stroke-width="3.5" stroke-linejoin="round"/>
                            <path d="M -70 20 C -45 28, -25 5, 5 10 C 35 15, 55 -5, 65 -25" 
                                  fill="none" stroke="#0F172A" stroke-width="45" stroke-linecap="round" stroke-linejoin="round"/>
                            <g mask="url(#v3-worm-body-mask)">
                                <rect x="-140" y="-80" width="250" height="150" fill="#5458F7"/>
                                <path d="M -75 5 Q -65 20 -55 35" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M -45 5 Q -35 18 -25 30" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M -15 -5 Q -5 10 5 25" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M 15 -2 Q 25 12 35 25" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                                <path d="M 45 -15 Q 55 -2 65 10" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
                            </g>
                            <g transform="translate(85, -35)">
                                <polygon points="0,-12 3.5,-3.5 12,0 3.5,3.5 0,12 -3.5,3.5 -12,0 -3.5,-3.5" fill="#FFD24A" stroke="#0F172A" stroke-width="2.2"/>
                            </g>
                            <rect x="44" y="-35" width="30" height="9" rx="4" fill="#0F172A"/>
                            <circle cx="51" cy="-31" r="5" fill="#86EFAC" stroke="#0F172A" stroke-width="1.8"/>
                            <circle cx="65" cy="-31" r="5" fill="#86EFAC" stroke="#0F172A" stroke-width="1.8"/>
                            <circle cx="58" cy="-24" r="7.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="61" cy="-24" r="4.2" fill="#0F172A"/>
                            <circle cx="59.5" cy="-26.5" r="1.5" fill="#FFFFFF"/>
                            <circle cx="70" cy="-23" r="7" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="72" cy="-23" r="3.9" fill="#0F172A"/>
                            <circle cx="70.5" cy="-25.5" r="1.4" fill="#FFFFFF"/>
                            <circle cx="10" cy="18" r="6" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
                            <circle cx="45" cy="16" r="6" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
                        </g>

                    </g>

                    <!-- ================= THE COZY SLEEPING WORM (BOTTOM RIGHT CLOUD) ================= -->
                    <!-- Exact pose from reference bottom-right: coiled like cinnamon roll with sleeping eyes -->
                    <g transform="translate(770, 360)">
                        <!-- Cozy Cloud Nest -->
                        <ellipse cx="0" cy="18" rx="46" ry="16" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
                        <!-- Coiled Worm Body: Violet with Indigo Stripes -->
                        <ellipse cx="0" cy="6" rx="36" ry="22" fill="#5458F7" stroke="#0F172A" stroke-width="3"/>
                        <!-- Coil spirals -->
                        <path d="M-28 6 C-28 18 28 18 28 6 C28 -6 -16 -6 -16 6 C-16 12 12 12 12 6" stroke="#3730A3" stroke-width="6" fill="none" stroke-linecap="round"/>
                        <path d="M-20 -2 C-10 -10 16 -10 24 -2" stroke="#3730A3" stroke-width="5" stroke-linecap="round"/>
                        <!-- Sleeping head in center with curved peaceful eyes ( -.- ) -->
                        <circle cx="0" cy="4" r="13" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
                        <!-- Closed arched eyes -->
                        <path d="M-6 4 Q-3 1 0 4" stroke="#0F172A" stroke-width="2" fill="none" stroke-linecap="round"/>
                        <path d="M2 4 Q5 1 8 4" stroke="#0F172A" stroke-width="2" fill="none" stroke-linecap="round"/>
                        <!-- 'Zzz' Floating -->
                        <text x="18" y="-14" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="11" fill="#FFD24A">z</text>
                        <text x="26" y="-22" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="14" fill="#FFD24A">Z</text>
                    </g>
                </svg>

                <!-- ================= BOTTOM CLOUD CONTAINER (PROBLEM & SOLUTION) ================= -->
                <div class="stage-bottom-deck">
                    <div class="cloud-title-container">
                        <div class="cloud-inner-fix">
                            <span class="problem-line">Too Shy to Ask in Class?</span>
                            <h1 class="solution-line">We Clear It After.</h1>
                            
                            <div class="subtitle-pill-row">
                                <span class="cloud-subtitle-pill">
                                    <span>★</span> 1-on-1 Guided Learning
                                </span>
                                <span class="dot-divider">·</span>
                                <span class="cloud-subtitle-pill">
                                    Zero Teacher Awkwardness
                                </span>
                                <span class="dot-divider">·</span>
                                <span class="cloud-subtitle-pill">
                                    Doubts Solved Before Dinner
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- HIGH-CONVERTING CTA BUTTON -->
                    <div class="cta-bottom-bar">
                        <a href="https://paathshala.app" class="btn-cta-packaging">
                            <span>Book Free 1-on-1 Class</span>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                                <polyline points="12 5 19 12 12 19"></polyline>
                            </svg>
                        </a>
                        <div class="cta-trust-note">
                            ✓ 100% Free Trial · No Card Needed · Classes 1–12
                        </div>
                    </div>
                </div>

            </main>
        </div>

    </div>

    <!-- ================= WORM CHARACTER DESIGN SHEET & POSE VARIATIONS ================= -->
    <div class="character-sheet-card">
        <div class="sheet-head">
            <div>
                <h2 class="sheet-title">Worm Mascot Action Variations</h2>
                <p class="sheet-desc">Engineered strictly from reference media_1792552882621_ebe33cd4.png. Click any card below to test it on the banner!</p>
            </div>
            <span class="spec-badge">3 ACTION POSES</span>
        </div>

        <div class="variations-grid">
            <!-- VARIATION 1 CARD -->
            <div class="variation-card current-active" id="card-v1" onclick="switchWormPose('v1', null)">
                <div class="variation-preview-box">
                    <svg width="220" height="150" viewBox="-120 -80 240 130" fill="none">
                        <!-- Rocket Pencil mini snippet -->
                        <rect x="-100" y="10" width="180" height="24" rx="2" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>
                        <polygon points="80,10 115,22 80,34" fill="#FDE68A" stroke="#0F172A" stroke-width="2.5"/>
                        <polygon points="102,18 115,22 102,26" fill="#0F172A"/>
                        <rect x="-116" y="12" width="16" height="20" rx="3" fill="#FF5A36" stroke="#0F172A" stroke-width="2.5"/>
                        <!-- Worm V1 mini -->
                        <path d="M -8 -16 C -50 -32 -85 -18 -115 8 C -90 2 -65 -12 -28 -6 Z" fill="#FF5A36" stroke="#0F172A" stroke-width="2.5"/>
                        <path d="M -50 15 C -35 4, -25 -12, -8 -14 C 8 -16, 18 -12, 26 -32" fill="none" stroke="#0F172A" stroke-width="36" stroke-linecap="round"/>
                        <path d="M -50 15 C -35 4, -25 -12, -8 -14 C 8 -16, 18 -12, 26 -32" fill="none" stroke="#5458F7" stroke-width="30" stroke-linecap="round"/>
                        <circle cx="23" cy="-36" r="6" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="24.5" cy="-36" r="3.2" fill="#0F172A"/>
                        <circle cx="34" cy="-34" r="5.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="35.5" cy="-34" r="3" fill="#0F172A"/>
                        <g transform="translate(26, -58)">
                            <polygon points="0,-10 3,-3 10,0 3,3 0,10 -3,3 -10,0 -3,-3" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>
                        </g>
                    </svg>
                </div>
                <div class="variation-info-box">
                    <span class="variation-pill-badge orange">★ Pose 1 · Recommended</span>
                    <h3 class="variation-name">The Rocket Surfer</h3>
                    <p class="variation-details">Smooth forward-curved capsule body riding the supersonic pencil. Fluttering orange headband ribbons and cape, holding golden star-wand pointing ahead.</p>
                </div>
            </div>

            <!-- VARIATION 2 CARD -->
            <div class="variation-card" id="card-v2" onclick="switchWormPose('v2', null)">
                <div class="variation-preview-box">
                    <svg width="220" height="150" viewBox="-110 -100 220 140" fill="none">
                        <rect x="-90" y="10" width="160" height="24" rx="2" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>
                        <polygon points="70,10 105,22 70,34" fill="#FDE68A" stroke="#0F172A" stroke-width="2.5"/>
                        <!-- Looping Worm V2 mini -->
                        <path d="M -45 15 C -40 -10, -20 -35, 5 -35 C 28 -35, 35 -12, 16 0 C 0 8, -20 0, -15 -24 C -12 -45, 8 -52, 28 -48" 
                              fill="none" stroke="#0F172A" stroke-width="34" stroke-linecap="round"/>
                        <path d="M -45 15 C -40 -10, -20 -35, 5 -35 C 28 -35, 35 -12, 16 0 C 0 8, -20 0, -15 -24 C -12 -45, 8 -52, 28 -48" 
                              fill="none" stroke="#5458F7" stroke-width="28" stroke-linecap="round"/>
                        <circle cx="23" cy="-50" r="5.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="24.5" cy="-50" r="3" fill="#0F172A"/>
                        <circle cx="33" cy="-48" r="5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="34.5" cy="-48" r="2.8" fill="#0F172A"/>
                        <g transform="translate(28, -72)">
                            <polygon points="0,-10 3,-3 10,0 3,3 0,10 -3,3 -10,0 -3,-3" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>
                        </g>
                    </svg>
                </div>
                <div class="variation-info-box">
                    <span class="variation-pill-badge yellow">⚡ Pose 2 · Acrobatic</span>
                    <h3 class="variation-name">The Looping Corkscrew</h3>
                    <p class="variation-details">Recreates the iconic loop from the top-left of the reference image, coiled acrobatically around the supersonic rocket with energetic excitement.</p>
                </div>
            </div>

            <!-- VARIATION 3 CARD -->
            <div class="variation-card" id="card-v3" onclick="switchWormPose('v3', null)">
                <div class="variation-preview-box">
                    <svg width="220" height="150" viewBox="-120 -60 240 120" fill="none">
                        <rect x="-90" y="10" width="160" height="24" rx="2" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>
                        <polygon points="70,10 105,22 70,34" fill="#FDE68A" stroke="#0F172A" stroke-width="2.5"/>
                        <!-- Glider Worm V3 mini -->
                        <path d="M 0 5 C -45 -18 -85 -10 -120 5 C -90 -2 -65 -10 -25 -2 Z" fill="#FF5A36" stroke="#0F172A" stroke-width="2.5"/>
                        <path d="M -55 15 C -35 22, -18 4, 5 8 C 28 12, 45 -4, 52 -20" 
                              fill="none" stroke="#0F172A" stroke-width="34" stroke-linecap="round"/>
                        <path d="M -55 15 C -35 22, -18 4, 5 8 C 28 12, 45 -4, 52 -20" 
                              fill="none" stroke="#5458F7" stroke-width="28" stroke-linecap="round"/>
                        <rect x="36" y="-28" width="24" height="7" rx="3" fill="#0F172A"/>
                        <circle cx="46" cy="-20" r="5.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="48" cy="-20" r="3" fill="#0F172A"/>
                        <circle cx="56" cy="-19" r="5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
                        <circle cx="58" cy="-19" r="2.8" fill="#0F172A"/>
                        <g transform="translate(68, -28)">
                            <polygon points="0,-9 2.5,-2.5 9,0 2.5,2.5 0,9 -2.5,2.5 -9,0 -2.5,-2.5" fill="#FFD24A" stroke="#0F172A" stroke-width="1.8"/>
                        </g>
                    </svg>
                </div>
                <div class="variation-info-box">
                    <span class="variation-pill-badge yellow">🚀 Pose 3 · Streamlined</span>
                    <h3 class="variation-name">Super-Mentor Glider</h3>
                    <p class="variation-details">Aerodynamic horizontal flight pose with wavy curves, aviator goggles, and twin hands steering the rocket like a supersonic superhero.</p>
                </div>
            </div>
        </div>
    </div>

</div>

<!-- SCRIPT TO INSTANTLY TOGGLE WORM POSES -->
<script>
function switchWormPose(poseId, btnElem) {
    // Hide all variations in the banner
    document.querySelectorAll('.worm-variation').forEach(el => el.classList.remove('active'));
    
    // Show selected variation
    const target = document.getElementById('worm-' + poseId);
    if (target) target.classList.add('active');

    // Update toggle buttons at the top
    document.querySelectorAll('.btn-pose-toggle').forEach(btn => btn.classList.remove('active'));
    if (btnElem) {
        btnElem.classList.add('active');
    } else {
        const matchingBtn = Array.from(document.querySelectorAll('.btn-pose-toggle')).find(b => b.innerText.toLowerCase().includes(poseId === 'v1' ? 'surfer' : poseId === 'v2' ? 'corkscrew' : 'glider'));
        if (matchingBtn) matchingBtn.classList.add('active');
    }

    // Update variation cards below
    document.querySelectorAll('.variation-card').forEach(c => c.classList.remove('current-active'));
    const targetCard = document.getElementById('card-' + poseId);
    if (targetCard) targetCard.classList.add('current-active');
}
</script>

</body>
</html>
'''

def main():
    target_dir = "/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning"
    banner_file = os.path.join(target_dir, "banner.html")
    homepage_file = os.path.join(target_dir, "homepage-section.html")

    with open(banner_file, "w") as f:
        f.write(BANNER_HTML)
    print(f"Updated: {banner_file}")

    with open(homepage_file, "w") as f:
        f.write(BANNER_HTML)
    print(f"Updated: {homepage_file}")

    # Copy to artifact directory
    artifact_dir = "/Users/srinibashbartia/.gemini/antigravity/brain/280bacfb-a77d-43c5-8fd5-6bc903a3d7fe"
    shutil.copy(banner_file, os.path.join(artifact_dir, "banner.html"))
    shutil.copy(homepage_file, os.path.join(artifact_dir, "homepage-section.html"))
    print("Copied files to brain artifact directory")

if __name__ == "__main__":
    main()
