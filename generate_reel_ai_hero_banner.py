#!/usr/bin/env python3
"""
generate_reel_ai_hero_banner.py
Transforms the banner into the modern AI/SaaS hero layout matching media_1792510256594_20151a64.png:
- Clean, premium light aesthetic with soft radial aura
- Display headline addressing the in-class hesitation problem and after-class 1-on-1 solution
- Dual pill CTAs ("Book Free 1-on-1 Class" and "Watch 60s Reel")
- Centerpiece 9:16 smartphone device playing the real video (reel.mp4) with interactive controls and live badge
- Four floating bento micro-cards matching the reference layout:
  1. Top-Left: "2:01 Micro-Reel" with doubt-solver visual
  2. Bottom-Left: "★★★★★" rating pill + Yellow Card "0% Hesitation · 100% Student's Pace"
  3. Top-Right: Mint Green Card "1-on-1 Mentor · After Every Class" with "100% Free Trial" badge
  4. Bottom-Right: Student Card "1.5k+ Doubts Solved Today" with social reactions
- Bottom syllabus trust logo strip: CBSE, ICSE, State Boards, NCERT, IGCSE, Foundation
- High conversion copy and authentic Paathshala colors.
"""

import os
import shutil

HERO_HTML = '''<!DOCTYPE html>
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
            --paathshala-orange: #FF5A36;
            --paathshala-orange-hover: #E04320;
            --paathshala-yellow: #FFD24A;
            --paathshala-mint: #86EFAC;
            --paathshala-mint-bg: #DCFCE7;
            --paathshala-mint-dark: #166534;
            --ink: #0F172A;
            --ink-secondary: #475569;
            --ink-muted: #94A3B8;
            --border-subtle: #E2E8F0;
            --border-card: #CBD5E1;
            --white: #FFFFFF;
            --bg-canvas: #FAFAFB;
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
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* -------------------------------------------------------------
           TOP NAVIGATION BAR (MATCHING REFERENCE /hello@reel.ai STYLE)
           ------------------------------------------------------------- */
        .site-nav {
            width: 100%;
            max-width: 1240px;
            margin: 0 auto;
            padding: 24px 32px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: relative;
            z-index: 20;
        }

        .nav-left {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--ink);
        }

        .nav-logo-mark {
            width: 32px;
            height: 32px;
            background-color: var(--paathshala-orange);
            border-radius: 9px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--white);
            font-weight: 900;
            font-size: 1.1rem;
            box-shadow: 0 2px 6px rgba(255, 90, 54, 0.3);
        }

        .nav-brand-title {
            font-size: 1.05rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: var(--ink);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .nav-brand-title span {
            color: var(--ink-muted);
            font-weight: 600;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 28px;
            list-style: none;
        }

        .nav-link-item a {
            text-decoration: none;
            color: var(--ink-secondary);
            font-size: 0.9rem;
            font-weight: 600;
            transition: color 0.15s ease;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .nav-link-item a:hover {
            color: var(--paathshala-violet);
        }

        .nav-chevron {
            font-size: 0.65rem;
            opacity: 0.6;
        }

        .nav-right {
            display: flex;
            align-items: center;
            gap: 18px;
        }

        .nav-btn-link {
            text-decoration: none;
            color: var(--ink);
            font-size: 0.9rem;
            font-weight: 700;
            transition: color 0.15s ease;
        }

        .nav-btn-link:hover {
            color: var(--paathshala-violet);
        }

        .nav-btn-primary {
            background-color: var(--ink);
            color: var(--white);
            text-decoration: none;
            padding: 10px 22px;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 700;
            letter-spacing: -0.01em;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
        }

        .nav-btn-primary:hover {
            background-color: var(--paathshala-violet);
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(84, 88, 247, 0.3);
        }

        /* -------------------------------------------------------------
           MAIN HERO SECTION
           ------------------------------------------------------------- */
        .hero-section {
            width: 100%;
            max-width: 1240px;
            margin: 0 auto;
            padding: 36px 24px 60px;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
        }

        /* SUBTLE BACKGROUND RADIAL GLOW (EXACT LIKE REFERENCE) */
        .hero-glow-aura {
            position: absolute;
            top: 280px;
            left: 50%;
            transform: translateX(-50%);
            width: 900px;
            height: 600px;
            background: radial-gradient(circle at 50% 65%, #FFF0EB 0%, #EEF2FF 40%, rgba(250, 250, 251, 0) 72%);
            z-index: 1;
            pointer-events: none;
            border-radius: 50%;
        }

        /* -------------------------------------------------------------
           HERO TEXT HEADLINE & SUBHEAD
           ------------------------------------------------------------- */
        .hero-copy-container {
            text-align: center;
            max-width: 860px;
            margin: 0 auto 36px;
            position: relative;
            z-index: 5;
        }

        .hero-badge-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background-color: #EEF2FF;
            color: var(--paathshala-violet);
            border: 1.5px solid #C7D2FE;
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 20px;
        }

        .hero-headline {
            font-size: clamp(2.4rem, 4.6vw, 4.2rem);
            font-weight: 900;
            letter-spacing: -0.04em;
            line-height: 1.08;
            color: var(--ink);
            margin-bottom: 18px;
        }

        .hero-headline .highlight-violet {
            color: var(--paathshala-violet);
            position: relative;
            display: inline-block;
        }

        .hero-subhead {
            font-size: clamp(1.05rem, 1.6vw, 1.25rem);
            font-weight: 500;
            color: var(--ink-secondary);
            line-height: 1.5;
            max-width: 680px;
            margin: 0 auto 28px;
        }

        /* DUAL ACTION CTAS (EXACT LIKE REFERENCE) */
        .hero-cta-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            flex-wrap: wrap;
        }

        .btn-cta-primary {
            background-color: var(--ink);
            color: var(--white);
            text-decoration: none;
            padding: 15px 36px;
            border-radius: 9999px;
            font-size: 1.02rem;
            font-weight: 800;
            letter-spacing: -0.01em;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 6px 20px rgba(15, 23, 42, 0.18);
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-cta-primary:hover {
            background-color: var(--paathshala-orange);
            transform: translateY(-2px);
            box-shadow: 0 10px 28px rgba(255, 90, 54, 0.35);
        }

        .btn-cta-secondary {
            background-color: var(--white);
            color: var(--ink);
            text-decoration: none;
            padding: 14px 30px;
            border-radius: 9999px;
            border: 1.5px solid var(--border-card);
            font-size: 1.02rem;
            font-weight: 700;
            letter-spacing: -0.01em;
            transition: all 0.2s ease;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-cta-secondary:hover {
            border-color: var(--ink);
            background-color: #F8FAFC;
            transform: translateY(-1px);
        }

        /* -------------------------------------------------------------
           CENTERPIECE STAGE: PHONE WITH VIDEO + 4 FLOATING BENTO CARDS
           ------------------------------------------------------------- */
        .stage-wrapper {
            position: relative;
            width: 100%;
            max-width: 980px;
            margin: 20px auto 40px;
            min-height: 600px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 5;
        }

        /* -------------------------------------------------------------
           CENTRAL SMARTPHONE MOCKUP (WITH REAL VIDEO reel.mp4)
           ------------------------------------------------------------- */
        .phone-mockup-frame {
            position: relative;
            width: 295px;
            height: 570px;
            background-color: #000000;
            border: 9px solid #1E293B;
            border-radius: 46px;
            box-shadow: 
                0 30px 80px -15px rgba(15, 23, 42, 0.30),
                0 0 0 1px rgba(15, 23, 42, 0.12),
                0 10px 25px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            z-index: 8;
        }

        /* PHONE DYNAMIC ISLAND / NOTCH */
        .phone-island {
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 90px;
            height: 22px;
            background-color: #000000;
            border-radius: 9999px;
            z-index: 25;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 8px;
        }

        .island-lens {
            width: 9px;
            height: 9px;
            background-color: #0F172A;
            border-radius: 50%;
            border: 1px solid #334155;
        }

        .island-sensor {
            width: 7px;
            height: 7px;
            background-color: #1E293B;
            border-radius: 50%;
        }

        /* VIDEO CONTAINER */
        .phone-video-container {
            position: relative;
            width: 100%;
            height: 100%;
            background-color: #090D16;
            overflow: hidden;
        }

        .phone-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* VIDEO TOP OVERLAY INFO (MENTOR + LIVE BADGE) */
        .video-header-overlay {
            position: absolute;
            top: 40px;
            left: 14px;
            right: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 15;
            pointer-events: none;
        }

        .mentor-profile-chip {
            display: flex;
            align-items: center;
            gap: 8px;
            background-color: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(8px);
            padding: 4px 12px 4px 5px;
            border-radius: 9999px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--white);
        }

        .mentor-avatar-img {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background-color: var(--paathshala-orange);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.68rem;
            font-weight: 900;
            color: var(--white);
            border: 1.5px solid var(--white);
        }

        .mentor-name-text {
            font-size: 0.74rem;
            font-weight: 800;
            letter-spacing: -0.01em;
        }

        .badge-live-red {
            background-color: #EF4444;
            color: var(--white);
            font-size: 0.65rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 9999px;
            display: flex;
            align-items: center;
            gap: 5px;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            box-shadow: 0 2px 8px rgba(239, 68, 68, 0.4);
        }

        .live-dot-pulse {
            width: 6px;
            height: 6px;
            background-color: var(--white);
            border-radius: 50%;
            animation: pulseDot 1.4s infinite;
        }

        @keyframes pulseDot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.8); }
        }

        /* BOTTOM OVERLAY IN VIDEO (LESSON & CONTROLS) */
        .video-bottom-overlay {
            position: absolute;
            bottom: 20px;
            left: 14px;
            right: 14px;
            z-index: 15;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .lesson-tag-card {
            background-color: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(10px);
            padding: 8px 12px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--white);
        }

        .lesson-tag-step {
            font-size: 0.65rem;
            font-weight: 700;
            color: var(--paathshala-yellow);
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        .lesson-tag-title {
            font-size: 0.78rem;
            font-weight: 800;
            line-height: 1.2;
            margin-top: 2px;
        }

        .video-controls-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .btn-video-control {
            background-color: rgba(255, 255, 255, 0.9);
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: var(--ink);
            font-size: 0.85rem;
            transition: all 0.15s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }

        .btn-video-control:hover {
            background-color: var(--white);
            transform: scale(1.08);
        }

        /* -------------------------------------------------------------
           THE 4 FLOATING BENTO MICRO-CARDS (MATCHING REFERENCE)
           ------------------------------------------------------------- */
        .floating-bento-card {
            position: absolute;
            z-index: 12;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
            cursor: default;
        }

        .floating-bento-card:hover {
            transform: translateY(-4px) !important;
        }

        /* -------------------------------------------------------------
           CARD 1: TOP-LEFT MICRO CARD (MICRO-REEL)
           ------------------------------------------------------------- */
        .card-top-left {
            top: 40px;
            left: 70px;
        }

        .card-micro-reel {
            background-color: #E2E8F0;
            border: 1.5px solid var(--border-card);
            border-radius: 20px;
            padding: 12px 16px;
            width: 170px;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .micro-reel-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .time-pill-black {
            background-color: var(--ink);
            color: var(--white);
            font-size: 0.68rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 6px;
        }

        .micro-reel-label {
            font-size: 0.82rem;
            font-weight: 800;
            color: var(--paathshala-violet);
        }

        .micro-reel-graphic {
            width: 100%;
            height: 52px;
            background-color: var(--paathshala-violet);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        .pill-capsule-icon {
            background-color: #3B82F6;
            color: var(--white);
            font-size: 0.72rem;
            font-weight: 900;
            padding: 6px 14px;
            border-radius: 9999px;
            border: 2px solid rgba(255,255,255,0.4);
            letter-spacing: 0.05em;
            transform: rotate(-5deg);
        }

        /* -------------------------------------------------------------
           CARD 2: BOTTOM-LEFT MICRO CARD (0% HESITATION & 5-STAR RATING)
           ------------------------------------------------------------- */
        .card-bottom-left {
            bottom: 40px;
            left: 55px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .rating-stars-bubble {
            background-color: var(--white);
            border: 1.5px solid var(--border-subtle);
            border-radius: 9999px;
            padding: 5px 14px;
            font-size: 0.75rem;
            font-weight: 900;
            color: #EAB308;
            box-shadow: 0 6px 16px rgba(15, 23, 42, 0.06);
            align-self: flex-start;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            letter-spacing: 2px;
        }

        .rating-num {
            color: var(--ink);
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: normal;
            margin-left: 4px;
        }

        .card-stat-yellow {
            background-color: var(--paathshala-yellow);
            border: 2px solid var(--ink);
            border-radius: 20px;
            padding: 14px 18px;
            width: 205px;
            box-shadow: 4px 4px 0px var(--ink);
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .stat-bars-icon {
            display: flex;
            align-items: flex-end;
            gap: 3px;
            height: 28px;
        }

        .stat-bar-elem {
            width: 6px;
            background-color: var(--ink);
            border-radius: 2px;
        }

        .stat-info-col {
            display: flex;
            flex-direction: column;
        }

        .stat-label-small {
            font-size: 0.65rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--ink);
            opacity: 0.85;
        }

        .stat-big-val {
            font-size: 1.45rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            color: var(--ink);
            line-height: 1.05;
        }

        .stat-eye-dot {
            font-size: 0.75rem;
            margin-left: 2px;
        }

        /* -------------------------------------------------------------
           CARD 3: TOP-RIGHT MICRO CARD (MINT GREEN 1-ON-1 MENTOR CARD)
           ------------------------------------------------------------- */
        .card-top-right {
            top: 45px;
            right: 50px;
        }

        .card-items-green {
            background-color: #BBF7D0;
            border: 2px solid var(--ink);
            border-radius: 22px;
            padding: 18px 20px;
            width: 225px;
            box-shadow: 4px 4px 0px var(--ink);
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: relative;
        }

        .green-card-text {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .green-card-headline {
            font-size: 1.25rem;
            font-weight: 900;
            color: var(--ink);
            letter-spacing: -0.03em;
            line-height: 1.1;
        }

        .green-card-sub {
            font-size: 0.72rem;
            font-weight: 700;
            color: #166534;
        }

        .green-badge-pill {
            margin-top: 8px;
            background-color: var(--white);
            color: var(--ink);
            border: 1.5px solid var(--ink);
            padding: 3px 10px;
            border-radius: 9999px;
            font-size: 0.68rem;
            font-weight: 800;
            width: fit-content;
        }

        .green-bottle-graphic {
            width: 48px;
            height: 72px;
            background-color: #15803D;
            border-radius: 14px 14px 10px 10px;
            border: 2px solid var(--ink);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            transform: rotate(8deg);
            box-shadow: 2px 2px 0px var(--ink);
        }

        .green-bottle-cap {
            position: absolute;
            top: -6px;
            width: 18px;
            height: 6px;
            background-color: var(--ink);
            border-radius: 3px;
        }

        .green-bottle-txt {
            color: var(--white);
            font-size: 0.75rem;
            font-weight: 900;
            letter-spacing: 0.05em;
        }

        /* -------------------------------------------------------------
           CARD 4: BOTTOM-RIGHT MICRO CARD (STUDENT & REACTION SOCIAL PROOF)
           ------------------------------------------------------------- */
        .card-bottom-right {
            bottom: 35px;
            right: 40px;
        }

        .card-reaction-white {
            background-color: var(--white);
            border: 1.5px solid var(--border-subtle);
            border-radius: 20px;
            padding: 10px 10px 12px;
            width: 175px;
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.12);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .reaction-thumb-area {
            width: 100%;
            height: 76px;
            border-radius: 14px;
            background: linear-gradient(135deg, #FFEDD5 0%, #FED7AA 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(0,0,0,0.06);
        }

        .reaction-student-avatar {
            font-size: 2.2rem;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
        }

        .reaction-counter-badge {
            position: absolute;
            bottom: 6px;
            left: 6px;
            background-color: var(--ink);
            color: var(--white);
            font-size: 0.65rem;
            font-weight: 800;
            padding: 2px 7px;
            border-radius: 6px;
        }

        .reaction-icons-strip {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 0 4px;
            color: var(--ink-secondary);
            font-size: 0.85rem;
        }

        .heart-icon {
            color: #EF4444;
            font-size: 0.95rem;
        }

        /* -------------------------------------------------------------
           BOTTOM SYLLABUS & TRUST PARTNER BAR
           ------------------------------------------------------------- */
        .trust-strip-container {
            width: 100%;
            max-width: 1080px;
            margin: 10px auto 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 16px;
            z-index: 5;
        }

        .trust-label {
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            color: var(--ink-muted);
            text-transform: uppercase;
        }

        .trust-logos-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: clamp(16px, 4vw, 42px);
            flex-wrap: wrap;
            opacity: 0.85;
        }

        .trust-logo-pill {
            font-size: 0.95rem;
            font-weight: 900;
            letter-spacing: 0.05em;
            color: var(--ink);
            text-transform: uppercase;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .trust-logo-bullet {
            color: var(--paathshala-orange);
            font-size: 1.2rem;
            line-height: 0;
        }

        /* -------------------------------------------------------------
           RESPONSIVE BREAKPOINTS
           ------------------------------------------------------------- */
        @media (max-width: 980px) {
            .nav-links {
                display: none;
            }

            .stage-wrapper {
                min-height: auto;
                flex-direction: column;
                gap: 24px;
            }

            .floating-bento-card {
                position: static;
                transform: none !important;
            }

            .cards-mobile-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 14px;
                width: 100%;
                max-width: 440px;
            }

            .card-micro-reel,
            .card-stat-yellow,
            .card-items-green,
            .card-reaction-white {
                width: 100%;
            }

            .hero-glow-aura {
                width: 100%;
                top: 200px;
            }
        }

        @media (max-width: 480px) {
            .hero-headline {
                font-size: 2.1rem;
            }
            .phone-mockup-frame {
                width: 260px;
                height: 510px;
            }
            .cards-mobile-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <!-- ================= TOP NAVIGATION BAR ================= -->
    <nav class="site-nav">
        <a href="https://paathshala.app" class="nav-left">
            <div class="nav-logo-mark">P</div>
            <div class="nav-brand-title">/ hello@paathshala.app</div>
        </a>

        <ul class="nav-links">
            <li class="nav-link-item">
                <a href="#features">Features <span class="nav-chevron">▼</span></a>
            </li>
            <li class="nav-link-item">
                <a href="#how-it-works">How It Works</a>
            </li>
            <li class="nav-link-item">
                <a href="#success-stories">Success Stories</a>
            </li>
            <li class="nav-link-item">
                <a href="#syllabus">Syllabus (1–12)</a>
            </li>
            <li class="nav-link-item">
                <a href="#pricing">Pricing</a>
            </li>
        </ul>

        <div class="nav-right">
            <a href="https://paathshala.app" class="nav-btn-link">Book A Demo</a>
            <a href="https://paathshala.app" class="nav-btn-primary">Get Started</a>
        </div>
    </nav>

    <!-- ================= HERO SECTION ================= -->
    <main class="hero-section">

        <!-- SUBTLE BACKGROUND GLOW AURA -->
        <div class="hero-glow-aura"></div>

        <!-- HERO HEADLINE & COPY (EXACT COPY REQUIREMENTS) -->
        <div class="hero-copy-container">
            <div class="hero-badge-pill">
                <span>★</span> AFTER-CLASS 1-ON-1 GUIDED LEARNING
            </div>

            <h1 class="hero-headline">
                Too Shy to Ask in Class?<br>
                <span class="highlight-violet">We Clear Every Doubt After.</span>
            </h1>

            <p class="hero-subhead">
                From hesitant silence to complete concept clarity — your dedicated 1-on-1 mentor re-explains every single lesson from scratch until it clicks. 100% judgment-free.
            </p>

            <div class="hero-cta-row">
                <a href="https://paathshala.app" class="btn-cta-primary">
                    <span>Book Free 1-on-1 Class</span>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </a>
                <a href="#features" class="btn-cta-secondary" onclick="togglePlayVideo()">
                    <span>Watch Class Reel</span>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                        <polygon points="5 3 19 12 5 21 5 3"></polygon>
                    </svg>
                </a>
            </div>
        </div>

        <!-- ================= CENTERPIECE STAGE: PHONE + 4 BENTO CARDS ================= -->
        <div class="stage-wrapper">

            <!-- CARD 1: TOP-LEFT MICRO CARD (2:01 MICRO-REEL) -->
            <div class="floating-bento-card card-top-left">
                <div class="card-micro-reel">
                    <div class="micro-reel-top">
                        <span class="time-pill-black">2:01</span>
                        <span class="micro-reel-label">Micro-Reel</span>
                    </div>
                    <div class="micro-reel-graphic">
                        <div class="pill-capsule-icon">REEL</div>
                    </div>
                </div>
            </div>

            <!-- CARD 2: BOTTOM-LEFT MICRO CARD (0% HESITATION + 5-STAR RATING) -->
            <div class="floating-bento-card card-bottom-left">
                <div class="rating-stars-bubble">
                    ★★★★★ <span class="rating-num">5.0</span>
                </div>
                <div class="card-stat-yellow">
                    <div class="stat-bars-icon">
                        <div class="stat-bar-elem" style="height: 12px;"></div>
                        <div class="stat-bar-elem" style="height: 20px;"></div>
                        <div class="stat-bar-elem" style="height: 28px;"></div>
                    </div>
                    <div class="stat-info-col">
                        <span class="stat-label-small">Zero Shyness</span>
                        <div class="stat-big-val">
                            0% <span class="stat-eye-dot">👁️</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CENTRAL SMARTPHONE DEVICE MOCKUP (WITH REAL VIDEO reel.mp4) -->
            <div class="phone-mockup-frame">
                <!-- Phone Island Notch -->
                <div class="phone-island">
                    <div class="island-lens"></div>
                    <div class="island-sensor"></div>
                </div>

                <!-- Video Frame -->
                <div class="phone-video-container">
                    <video id="classReelVideo" class="phone-video" playsinline autoplay muted loop poster="reel-poster.jpg">
                        <source src="reel.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>

                    <!-- Video Top Overlay -->
                    <div class="video-header-overlay">
                        <div class="mentor-profile-chip">
                            <div class="mentor-avatar-img">A</div>
                            <span class="mentor-name-text">Aditi · 1-on-1 Mentor</span>
                        </div>
                        <div class="badge-live-red">
                            <div class="live-dot-pulse"></div>
                            <span>Live</span>
                        </div>
                    </div>

                    <!-- Video Bottom Overlay -->
                    <div class="video-bottom-overlay">
                        <div class="lesson-tag-card">
                            <div class="lesson-tag-step">Step 2 of 4 · Step-by-Step</div>
                            <div class="lesson-tag-title">Quadratic Equations Explained Simply</div>
                        </div>
                        <div class="video-controls-row">
                            <button class="btn-video-control" id="btnPlayPause" onclick="togglePlayVideo()" title="Play/Pause">
                                ❚❚
                            </button>
                            <button class="btn-video-control" id="btnAudioToggle" onclick="toggleMuteVideo()" title="Mute/Unmute">
                                🔇
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CARD 3: TOP-RIGHT MICRO CARD (MINT GREEN 1-ON-1 MENTOR CARD) -->
            <div class="floating-bento-card card-top-right">
                <div class="card-items-green">
                    <div class="green-card-text">
                        <div class="green-card-headline">1-on-1 Mentor</div>
                        <div class="green-card-sub">After every class</div>
                        <div class="green-badge-pill">100% Free</div>
                    </div>
                    <div class="green-bottle-graphic">
                        <div class="green-bottle-cap"></div>
                        <span class="green-bottle-txt">AG</span>
                    </div>
                </div>
            </div>

            <!-- CARD 4: BOTTOM-RIGHT MICRO CARD (STUDENT & SOCIAL PROOF) -->
            <div class="floating-bento-card card-bottom-right">
                <div class="card-reaction-white">
                    <div class="reaction-thumb-area">
                        <div class="reaction-student-avatar">👧🏽</div>
                        <div class="reaction-counter-badge">1.5k doubts solved</div>
                    </div>
                    <div class="reaction-icons-strip">
                        <span class="heart-icon">❤️</span>
                        <span>💬</span>
                        <span>🚀</span>
                    </div>
                </div>
            </div>

        </div>

        <!-- ================= BOTTOM SYLLABUS & TRUST STRIP ================= -->
        <div class="trust-strip-container">
            <span class="trust-label">FULL SYLLABUS COVERAGE · CLASSES 1 TO 12</span>
            <div class="trust-logos-row">
                <div class="trust-logo-pill">CBSE</div>
                <div class="trust-logo-bullet">·</div>
                <div class="trust-logo-pill">ICSE</div>
                <div class="trust-logo-bullet">·</div>
                <div class="trust-logo-pill">STATE BOARDS</div>
                <div class="trust-logo-bullet">·</div>
                <div class="trust-logo-pill">NCERT</div>
                <div class="trust-logo-bullet">·</div>
                <div class="trust-logo-pill">IGCSE</div>
                <div class="trust-logo-bullet">·</div>
                <div class="trust-logo-pill">IB FOUNDATION</div>
            </div>
        </div>

    </main>

    <!-- SCRIPT FOR VIDEO CONTROLS -->
    <script>
        const video = document.getElementById('classReelVideo');
        const btnPlayPause = document.getElementById('btnPlayPause');
        const btnAudio = document.getElementById('btnAudioToggle');

        function togglePlayVideo() {
            if (video.paused) {
                video.play();
                btnPlayPause.innerText = '❚❚';
            } else {
                video.pause();
                btnPlayPause.innerText = '▶';
            }
        }

        function toggleMuteVideo() {
            video.muted = !video.muted;
            btnAudio.innerText = video.muted ? '🔇' : '🔊';
        }

        // Auto-play attempt on page load
        document.addEventListener('DOMContentLoaded', () => {
            video.play().catch(e => console.log('Autoplay muted triggered'));
        });
    </script>

</body>
</html>
'''

def main():
    target_dir = "/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning"
    banner_file = os.path.join(target_dir, "banner.html")
    homepage_file = os.path.join(target_dir, "homepage-section.html")

    with open(banner_file, "w") as f:
        f.write(HERO_HTML)
    print(f"Updated banner: {banner_file}")

    with open(homepage_file, "w") as f:
        f.write(HERO_HTML)
    print(f"Updated homepage: {homepage_file}")

    # Also update artifact directory
    artifact_dir = "/Users/srinibashbartia/.gemini/antigravity/brain/280bacfb-a77d-43c5-8fd5-6bc903a3d7fe"
    shutil.copy(banner_file, os.path.join(artifact_dir, "banner.html"))
    shutil.copy(homepage_file, os.path.join(artifact_dir, "homepage-section.html"))
    print("Copied files to brain artifact directory")

if __name__ == "__main__":
    main()
