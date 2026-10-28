#!/usr/bin/env python3
"""Builds the 24/7 AI Guided Learning / Mitra AI showcase as a native full-width website SECTION.

Transforms the standalone banner canvas into a responsive <section> element styled to dock
directly beneath the Hero Section and Carousel.

Outputs:
1. paathshala-guided-learning/homepage-section.html (standalone section component & preview)
2. paathshala-guided-learning/landing-with-ai-section.html (full page showing Hero + Carousel + AI Section)
3. Updates paathshala-website/src/main/resources/static/locations-mumbai.html (placed directly below hero section / carousel)
"""

import re
from pathlib import Path

def build_perspective_keys() -> str:
    rows = [
        (23, 36, [1]*14),
        (40, 54, [1.4] + [1]*12 + [1.4]),
        (58, 72, [1.7] + [1]*11 + [1.8]),
        (76, 90, [2.2] + [1]*10 + [2.2]),
        (94, 108, [1.2, 1.2, 1.4, 5.2, 1.4, 1.2, 1.2]),
    ]
    polys = []
    for r_idx, (yt, yb, weights) in enumerate(rows):
        lx_t = 136 - (yt - 20) * 0.40
        rx_t = 864 + (yt - 20) * 0.40
        lx_b = 136 - (yb - 20) * 0.40
        rx_b = 864 + (yb - 20) * 0.40
        total_w = sum(weights)
        cur_w = 0.0
        for k_idx, w in enumerate(weights):
            f0 = cur_w / total_w
            f1 = (cur_w + w) / total_w
            cur_w += w
            x0_t = lx_t + (rx_t - lx_t) * f0 + 2.2
            x1_t = lx_t + (rx_t - lx_t) * f1 - 2.2
            x0_b = lx_b + (rx_b - lx_b) * f0 + 2.4
            x1_b = lx_b + (rx_b - lx_b) * f1 - 2.4
            fill = "#FF5A36" if (r_idx == 0 and k_idx == 0) or (r_idx == 2 and k_idx == len(weights) - 1) else "#1E293B"
            pts = f"{x0_t:.1f},{yt} {x1_t:.1f},{yt} {x1_b:.1f},{yb} {x0_b:.1f},{yb}"
            polys.append(f'<polygon points="{pts}" fill="{fill}" stroke="#0F172A" stroke-width="1.2" stroke-linejoin="round"/>')
    return "\n              ".join(polys)

KEYS_SVG = build_perspective_keys()

