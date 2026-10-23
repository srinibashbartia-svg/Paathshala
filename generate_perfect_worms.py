#!/usr/bin/env python3
"""
generate_perfect_worms.py
Generates the revised high-fidelity worm characters for the Paathshala Guided Learning banner.
"""

def get_hero_worm_pose1():
    """
    Pose 1: The Rocket Rider Surfer
    The worm rides atop the supersonic rocket pencil.
    Body curves smoothly from the tail on the pencil up into a confident forward lean.
    """
    # Centerline path for the worm body (relative to rocket center at 0,0)
    # Starts at tail (-70, 18), curves up and over, head at (35, -35)
    spine_d = "M -60 18 C -45 5, -35 -15, -15 -18 C 5 -20, 20 -15, 30 -35"
    
    # Stripes along the spine:
    # 5 dark indigo curved stripes across the tube
    stripes = '''
      <!-- Stripe 1 (tail) -->
      <path d="M -58 6 Q -50 14 -42 22" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
      <!-- Stripe 2 (mid-lower) -->
      <path d="M -38 -8 Q -30 2 -22 12" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
      <!-- Stripe 3 (mid-arch) -->
      <path d="M -18 -26 Q -12 -14 -6 -2" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
      <!-- Stripe 4 (chest) -->
      <path d="M 6 -32 Q 12 -20 18 -8" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
      <!-- Stripe 5 (neck) -->
      <path d="M 18 -46 Q 26 -34 34 -22" stroke="#3730A3" stroke-width="14" stroke-linecap="round"/>
    '''
    
    return spine_d, stripes

print("Pose 1 ready")
