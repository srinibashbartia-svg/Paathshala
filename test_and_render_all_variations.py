#!/usr/bin/env python3
"""
test_and_render_all_variations.py
Generates an interactive standalone showcase of the 3 distinct Worm Character Action poses,
plus integrates them into the hero banner.
"""

import os

WORM_VARIATION_1_SVG = '''
<!-- ================= VARIATION 1: THE ROCKET SURFER (CHEF-D'OEUVRE) ================= -->
<g class="worm-variation worm-v1" id="worm-v1-group">
  <defs>
    <!-- Mask for Rocket Surfer Worm Tube (Uniform 40px width with perfect rounded caps) -->
    <mask id="v1-worm-body-mask">
      <path d="M -60 20 C -45 8, -35 -14, -14 -16 C 6 -18, 22 -14, 32 -38" 
            fill="none" stroke="#FFFFFF" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>
    </mask>
  </defs>

  <!-- 1. Cape Fluttering in the Supersonic Wind (Behind Body) -->
  <path d="M -8 -16 C -50 -32 -85 -18 -115 8 C -90 2 -65 -12 -28 -6 Z" 
        fill="#FF5A36" stroke="#0F172A" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M -22 -10 C -60 -18 -85 -6 -100 6" stroke="#0F172A" stroke-width="2" fill="none"/>

  <!-- 2. Solid Black Outer Border of Worm Body (Ensures crisp 3.5px outline everywhere) -->
  <path d="M -60 20 C -45 8, -35 -14, -14 -16 C 6 -18, 22 -14, 32 -38" 
        fill="none" stroke="#0F172A" stroke-width="47" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- 3. Masked Interior: Smooth Violet Base + Seamless Cylindrical Indigo Stripes -->
  <g mask="url(#v1-worm-body-mask)">
    <!-- Base Violet Body Fill -->
    <rect x="-140" y="-120" width="240" height="200" fill="#5458F7"/>
    
    <!-- Curved Cylindrical Stripes matching reference media_1792552882621_ebe33cd4.png -->
    <!-- Stripe 1 (tail wrap) -->
    <path d="M -72 6 Q -60 18 -48 30" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
    <!-- Stripe 2 (lower body) -->
    <path d="M -48 -6 Q -36 8 -24 22" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
    <!-- Stripe 3 (mid arch) -->
    <path d="M -24 -26 Q -14 -12 -4 2" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
    <!-- Stripe 4 (chest) -->
    <path d="M 2 -32 Q 12 -18 22 -4" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
    <!-- Stripe 5 (neck) -->
    <path d="M 16 -48 Q 28 -34 38 -20" stroke="#3730A3" stroke-width="15" stroke-linecap="round"/>
  </g>

  <!-- 4. Floating Golden Star (Exact feature from reference top-right worm) -->
  <g transform="translate(32, -72)">
    <polygon points="0,-13 4,-4 13,0 4,4 0,13 -4,4 -13,0 -4,-4" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>
  </g>

  <!-- 5. Paathshala Orange Headband with Fluttering Ribbon Tails -->
  <!-- Ribbon Tails streaming back in wind -->
  <path d="M 16 -40 C -2 -48 -18 -38 -32 -50 C -22 -40 -10 -42 12 -34" 
        fill="#FF5A36" stroke="#0F172A" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M 18 -36 C 4 -40 -6 -28 -18 -34 C -8 -28 2 -32 16 -30" 
        fill="#FF5A36" stroke="#0F172A" stroke-width="2" stroke-linejoin="round"/>
  <!-- Headband Front Wrap -->
  <path d="M 14 -44 C 22 -36 34 -34 46 -42" stroke="#FF5A36" stroke-width="8" stroke-linecap="round"/>
  <path d="M 14 -44 C 22 -36 34 -34 46 -42" stroke="#0F172A" stroke-width="2" fill="none"/>

  <!-- 6. Expressive Cartoon Eyes (Exact design from reference image) -->
  <!-- Left Eye -->
  <circle cx="28" cy="-44" r="8" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="30" cy="-44" r="4.5" fill="#0F172A"/>
  <circle cx="28.5" cy="-46.5" r="1.6" fill="#FFFFFF"/>

  <!-- Right Eye -->
  <circle cx="42" cy="-42" r="7.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="44" cy="-42" r="4.2" fill="#0F172A"/>
  <circle cx="42.5" cy="-44.5" r="1.5" fill="#FFFFFF"/>

  <!-- Confident Smile -->
  <path d="M 28 -28 Q 36 -22 42 -28" stroke="#0F172A" stroke-width="3" fill="none" stroke-linecap="round"/>

  <!-- 7. Hands & Steering -->
  <!-- Left Hand resting on rocket pencil -->
  <circle cx="-16" cy="14" r="6" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
  <!-- Right Arm & Golden Mentor Wand -->
  <path d="M 28 -14 Q 48 -10 62 -18" stroke="#5458F7" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M 28 -14 Q 48 -10 62 -18" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <circle cx="62" cy="-18" r="5.5" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
  <!-- Golden Wand Shaft -->
  <line x1="62" y1="-18" x2="88" y2="-28" stroke="#FFD24A" stroke-width="4.5" stroke-linecap="round"/>
  <!-- Wand Starburst Sparkle -->
  <g transform="translate(92, -30)">
    <path d="M 0 -8 C 1 -2 3 -1 8 0 C 3 1 1 3 0 8 C -1 3 -3 1 -8 0 C -3 -1 -1 -3 0 -8 Z" fill="#FFD24A" stroke="#0F172A" stroke-width="1.8"/>
  </g>
</g>
'''