SECTION_CSS = """
  /* =========================================================================
     24/7 AI GUIDED LEARNING (MITRA AI TUTOR) SECTION STYLES
     ========================================================================= */
  .ai-guided-learning-section {
    position: relative;
    width: 100%;
    background-color: #5458F7;
    background-image: radial-gradient(rgba(255, 255, 255, 0.22) 1.5px, transparent 1.5px);
    background-size: 24px 24px;
    border-top: 4px solid #0F172A;
    border-bottom: 4px solid #0F172A;
    color: #0F172A;
    padding-top: clamp(3rem, 5vw, 5.5rem);
    padding-bottom: clamp(3rem, 5vw, 5.5rem);
    overflow: hidden;
    isolation: isolate;
  }

  .ai-section-container {
    max-width: 1280px;
    margin-left: auto;
    margin-right: auto;
    padding-left: clamp(1rem, 3vw, 2.5rem);
    padding-right: clamp(1rem, 3vw, 2.5rem);
    position: relative;
    z-index: 10;
    width: 100%;
    box-sizing: border-box;
  }

  .ai-corner-burst {
    position: absolute;
    top: -24px;
    left: -24px;
    width: clamp(120px, 14vw, 170px);
    height: clamp(120px, 14vw, 170px);
    z-index: 2;
    pointer-events: none;
    filter: drop-shadow(5px 5px 0px #0F172A);
  }

  .ai-section-grid {
    display: grid;
    grid-template-columns: 0.9fr 1.3fr;
    gap: clamp(1.8rem, 3.5vw, 3.5rem);
    align-items: center;
    width: 100%;
  }

  /* Left Column: Outcome Copy */
  .ai-left-copy {
    position: relative;
    z-index: 4;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-align: start;
  }

  .ai-eyebrow-pill {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background-color: #FAF7F2;
    color: #0F172A;
    border: 2.5px solid #0F172A;
    border-radius: 999px;
    padding: 5px 14px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: clamp(0.7rem, 0.64rem + 0.25vw, 0.8rem);
    letter-spacing: 0.02em;
    box-shadow: 3.5px 3.5px 0px #0F172A;
    margin-bottom: 0.85rem;
  }

  .ai-eyebrow-pill .sparkle {
    color: #7C3AED;
    font-size: 0.95rem;
    line-height: 1;
  }

  .ai-eyebrow-pill .pill-divider {
    color: #94A3B8;
    font-weight: 400;
  }

  .ai-section-heading {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: clamp(1.9rem, 1.25rem + 2vw, 2.9rem);
    line-height: 1.12;
    letter-spacing: -0.03em;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.35rem;
    margin: 0;
    padding: 0;
  }

  .ai-heading-hook {
    color: #FFFFFF;
    text-shadow: 3px 3px 0px #0F172A;
    display: block;
  }

  .ai-heading-highlight {
    display: inline-block;
    background-color: #FFD24A;
    color: #0F172A;
    font-family: 'Outfit', sans-serif;
    font-weight: 900;
    font-size: clamp(1.75rem, 1.15rem + 1.8vw, 2.65rem);
    line-height: 1.05;
    letter-spacing: -0.035em;
    padding: 0.14em 0.44em 0.18em;
    border: 3.5px solid #0F172A;
    box-shadow: 6px 6px 0px #0F172A;
    transform: rotate(-1.2deg);
    margin-top: 0.15rem;
  }

  .ai-subheadline {
    margin-top: 0.9rem;
    font-size: clamp(0.88rem, 0.8rem + 0.22vw, 1rem);
    line-height: 1.45;
    color: #FAF7F2;
    font-weight: 600;
    max-width: 48ch;
  }

  .ai-value-points-list {
    list-style: none;
    margin: 1.1rem 0 0 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    max-width: 50ch;
  }

  .ai-value-point-item {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
    font-size: clamp(0.82rem, 0.74rem + 0.2vw, 0.9rem);
    line-height: 1.35;
    color: #FAF7F2;
    font-weight: 500;
  }

  .ai-point-check-badge {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background-color: #86EFAC;
    color: #0F172A;
    border: 2px solid #0F172A;
    box-shadow: 2px 2px 0px #0F172A;
    display: inline-grid;
    place-items: center;
    font-family: 'Outfit', sans-serif;
    font-weight: 900;
    font-size: 0.68rem;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .ai-point-text strong {
    color: #FFD24A;
    font-weight: 800;
  }

  .ai-cta-group {
    margin-top: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
    align-items: flex-start;
  }

  .ai-cta-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.85rem;
  }

  .ai-primary-cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    background-color: #FF5A36;
    color: #FFFFFF;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: clamp(0.92rem, 0.82rem + 0.32vw, 1.05rem);
    padding: 0.75rem 1.5rem;
    border: 3px solid #0F172A;
    border-radius: 12px;
    box-shadow: 5px 5px 0px #0F172A;
    text-decoration: none;
    cursor: pointer;
    transition: transform 0.12s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.12s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.12s;
  }

  .ai-primary-cta-btn:hover {
    transform: translate(-2px, -2px);
    box-shadow: 7px 7px 0px #0F172A;
    background-color: #FF6B4A;
  }

  .ai-primary-cta-btn:active {
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0px #0F172A;
  }

  .ai-cta-subnote {
    font-size: 0.76rem;
    font-weight: 600;
    color: rgba(250, 247, 242, 0.88);
    letter-spacing: 0.01em;
  }

  .ai-trust-note {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    margin-top: 0.9rem;
    font-size: 0.74rem;
    font-weight: 700;
    color: rgba(250, 247, 242, 0.88);
    letter-spacing: 0.01em;
    line-height: 1.35;
    max-width: 54ch;
  }

  .ai-trust-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background-color: #86EFAC;
    border: 1.5px solid #0F172A;
    flex-shrink: 0;
  }

  /* Right Column: Outer Tabs + Laptop Assembly */
  .ai-right-laptop-col {
    position: relative;
    z-index: 3;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .ai-laptop-external-nav {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 8px;
    margin-bottom: 14px;
    width: 100%;
    z-index: 5;
  }

  .ai-ext-nav-tab {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background-color: #FAF7F2;
    color: #0F172A;
    border: 2.5px solid #0F172A;
    border-radius: 999px;
    padding: 6px 14px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: clamp(0.72rem, 0.68rem + 0.2vw, 0.82rem);
    cursor: pointer;
    box-shadow: 3.5px 3.5px 0px #0F172A;
    transition: transform 0.12s ease, box-shadow 0.12s ease, background-color 0.12s ease;
    user-select: none;
  }

  .ai-ext-nav-tab:hover {
    transform: translate(-1.5px, -1.5px);
    box-shadow: 5px 5px 0px #0F172A;
    background-color: #FFFFFF;
  }

  .ai-ext-nav-tab.active {
    background-color: #FFD24A;
    border-color: #0F172A;
    box-shadow: 4px 4px 0px #0F172A;
    transform: translate(-1px, -1px);
  }

  .ai-ext-tab-icon {
    font-size: 0.92rem;
    line-height: 1;
  }

  /* Laptop Canvas Assembly */
  .ai-laptop-assembly {
    position: relative;
    width: 100%;
    max-width: 640px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .ai-laptop-lid {
    position: relative;
    width: 82%;
    z-index: 2;
  }

  .ai-laptop-bezel {
    position: relative;
    background-color: #0F172A;
    border: 3.5px solid #0F172A;
    border-radius: 12px 12px 0 0;
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45), inset 0 0 0 1.5px rgba(255, 255, 255, 0.1);
    padding: 8px 9px 15px 9px;
    overflow: hidden;
    box-sizing: border-box;
  }

  .ai-webcam-notch {
    position: absolute;
    top: 2px;
    left: 50%;
    transform: translateX(-50%);
    width: 28px;
    height: 4px;
    background-color: #000000;
    border-radius: 0 0 3px 3px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 3px;
    z-index: 10;
  }

  .ai-webcam-lens {
    width: 2.5px;
    height: 2.5px;
    border-radius: 50%;
    background-color: #1E293B;
  }

  .ai-webcam-led {
    width: 1.5px;
    height: 1.5px;
    border-radius: 50%;
    background-color: #86EFAC;
  }

  .ai-bezel-chin {
    position: absolute;
    bottom: 2px;
    left: 50%;
    transform: translateX(-50%);
    font-family: 'Outfit', sans-serif;
    font-size: 0.48rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    color: rgba(255, 255, 255, 0.28);
    pointer-events: none;
  }

  .ai-laptop-screen {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 10;
    background-color: #090D16;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.08);
  }

  .ai-screen-views-wrapper {
    position: relative;
    width: 100%;
    height: 100%;
  }

  .ai-screen-view {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    pointer-events: none;
    visibility: hidden;
    transition: opacity 0.22s ease;
  }

  .ai-screen-view.active {
    opacity: 1;
    pointer-events: auto;
    visibility: visible;
    z-index: 2;
  }

  /* Screen 1: Reel Video Player */
  .ai-view-full-video {
    position: relative;
    width: 100%;
    height: 100%;
    background-color: #05070B;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .ai-reel-ambient-bg {
    position: absolute;
    inset: -20px;
    width: calc(100% + 40px);
    height: calc(100% + 40px);
    object-fit: cover;
    filter: blur(28px) brightness(0.42) saturate(1.4);
    opacity: 0.85;
    pointer-events: none;
    z-index: 1;
    transform: scale(1.08);
  }

  .ai-main-reel-frame {
    position: relative;
    z-index: 2;
    height: 100%;
    aspect-ratio: 9 / 16;
    max-width: 100%;
    background-color: #000000;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 32px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.12);
    transition: all 0.25s ease;
  }

  .ai-main-reel-frame.mode-fill {
    aspect-ratio: unset;
    width: 100%;
  }

  .ai-main-reel-frame video {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    transition: object-fit 0.2s ease;
  }

  .ai-main-reel-frame.mode-fill video {
    object-fit: cover;
  }

  .ai-video-overlay-top {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    z-index: 4;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 12px;
    background: linear-gradient(180deg, rgba(9, 13, 22, 0.9) 0%, rgba(9, 13, 22, 0.45) 60%, transparent 100%);
    pointer-events: none;
  }

  .ai-video-top-left-group {
    display: flex;
    align-items: center;
    gap: 6px;
    pointer-events: auto;
  }

  .ai-video-topic-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background-color: rgba(15, 23, 42, 0.88);
    color: #FFD24A;
    border: 1px solid rgba(255, 210, 74, 0.6);
    border-radius: 999px;
    padding: 3px 9px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 0.52rem;
    letter-spacing: 0.02em;
    backdrop-filter: blur(6px);
  }

  .ai-video-hub-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background-color: rgba(15, 23, 42, 0.88);
    color: #86EFAC;
    border: 1px solid rgba(134, 239, 172, 0.55);
    border-radius: 999px;
    padding: 3px 8px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 0.48rem;
    letter-spacing: 0.02em;
    backdrop-filter: blur(6px);
  }

  .ai-hub-status-dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background-color: #86EFAC;
    box-shadow: 0 0 5px #86EFAC;
  }

  .ai-video-top-right-group {
    display: flex;
    gap: 6px;
    align-items: center;
    pointer-events: auto;
  }

  .ai-video-quality-tag {
    background-color: rgba(15, 23, 42, 0.88);
    color: #86EFAC;
    border-radius: 999px;
    padding: 3px 8px;
    font-size: 0.48rem;
    font-weight: 800;
    border: 1px solid rgba(134, 239, 172, 0.6);
    backdrop-filter: blur(6px);
  }

  .ai-video-mode-toggle-btn {
    background-color: rgba(15, 23, 42, 0.88);
    color: #FAF7F2;
    border-radius: 999px;
    padding: 3px 8px;
    font-size: 0.48rem;
    font-weight: 700;
    border: 1px solid rgba(255, 255, 255, 0.35);
    backdrop-filter: blur(6px);
    cursor: pointer;
    transition: all 0.15s ease;
  }

  .ai-video-mode-toggle-btn:hover {
    background-color: #FF5A36;
    color: #FFFFFF;
    border-color: #FF5A36;
  }

  .ai-video-overlay-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 4;
    padding: 6px 12px 8px 12px;
    background: linear-gradient(0deg, rgba(9, 13, 22, 0.95) 0%, rgba(9, 13, 22, 0.6) 70%, transparent 100%);
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .ai-video-progress-track {
    width: 100%;
    height: 4px;
    background-color: rgba(255, 255, 255, 0.25);
    border-radius: 2px;
    cursor: pointer;
    overflow: hidden;
  }

  .ai-video-progress-fill {
    height: 100%;
    width: 0%;
    background-color: #FF5A36;
    border-radius: 2px;
    transition: width 0.1s linear;
  }

  .ai-video-ctrl-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .ai-video-btn-group {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .ai-video-ctrl-btn {
    background-color: rgba(255, 255, 255, 0.12);
    border: none;
    color: #FAF7F2;
    padding: 3px 7px;
    border-radius: 4px;
    font-size: 0.5rem;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 3px;
    transition: background-color 0.12s ease;
  }

  .ai-video-ctrl-btn:hover {
    background-color: rgba(255, 255, 255, 0.25);
    color: #FFFFFF;
  }

  .ai-video-time {
    font-size: 0.5rem;
    font-weight: 700;
    color: #94A3B8;
    font-variant-numeric: tabular-nums;
  }

  /* Screen 2: AI Doubt Solver Chat */
  .ai-view-mentor-chat {
    height: 100%;
    display: flex;
    flex-direction: column;
    background-color: #0E1524;
    padding: 10px 14px;
    box-sizing: border-box;
    gap: 8px;
  }

  .ai-mentor-profile-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 8px;
    border-bottom: 1px solid #1E293B;
  }

  .ai-mentor-id-group {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .ai-mentor-avatar {
    width: 26px;
    height: 26px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7C3AED, #5458F7);
    color: #FFFFFF;
    display: grid;
    place-items: center;
    font-family: 'Outfit', sans-serif;
    font-weight: 900;
    font-size: 0.62rem;
    border: 1.5px solid #FFFFFF;
    box-shadow: 0 0 8px rgba(124, 58, 237, 0.6);
  }

  .ai-mentor-name {
    font-family: 'Outfit', sans-serif;
    font-size: 0.68rem;
    font-weight: 800;
    color: #FFFFFF;
  }

  .ai-mentor-tag-pill {
    background-color: rgba(134, 239, 172, 0.18);
    color: #86EFAC;
    border: 1px solid rgba(134, 239, 172, 0.5);
    border-radius: 999px;
    padding: 2px 8px;
    font-size: 0.48rem;
    font-weight: 800;
    letter-spacing: 0.02em;
  }

  .ai-chat-thread-container {
    flex: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding-bottom: 4px;
  }

  .ai-chat-bubble {
    padding: 7px 11px;
    border-radius: 8px;
    font-size: 0.58rem;
    line-height: 1.35;
    max-width: 88%;
    box-shadow: 2px 2px 0px rgba(0, 0, 0, 0.3);
  }

  .ai-chat-bubble.student {
    background-color: #FAF7F2;
    color: #0F172A;
    align-self: flex-start;
    border: 1.5px solid #0F172A;
    border-bottom-left-radius: 2px;
  }

  .ai-chat-bubble.mentor {
    background-color: #5458F7;
    color: #FFFFFF;
    align-self: flex-end;
    border: 1.5px solid #0F172A;
    border-bottom-right-radius: 2px;
  }

  .ai-chat-prompt-chips {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    padding-top: 4px;
    border-top: 1px solid #1E293B;
  }

  .ai-prompt-chip-btn {
    background-color: #1E293B;
    color: #FAF7F2;
    border: 1px solid #334155;
    border-radius: 999px;
    padding: 3px 9px;
    font-size: 0.5rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.12s ease;
  }

  .ai-prompt-chip-btn:hover {
    background-color: #FF5A36;
    color: #FFFFFF;
    border-color: #FF5A36;
  }

  /* Screen 3: Revision Notes */
  .ai-view-class-notes {
    height: 100%;
    background-color: #0E1524;
    padding: 12px 14px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .ai-notes-header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 7px;
    border-bottom: 1px solid #1E293B;
  }

  .ai-notes-title {
    font-family: 'Outfit', sans-serif;
    font-size: 0.66rem;
    font-weight: 800;
    color: #FFD24A;
  }

  .ai-notes-badge {
    background-color: rgba(255, 90, 54, 0.22);
    color: #FF8566;
    border: 1px solid rgba(255, 90, 54, 0.5);
    border-radius: 3px;
    padding: 2px 6px;
    font-size: 0.5rem;
    font-weight: 800;
  }

  .ai-notes-formula-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 8px;
    margin-bottom: 8px;
  }

  .ai-formula-card {
    background-color: #172136;
    border: 1px solid #2A3854;
    border-radius: 6px;
    padding: 7px 10px;
  }

  .ai-formula-lbl {
    font-size: 0.5rem;
    font-weight: 700;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .ai-formula-math {
    font-family: 'Outfit', sans-serif;
    font-size: 0.66rem;
    font-weight: 800;
    color: #FFFFFF;
    margin-top: 2px;
  }

  .ai-notes-bullets-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-size: 0.54rem;
    font-weight: 600;
    color: #FAF7F2;
    line-height: 1.35;
    margin: 0;
    padding: 0;
  }

  .ai-notes-bullets-list li::before {
    content: "✓ ";
    color: #86EFAC;
    font-weight: 800;
  }

  .ai-notes-footer-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 8px;
    border-top: 1px solid #1E293B;
  }

  .ai-notes-download-btn {
    background-color: #86EFAC;
    color: #0F172A;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 0.54rem;
    padding: 3.5px 10px;
    border-radius: 4px;
    border: 1px solid #0F172A;
    text-decoration: none;
    cursor: pointer;
  }

  /* 3D Laptop Hardware Deck */
  .ai-laptop-base-svg {
    width: 100%;
    height: auto;
    display: block;
    margin-top: -3px;
    z-index: 3;
    filter: drop-shadow(0px 10px 0px #0F172A);
  }

  /* Built-in Demo Toast */
  .ai-demo-toast {
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%) translateY(100px);
    background-color: #FFD24A;
    color: #0F172A;
    border: 3px solid #0F172A;
    box-shadow: 6px 6px 0px #0F172A;
    border-radius: 999px;
    padding: 10px 22px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: clamp(0.78rem, 0.72rem + 0.3vw, 0.92rem);
    z-index: 9999;
    display: flex;
    align-items: center;
    gap: 8px;
    opacity: 0;
    pointer-events: none;
    transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.25s ease;
  }

  .ai-demo-toast.show {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
    pointer-events: auto;
  }

  @media (max-width: 1040px) {
    .ai-section-grid {
      grid-template-columns: 1fr;
      text-align: center;
    }
    .ai-left-copy {
      align-items: center;
      text-align: center;
    }
    .ai-section-heading {
      align-items: center;
    }
    .ai-subheadline {
      text-align: center;
    }
    .ai-value-points-list {
      align-items: flex-start;
      text-align: start;
    }
    .ai-cta-group {
      align-items: center;
    }
    .ai-cta-row {
      justify-content: center;
    }
    .ai-trust-note {
      justify-content: center;
      text-align: center;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .ai-ext-nav-tab,
    .ai-primary-cta-btn {
      transition: none;
    }
  }
"""

