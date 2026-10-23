import re

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "r") as f:
    content = f.read()

# 1. Restore Scene CSS with full transitions
scene_css_old = r'\.scene\s*\{[\s\S]*?\.scene:not\(\.on\):not\(\.out\)\s*\*[\s\S]*?\}'
scene_css_new = '''.scene {
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
        }

        .scene.on {
            opacity: 1;
            z-index: 3;
            pointer-events: auto;
            clip-path: circle(150% at var(--o, 50% 50%));
            transform: none;
        }

        .scene.out {
            opacity: 1;
            z-index: 2;
            clip-path: circle(150% at 50% 50%);
            transform: scale(0.88);
            filter: brightness(0.4) blur(6px);
            transition: transform 1.2s, filter 1.2s;
        }

        .scene:not(.on):not(.out) * {
            transition-duration: 0s !important;
            transition-delay: 0s !important;
        }'''

content = re.sub(scene_css_old, scene_css_new, content)

# 2. Restore Mask and Caption animations
mask_cap_old = r'\.mask\s*\{[\s\S]*?\.on \.cap\s*\{[\s\S]*?\}'
mask_cap_new = '''.mask {
            clip-path: inset(0 100% 0 0);
            transition: clip-path 1s cubic-bezier(.7, 0, .2, 1);
        }

        .on .mask {
            clip-path: inset(0 0 0 0);
            transition-delay: 0.55s;
        }

        .cap {
            color: var(--mut);
            font-size: clamp(15px, 2vw, 20px);
            margin-top: 16px;
            max-width: 46ch;
            opacity: 0;
            transform: translateY(20px);
            transition: 0.8s 0.7s;
            line-height: 1.5;
        }

        .on .cap {
            opacity: 1;
            transform: none;
            transition-delay: 1s;
        }'''

content = re.sub(mask_cap_old, mask_cap_new, content)

# 3. Restore Whiteboard & Tile animations (Teacher & Student spring in, 2x+3=11 at 1.3s, x=4 at 2.3s)
tile_wb_old = r'\.tile\s*\{[\s\S]*?\.on \.t2\s*\{[\s\S]*?\}'
tile_wb_new = '''.tile {
            transform-box: fill-box;
            transform-origin: center;
            transform: scale(0);
            transition: transform 0.7s cubic-bezier(.3, 1.5, .4, 1) 0.6s;
        }

        .on .tile {
            transform: none;
        }

        .wb text {
            font-family: 'Outfit', sans-serif;
            font-size: 30px;
            font-weight: 800;
            opacity: 0;
            transition: opacity 0.5s;
        }

        .on .t1 {
            opacity: 1;
            transition-delay: 1.3s;
        }

        .on .t2 {
            opacity: 1;
            transition-delay: 2.3s;
        }'''

content = re.sub(tile_wb_old, tile_wb_new, content)

# 4. Restore Path Curve drawing (2.6s stroke drawing) and sequential node popping
curve_old = r'svg\.tg\s*\{[\s\S]*?\.tg \.em\s*\{[\s\S]*?\}'
curve_new = '''svg.tg {
            width: min(94vw, 900px);
            overflow: visible;
            margin-top: 18px;
        }

        .tg path {
            fill: none;
            stroke: var(--g);
            stroke-width: 8;
            stroke-linecap: round;
            stroke-dasharray: 1;
            stroke-dashoffset: 1;
            transition: stroke-dashoffset 2.6s linear;
        }

        .on .tg path {
            stroke-dashoffset: 0;
        }

        .tg circle {
            fill: var(--card-bg);
            stroke: var(--border-dark);
            stroke-width: 2.5;
            transform-box: fill-box;
            transform-origin: center;
            transform: scale(0);
            transition: transform 0.6s cubic-bezier(.3, 1.8, .4, 1) calc(var(--n) * 0.85s);
        }

        .on .tg circle {
            transform: scale(1);
        }

        .tg text {
            fill: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 22px;
            text-anchor: middle;
            opacity: 0;
            transition: opacity 0.6s calc(var(--n) * 0.85s + 0.2s);
        }

        .on .tg text {
            opacity: 1;
        }

        .tg .em {
            font-size: 26px;
            fill: #000000;
        }'''

content = re.sub(curve_old, curve_new, content)

# 5. Restore 3D Cards fanning out and Row SVG springing
cards_row_old = r'\.cards\s*\{[\s\S]*?\.on \.row svg\s*\{[\s\S]*?\}'
cards_row_new = '''.cards {
            display: flex;
            justify-content: center;
            margin: 24px 0 8px;
            perspective: 900px;
        }

        .tc {
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
            border: 2.5px solid var(--border-dark);
            box-shadow: 4px 4px 0px var(--border-dark);
        }

        .on .tc {
            opacity: 1;
            margin: 0 8px;
            transform: rotate(var(--r)) translateY(var(--y));
        }

        .row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 2vw;
        }

        .row svg {
            width: clamp(70px, 14vw, 150px);
            transform: scale(0);
            transition: transform 0.8s cubic-bezier(.3, 1.5, .4, 1) 0.9s;
        }

        .on .row svg {
            transform: none;
        }'''

content = re.sub(cards_row_old, cards_row_new, content)

# 6. Restore original JavaScript go(i) timing engine with 450ms curtain wipe
js_go_old = r'var d = 0;[\s\S]*?setTimeout\(function\(\) \{\s*sc\.forEach\(function\(e, j\) \{\s*if \(j !== cur\) e\.classList\.remove\("out"\);\s*\}\);\s*\}, 600\);\s*\}, d\);'
js_go_new = '''var d = 0;
            if (prev >= 0) {
                d = 450;
                cu.classList.remove("go");
                void cu.offsetWidth;
                cu.classList.add("go");
            }

            to = setTimeout(function() {
                sc.forEach(function(e, j) {
                    e.classList.remove("out");
                    if (j === prev) {
                        e.classList.remove("on");
                        e.classList.add("out");
                    } else if (j !== i) {
                        e.classList.remove("on");
                    }
                });
                sc[i].classList.add("on");
                setTimeout(function() {
                    sc.forEach(function(e) { e.classList.remove("out"); });
                }, 1500);
            }, d);'''

content = re.sub(js_go_old, js_go_new, content)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(content)

print("Restored all rich step animations in landing.html!")
