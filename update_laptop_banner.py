#!/usr/bin/env python3
"""Updates the Laptop Showcase Banner with:
1. Centered, immersive Reel player that fits the laptop screen naturally with zero clipping.
2. Ambient backdrop matching the video for an authentic desktop media player experience.
3. Interactive "Fit 9:16 / Fill Screen" toggle button so users can switch viewing modes instantly.
4. Prominent external navigation tabs placed outside the laptop for effortless switching.
5. All distracting pills removed.
"""

from pathlib import Path

def build_perspective_keys() -> str:
    """Builds 5 rows of perspective-aligned trapezoid keys inside the MacBook keyboard well."""
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
<title>Paathshala · Guided Learning After Class Horizontal Banner</title>
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

    .headline-stack {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 0.45rem;
    }}

    .hl-tier-1 {{
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(2.15rem, 1.4rem + 2.4vw, 3.3rem);
      line-height: 1.04;
      letter-spacing: -0.03em;
      color: var(--white);
      text-shadow: 3px 3px 0px var(--ink);
    }}

    .hl-tier-2 {{
      display: inline-block;
      background-color: var(--cream);
      color: var(--ink);
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(2.2rem, 1.4rem + 2.5vw, 3.4rem);
      line-height: 1.04;
      letter-spacing: -0.03em;
      padding: 0.12em 0.48em 0.16em;
      border: 3px solid var(--ink);
      box-shadow: 5px 5px 0px var(--ink);
      transform: rotate(-1.5deg);
    }}

    .hl-tier-3 {{
      display: inline-block;
      background-color: var(--yellow);
      color: var(--ink);
      font-family: var(--font-display);
      font-weight: 900;
      font-size: clamp(2.55rem, 1.6rem + 3vw, 4rem);
      line-height: 1.02;
      letter-spacing: -0.035em;
      padding: 0.12em 0.42em 0.16em;
      border: 3.5px solid var(--ink);
      box-shadow: 6px 6px 0px var(--ink);
      transform: rotate(1.5deg);
      margin-block-start: 0.15rem;
    }}

    .value-points-list {{
      list-style: none;
      margin-block-start: 1.15rem;
      display: flex;
      flex-direction: column;
      gap: 0.52rem;
      max-inline-size: 44ch;
    }}

    .value-point-item {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-size: clamp(0.86rem, 0.78rem + 0.3vw, 0.96rem);
      line-height: 1.35;
      color: var(--cream);
      font-weight: 600;
    }}

    .point-check-badge {{
      inline-size: 21px;
      block-size: 21px;
      border-radius: 50%;
      background-color: var(--mint);
      color: var(--ink);
      border: 2px solid var(--ink);
      box-shadow: 2px 2px 0px var(--ink);
      display: inline-grid;
      place-items: center;
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 0.7rem;
      flex-shrink: 0;
    }}

    .point-text strong {{
      color: var(--yellow);
      font-weight: 800;
    }}

    .left-cta-row {{
      margin-block-start: 1.25rem;
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
      font-size: clamp(0.96rem, 0.85rem + 0.35vw, 1.1rem);
      text-decoration: none;
      padding: 0.76rem 1.45rem;
      border-radius: 999px;
      border: 3px solid var(--ink);
      box-shadow: 5px 5px 0px var(--ink);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}

    .primary-cta-btn:hover {{
      transform: translate(-2px, -2px);
      box-shadow: 7px 7px 0px var(--ink);
    }}

    .primary-cta-btn:focus-visible {{
      outline: 3px solid var(--yellow);
      outline-offset: 4px;
    }}

    .trust-micro-note {{
      margin-block-start: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: clamp(0.78rem, 0.72rem + 0.22vw, 0.86rem);
      font-weight: 700;
      color: var(--cream);
      opacity: 0.95;
    }}

    .trust-micro-dot {{
      inline-size: 8px;
      block-size: 8px;
      border-radius: 50%;
      background-color: var(--mint);
      border: 1.5px solid var(--ink);
      flex-shrink: 0;
    }}

    .trust-micro-domain {{
      color: var(--yellow);
      font-weight: 800;
      text-decoration: underline;
      text-underline-offset: 3px;
    }}

    /* 3. Right Column: Realistic Open Laptop Showcase + Prominent External Tabs */
    .right-laptop-col {{
      position: relative;
      z-index: 4;
      display: flex;
      flex-direction: column;
      align-items: center;
      inline-size: 100%;
    }}

    /* Prominent External Navigation Bar Outside the Laptop */
    .laptop-external-nav {{
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-block-end: 14px;
      inline-size: 100%;
      z-index: 10;
    }}

    .ext-nav-tab {{
      background-color: var(--white);
      color: var(--ink);
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(0.72rem, 0.65rem + 0.35vw, 0.85rem);
      letter-spacing: 0.02em;
      padding: 0.52em 1.1em;
      border-radius: 999px;
      border: 2px solid var(--ink);
      box-shadow: 2.5px 2.5px 0px var(--ink);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      transition: transform 0.18s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.18s ease, background-color 0.18s ease;
    }}

    .ext-nav-tab:hover {{
      transform: translateY(-2px);
      box-shadow: 4px 4px 0px var(--ink);
      background-color: #FEF3C7;
    }}

    .ext-nav-tab.active {{
      background-color: var(--yellow);
      color: var(--ink);
      border-color: var(--ink);
      box-shadow: 3.5px 3.5px 0px var(--ink);
      transform: translateY(-2px);
    }}

    .ext-nav-tab:focus-visible {{
      outline: 3px solid var(--orange);
      outline-offset: 2px;
    }}

    .ext-tab-icon {{
      font-size: 1rem;
      line-height: 1;
    }}

    .laptop-assembly {{
      position: relative;
      inline-size: 100%;
      max-inline-size: 670px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    /* Open Laptop Lid: Exact 82% width to match the top of the SVG Trapezoid Base */
    .laptop-lid {{
      position: relative;
      inline-size: 82%;
      background-color: var(--yellow);
      border: 3px solid var(--ink);
      border-radius: 18px 18px 4px 4px;
      padding: 6px 6px 0 6px;
      box-shadow: 0 -2px 0px var(--ink);
    }}

    /* Realistic MacBook Dark Glass Bezel */
    .laptop-bezel {{
      position: relative;
      background-color: #090D16;
      border: 2.5px solid var(--ink);
      border-radius: 13px 13px 0 0;
      padding: 10px 8px 8px;
    }}

    /* Webcam Notch at Top Center of Bezel */
    .webcam-notch {{
      position: absolute;
      inset-block-start: 0;
      inset-inline-start: 50%;
      transform: translateX(-50%);
      inline-size: 62px;
      block-size: 9px;
      background-color: #090D16;
      border-radius: 0 0 6px 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      z-index: 5;
    }}

    .webcam-lens {{
      inline-size: 4px;
      block-size: 4px;
      border-radius: 50%;
      background-color: #334155;
    }}

    .webcam-led {{
      inline-size: 3.5px;
      block-size: 3.5px;
      border-radius: 50%;
      background-color: var(--mint);
    }}

    /* Illuminated Display Screen Inside Bezel */
    .laptop-screen {{
      position: relative;
      background-color: #060A12;
      border: 1.5px solid #1E293B;
      border-radius: 6px;
      padding: 0;
      color: var(--white);
      overflow: hidden;
      min-block-size: 335px;
      block-size: 335px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
    }}

    /* Screen Views Wrapper */
    .screen-views-wrapper {{
      position: relative;
      flex: 1;
      block-size: 100%;
      display: grid;
    }}

    .screen-view {{
      grid-area: 1 / 1;
      block-size: 100%;
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transform: scale(0.99);
      transition: opacity 0.22s ease, transform 0.22s ease, visibility 0.22s ease;
      display: flex;
      flex-direction: column;
    }}

    .screen-view.active {{
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
      transform: scale(1);
      z-index: 2;
    }}

    /* Screen 1: Full Detailed Concept Reel Studio Screen (Fits the screen perfectly) */
    .view-full-video {{
      position: relative;
      inline-size: 100%;
      block-size: 100%;
      overflow: hidden;
      background-color: #060A12;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* Ambient blurred glowing backdrop reflecting the reel */
    .reel-ambient-bg {{
      position: absolute;
      inset: 0;
      inline-size: 100%;
      block-size: 100%;
      object-fit: cover;
      filter: blur(24px) brightness(0.36) saturate(1.4);
      opacity: 0.72;
      pointer-events: none;
      z-index: 1;
      transform: scale(1.1);
    }}

    /* Centered Reel Frame fitting 100% height of the laptop screen */
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
      object-fit: contain; /* Full 720x1280 dimension, 100% uncropped */
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
      pointer-events: auto;
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
      padding: 12px 14px 10px;
      background: linear-gradient(0deg, rgba(9, 13, 22, 0.95) 0%, rgba(9, 13, 22, 0.6) 65%, transparent 100%);
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .video-progress-track {{
      inline-size: 100%;
      block-size: 5px;
      background-color: rgba(255, 255, 255, 0.28);
      border-radius: 999px;
      overflow: hidden;
      cursor: pointer;
    }}

    .video-progress-fill {{
      inline-size: 0%;
      block-size: 100%;
      background-color: var(--orange);
      border-radius: 999px;
      transition: inline-size 0.1s linear;
    }}

    .video-ctrl-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .video-btn-group {{
      display: flex;
      gap: 6px;
      align-items: center;
    }}

    .video-ctrl-btn {{
      background-color: rgba(255, 255, 255, 0.18);
      color: var(--white);
      border: 1px solid rgba(255, 255, 255, 0.32);
      border-radius: 4px;
      padding: 3px 8px;
      font-size: 0.52rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
      backdrop-filter: blur(4px);
    }}

    .video-ctrl-btn:hover {{
      background-color: var(--orange);
      color: var(--white);
      border-color: var(--orange);
    }}

    .video-time {{
      font-size: 0.52rem;
      font-family: var(--font-display);
      font-weight: 700;
      color: var(--cream);
      letter-spacing: 0.04em;
    }}

    /* Screen 2: Interactive Doubt Chat View */
    .view-mentor-chat {{
      background-color: #0E1526;
      border-radius: 6px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      block-size: 100%;
      box-sizing: border-box;
    }}

    .mentor-profile-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-block-end: 7px;
      border-block-end: 1px solid #1E293B;
    }}

    .mentor-id-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .mentor-avatar {{
      inline-size: 24px;
      block-size: 24px;
      border-radius: 50%;
      background-color: var(--orange);
      color: var(--white);
      display: grid;
      place-items: center;
      font-size: 0.58rem;
      font-weight: 800;
      border: 1.2px solid var(--ink);
    }}

    .mentor-name {{
      font-size: 0.62rem;
      font-weight: 800;
      color: var(--cream);
    }}

    .mentor-tag-pill {{
      font-size: 0.5rem;
      font-weight: 700;
      background-color: rgba(134, 239, 172, 0.18);
      color: var(--mint);
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid var(--mint);
    }}

    .chat-thread-container {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding-block: 10px;
      overflow-y: auto;
      max-block-size: 195px;
    }}

    .chat-bubble {{
      max-inline-size: 88%;
      padding: 7px 10px;
      border-radius: 7px;
      font-size: 0.6rem;
      font-weight: 600;
      line-height: 1.35;
    }}

    .chat-bubble.student {{
      align-self: flex-start;
      background-color: #1E293B;
      color: var(--cream);
      border: 1px solid #334155;
    }}

    .chat-bubble.mentor {{
      align-self: flex-end;
      background-color: var(--violet);
      color: var(--white);
      border: 1px solid #7377F9;
      box-shadow: 0 2px 8px rgba(84, 88, 247, 0.35);
    }}

    .chat-prompt-chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      padding-block-start: 8px;
      border-block-start: 1px solid #1E293B;
    }}

    .prompt-chip-btn {{
      background-color: #162032;
      color: var(--cream);
      border: 1px solid #2B3855;
      border-radius: 4px;
      padding: 3.5px 8px;
      font-size: 0.52rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .prompt-chip-btn:hover {{
      background-color: var(--yellow);
      color: var(--ink);
      border-color: var(--ink);
    }}

    /* Screen 3: Important Revision Notes Screen */
    .view-class-notes {{
      background-color: #0E1526;
      border-radius: 6px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      block-size: 100%;
      box-sizing: border-box;
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

    /* Screen 4: Split Hub Overview Screen */
    .view-hub-overview {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      block-size: 100%;
      box-sizing: border-box;
      padding: 10px 12px;
    }}

    .screen-stage {{
      position: relative;
      margin-block: 6px;
      display: grid;
      grid-template-columns: 0.95fr 1.25fr;
      gap: 10px;
      align-items: center;
    }}

    .screen-card-reel {{
      position: relative;
      background-color: var(--slate-dark);
      border: 2px solid var(--cream);
      border-radius: 7px;
      overflow: hidden;
      aspect-ratio: 4 / 3;
    }}

    .screen-card-reel video {{
      inline-size: 100%;
      block-size: 100%;
      object-fit: cover;
      display: block;
    }}

    .screen-card-mentor {{
      position: relative;
      background-color: var(--slate-dark);
      border: 2px solid var(--cream);
      border-radius: 7px;
      padding: 10px 12px;
      min-block-size: 115px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 6px;
    }}

    .chat-msg {{
      font-size: 0.58rem;
      font-weight: 700;
      padding: 5px 8px;
      border-radius: 6px;
      line-height: 1.25;
    }}

    .chat-msg.student {{
      background-color: var(--cream);
      color: var(--ink);
      align-self: flex-start;
      border: 1.5px solid var(--ink);
    }}

    .chat-msg.mentor {{
      background-color: var(--mint);
      color: var(--ink);
      align-self: flex-end;
      border: 1.5px solid var(--ink);
    }}

    .screen-bottom {{
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 8px;
      padding-block-start: 8px;
      border-block-start: 1px solid #1E293B;
    }}

    .screen-proof {{
      font-size: 0.54rem;
      font-weight: 600;
      color: var(--cream);
      line-height: 1.3;
      text-align: start;
    }}

    .screen-proof strong {{
      color: var(--yellow);
      display: block;
      font-family: var(--font-display);
      font-size: 0.6rem;
      font-weight: 800;
    }}

    .screen-circle-cta {{
      inline-size: 48px;
      block-size: 48px;
      border-radius: 50%;
      background-color: var(--cream);
      color: var(--ink);
      border: 2px solid var(--yellow);
      box-shadow: 0 0 0 2px var(--ink);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      text-decoration: none;
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 0.48rem;
      line-height: 1.1;
      letter-spacing: 0.02em;
      text-transform: uppercase;
      cursor: pointer;
      transition: transform 0.15s ease, background-color 0.15s ease;
    }}

    .screen-circle-cta:hover {{
      background-color: var(--yellow);
      transform: scale(1.06);
    }}

    .screen-mini-card {{
      justify-self: end;
      background-color: var(--cream);
      color: var(--ink);
      border: 1.5px solid var(--ink);
      border-radius: 6px;
      padding: 3px 6px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .mini-card-title {{
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 0.54rem;
      color: var(--ink);
    }}

    .mini-card-status {{
      font-size: 0.48rem;
      font-weight: 800;
      color: var(--ink);
      background-color: var(--mint);
      padding: 1px 4px;
      border-radius: 3px;
      border: 1px solid var(--ink);
    }}

    .bezel-chin {{
      text-align: center;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 0.46rem;
      letter-spacing: 0.18em;
      color: #64748B;
      padding-block-start: 4px;
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
      .headline-stack {{
        align-items: center;
      }}
      .value-points-list {{
        align-items: flex-start;
        text-align: start;
      }}
      .left-cta-row {{
        justify-content: center;
      }}
    }}

    @media (max-width: 680px) {{
      .screen-stage {{
        grid-template-columns: 1fr;
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

<section class="banner-canvas" aria-label="Paathshala Guided Learning After Class Horizontal Banner">

  <!-- 1. Top-Left Organic Petal Burst (Exact Reference Motif in Paathshala Gold + Ink Outline) -->
  <svg class="corner-burst" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M20 -10 C55 -10, 145 10, 155 38 C165 65, 95 62, 65 55 C115 72, 185 95, 175 125 C165 152, 95 115, 58 92 C92 128, 128 178, 102 192 C78 204, 48 145, 32 105 C35 148, 25 195, 2 192 C-18 188, -5 130, 0 88 L-20 88 L-20 -10 Z"
          fill="#FFD24A" stroke="#0F172A" stroke-width="5" stroke-linejoin="round" />
    <circle cx="26" cy="32" r="14" fill="#FF5A36" stroke="#0F172A" stroke-width="4" />
  </svg>

  <!-- Horizontal 2-Column Main Stage -->
  <div class="banner-body">

    <!-- Left Column: 3-Tier Stacked Headline + Subcopy + CTA -->
    <header class="left-copy-col">
      <div class="headline-stack">
        <h1 class="hl-tier-1">Too Shy to Ask</h1>
        <div class="hl-tier-2">in Class?</div>
        <div class="hl-tier-3">Clear It After!</div>
      </div>

      <ul class="value-points-list" aria-label="Key Guided Learning benefits">
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>Important Notes:</strong> Chapter revision sheets &amp; formula summaries</span>
        </li>
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>60s Concept Clips:</strong> Bite-sized visual animations for tough topics</span>
        </li>
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>Zero Teacher Fear:</strong> Doubts cleared 1-on-1 without asking in class</span>
        </li>
        <li class="value-point-item">
          <span class="point-check-badge" aria-hidden="true">✓</span>
          <span class="point-text"><strong>After-Class Care:</strong> Complete guided support the moment school ends</span>
        </li>
      </ul>

      <div class="left-cta-row">
        <a href="/landing.html" class="primary-cta-btn">
          <span>Book Free 1-on-1 Session</span>
          <span aria-hidden="true">➔</span>
        </a>
      </div>

      <div class="trust-micro-note">
        <span class="trust-micro-dot" aria-hidden="true"></span>
        <span>Trusted by 10,000+ Students &amp; Parents · <a href="/landing.html" class="trust-micro-domain">paathshala.app</a></span>
      </div>
    </header>

    <!-- Right Column: Realistic Open Laptop Showcase + Clean Outer Tabs -->
    <div class="right-laptop-col">

      <!-- Prominent External Navigation Bar Outside the Laptop -->
      <nav class="laptop-external-nav" role="tablist" aria-label="Explore Guided Learning Features">
        <button type="button" class="ext-nav-tab active" role="tab" id="tab-reel" aria-selected="true" aria-controls="view-reel" data-screen="reel">
          <span class="ext-tab-icon">⚡</span>
          <span>60s Concept Reel</span>
        </button>
        <button type="button" class="ext-nav-tab" role="tab" id="tab-mentor" aria-selected="false" aria-controls="view-mentor" data-screen="mentor">
          <span class="ext-tab-icon">💬</span>
          <span>1:1 Doubt Mentor</span>
        </button>
        <button type="button" class="ext-nav-tab" role="tab" id="tab-notes" aria-selected="false" aria-controls="view-notes" data-screen="notes">
          <span class="ext-tab-icon">📝</span>
          <span>Smart Class Notes</span>
        </button>
        <button type="button" class="ext-nav-tab" role="tab" id="tab-hub" aria-selected="false" aria-controls="view-hub" data-screen="hub">
          <span class="ext-tab-icon">🎛️</span>
          <span>Study Dashboard</span>
        </button>
      </nav>

      <div class="laptop-assembly">

        <!-- Open Laptop Lid & Display Bezel (82% width to match top of trapezoid base) -->
        <div class="laptop-lid">
          <div class="laptop-bezel">
            <div class="webcam-notch" aria-hidden="true">
              <span class="webcam-lens"></span>
              <span class="webcam-led"></span>
            </div>

            <div class="laptop-screen">
              <!-- Screen Views Container -->
              <div class="screen-views-wrapper">

                <!-- 1. Full Detailed Video Screen (Centered 9:16 Reel fitting the screen with ambient mode) -->
                <div class="screen-view active" id="view-reel" role="tabpanel" aria-labelledby="tab-reel">
                  <div class="view-full-video">

                    <!-- Ambient blurred glowing background -->
                    <video id="ambientReelVideo" class="reel-ambient-bg" src="reel.mp4" autoplay loop muted playsinline aria-hidden="true"></video>

                    <!-- Centered Uncropped 9:16 Reel Player Frame -->
                    <div class="main-reel-frame" id="mainReelFrame">
                      <video id="fullReelVideo" src="reel.mp4" poster="reel-poster.jpg" autoplay loop muted playsinline></video>
                    </div>

                    <!-- Top Floating Header Bar -->
                    <div class="video-overlay-top">
                      <div class="video-topic-badge">
                        <span>⚡ Concept Reel:</span>
                        <span>Nuclear Strong Force</span>
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

                <!-- 2. Interactive Doubt Chat Screen -->
                <div class="screen-view" id="view-mentor" role="tabpanel" aria-labelledby="tab-mentor">
                  <div class="view-mentor-chat">
                    <div class="mentor-profile-header">
                      <div class="mentor-id-group">
                        <div class="mentor-avatar">AS</div>
                        <div>
                          <div class="mentor-name">Prof. Amit Sharma · Physics Mentor</div>
                        </div>
                      </div>
                      <span class="mentor-tag-pill">🛡️ 100% Judgment-Free</span>
                    </div>

                    <div class="chat-thread-container" id="mentorChatStream">
                      <div class="chat-bubble student">
                        "Sir, I was too shy to ask in class: why don't protons repel each other in the nucleus?"
                      </div>
                      <div class="chat-bubble mentor">
                        "Never hesitate! The Strong Nuclear Force is 137x stronger than electrostatic repulsion at distances &lt; 1 Fermi. It locks them tight! 💡"
                      </div>
                    </div>

                    <div class="chat-prompt-chips">
                      <button type="button" class="prompt-chip-btn" data-q="neutrons">⚡ Why do neutrons matter?</button>
                      <button type="button" class="prompt-chip-btn" data-q="atomic">🔬 What if Z &gt; 82?</button>
                      <button type="button" class="prompt-chip-btn" data-q="gravity">🛡️ Stronger than gravity?</button>
                    </div>
                  </div>
                </div>

                <!-- 3. Important Revision Notes Screen -->
                <div class="screen-view" id="view-notes" role="tabpanel" aria-labelledby="tab-notes">
                  <div class="view-class-notes">
                    <div class="notes-header-row">
                      <span class="notes-title">📖 Chapter 4: Nuclei &amp; Strong Forces</span>
                      <span class="notes-badge">CBSE &amp; ICSE Class 12</span>
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
                      <li>Strong Nuclear Force is charge-independent (acts equally between p-p, n-n, p-n).</li>
                      <li>Operates at femtometre range (~10⁻¹⁵ m) and completely overpowers electric repulsion.</li>
                      <li>Saturated force: only attracts immediate nearest neighbor nucleons.</li>
                    </ul>

                    <div class="notes-footer-row">
                      <a href="/landing.html" class="notes-download-btn">📥 Download 1-Page Summary PDF</a>
                      <span style="font-size:0.52rem; color:#94A3B8; font-weight:700;">Revision Sheet #04</span>
                    </div>
                  </div>
                </div>

                <!-- 4. Split Hub Overview Screen -->
                <div class="screen-view" id="view-hub" role="tabpanel" aria-labelledby="tab-hub">
                  <div class="view-hub-overview">
                    <div class="screen-stage">
                      <div class="screen-card-reel">
                        <video src="reel.mp4" poster="reel-poster.jpg" autoplay loop muted playsinline></video>
                      </div>
                      <div class="screen-card-mentor">
                        <div class="chat-msg student">
                          "I was too shy to ask in class… why don't protons repel each other?"
                        </div>
                        <div class="chat-msg mentor">
                          "Great question! Strong Nuclear Force locks them tight in 60s! 💡"
                        </div>
                      </div>
                    </div>

                    <div class="screen-bottom">
                      <div class="screen-proof">
                        <strong>Same-Day Doubt Clearing</strong>
                        1-on-1 Mentor · Zero Classroom Fear
                      </div>
                      <a href="/landing.html" class="screen-circle-cta">
                        <span>BOOK</span>
                        <span>FREE 1:1</span>
                      </a>
                      <div class="screen-mini-card">
                        <svg width="22" height="22" viewBox="0 0 48 48" fill="none" aria-hidden="true">
                          <circle cx="24" cy="24" r="21" fill="#5458F7" stroke="#0F172A" stroke-width="3"/>
                          <circle cx="24" cy="19" r="9" fill="#FF5A36" stroke="#0F172A" stroke-width="3"/>
                          <circle cx="21" cy="18" r="2.2" fill="#FFFFFF"/>
                          <circle cx="27" cy="18" r="2.2" fill="#FFFFFF"/>
                          <path d="M21 22 Q24 25 27 22" stroke="#0F172A" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                        <div>
                          <div class="mini-card-title">Class Doubts</div>
                          <div class="mini-card-status">✓ 3/3 Cleared</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>

            <div class="bezel-chin" aria-hidden="true">PAATHSHALA BOOK PRO</div>
          </div>
        </div>

        <!-- True 3D Trapezoidal Open Laptop Keyboard Deck, Trackpad & Front Lip (SVG) -->
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

<script>
  // --- External Navigation Tabs Architecture ---
  const screenTabs = document.querySelectorAll('.ext-nav-tab');
  const screenViews = document.querySelectorAll('.screen-view');
  const fullVideo = document.getElementById('fullReelVideo');
  const ambientVideo = document.getElementById('ambientReelVideo');

  function activateScreen(screenId) {{
    // Deactivate all tabs and views
    screenTabs.forEach((tab) => {{
      const isTarget = tab.getAttribute('data-screen') === screenId;
      tab.classList.toggle('active', isTarget);
      tab.setAttribute('aria-selected', isTarget ? 'true' : 'false');
    }});

    screenViews.forEach((view) => {{
      const isTarget = view.id === `view-${{screenId}}`;
      view.classList.toggle('active', isTarget);
    }});

    // Autoplay video when reel screen is active
    if (screenId === 'reel') {{
      if (fullVideo && fullVideo.paused) fullVideo.play().catch(() => {{}});
      if (ambientVideo && ambientVideo.paused) ambientVideo.play().catch(() => {{}});
    }}
  }}

  // Tab click events
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
    // Keep ambient video in sync
    if (ambientVideo) {{
      fullVideo.addEventListener('play', () => ambientVideo.play().catch(() => {{}}));
      fullVideo.addEventListener('pause', () => ambientVideo.pause());
      fullVideo.addEventListener('seeking', () => {{ ambientVideo.currentTime = fullVideo.currentTime; }});
      fullVideo.addEventListener('seeked', () => {{ ambientVideo.currentTime = fullVideo.currentTime; }});
    }}

    // Play/Pause toggle
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

    // Mute/Unmute toggle
    if (muteBtn) {{
      muteBtn.addEventListener('click', () => {{
        fullVideo.muted = !fullVideo.muted;
        if (ambientVideo) ambientVideo.muted = true;
        if (muteIcon) muteIcon.textContent = fullVideo.muted ? '🔇' : '🔊';
        if (muteText) muteText.textContent = fullVideo.muted ? 'Unmute' : 'Mute';
      }});
    }}

    // Replay button
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

    // Time update listener
    fullVideo.addEventListener('timeupdate', () => {{
      if (fullVideo.duration) {{
        const percent = (fullVideo.currentTime / fullVideo.duration) * 100;
        if (progressFill) progressFill.style.inlineSize = `${{percent}}%`;
        if (timeDisplay) {{
          timeDisplay.textContent = `${{formatTime(fullVideo.currentTime)}} / ${{formatTime(fullVideo.duration)}}`;
        }}
      }}
    }});

    // Click on progress track to seek
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

  // --- Interactive Doubt Chat Prompts ---
  const chatStream = document.getElementById('mentorChatStream');
  const chatReplies = {{
    neutrons: {{
      q: "Why do neutrons matter?",
      a: "Neutrons provide extra Strong Nuclear Force attraction without adding repulsive charge, acting as the 'nuclear glue' that stabilizes the core! 🧪"
    }},
    atomic: {{
      q: "What if Z > 82?",
      a: "For bismuth and heavier atoms, the electrostatic repulsion overpowers the short-range strong force, making the nucleus naturally radioactive! ☢️"
    }},
    gravity: {{
      q: "Stronger than gravity?",
      a: "Infinitely so! The Strong Nuclear Force is 10³⁸ times stronger than gravity at nuclear distances. That's why atomic nuclei never fall apart on their own! 🚀"
    }}
  }};

  document.querySelectorAll('.prompt-chip-btn').forEach((btn) => {{
    btn.addEventListener('click', () => {{
      const qKey = btn.getAttribute('data-q');
      const item = chatReplies[qKey];
      if (!item || !chatStream) return;

      // Add user question
      const studentBubble = document.createElement('div');
      studentBubble.className = 'chat-bubble student';
      studentBubble.textContent = `"${{item.q}}"`;
      chatStream.appendChild(studentBubble);

      chatStream.scrollTop = chatStream.scrollHeight;

      // Mentor reply after brief pause
      setTimeout(() => {{
        const mentorBubble = document.createElement('div');
        mentorBubble.className = 'chat-bubble mentor';
        mentorBubble.textContent = item.a;
        chatStream.appendChild(mentorBubble);
        chatStream.scrollTop = chatStream.scrollHeight;
      }}, 350);
    }});
  }});
</script>
</body>
</html>
"""

out_dir = Path("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning")
brain_dir = Path("/Users/srinibashbartia/.gemini/antigravity/brain/280bacfb-a77d-43c5-8fd5-6bc903a3d7fe")
surge_dir = out_dir / "dist-surge"

# Write to scratch and brain artifacts
for name in ("banner.html", "banner-laptop.html", "homepage-section.html"):
    (out_dir / name).write_text(HTML_CONTENT, encoding="utf-8")
    (brain_dir / name).write_text(HTML_CONTENT, encoding="utf-8")

# Update dist-surge files for immediate deployment
(surge_dir / "index.html").write_text(HTML_CONTENT, encoding="utf-8")
(surge_dir / "banner.html").write_text(HTML_CONTENT, encoding="utf-8")

print("Successfully updated banner files with centered reel fitting laptop screen!")