SECTION_HTML = f"""
<!-- ================= 24/7 AI GUIDED LEARNING (MITRA AI TUTOR) SECTION ================= -->
<section id="ai-guided-learning-section" class="ai-guided-learning-section relative overflow-hidden" aria-label="Paathshala 24/7 AI Guided Learning After Class">

  <!-- Top-Left Organic Petal Burst Decorative Graphic -->
  <svg class="ai-corner-burst" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M20 -10 C55 -10, 145 10, 155 38 C165 65, 95 62, 65 55 C115 72, 185 95, 175 125 C165 152, 95 115, 58 92 C92 128, 128 178, 102 192 C78 204, 48 145, 32 105 C35 148, 25 195, 2 192 C-18 188, -5 130, 0 88 L-20 88 L-20 -10 Z"
          fill="#FFD24A" stroke="#0F172A" stroke-width="5" stroke-linejoin="round" />
    <circle cx="26" cy="32" r="14" fill="#FF5A36" stroke="#0F172A" stroke-width="4" />
  </svg>

  <div class="ai-section-container">
    <div class="ai-section-grid">

      <!-- Left Column: Outcome Copy + Mitra AI Value Props + Dual CTA -->
      <div class="ai-left-copy">
        <div class="ai-eyebrow-pill">
          <span class="sparkle" aria-hidden="true">✨</span>
          <span>Free for Paathshala students [confirm]</span>
          <span class="pill-divider" aria-hidden="true">|</span>
          <span>Safe and DPDP compliant</span>
        </div>

        <h2 class="ai-section-heading">
          <span class="ai-heading-hook">Class Moved Too Fast?</span>
          <span class="ai-heading-highlight">Meet Mitra, Your 24/7 AI Tutor</span>
        </h2>

        <p class="ai-subheadline">
          Step-by-step homework help and doubt solving for Classes [6 to 12] in Maths, Science and more. Built for CBSE, ICSE and State Board students.
        </p>

        <ul class="ai-value-points-list" aria-label="Key Mitra AI Guided Learning benefits">
          <li class="ai-value-point-item">
            <span class="ai-point-check-badge" aria-hidden="true">✓</span>
            <span class="ai-point-text"><strong>Homework help at 11 PM:</strong> Stuck on a sum? Mitra explains every step, so you learn the method, not just the answer.</span>
          </li>
          <li class="ai-value-point-item">
            <span class="ai-point-check-badge" aria-hidden="true">✓</span>
            <span class="ai-point-text"><strong>60-second concept reels:</strong> Understand tough chapters and formulas in a minute, not a 1-hour video.</span>
          </li>
          <li class="ai-value-point-item">
            <span class="ai-point-check-badge" aria-hidden="true">✓</span>
            <span class="ai-point-text"><strong>Ask as many times as you need:</strong> Mitra never gets tired of questions, so no doubt is too small.</span>
          </li>
          <li class="ai-value-point-item">
            <span class="ai-point-check-badge" aria-hidden="true">✓</span>
            <span class="ai-point-text"><strong>Revision notes that save themselves:</strong> Chapter summaries and key formulas, ready for exam week.</span>
          </li>
        </ul>

        <div class="ai-cta-group">
          <div class="ai-cta-row">
            <button type="button" class="ai-primary-cta-btn" onclick="handleAiDummyCta(event, 'Ask Mitra Your First Doubt, Free')">
              <span>Ask Mitra Your First Doubt, Free</span>
              <span aria-hidden="true">➔</span>
            </button>
          </div>
          <div class="ai-cta-subnote">
            <span>Sign in with your phone number. No card needed. [confirm]</span>
          </div>
        </div>

        <div class="ai-trust-note">
          <span class="ai-trust-dot" aria-hidden="true"></span>
          <span>CBSE, ICSE and State Boards &nbsp;|&nbsp; No ads profiling children &nbsp;|&nbsp; Real Paathshala teachers when you need one</span>
        </div>
      </div>

      <!-- Right Column: Outer Tabs + Interactive Open Laptop -->
      <div class="ai-right-laptop-col">

        <!-- Outer Tabs Bar -->
        <nav class="ai-laptop-external-nav" role="tablist" aria-label="Explore Mitra AI Features">
          <button type="button" class="ai-ext-nav-tab active" role="tab" id="ai-tab-reel" aria-selected="true" aria-controls="ai-view-reel" data-screen="reel">
            <span class="ai-ext-tab-icon">⚡</span>
            <span>Concept Reels</span>
          </button>
          <button type="button" class="ai-ext-nav-tab" role="tab" id="ai-tab-mentor" aria-selected="false" aria-controls="ai-view-mentor" data-screen="mentor">
            <span class="ai-ext-tab-icon">🤖</span>
            <span>Doubt Solver</span>
          </button>
          <button type="button" class="ai-ext-nav-tab" role="tab" id="ai-tab-notes" aria-selected="false" aria-controls="ai-view-notes" data-screen="notes">
            <span class="ai-ext-tab-icon">📝</span>
            <span>Revision Notes</span>
          </button>
        </nav>

        <div class="ai-laptop-assembly">

          <!-- Open Laptop Lid & Screen Housing -->
          <div class="ai-laptop-lid">
            <div class="ai-laptop-bezel">
              <div class="ai-webcam-notch" aria-hidden="true">
                <span class="ai-webcam-lens"></span>
                <span class="ai-webcam-led"></span>
              </div>

              <div class="ai-laptop-screen">
                <div class="ai-screen-views-wrapper">

                  <!-- 1. Full Detailed Video Screen (Reel) -->
                  <div class="ai-screen-view active" id="ai-view-reel" role="tabpanel" aria-labelledby="ai-tab-reel">
                    <div class="ai-view-full-video">
                      <video id="aiAmbientReelVideo" class="ai-reel-ambient-bg" poster="reel-poster.jpg" autoplay loop muted playsinline aria-hidden="true">
                        <source src="reel.mp4" type="video/mp4">
                        <source src="/images/reel.mp4" type="video/mp4">
                      </video>

                      <div class="ai-main-reel-frame" id="aiMainReelFrame">
                        <video id="aiFullReelVideo" poster="reel-poster.jpg" autoplay loop muted playsinline>
                          <source src="reel.mp4" type="video/mp4">
                          <source src="/images/reel.mp4" type="video/mp4">
                        </video>
                      </div>

                      <div class="ai-video-overlay-top">
                        <div class="ai-video-top-left-group">
                          <div class="ai-video-topic-badge">
                            <span>⚡ 60s Reel:</span>
                            <span>Nuclear Strong Force</span>
                          </div>
                          <div class="ai-video-hub-badge">
                            <span class="ai-hub-status-dot" aria-hidden="true"></span>
                            <span>Today: 3/3 Doubts Cleared</span>
                          </div>
                        </div>
                        <div class="ai-video-top-right-group">
                          <button type="button" class="ai-video-mode-toggle-btn" id="aiVideoModeToggleBtn" title="Toggle between Fit and Fill view">
                            <span id="aiVideoModeText">↔ Fill View</span>
                          </button>
                          <span class="ai-video-quality-tag">HD 1080p</span>
                        </div>
                      </div>

                      <div class="ai-video-overlay-bottom">
                        <div class="ai-video-progress-track" id="aiVideoProgressTrack" title="Seek video position">
                          <div class="ai-video-progress-fill" id="aiVideoProgressFill"></div>
                        </div>
                        <div class="ai-video-ctrl-row">
                          <div class="ai-video-btn-group">
                            <button type="button" class="ai-video-ctrl-btn" id="aiVideoPlayBtn" aria-label="Play or Pause Video">
                              <span id="aiPlayIcon">❚❚</span>
                              <span id="aiPlayText">Pause</span>
                            </button>
                            <button type="button" class="ai-video-ctrl-btn" id="aiVideoMuteBtn" aria-label="Toggle Sound">
                              <span id="aiMuteIcon">🔇</span>
                              <span id="aiMuteText">Unmute</span>
                            </button>
                            <button type="button" class="ai-video-ctrl-btn" id="aiVideoReplayBtn" aria-label="Replay from start">
                              <span>↺ Replay</span>
                            </button>
                          </div>
                          <span class="ai-video-time" id="aiVideoTimeDisplay">0:00 / 0:58</span>
                        </div>
                      </div>

                    </div>
                  </div>

                  <!-- 2. Interactive Doubt Chat Screen (Mitra Doubt Mentor) -->
                  <div class="ai-screen-view" id="ai-view-mentor" role="tabpanel" aria-labelledby="ai-tab-mentor">
                    <div class="ai-view-mentor-chat">
                      <div class="ai-mentor-profile-header">
                        <div class="ai-mentor-id-group">
                          <div class="ai-mentor-avatar">AI</div>
                          <div>
                            <div class="ai-mentor-name">Mitra · AI Doubt Solver</div>
                          </div>
                        </div>
                        <span class="ai-mentor-tag-pill">🛡️ 100% Patient &amp; Friendly</span>
                      </div>

                      <div class="ai-chat-thread-container" id="aiMentorChatStream">
                        <div class="ai-chat-bubble student">
                          "Teacher went fast today: why don't positive protons repel each other in the nucleus?"
                        </div>
                        <div class="ai-chat-bubble mentor">
                          "Hi! I'm Mitra. Don't worry—let's break it down step-by-step: The Strong Nuclear Force is 137x stronger than electric repulsion at subatomic range. It glues them together tight! 💡"
                        </div>
                      </div>

                      <div class="ai-chat-prompt-chips">
                        <button type="button" class="ai-prompt-chip-btn" data-q="neutrons">⚡ Ask Mitra: Why do neutrons matter?</button>
                        <button type="button" class="ai-prompt-chip-btn" data-q="atomic">🔬 Ask Mitra: What if Z &gt; 82?</button>
                        <button type="button" class="ai-prompt-chip-btn" data-q="gravity">🛡️ Ask Mitra: Stronger than gravity?</button>
                      </div>
                    </div>
                  </div>

                  <!-- 3. Revision Notes Screen -->
                  <div class="ai-screen-view" id="ai-view-notes" role="tabpanel" aria-labelledby="ai-tab-notes">
                    <div class="ai-view-class-notes">
                      <div class="ai-notes-header-row">
                        <span class="ai-notes-title">📖 Chapter 4: Nuclei &amp; Strong Forces</span>
                        <span class="ai-notes-badge">✨ Exam-Ready Notes · Class 12</span>
                      </div>

                      <div class="ai-notes-formula-grid">
                        <div class="ai-formula-card">
                          <div class="ai-formula-lbl">Nuclear Radius Formula</div>
                          <div class="ai-formula-math">R = R₀ · A^(1/3)</div>
                        </div>
                        <div class="ai-formula-card">
                          <div class="ai-formula-lbl">Mass-Energy Equivalence</div>
                          <div class="ai-formula-math">E = Δm · c² (931.5 MeV)</div>
                        </div>
                      </div>

                      <ul class="ai-notes-bullets-list">
                        <li><strong>Short-range force:</strong> Operates strictly under ~10⁻¹⁵ m (femtometers).</li>
                        <li><strong>Charge independent:</strong> P-P, P-N, and N-N forces are approximately equal.</li>
                        <li><strong>Saturation property:</strong> Nucleons only interact with immediate neighbors.</li>
                      </ul>

                      <div class="ai-notes-footer-row">
                        <span style="font-size: 0.5rem; color: #94A3B8; font-weight: 600;">Auto-saved to Student Vault</span>
                        <button type="button" class="ai-notes-download-btn" onclick="handleAiDummyCta(event, 'Download Chapter 4 PDF Revision Notes')">
                          📥 Download PDF
                        </button>
                      </div>
                    </div>
                  </div>

                </div>
              </div>

              <div class="ai-bezel-chin">PAATHSHALA STUDIO DISPLAY</div>
            </div>
          </div>

          <!-- Realistic 3D Trapezoidal Open MacBook Pro Base (SVG Hardware Deck) -->
          <svg class="ai-laptop-base-svg" viewBox="0 0 1000 240" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="MacBook Pro Keyboard Deck">
            <defs>
              <linearGradient id="aiHingeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#0F172A" />
                <stop offset="50%" stop-color="#1E293B" />
                <stop offset="100%" stop-color="#0F172A" />
              </linearGradient>
              <linearGradient id="aiTopPlateGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#334155" />
                <stop offset="35%" stop-color="#1E293B" />
                <stop offset="100%" stop-color="#0F172A" />
              </linearGradient>
              <linearGradient id="aiFrontLipGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#64748B" />
                <stop offset="40%" stop-color="#334155" />
                <stop offset="100%" stop-color="#0F172A" />
              </linearGradient>
              <linearGradient id="aiTrackpadGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#1E293B" />
                <stop offset="100%" stop-color="#0F172A" />
              </linearGradient>
            </defs>

            <rect x="90" y="0" width="820" height="8" rx="2" fill="url(#aiHingeGrad)" stroke="#0F172A" stroke-width="2" />
            <polygon points="90,8 910,8 988,198 12,198" fill="url(#aiTopPlateGrad)" stroke="#0F172A" stroke-width="3" stroke-linejoin="round" />
            <polygon points="120,18 880,18 920,118 80,118" fill="#0A0E17" stroke="#0F172A" stroke-width="2" stroke-linejoin="round" />

            <!-- Perspective Keyboard Keys Rows -->
            <g id="aiPerspectiveKeys">
              {KEYS_SVG}
            </g>

            <!-- Centered Glass Trackpad with Thumb Scoop -->
            <polygon points="380,128 620,128 642,188 358,188" fill="url(#aiTrackpadGrad)" stroke="#475569" stroke-width="1.6" stroke-linejoin="round" />
            <path d="M472,198 C472,194 528,194 528,198 Z" fill="#64748B" />

            <!-- Front Aluminum Lip (Beveled Edge) -->
            <polygon points="12,198 988,198 980,214 20,214" fill="url(#aiFrontLipGrad)" stroke="#0F172A" stroke-width="3" stroke-linejoin="round" />
            <polygon points="20,214 980,214 968,222 32,222" fill="#0A0F1D" />
          </svg>

        </div>
      </div>

    </div>
  </div>

</section>

<!-- Floating Demo Toast Notification -->
<div class="ai-demo-toast" id="aiDemoToast" role="alert" aria-live="polite">
  <span style="font-size: 1.1rem;">✨</span>
  <span id="aiDemoToastText">Prototype Demo Action</span>
</div>

<script>
  (function initAiGuidedLearningSection() {{
    // --- External Navigation Tabs ---
    const screenTabs = document.querySelectorAll('.ai-ext-nav-tab');
    const screenViews = document.querySelectorAll('.ai-screen-view');
    const fullVideo = document.getElementById('aiFullReelVideo');
    const ambientVideo = document.getElementById('aiAmbientReelVideo');

    function activateScreen(screenId) {{
      screenTabs.forEach((tab) => {{
        const isTarget = tab.getAttribute('data-screen') === screenId;
        tab.classList.toggle('active', isTarget);
        tab.setAttribute('aria-selected', isTarget ? 'true' : 'false');
      }});

      screenViews.forEach((view) => {{
        const isTarget = view.id === `ai-view-${{screenId}}`;
        view.classList.toggle('active', isTarget);
      }});

      if (screenId === 'reel') {{
        if (fullVideo && fullVideo.paused) fullVideo.play().catch(() => {{}});
        if (ambientVideo && ambientVideo.paused) ambientVideo.play().catch(() => {{}});
      }}
    }}

    screenTabs.forEach((tab) => {{
      tab.addEventListener('click', () => {{
        const screenId = tab.getAttribute('data-screen');
        activateScreen(screenId);
      }});
    }});

    // --- Fit vs Fill Toggle Button ---
    const modeBtn = document.getElementById('aiVideoModeToggleBtn');
    const modeText = document.getElementById('aiVideoModeText');
    const reelFrame = document.getElementById('aiMainReelFrame');
    let isFillMode = false;

    if (modeBtn && reelFrame) {{
      modeBtn.addEventListener('click', () => {{
        isFillMode = !isFillMode;
        reelFrame.classList.toggle('mode-fill', isFillMode);
        if (modeText) {{
          modeText.textContent = isFillMode ? '📐 Fit (9:16)' : '↔ Fill View';
        }}
      }});
    }}

    // --- Full Video Player Controls ---
    const playBtn = document.getElementById('aiVideoPlayBtn');
    const playIcon = document.getElementById('aiPlayIcon');
    const playText = document.getElementById('aiPlayText');
    const muteBtn = document.getElementById('aiVideoMuteBtn');
    const muteIcon = document.getElementById('aiMuteIcon');
    const muteText = document.getElementById('aiMuteText');
    const replayBtn = document.getElementById('aiVideoReplayBtn');
    const progressTrack = document.getElementById('aiVideoProgressTrack');
    const progressFill = document.getElementById('aiVideoProgressFill');
    const timeDisplay = document.getElementById('aiVideoTimeDisplay');

    function formatTime(seconds) {{
      if (isNaN(seconds)) return '0:00';
      const m = Math.floor(seconds / 60);
      const s = Math.floor(seconds % 60);
      return `${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
    }}

    if (fullVideo) {{
      if (ambientVideo) {{
        fullVideo.addEventListener('play', () => ambientVideo.play().catch(() => {{}}));
        fullVideo.addEventListener('pause', () => ambientVideo.pause());
        fullVideo.addEventListener('seeking', () => {{ ambientVideo.currentTime = fullVideo.currentTime; }});
        fullVideo.addEventListener('seeked', () => {{ ambientVideo.currentTime = fullVideo.currentTime; }});
      }}

      function togglePlay() {{
        if (fullVideo.paused) {{
          fullVideo.play().then(() => {{
            if (ambientVideo) ambientVideo.play().catch(() => {{}});
            if (playIcon) playIcon.textContent = '❚❚';
            if (playText) playText.textContent = 'Pause';
          }}).catch(() => {{}});
        }} else {{
          fullVideo.pause();
          if (ambientVideo) ambientVideo.pause();
          if (playIcon) playIcon.textContent = '▶';
          if (playText) playText.textContent = 'Play';
        }}
      }}

      if (playBtn) playBtn.addEventListener('click', togglePlay);

      if (muteBtn) {{
        muteBtn.addEventListener('click', () => {{
          fullVideo.muted = !fullVideo.muted;
          if (ambientVideo) ambientVideo.muted = true;
          if (muteIcon) muteIcon.textContent = fullVideo.muted ? '🔇' : '🔊';
          if (muteText) muteText.textContent = fullVideo.muted ? 'Unmute' : 'Mute';
        }});
      }}

      if (replayBtn) {{
        replayBtn.addEventListener('click', () => {{
          fullVideo.currentTime = 0;
          if (ambientVideo) ambientVideo.currentTime = 0;
          fullVideo.play().then(() => {{
            if (ambientVideo) ambientVideo.play().catch(() => {{}});
            if (playIcon) playIcon.textContent = '❚❚';
            if (playText) playText.textContent = 'Pause';
          }}).catch(() => {{}});
        }});
      }}

      fullVideo.addEventListener('timeupdate', () => {{
        if (fullVideo.duration) {{
          const percent = (fullVideo.currentTime / fullVideo.duration) * 100;
          if (progressFill) progressFill.style.width = `${{percent}}%`;
          if (timeDisplay) {{
            timeDisplay.textContent = `${{formatTime(fullVideo.currentTime)}} / ${{formatTime(fullVideo.duration)}}`;
          }}
        }}
      }});

      if (progressTrack) {{
        progressTrack.addEventListener('click', (e) => {{
          const rect = progressTrack.getBoundingClientRect();
          const clickPos = (e.clientX - rect.left) / rect.width;
          if (fullVideo.duration) {{
            const targetTime = clickPos * fullVideo.duration;
            fullVideo.currentTime = targetTime;
            if (ambientVideo) ambientVideo.currentTime = targetTime;
          }}
        }});
      }}
    }}

    // --- Interactive AI Doubt Chat Prompts ---
    const chatStream = document.getElementById('aiMentorChatStream');
    const chatReplies = {{
      neutrons: {{
        q: "Why do neutrons matter?",
        a: "Neutrons provide strong nuclear attraction without electrical repulsion, acting as the 'nuclear glue' that stabilizes the core! 🧪"
      }},
      atomic: {{
        q: "What if Z > 82?",
        a: "For bismuth and heavier atoms, electrostatic repulsion overpowers the short-range strong force, making the nucleus naturally radioactive! ☢️"
      }},
      gravity: {{
        q: "Stronger than gravity?",
        a: "Infinitely so! The Strong Nuclear Force is 10³⁸ times stronger than gravity at nuclear scale. That's why atomic nuclei never fall apart! 🚀"
      }}
    }};

    document.querySelectorAll('.ai-prompt-chip-btn').forEach((btn) => {{
      btn.addEventListener('click', () => {{
        const qKey = btn.getAttribute('data-q');
        const item = chatReplies[qKey];
        if (!item || !chatStream) return;

        const studentBubble = document.createElement('div');
        studentBubble.className = 'ai-chat-bubble student';
        studentBubble.textContent = `"${{item.q}}"`;
        chatStream.appendChild(studentBubble);
        chatStream.scrollTop = chatStream.scrollHeight;

        setTimeout(() => {{
          const mentorBubble = document.createElement('div');
          mentorBubble.className = 'ai-chat-bubble mentor';
          mentorBubble.textContent = item.a;
          chatStream.appendChild(mentorBubble);
          chatStream.scrollTop = chatStream.scrollHeight;
        }}, 350);
      }});
    }});

    // --- Built-in Dummy Action Toast Handler ---
    window.handleAiDummyCta = function(event, actionName) {{
      if (event) event.preventDefault();
      const toast = document.getElementById('aiDemoToast');
      const toastText = document.getElementById('aiDemoToastText');
      if (toast && toastText) {{
        toastText.textContent = `✨ Demo: "${{actionName}}" triggered (Safe Prototype · Real site untouched)`;
        toast.classList.add('show');
        clearTimeout(window._aiToastTimeout);
        window._aiToastTimeout = setTimeout(() => {{
          toast.classList.remove('show');
        }}, 3200);
      }}
    }};
  }})();
</script>
"""

