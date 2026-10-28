#!/usr/bin/env python3
"""Updates the Laptop Showcase Banner with high-converting, sellable copy:
1. Headline reframed from negative ("Too shy") to empathetic & outcome-driven:
   - "Class Moved Too Fast?"
   - "Master It Tonight"
   - "With Your 24/7 AI Tutor!"
2. Bullet points focused on tangible outcomes for parents (better grades, homework clarity, exam confidence)
   and students (zero embarrassment, 60s visual reels, instant step-by-step solutions).
3. Safe dummy links with interactive demo toast.
"""

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

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>Paathshala · 24/7 AI Guided Learning After Class (Prototype)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  @layer reset, tokens, layout, components, utilities;

  @layer tokens {{
    :root {{
      --violet: #5458F7;
      --orange: #FF5A36;
      --yellow: #FFD24A;
      --mint: #86EFAC;
      --cream: #FAF7F2;
      --white: #FFFFFF;
      --ink: #0F172A;
      --slate-dark: #1E293B;
      --font-display: 'Outfit', system-ui, -apple-system, sans-serif;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    }}
  }}

  @layer reset {{
    :where(html, body, div, section, header, footer, main, nav, h1, h2, h3, h4, p, span, a, button, ul, li, figure, video, svg) {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
  }}

  @layer layout {{
    html, body {{
      min-block-size: 100%;
      background-color: var(--ink);
      font-family: var(--font-sans);
      color: var(--ink);
      line-height: 1.4;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      display: flex;
      align-items: center;
      justify-content: center;
      padding: clamp(0.75rem, 2vw, 1.5rem);
      min-height: 100vh;
    }}

    /* Wide Horizontal Ad / Hero Banner Canvas */
    .banner-canvas {{
      position: relative;
      inline-size: 100%;
      max-inline-size: 1280px;
      min-block-size: 540px;
      background-color: var(--violet);
      background-image: radial-gradient(rgba(255, 255, 255, 0.22) 1.5px, transparent 1.5px);
      background-size: 24px 24px;
      border: 3.5px solid var(--ink);
      border-radius: 26px;
      box-shadow: 12px 12px 0px var(--ink);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      isolation: isolate;
    }}

    /* Horizontal 2-Column Main Grid */
    .banner-body {{
      position: relative;
      z-index: 3;
      display: grid;
      grid-template-columns: 0.88fr 1.32fr;
      align-items: center;
      gap: clamp(1.2rem, 2.5vw, 2.5rem);
      padding: clamp(2rem, 3vw, 2.75rem) clamp(2rem, 3.2vw, 3rem);
      flex: 1;
    }}
  }}

  @layer components {{
    /* 1. Top-Left Organic Burst Petal Graphic */
    .corner-burst {{
      position: absolute;
      inset-block-start: -38px;
      inset-inline-start: -38px;
      inline-size: clamp(115px, 12vw, 150px);
      block-size: clamp(115px, 12vw, 150px);
      z-index: 2;
      pointer-events: none;
      filter: drop-shadow(5px 5px 0px var(--ink));
    }}

    /* 2. Left Column: 3-Tier Stacked Headline + Subcopy + CTA */
    .left-copy-col {{
      position: relative;
      z-index: 4;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: start;
      padding-inline-start: clamp(0.5rem, 1.5vw, 1.25rem);
      padding-block-end: 1rem;
    }}

    /* Prominent Sellable Eyebrow Pill */
    .ai-eyebrow-pill {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background-color: var(--cream);
      color: var(--ink);
      border: 2.5px solid var(--ink);
      border-radius: 999px;
      padding: 5px 14px;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(0.66rem, 0.6rem + 0.25vw, 0.76rem);
      letter-spacing: 0.02em;
      box-shadow: 3.5px 3.5px 0px var(--ink);
      margin-block-end: 0.85rem;
    }}

    .ai-eyebrow-pill .sparkle {{
      color: #7C3AED;
      font-size: 0.95rem;
      line-height: 1;
    }}

    .ai-eyebrow-pill .pill-divider {{
      color: #94A3B8;
      font-weight: 400;
      opacity: 0.7;
    }}

    /* Single H1 Heading (Unified) */
    .single-h1-heading {{
      font-family: var(--font-display);
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
    }}

    .h1-hook {{
      color: var(--white);
      text-shadow: 3px 3px 0px var(--ink);
      display: block;
    }}

    .h1-badge-highlight {{
      display: inline-block;
      background-color: var(--yellow);
      color: var(--ink);
      font-family: var(--font-display);
      font-weight: 900;
      font-size: clamp(1.8rem, 1.15rem + 1.8vw, 2.7rem);
      line-height: 1.05;
      letter-spacing: -0.035em;
      padding: 0.14em 0.44em 0.18em;
      border: 3.5px solid var(--ink);
      box-shadow: 6px 6px 0px var(--ink);
      transform: rotate(-1.2deg);
      margin-block-start: 0.15rem;
    }}

    /* Subheadline */
    .banner-subheadline {{
      margin-block-start: 0.9rem;
      font-size: clamp(0.86rem, 0.78rem + 0.22vw, 0.96rem);
      line-height: 1.45;
      color: var(--cream);
      font-weight: 600;
      max-inline-size: 46ch;
    }}

    .value-points-list {{
      list-style: none;
      margin-block-start: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.52rem;
      max-inline-size: 48ch;
    }}

    .value-point-item {{
      display: flex;
      align-items: flex-start;
      gap: 0.65rem;
      font-size: clamp(0.8rem, 0.72rem + 0.2vw, 0.88rem);
      line-height: 1.35;
      color: var(--cream);
      font-weight: 500;
    }}

    .point-check-badge {{
      inline-size: 20px;
      block-size: 20px;
      border-radius: 50%;
      background-color: var(--mint);
      color: var(--ink);
      border: 2px solid var(--ink);
      box-shadow: 2px 2px 0px var(--ink);
      display: inline-grid;
      place-items: center;
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 0.68rem;
      flex-shrink: 0;
      margin-top: 1px;
    }}

    .point-text strong {{
      color: var(--yellow);
      font-weight: 800;
    }}

    .left-cta-group {{
      margin-block-start: 1.15rem;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      align-items: flex-start;
    }}

    .left-cta-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.85rem;
    }}

    .primary-cta-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      background-color: var(--orange);
      color: var(--white);
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(0.92rem, 0.82rem + 0.32vw, 1.05rem);
      padding: 0.75rem 1.5rem;
      border: 3px solid var(--ink);
      border-radius: 12px;
      box-shadow: 5px 5px 0px var(--ink);
      text-decoration: none;
      cursor: pointer;
      transition: transform 0.12s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.12s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .primary-cta-btn:hover {{
      transform: translate(-2px, -2px);
      box-shadow: 7px 7px 0px var(--ink);
      background-color: #FF6B4A;
    }}

    .primary-cta-btn:active {{
      transform: translate(2px, 2px);
      box-shadow: 2px 2px 0px var(--ink);
    }}

    .cta-secondary-note {{
      font-size: 0.74rem;
      font-weight: 600;
      color: rgba(250, 247, 242, 0.88);
      letter-spacing: 0.01em;
    }}

    .trust-micro-note {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      margin-block-start: 0.85rem;
      font-size: 0.72rem;
      font-weight: 700;
      color: rgba(250, 247, 242, 0.88);
      letter-spacing: 0.01em;
      line-height: 1.35;
      max-inline-size: 52ch;
    }}

    .trust-micro-dot {{
      inline-size: 7px;
      block-size: 7px;
      border-radius: 50%;
      background-color: var(--mint);
      border: 1.5px solid var(--ink);
      flex-shrink: 0;
    }}

    .trust-micro-domain {{
      color: var(--yellow);
      text-decoration: underline;
      text-decoration-thickness: 1.5px;
      cursor: pointer;
    }}

    /* 3. Right Column: External Navigation Tabs + Laptop */
    .right-laptop-col {{
      position: relative;
      z-index: 3;
      display: flex;
      flex-direction: column;
      align-items: center;
      inline-size: 100%;
    }}

    /* Outer Navigation Tabs outside the laptop */
    .laptop-external-nav {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      gap: 8px;
      margin-block-end: 14px;
      inline-size: 100%;
      z-index: 5;
    }}

    .ext-nav-tab {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--cream);
      color: var(--ink);
      border: 2.5px solid var(--ink);
      border-radius: 999px;
      padding: 6px 14px;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(0.72rem, 0.68rem + 0.2vw, 0.82rem);
      cursor: pointer;
      box-shadow: 3.5px 3.5px 0px var(--ink);
      transition: transform 0.12s ease, box-shadow 0.12s ease, background-color 0.12s ease;
      user-select: none;
    }}

    .ext-nav-tab:hover {{
      transform: translate(-1.5px, -1.5px);
      box-shadow: 5px 5px 0px var(--ink);
      background-color: #FFFFFF;
    }}

    .ext-nav-tab.active {{
      background-color: var(--yellow);
      border-color: var(--ink);
      box-shadow: 4px 4px 0px var(--ink);
      transform: translate(-1px, -1px);
    }}

    .ext-tab-icon {{
      font-size: 0.92rem;
      line-height: 1;
    }}

    /* Laptop Device Canvas Assembly */
    .laptop-assembly {{
      position: relative;
      inline-size: 100%;
      max-inline-size: 640px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    /* Lid & Screen Housing (82% width matching base hinge) */
    .laptop-lid {{
      position: relative;
      inline-size: 82%;
      z-index: 2;
    }}

    .laptop-bezel {{
      position: relative;
      background-color: #0F172A;
      border: 3.5px solid #0F172A;
      border-radius: 12px 12px 0 0;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45), inset 0 0 0 1.5px rgba(255, 255, 255, 0.1);
      padding: 8px 9px 15px 9px;
      overflow: hidden;
    }}

    .webcam-notch {{
      position: absolute;
      inset-block-start: 2px;
      inset-inline-start: 50%;
      transform: translateX(-50%);
      inline-size: 28px;
      block-size: 4px;
      background-color: #000000;
      border-radius: 0 0 3px 3px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 3px;
      z-index: 10;
    }}

    .webcam-lens {{
      inline-size: 2.5px;
      block-size: 2.5px;
      border-radius: 50%;
      background-color: #1E293B;
    }}

    .webcam-led {{
      inline-size: 1.5px;
      block-size: 1.5px;
      border-radius: 50%;
      background-color: var(--mint);
    }}

    .bezel-chin {{
      position: absolute;
      inset-block-end: 2px;
      inset-inline-start: 50%;
      transform: translateX(-50%);
      font-family: var(--font-display);
      font-size: 0.48rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      color: rgba(255, 255, 255, 0.28);
      pointer-events: none;
    }}

    /* Laptop Screen (16:10 ratio) */
    .laptop-screen {{
      position: relative;
      inline-size: 100%;
      aspect-ratio: 16 / 10;
      background-color: #090D16;
      border-radius: 6px;
      overflow: hidden;
      box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.08);
    }}

    /* Screen Views Container */
    .screen-views-wrapper {{
      position: relative;
      inline-size: 100%;
      block-size: 100%;
    }}

    .screen-view {{
      position: absolute;
      inset: 0;
      inline-size: 100%;
      block-size: 100%;
      opacity: 0;
      pointer-events: none;
      visibility: hidden;
      transition: opacity 0.22s ease;
    }}

    .screen-view.active {{
      opacity: 1;
      pointer-events: auto;
      visibility: visible;
      z-index: 2;
    }}

    /* --- Screen 1: Full Video Player Screen (Reel) --- */
    .view-full-video {{
      position: relative;
      inline-size: 100%;
      block-size: 100%;
      background-color: #05070B;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    /* Ambient blurred video background */
    .reel-ambient-bg {{
      position: absolute;
      inset: -20px;
      inline-size: calc(100% + 40px);
      block-size: calc(100% + 40px);
      object-fit: cover;
      filter: blur(28px) brightness(0.42) saturate(1.4);
      opacity: 0.85;
      pointer-events: none;
      z-index: 1;
      transform: scale(1.08);
    }}

    /* Centered Reel Frame (9:16 default, full dimensions) */
    .main-reel-frame {{
      position: relative;
      z-index: 2;
      block-size: 100%;
      aspect-ratio: 9 / 16;
      max-inline-size: 100%;
      background-color: #000000;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 32px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.12);
      transition: all 0.25s ease;
    }}

    /* When Fill mode is toggled */
    .main-reel-frame.mode-fill {{
      aspect-ratio: unset;
      inline-size: 100%;
    }}

    .main-reel-frame video {{
      inline-size: 100%;
      block-size: 100%;
      object-fit: contain;
      display: block;
      transition: object-fit 0.2s ease;
    }}

    .main-reel-frame.mode-fill video {{
      object-fit: cover;
    }}

    /* Floating Top Tag Overlay */
    .video-overlay-top {{
      position: absolute;
      inset-block-start: 0;
      inset-inline: 0;
      z-index: 4;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 12px;
      background: linear-gradient(180deg, rgba(9, 13, 22, 0.9) 0%, rgba(9, 13, 22, 0.45) 60%, transparent 100%);
      pointer-events: none;
    }}

    .video-top-left-group {{
      display: flex;
      align-items: center;
      gap: 6px;
      pointer-events: auto;
    }}

    .video-topic-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background-color: rgba(15, 23, 42, 0.88);
      color: var(--yellow);
      border: 1px solid rgba(255, 210, 74, 0.6);
      border-radius: 999px;
      padding: 3px 9px;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 0.52rem;
      letter-spacing: 0.02em;
      backdrop-filter: blur(6px);
    }}

    .video-hub-badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background-color: rgba(15, 23, 42, 0.88);
      color: var(--mint);
      border: 1px solid rgba(134, 239, 172, 0.55);
      border-radius: 999px;
      padding: 3px 8px;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 0.48rem;
      letter-spacing: 0.02em;
      backdrop-filter: blur(6px);
    }}

    .hub-status-dot {{
      inline-size: 5px;
      block-size: 5px;
      border-radius: 50%;
      background-color: var(--mint);
      box-shadow: 0 0 5px var(--mint);
    }}

    .video-top-right-group {{
      display: flex;
      gap: 6px;
      align-items: center;
      pointer-events: auto;
    }}

    .video-quality-tag {{
      background-color: rgba(15, 23, 42, 0.88);
      color: var(--mint);
      border-radius: 999px;
      padding: 3px 8px;
      font-size: 0.48rem;
      font-weight: 800;
      border: 1px solid rgba(134, 239, 172, 0.6);
      backdrop-filter: blur(6px);
    }}

    .video-mode-toggle-btn {{
      background-color: rgba(15, 23, 42, 0.88);
      color: var(--cream);
      border-radius: 999px;
      padding: 3px 8px;
      font-size: 0.48rem;
      font-weight: 700;
      border: 1px solid rgba(255, 255, 255, 0.35);
      backdrop-filter: blur(6px);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .video-mode-toggle-btn:hover {{
      background-color: var(--orange);
      color: var(--white);
      border-color: var(--orange);
    }}

    /* Floating Bottom Video Controls Bar Overlay */
    .video-overlay-bottom {{
      position: absolute;
      inset-block-end: 0;
      inset-inline: 0;
      z-index: 4;
      padding: 6px 12px 8px 12px;
      background: linear-gradient(0deg, rgba(9, 13, 22, 0.95) 0%, rgba(9, 13, 22, 0.6) 70%, transparent 100%);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .video-progress-track {{
      inline-size: 100%;
      block-size: 4px;
      background-color: rgba(255, 255, 255, 0.25);
      border-radius: 2px;
      cursor: pointer;
      overflow: hidden;
    }}

    .video-progress-fill {{
      block-size: 100%;
      inline-size: 28%;
      background-color: var(--orange);
      border-radius: 2px;
      transition: inline-size 0.1s linear;
    }}

    .video-ctrl-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .video-btn-group {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .video-ctrl-btn {{
      background-color: rgba(255, 255, 255, 0.12);
      border: none;
      color: var(--cream);
      padding: 3px 7px;
      border-radius: 4px;
      font-size: 0.5rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 3px;
      transition: background-color 0.12s ease;
    }}

    .video-ctrl-btn:hover {{
      background-color: rgba(255, 255, 255, 0.25);
      color: var(--white);
    }}

    .video-time {{
      font-size: 0.5rem;
      font-weight: 700;
      color: #94A3B8;
      font-variant-numeric: tabular-nums;
    }}

    /* --- Screen 2: Interactive Doubt Chat Screen (AI Doubt Mentor) --- */
    .view-mentor-chat {{
      block-size: 100%;
      display: flex;
      flex-direction: column;
      background-color: #0E1524;
      padding: 10px 14px;
      box-sizing: border-box;
      gap: 8px;
    }}

    .mentor-profile-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-block-end: 8px;
      border-block-end: 1px solid #1E293B;
    }}

    .mentor-id-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .mentor-avatar {{
      inline-size: 26px;
      block-size: 26px;
      border-radius: 50%;
      background: linear-gradient(135deg, #7C3AED, #5458F7);
      color: var(--white);
      display: grid;
      place-items: center;
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 0.62rem;
      border: 1.5px solid var(--white);
      box-shadow: 0 0 8px rgba(124, 58, 237, 0.6);
    }}

    .mentor-name {{
      font-family: var(--font-display);
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--white);
    }}

    .mentor-tag-pill {{
      background-color: rgba(134, 239, 172, 0.18);
      color: var(--mint);
      border: 1px solid rgba(134, 239, 172, 0.5);
      border-radius: 999px;
      padding: 2px 8px;
      font-size: 0.48rem;
      font-weight: 800;
      letter-spacing: 0.02em;
    }}

    .chat-thread-container {{
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding-block-end: 4px;
    }}

    .chat-bubble {{
      padding: 7px 11px;
      border-radius: 8px;
      font-size: 0.58rem;
      line-height: 1.35;
      max-inline-size: 88%;
      box-shadow: 2px 2px 0px rgba(0, 0, 0, 0.3);
    }}

    .chat-bubble.student {{
      background-color: var(--cream);
      color: var(--ink);
      align-self: flex-start;
      border: 1.5px solid var(--ink);
      border-bottom-left-radius: 2px;
    }}

    .chat-bubble.mentor {{
      background-color: #5458F7;
      color: var(--white);
      align-self: flex-end;
      border: 1.5px solid var(--ink);
      border-bottom-right-radius: 2px;
    }}

    .chat-prompt-chips {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      padding-block-start: 4px;
      border-block-start: 1px solid #1E293B;
    }}

    .prompt-chip-btn {{
      background-color: #1E293B;
      color: var(--cream);
      border: 1px solid #334155;
      border-radius: 999px;
      padding: 3px 9px;
      font-size: 0.5rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.12s ease;
    }}

    .prompt-chip-btn:hover {{
      background-color: var(--orange);
      color: var(--white);
      border-color: var(--orange);
    }}

    /* --- Screen 3: Important Revision Notes Screen (AI Notes) --- */
    .view-class-notes {{
      block-size: 100%;
      background-color: #0E1524;
      padding: 12px 14px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .notes-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-block-end: 7px;
      border-block-end: 1px solid #1E293B;
    }}

    .notes-title {{
      font-family: var(--font-display);
      font-size: 0.66rem;
      font-weight: 800;
      color: var(--yellow);
    }}

    .notes-badge {{
      background-color: rgba(255, 90, 54, 0.22);
      color: #FF8566;
      border: 1px solid rgba(255, 90, 54, 0.5);
      border-radius: 3px;
      padding: 2px 6px;
      font-size: 0.5rem;
      font-weight: 800;
    }}

    .notes-formula-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-block: 8px;
    }}

    .formula-card {{
      background-color: #172136;
      border: 1px solid #2A3854;
      border-radius: 6px;
      padding: 7px 10px;
    }}

    .formula-lbl {{
      font-size: 0.5rem;
      font-weight: 700;
      color: #94A3B8;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .formula-math {{
      font-family: var(--font-display);
      font-size: 0.66rem;
      font-weight: 800;
      color: var(--white);
      margin-block-start: 2px;
    }}

    .notes-bullets-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 0.54rem;
      font-weight: 600;
      color: var(--cream);
      line-height: 1.35;
    }}

    .notes-bullets-list li::before {{
      content: "✓ ";
      color: var(--mint);
      font-weight: 800;
    }}

    .notes-footer-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-block-start: 8px;
      border-block-start: 1px solid #1E293B;
    }}

    .notes-download-btn {{
      background-color: var(--mint);
      color: var(--ink);
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 0.54rem;
      padding: 3.5px 10px;
      border-radius: 4px;
      border: 1px solid var(--ink);
      text-decoration: none;
      cursor: pointer;
    }}

    /* True 3D Trapezoidal Open MacBook Pro Base (SVG Hardware Deck) */
    .laptop-base-svg {{
      inline-size: 100%;
      block-size: auto;
      display: block;
      margin-block-start: -3px;
      z-index: 3;
      filter: drop-shadow(0px 10px 0px var(--ink));
    }}

    /* Built-in Interactive Demo Toast Notification */
    .demo-toast {{
      position: fixed;
      inset-block-end: 24px;
      inset-inline-start: 50%;
      transform: translateX(-50%) translateY(100px);
      background-color: var(--yellow);
      color: var(--ink);
      border: 3px solid var(--ink);
      box-shadow: 6px 6px 0px var(--ink);
      border-radius: 999px;
      padding: 10px 22px;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(0.78rem, 0.72rem + 0.3vw, 0.92rem);
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 8px;
      opacity: 0;
      pointer-events: none;
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.25s ease;
    }}

    .demo-toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
      pointer-events: auto;
    }}
  }}

  @layer utilities {{
    @media (max-width: 1040px) {{
      .banner-body {{
        grid-template-columns: 1fr;
        text-align: center;
        padding-block-start: 2.5rem;
      }}
      .left-copy-col {{
        align-items: center;
        text-align: center;
        padding-inline-start: 0;
      }}
      .single-h1-heading {{
        align-items: center;
      }}
      .banner-subheadline {{
        text-align: center;
      }}
      .value-points-list {{
        align-items: flex-start;
        text-align: start;
      }}
      .left-cta-group {{
        align-items: center;
      }}
      .left-cta-row {{
        justify-content: center;
      }}
      .trust-micro-note {{
        justify-content: center;
        text-align: center;
      }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      .ext-nav-tab,
      .screen-circle-cta,
      .primary-cta-btn {{
        transition: none;
      }}
    }}
  }}
</style>
</head>
<body>

<section class="banner-canvas" aria-label="Paathshala 24/7 AI Guided Learning After Class Horizontal Banner">

  <!-- 1. Top-Left Organic Petal Burst -->
  <svg class="corner-burst" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M20 -10 C55 -10, 145 10, 155 38 C165 65, 95 62, 65 55 C115 72, 185 95, 175 125 C165 152, 95 115, 58 92 C92 128, 128 178, 102 192 C78 204, 48 145, 32 105 C35 148, 25 195, 2 192 C-18 188, -5 130, 0 88 L-20 88 L-20 -10 Z"
          fill="#FFD24A" stroke="#0F172A" stroke-width="5" stroke-linejoin="round" />
    <circle cx="26" cy="32" r="14" fill="#FF5A36" stroke="#0F172A" stroke-width="4" />
  </svg>

  <!-- Horizontal 2-Column Main Stage -->
  <div class="banner-body">

    <!-- Left Column: Outcome-Driven Headline + Mitra AI Subcopy + Bullets + Dual CTA -->
    <header class="left-copy-col">
      <div class="ai-eyebrow-pill">
        <span class="sparkle" aria-hidden="true">✨</span>
        <span>Free for Paathshala students [confirm]</span>
        <span class="pill-divider" aria-hidden="true">|</span>
        <span>Safe and DPDP compliant</span>
      </div>

      <h1 class="single-h1-heading">
        <span class="h1-hook">Class Moved Too Fast?</span>
        <span class="h1-badge-highlight">Meet Mitra, Your 24/7 AI Tutor</span>
      </h1>

      <p class="banner-subheadline">
        Step-by-step homework help and doubt solving for Classes [6 to 12] in Maths, Science and more. Built for CBSE, ICSE and State Board students.
      </p>

      <ul class="value-points-list" aria-label="Key Mitra AI Guided Learning benefits">
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>Homework help at 11 PM:</strong> Stuck on a sum? Mitra explains every step, so you learn the method, not just the answer.</span>
        </li>
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>60-second concept reels:</strong> Understand tough chapters and formulas in a minute, not a 1-hour video.</span>
        </li>
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>Ask as many times as you need:</strong> Mitra never gets tired of questions, so no doubt is too small.</span>
        </li>
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>Revision notes that save themselves:</strong> Chapter summaries and key formulas, ready for exam week.</span>
        </li>
      </ul>

      <div class="left-cta-group">
        <div class="left-cta-row">
          <button type="button" class="primary-cta-btn" onclick="handleDummyCta(event, 'Ask Mitra Your First Doubt, Free')">
            <span>Ask Mitra Your First Doubt, Free</span>
            <span aria-hidden="true">➔</span>
          </button>
        </div>
        <div class="cta-secondary-note">
          <span>Sign in with your phone number. No card needed. [confirm]</span>
        </div>
      </div>

      <div class="trust-micro-note">
        <span class="trust-micro-dot" aria-hidden="true"></span>
        <span>CBSE, ICSE and State Boards &nbsp;|&nbsp; No ads profiling children &nbsp;|&nbsp; Real Paathshala teachers when you need one</span>
      </div>
    </header>

    <!-- Right Column: Realistic Open Laptop Showcase + Clean Outer Tabs -->
    <div class="right-laptop-col">

      <!-- Prominent External Navigation Bar Outside the Laptop -->
      <nav class="laptop-external-nav" role="tablist" aria-label="Explore Mitra AI Features">
        <button type="button" class="ext-nav-tab active" role="tab" id="tab-reel" aria-selected="true" aria-controls="view-reel" data-screen="reel">
          <span class="ext-tab-icon">⚡</span>
          <span>Concept Reels</span>
        </button>
        <button type="button" class="ext-nav-tab" role="tab" id="tab-mentor" aria-selected="false" aria-controls="view-mentor" data-screen="mentor">
          <span class="ext-tab-icon">🤖</span>
          <span>Doubt Solver</span>
        </button>
        <button type="button" class="ext-nav-tab" role="tab" id="tab-notes" aria-selected="false" aria-controls="view-notes" data-screen="notes">
          <span class="ext-tab-icon">📝</span>
          <span>Revision Notes</span>
        </button>
      </nav>

      <div class="laptop-assembly">

        <!-- Open Laptop Lid & Display Bezel -->
        <div class="laptop-lid">
          <div class="laptop-bezel">
            <div class="webcam-notch" aria-hidden="true">
              <span class="webcam-lens"></span>
              <span class="webcam-led"></span>
            </div>

            <div class="laptop-screen">
              <!-- Screen Views Container -->
              <div class="screen-views-wrapper">

                <!-- 1. Full Detailed Video Screen (Centered 9:16 Reel fitting the screen with ambient mode & study hub) -->
                <div class="screen-view active" id="view-reel" role="tabpanel" aria-labelledby="tab-reel">
                  <div class="view-full-video">

                    <!-- Ambient blurred glowing background -->
                    <video id="ambientReelVideo" class="reel-ambient-bg" src="reel.mp4" autoplay loop muted playsinline aria-hidden="true"></video>

                    <!-- Centered Uncropped 9:16 Reel Player Frame -->
                    <div class="main-reel-frame" id="mainReelFrame">
                      <video id="fullReelVideo" src="reel.mp4" poster="reel-poster.jpg" autoplay loop muted playsinline></video>
                    </div>

                    <!-- Top Floating Header Bar (Topic + Hub Mastery Status) -->
                    <div class="video-overlay-top">
                      <div class="video-top-left-group">
                        <div class="video-topic-badge">
                          <span>⚡ 60s Reel:</span>
                          <span>Nuclear Strong Force</span>
                        </div>
                        <div class="video-hub-badge">
                          <span class="hub-status-dot" aria-hidden="true"></span>
                          <span>Today: 3/3 Doubts Cleared</span>
                        </div>
                      </div>
                      <div class="video-top-right-group">
                        <button type="button" class="video-mode-toggle-btn" id="videoModeToggleBtn" title="Toggle between Fit and Fill view">
                          <span id="videoModeText">↔ Fill View</span>
                        </button>
                        <span class="video-quality-tag">HD 1080p</span>
                      </div>
                    </div>

                    <!-- Bottom Custom Video Player Bar -->
                    <div class="video-overlay-bottom">
                      <div class="video-progress-track" id="videoProgressTrack" title="Seek video position">
                        <div class="video-progress-fill" id="videoProgressFill"></div>
                      </div>
                      <div class="video-ctrl-row">
                        <div class="video-btn-group">
                          <button type="button" class="video-ctrl-btn" id="videoPlayBtn" aria-label="Play or Pause Video">
                            <span id="playIcon">❚❚</span>
                            <span id="playText">Pause</span>
                          </button>
                          <button type="button" class="video-ctrl-btn" id="videoMuteBtn" aria-label="Toggle Sound">
                            <span id="muteIcon">🔇</span>
                            <span id="muteText">Unmute</span>
                          </button>
                          <button type="button" class="video-ctrl-btn" id="videoReplayBtn" aria-label="Replay from start">
                            <span>↺ Replay</span>
                          </button>
                        </div>
                        <span class="video-time" id="videoTimeDisplay">0:00 / 0:58</span>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- 2. Interactive Doubt Chat Screen (AI Doubt Mentor) -->
                <div class="screen-view" id="view-mentor" role="tabpanel" aria-labelledby="tab-mentor">
                  <div class="view-mentor-chat">
                    <div class="mentor-profile-header">
                      <div class="mentor-id-group">
                        <div class="mentor-avatar">AI</div>
                        <div>
                          <div class="mentor-name">Mitra · AI Doubt Solver</div>
                        </div>
                      </div>
                      <span class="mentor-tag-pill">🛡️ 100% Patient &amp; Friendly</span>
                    </div>

                    <div class="chat-thread-container" id="mentorChatStream">
                      <div class="chat-bubble student">
                        "Teacher went fast today: why don't positive protons repel each other in the nucleus?"
                      </div>
                      <div class="chat-bubble mentor">
                        "Hi! I'm Mitra. Don't worry—let's break it down step-by-step: The Strong Nuclear Force is 137x stronger than electric repulsion at subatomic range. It glues them together tight! 💡"
                      </div>
                    </div>

                    <div class="chat-prompt-chips">
                      <button type="button" class="prompt-chip-btn" data-q="neutrons">⚡ Ask Mitra: Why do neutrons matter?</button>
                      <button type="button" class="prompt-chip-btn" data-q="atomic">🔬 Ask Mitra: What if Z &gt; 82?</button>
                      <button type="button" class="prompt-chip-btn" data-q="gravity">🛡️ Ask Mitra: Stronger than gravity?</button>
                    </div>
                  </div>
                </div>

                <!-- 3. Important Revision Notes Screen (AI Generated) -->
                <div class="screen-view" id="view-notes" role="tabpanel" aria-labelledby="tab-notes">
                  <div class="view-class-notes">
                    <div class="notes-header-row">
                      <span class="notes-title">📖 Chapter 4: Nuclei &amp; Strong Forces</span>
                      <span class="notes-badge">✨ Exam-Ready Notes · Class 12</span>
                    </div>

                    <div class="notes-formula-grid">
                      <div class="formula-card">
                        <div class="formula-lbl">Coulomb Repulsion</div>
                        <div class="formula-math">F = k · (q₁q₂ / r²)</div>
                      </div>
                      <div class="formula-card">
                        <div class="formula-lbl">Nuclear Radius</div>
                        <div class="formula-math">R = R₀ · A^(1/3)</div>
                      </div>
                    </div>

                    <ul class="notes-bullets-list">
                      <li><strong>Key Takeaway:</strong> Strong Nuclear Force operates equally on p-p, n-n, and p-n pairs.</li>
                      <li>Operates at femtometre range (~10⁻¹⁵ m) and completely overpowers electric repulsion.</li>
                      <li>Saturated force: only attracts nearest neighbor nucleons.</li>
                    </ul>

                    <div class="notes-footer-row">
                      <button type="button" class="notes-download-btn" onclick="handleDummyCta(event, 'Download Class 12 Revision Sheet PDF')">📥 Download 1-Page Summary PDF</button>
                      <span style="font-size:0.52rem; color:#94A3B8; font-weight:700;">Revision Sheet #04</span>
                    </div>
                  </div>
                </div>

              </div>
            </div>

            <div class="bezel-chin" aria-hidden="true">PAATHSHALA BOOK PRO</div>
          </div>
        </div>

        <!-- True 3D Trapezoidal Open MacBook Pro Base (SVG Hardware Deck) -->
        <svg class="laptop-base-svg" viewBox="0 0 1000 190" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <!-- Top Hinge Shadow & Cylinder (Matches 82% Lid Width: x=90 to x=910) -->
          <polygon points="90,2 910,2 990,158 10,158" fill="#E2E8F0" stroke="#0F172A" stroke-width="6" stroke-linejoin="round"/>
          <!-- Dark Cylindrical Hinge Barrel -->
          <rect x="230" y="0" width="540" height="10" rx="4" fill="#0F172A"/>

          <!-- Left & Right Speaker Perforation Grilles on Deck Flanks -->
          <polygon points="102,24 122,24 90,106 66,106" fill="#94A3B8" opacity="0.55"/>
          <polygon points="878,24 898,24 934,106 910,106" fill="#94A3B8" opacity="0.55"/>

          <!-- Recessed Trapezoid Keyboard Well -->
          <polygon points="132,18 868,18 906,112 94,112" fill="#090D16" stroke="#0F172A" stroke-width="4" stroke-linejoin="round"/>

          <!-- 5 Rows of Perspective Keycaps -->
          <g>
              {KEYS_SVG}
          </g>

          <!-- Perspective Glass Trackpad Centered Below Spacebar -->
          <polygon points="365,120 635,120 648,152 352,152" fill="#CBD5E1" stroke="#0F172A" stroke-width="3.5" stroke-linejoin="round"/>

          <!-- Front Aluminum Unibody Lip Edge & Center Thumb Scoop Notch -->
          <path d="M10,158 L990,158 L990,168 C990,176 980,180 966,180 L34,180 C20,180 10,176 10,168 Z"
                fill="#94A3B8" stroke="#0F172A" stroke-width="6" stroke-linejoin="round"/>
          <path d="M430,158 L570,158 L562,169 C560,172 554,173 546,173 L454,173 C446,173 440,172 438,169 Z"
                fill="#0F172A"/>
        </svg>

      </div>
    </div>

  </div>

</section>

<!-- Floating Demo Toast Notification -->
<div class="demo-toast" id="demoToast" role="alert" aria-live="polite">
  <span style="font-size: 1.1rem;">✨</span>
  <span id="demoToastText">Prototype Demo Action</span>
</div>

<script>
  // --- External Navigation Tabs Architecture ---
  const screenTabs = document.querySelectorAll('.ext-nav-tab');
  const screenViews = document.querySelectorAll('.screen-view');
  const fullVideo = document.getElementById('fullReelVideo');
  const ambientVideo = document.getElementById('ambientReelVideo');

  function activateScreen(screenId) {{
    screenTabs.forEach((tab) => {{
      const isTarget = tab.getAttribute('data-screen') === screenId;
      tab.classList.toggle('active', isTarget);
      tab.setAttribute('aria-selected', isTarget ? 'true' : 'false');
    }});

    screenViews.forEach((view) => {{
      const isTarget = view.id === `view-${{screenId}}`;
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
  const modeBtn = document.getElementById('videoModeToggleBtn');
  const modeText = document.getElementById('videoModeText');
  const reelFrame = document.getElementById('mainReelFrame');
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
  const playBtn = document.getElementById('videoPlayBtn');
  const playIcon = document.getElementById('playIcon');
  const playText = document.getElementById('playText');
  const muteBtn = document.getElementById('videoMuteBtn');
  const muteIcon = document.getElementById('muteIcon');
  const muteText = document.getElementById('muteText');
  const replayBtn = document.getElementById('videoReplayBtn');
  const progressTrack = document.getElementById('videoProgressTrack');
  const progressFill = document.getElementById('videoProgressFill');
  const timeDisplay = document.getElementById('videoTimeDisplay');

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
        if (progressFill) progressFill.style.inlineSize = `${{percent}}%`;
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
  const chatStream = document.getElementById('mentorChatStream');
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

  document.querySelectorAll('.prompt-chip-btn').forEach((btn) => {{
    btn.addEventListener('click', () => {{
      const qKey = btn.getAttribute('data-q');
      const item = chatReplies[qKey];
      if (!item || !chatStream) return;

      const studentBubble = document.createElement('div');
      studentBubble.className = 'chat-bubble student';
      studentBubble.textContent = `"${{item.q}}"`;
      chatStream.appendChild(studentBubble);

      chatStream.scrollTop = chatStream.scrollHeight;

      setTimeout(() => {{
        const mentorBubble = document.createElement('div');
        mentorBubble.className = 'chat-bubble mentor';
        mentorBubble.textContent = item.a;
        chatStream.appendChild(mentorBubble);
        chatStream.scrollTop = chatStream.scrollHeight;
      }}, 350);
    }});
  }});

  // --- Built-in Dummy Action Toast Handler ---
  function handleDummyCta(event, actionName) {{
    if (event) event.preventDefault();
    const toast = document.getElementById('demoToast');
    const toastText = document.getElementById('demoToastText');
    if (toast && toastText) {{
      toastText.textContent = `✨ Demo: "${{actionName}}" triggered (Safe Prototype · Real site untouched)`;
      toast.classList.add('show');
      clearTimeout(window._toastTimeout);
      window._toastTimeout = setTimeout(() => {{
        toast.classList.remove('show');
      }}, 3200);
    }}
  }}
</script>
</body>
</html>
"""

out_dir = Path("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning")
brain_dir = Path("/Users/srinibashbartia/.gemini/antigravity/brain/44549ce3-e614-40a0-8bbb-9a9fafdf87de")
surge_dir = out_dir / "dist-surge"

for name in ("banner.html", "banner-laptop.html", "homepage-section.html"):
    (out_dir / name).write_text(HTML_CONTENT, encoding="utf-8")
    try:
        (brain_dir / name).write_text(HTML_CONTENT, encoding="utf-8")
    except Exception:
        pass

if surge_dir.exists():
    (surge_dir / "index.html").write_text(HTML_CONTENT, encoding="utf-8")
    (surge_dir / "banner.html").write_text(HTML_CONTENT, encoding="utf-8")

print("Successfully updated banner files with sellable copy!")