WORM_VARIATION_2_SVG = '''
<!-- ================= VARIATION 2: THE LOOPING CORKSCREW PILOT ================= -->
<!-- Directly incorporating the cursive "e" loop from reference media_1792552882621_ebe33cd4.png (top-left) -->
<g class="worm-variation worm-v2" id="worm-v2-group">
  <defs>
    <!-- Loop Mask -->
    <mask id="v2-worm-body-mask">
      <!-- Lower arch + loop-de-loop + head leaning forward -->
      <path d="M -55 24 C -50 -10, -25 -45, 5 -45 C 35 -45, 45 -15, 20 -2 C 0 8, -25 0, -20 -30 C -15 -55, 10 -65, 35 -60" 
            fill="none" stroke="#FFFFFF" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
    </mask>
  </defs>

  <!-- Cape Billowing -->
  <path d="M -15 -25 C -55 -45 -85 -25 -110 5 C -85 -5 -60 -15 -25 -12 Z" 
        fill="#FF5A36" stroke="#0F172A" stroke-width="3.5" stroke-linejoin="round"/>

  <!-- Solid Outer Ink Border -->
  <path d="M -55 24 C -50 -10, -25 -45, 5 -45 C 35 -45, 45 -15, 20 -2 C 0 8, -25 0, -20 -30 C -15 -55, 10 -65, 35 -60" 
        fill="none" stroke="#0F172A" stroke-width="45" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Masked Interior -->
  <g mask="url(#v2-worm-body-mask)">
    <rect x="-130" y="-120" width="230" height="200" fill="#5458F7"/>
    <!-- Stripes around the loop -->
    <path d="M -60 10 Q -45 15 -35 25" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M -45 -25 Q -30 -20 -20 -10" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M -10 -55 Q 5 -45 15 -35" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M 35 -30 Q 25 -20 15 -10" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M 10 5 Q 0 -5 -10 -15" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M -30 -35 Q -15 -35 0 -45" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M 0 -70 Q 15 -60 30 -55" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
  </g>

  <!-- Floating Golden Star above head (35, -60) -->
  <g transform="translate(35, -92)">
    <polygon points="0,-13 4,-4 13,0 4,4 0,13 -4,4 -13,0 -4,-4" fill="#FFD24A" stroke="#0F172A" stroke-width="2.5"/>
  </g>

  <!-- Headband with streaming ribbons -->
  <path d="M 18 -66 C 0 -74 -12 -65 -26 -75" stroke="#FF5A36" stroke-width="6" stroke-linecap="round" fill="none"/>
  <path d="M 18 -66 C 0 -74 -12 -65 -26 -75" stroke="#0F172A" stroke-width="2" stroke-linecap="round" fill="none"/>
  <rect x="20" y="-72" width="28" height="8" rx="3" fill="#FF5A36" stroke="#0F172A" stroke-width="2"/>

  <!-- Eyes at (35, -60) -->
  <circle cx="30" cy="-62" r="7.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="32" cy="-62" r="4.2" fill="#0F172A"/>
  <circle cx="30.5" cy="-64.5" r="1.5" fill="#FFFFFF"/>

  <circle cx="43" cy="-60" r="7" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="45" cy="-60" r="3.9" fill="#0F172A"/>
  <circle cx="43.5" cy="-62.5" r="1.4" fill="#FFFFFF"/>

  <!-- Open excited mouth -->
  <path d="M 32 -48 Q 38 -42 44 -48 Z" fill="#FFD24A" stroke="#0F172A" stroke-width="2"/>

  <!-- Waving cheering hand -->
  <path d="M 40 -35 Q 58 -40 68 -55" stroke="#5458F7" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M 40 -35 Q 58 -40 68 -55" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <circle cx="68" cy="-55" r="5" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
</g>
'''