# 1. Generate standalone component homepage-section.html
STANDALONE_PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>Paathshala · 24/7 AI Guided Learning Section (Under Hero & Carousel)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{
    --font-display: 'Outfit', system-ui, -apple-system, sans-serif;
    --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    background-color: #FFFFFF;
    background-image: radial-gradient(rgba(15, 23, 42, 0.12) 1.5px, transparent 1.5px);
    background-size: 24px 24px;
    font-family: var(--font-sans);
    color: #0F172A;
    line-height: 1.4;
    overflow-x: hidden;
  }}

  /* Mock Header to show in-context section placement */
  .mock-page-header {{
    background: #FFFFFF;
    border-bottom: 2px solid #0F172A;
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1280px;
    margin: 0 auto;
  }}
  .mock-logo {{
    font-family: 'Outfit', sans-serif;
    font-weight: 900;
    font-size: 1.25rem;
  }}
  .mock-badge {{
    background: #FEF08A;
    border: 2px solid #0F172A;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 800;
  }}

  /* Mock Hero Section with Carousel Placeholder */
  .mock-hero-section {{
    padding: 3rem 1.5rem 2.5rem;
    text-align: center;
    max-width: 1280px;
    margin: 0 auto;
  }}
  .mock-hero-badge {{
    display: inline-flex;
    padding: 6px 16px;
    border-radius: 999px;
    background: #FEF08A;
    border: 2px solid #0F172A;
    font-size: 0.8rem;
    font-weight: 800;
    margin-bottom: 1.2rem;
    box-shadow: 2px 2px 0px #0F172A;
  }}
  .mock-hero-title {{
    font-family: 'Outfit', sans-serif;
    font-size: clamp(2rem, 4vw, 3.5rem);
    font-weight: 900;
    color: #0F172A;
    line-height: 1.15;
    margin-bottom: 1rem;
  }}
  .mock-hero-sub {{
    font-size: 1.1rem;
    color: #475569;
    font-weight: 600;
    max-width: 600px;
    margin: 0 auto 2rem;
  }}

  /* Mock Carousel Stage */
  .mock-carousel-stage {{
    background: #FAF7F2;
    border: 3px solid #0F172A;
    border-radius: 24px;
    box-shadow: 6px 6px 0px #0F172A;
    padding: 2rem 1.5rem;
    margin: 1.5rem auto 3rem;
    max-width: 960px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }}
  .mock-carousel-cards {{
    display: flex;
    gap: 1.25rem;
    overflow-x: auto;
    width: 100%;
    padding: 0.5rem;
    justify-content: center;
  }}
  .mock-card {{
    background: #FFFFFF;
    border: 2.5px solid #0F172A;
    border-radius: 16px;
    box-shadow: 3px 3px 0px #0F172A;
    padding: 1rem 1.25rem;
    min-width: 160px;
    text-align: center;
    font-weight: 800;
    font-size: 0.9rem;
  }}
  .mock-card .stars {{
    color: #E76F51;
    font-size: 0.8rem;
    margin-top: 4px;
  }}

  {SECTION_CSS}
