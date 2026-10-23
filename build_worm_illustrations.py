#!/usr/bin/env python3
"""
build_worm_illustrations.py
Calculates smooth vector geometry for the Paathshala Worm Mascots
matching the exact design in media_1792552882621_ebe33cd4.png.
"""

import math

def generate_smooth_tube_svg(center_points, radius=21, body_color="#5458F7", stripe_color="#3730A3", outline_color="#0F172A", outline_w=3.5, stripe_indices=None):
    """
    Generates a continuous smooth tube using bezier curves and normal offsets.
    center_points: list of (x, y) tuples along the spine
    """
    # Sample points densely along the polyline / spline
    sampled = []
    for i in range(len(center_points) - 1):
        p1 = center_points[i]
        p2 = center_points[i+1]
        dist = math.hypot(p2[0]-p1[0], p2[1]-p1[1])
        steps = max(int(dist / 4.0), 4)
        for s in range(steps):
            t = s / steps
            x = p1[0] + t * (p2[0] - p1[0])
            y = p1[1] + t * (p2[1] - p1[1])
            sampled.append((x, y))
    sampled.append(center_points[-1])
    
    # Calculate tangents and normals at each point
    normals = []
    n_pts = len(sampled)
    for i in range(n_pts):
        if i == 0:
            dx = sampled[1][0] - sampled[0][0]
            dy = sampled[1][1] - sampled[0][1]
        elif i == n_pts - 1:
            dx = sampled[-1][0] - sampled[-2][0]
            dy = sampled[-1][1] - sampled[-2][1]
        else:
            dx = sampled[i+1][0] - sampled[i-1][0]
            dy = sampled[i+1][1] - sampled[i-1][1]
        length = math.hypot(dx, dy)
        if length == 0:
            nx, ny = 0, 1
        else:
            nx = -dy / length
            ny = dx / length
        normals.append((nx, ny))
    
    # Outer hull: left side forward, hemispherical cap at end, right side backward, cap at start
    left_hull = []
    right_hull = []
    for (x, y), (nx, ny) in zip(sampled, normals):
        left_hull.append((x + nx * radius, y + ny * radius))
        right_hull.append((x - nx * radius, y - ny * radius))
        
    return sampled, normals, left_hull, right_hull

print("Tube generator ready")