WORM_VARIATION_3_SVG = '''
<!-- ================= VARIATION 3: THE SUPER-MENTOR GLIDER ================= -->
<!-- Aerodynamic horizontal wave flight pose, steering supersonic rocket with two hands -->
<g class="worm-variation worm-v3" id="worm-v3-group">
  <defs>
    <!-- Glider Mask -->
    <mask id="v3-worm-body-mask">
      <path d="M -70 20 C -45 28, -25 5, 5 10 C 35 15, 55 -5, 65 -25" 
            fill="none" stroke="#FFFFFF" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
    </mask>
  </defs>

  <!-- Big Superhero Cape streaming horizontally -->
  <path d="M 0 5 C -45 -18 -85 -10 -120 5 C -90 -2 -65 -10 -25 -2 Z" 
        fill="#FF5A36" stroke="#0F172A" stroke-width="3.5" stroke-linejoin="round"/>

  <!-- Solid Outer Ink Border -->
  <path d="M -70 20 C -45 28, -25 5, 5 10 C 35 15, 55 -5, 65 -25" 
            fill="none" stroke="#0F172A" stroke-width="45" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Masked Interior -->
  <g mask="url(#v3-worm-body-mask)">
    <rect x="-140" y="-80" width="250" height="150" fill="#5458F7"/>
    <!-- Transverse cylindrical stripes -->
    <path d="M -75 5 Q -65 20 -55 35" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M -45 5 Q -35 18 -25 30" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M -15 -5 Q -5 10 5 25" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M 15 -2 Q 25 12 35 25" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    <path d="M 45 -15 Q 55 -2 65 10" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
  </g>

  <!-- Floating Star ahead of flight -->
  <g transform="translate(85, -35)">
    <polygon points="0,-12 3.5,-3.5 12,0 3.5,3.5 0,12 -3.5,3.5 -12,0 -3.5,-3.5" fill="#FFD24A" stroke="#0F172A" stroke-width="2.2"/>
  </g>

  <!-- Aviator Goggles on Forehead -->
  <rect x="44" y="-35" width="30" height="9" rx="4" fill="#0F172A"/>
  <circle cx="51" cy="-31" r="5" fill="#86EFAC" stroke="#0F172A" stroke-width="1.8"/>
  <circle cx="65" cy="-31" r="5" fill="#86EFAC" stroke="#0F172A" stroke-width="1.8"/>

  <!-- Forward Looking Eyes at (65, -25) -->
  <circle cx="58" cy="-24" r="7.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="61" cy="-24" r="4.2" fill="#0F172A"/>
  <circle cx="59.5" cy="-26.5" r="1.5" fill="#FFFFFF"/>

  <circle cx="70" cy="-23" r="7" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="72" cy="-23" r="3.9" fill="#0F172A"/>
  <circle cx="70.5" cy="-25.5" r="1.4" fill="#FFFFFF"/>

  <!-- Dual Grip Hands on Pencil -->
  <circle cx="10" cy="18" r="6" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="45" cy="16" r="6" fill="#5458F7" stroke="#0F172A" stroke-width="2.5"/>
</g>
'''

print("All 3 variations defined")