</style>
</head>
<body>

  <!-- Mock Header -->
  <header class="mock-page-header">
    <div class="mock-logo">Paathshala<span style="color: #5458F7;">.</span></div>
    <div class="mock-badge">Live Page Context Demo</div>
  </header>

  <!-- 1. HERO SECTION (CONTAINING THE CAROUSEL) -->
  <section class="mock-hero-section">
    <div class="mock-hero-badge">🚆 AAMCHI MUMBAI | SKIP THE 6 PM TUITION RUSH</div>
    <h1 class="mock-hero-title">Top 1-on-1 Tutors for Mumbai's Bright Minds.</h1>
    <p class="mock-hero-sub">Learn live 1-on-1 with India's top 1% dedicated educators. Personalized for ICSE, CBSE, and IB boards.</p>

    <!-- Teacher Carousel Stage (Directly Above Our AI Section) -->
    <div class="mock-carousel-stage">
      <div style="font-weight: 900; font-size: 0.85rem; letter-spacing: 0.05em; color: #E76F51;">
        ✨ 1-ON-1 VERIFIED FACULTY CAROUSEL
      </div>
      <div class="mock-carousel-cards">
        <div class="mock-card">
          <div style="font-size: 2rem;">👩‍🏫</div>
          <div>Shivani</div>
          <div style="font-size: 0.75rem; color: #64748B;">ICSE & CBSE · 5+ Yrs</div>
          <div class="stars">⭐ 4.98</div>
        </div>
        <div class="mock-card" style="border-color: #5458F7; transform: scale(1.05);">
          <div style="font-size: 2rem;">🧪</div>
          <div>Soumi Sarkar</div>
          <div style="font-size: 0.75rem; color: #64748B;">Chemistry UGC NET</div>
          <div class="stars">⭐ 5.0</div>
        </div>
        <div class="mock-card">
          <div style="font-size: 2rem;">📐</div>
          <div>Mansi</div>
          <div style="font-size: 0.75rem; color: #64748B;">Mathematics Specialist</div>
          <div class="stars">⭐ 4.95</div>
        </div>
      </div>
      <div style="font-size: 0.75rem; color: #64748B; font-weight: 700;">
        (Carousel ends here — new section directly underneath ↓)
      </div>
    </div>
  </section>

  <!-- 2. NEW NATIVE SECTION: 24/7 AI GUIDED LEARNING (DIRECTLY UNDER HERO & BELOW CAROUSEL) -->
  {SECTION_HTML}

  <!-- Mock Subsequent Section (e.g., Why 1-on-1 / School Marquee) -->
  <section style="padding: 4rem 1.5rem; text-align: center; max-width: 960px; margin: 0 auto;">
    <span style="display: inline-block; padding: 4px 12px; border-radius: 999px; background: #E0E7FF; border: 2px solid #0F172A; font-size: 0.75rem; font-weight: 800; color: #4338CA; margin-bottom: 0.8rem;">
      THE MUMBAI ADVANTAGE
    </span>
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 2.2rem; font-weight: 900; margin-bottom: 1rem;">
      Why Smart Parents in Mumbai Choose 1-on-1 Paathshala
    </h2>
    <p style="color: #64748B; font-weight: 600;">
      No more hours lost in Western Express Highway or local train traffic. Just uninterrupted focused learning at home.
    </p>
  </section>

</body>
</html>
"""

def main():
    guided_learning_dir = Path("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning")
    website_dir = Path("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-website")

    # 1. Write standalone demonstration in paathshala-guided-learning
    homepage_section_path = guided_learning_dir / "homepage-section.html"
    homepage_section_path.write_text(STANDALONE_PAGE, encoding="utf-8")
    print(f"✓ Updated {homepage_section_path}")

    full_preview_path = guided_learning_dir / "landing-with-ai-section.html"
    full_preview_path.write_text(STANDALONE_PAGE, encoding="utf-8")
    print(f"✓ Generated {full_preview_path}")

    # 2. Integrate directly into paathshala-website location landing pages
    location_pages = [
        "locations-mumbai.html",
        "locations-bangalore.html",
        "locations-delhi-ncr.html",
    ]

    for page_name in location_pages:
        target_path = website_dir / f"src/main/resources/static/{page_name}"
        if target_path.exists():
            content = target_path.read_text(encoding="utf-8")

            # If section is already present, update its markup
            if "ai-guided-learning-section" in content:
                sec_pattern = r'<!-- ================= 24/7 AI GUIDED LEARNING[\s\S]*?<\/script>'
                content = re.sub(sec_pattern, SECTION_HTML, content, count=1)
                target_path.write_text(content, encoding="utf-8")
                print(f"✓ Updated existing AI section in {page_name}")
            else:
                # Inject CSS before </head>
                style_injection = f"\n<style>\n{SECTION_CSS}\n</style>\n</head>"
                content = content.replace("</head>", style_injection, 1)

                # Locate the end of the hero section: </section>
                hero_close_pattern = r'(<section id="hero-section"[\s\S]*?</section>)'
                match = re.search(hero_close_pattern, content)
                if match:
                    hero_section_block = match.group(1)
                    replacement = f"{hero_section_block}\n\n{SECTION_HTML}\n"
                    content = content.replace(hero_section_block, replacement, 1)
                    target_path.write_text(content, encoding="utf-8")
                    print(f"✓ Successfully inserted AI Guided Learning section directly below Hero Carousel in {target_path}")
                else:
                    print(f"⚠ Could not find #hero-section block in {page_name}")

if __name__ == "__main__":
    main()
