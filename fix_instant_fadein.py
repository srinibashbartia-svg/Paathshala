import re

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "r") as f:
    content = f.read()

# Replace delayed transition CSS with instant fade-in transitions

# 1. Mask headline reveal: instant (no 0.55s delay)
content = re.sub(
    r'\.mask\s*\{[\s\S]*?\.on \.mask\s*\{[\s\S]*?\}',
    '''.mask {
            clip-path: inset(0 100% 0 0);
            transition: clip-path 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .on .mask {
            clip-path: inset(0 0 0 0);
            transition-delay: 0.05s;
        }''',
    content
)

# 2. Caption: instant fade in (no 0.9s delay)
content = re.sub(
    r'\.cap\s*\{[\s\S]*?\.on \.cap\s*\{[\s\S]*?\}',
    '''.cap {
            color: var(--mut);
            font-size: clamp(15px, 2vw, 20px);
            margin-top: 16px;
            max-width: 46ch;
            opacity: 0;
            transform: translateY(12px);
            transition: opacity 0.35s ease, transform 0.35s ease;
            line-height: 1.5;
        }

        .on .cap {
            opacity: 1;
            transform: none;
            transition-delay: 0.08s;
        }''',
    content
)

# 3. Tile & whiteboard text: instant fade in (no 1.3s / 2.3s delays)
content = re.sub(
    r'\.tile\s*\{[\s\S]*?\.on \.t2\s*\{[\s\S]*?\}',
    '''.tile {
            transform-box: fill-box;
            transform-origin: center;
            transform: scale(0.9);
            opacity: 0;
            transition: transform 0.35s cubic-bezier(.3, 1.4, .4, 1), opacity 0.35s ease;
        }

        .on .tile {
            transform: none;
            opacity: 1;
        }

        .wb text {
            font-family: 'Outfit', sans-serif;
            font-size: 30px;
            font-weight: 800;
            opacity: 0;
            transition: opacity 0.25s ease;
        }

        .on .t1 {
            opacity: 1;
            transition-delay: 0.1s;
        }

        .on .t2 {
            opacity: 1;
            transition-delay: 0.18s;
        }''',
    content
)

# 4. Curve nodes & text: snappy reveal without multi-second delays
content = re.sub(
    r'svg\.tg\s*\{[\s\S]*?\.tg \.em\s*\{[\s\S]*?\}',
    '''svg.tg {
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
            transition: stroke-dashoffset 0.8s ease;
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
            transition: transform 0.35s cubic-bezier(.3, 1.8, .4, 1) calc(var(--n) * 0.1s);
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
            transition: opacity 0.3s calc(var(--n) * 0.1s + 0.05s);
        }

        .on .tg text {
            opacity: 1;
        }

        .tg .em {
            font-size: 26px;
            fill: #000000;
        }''',
    content
)

# 5. Cards & Row SVG: instant fade in
content = re.sub(
    r'\.tc\s*\{[\s\S]*?\.on \.tc\s*\{[\s\S]*?\}',
    '''.tc {
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
            transform: translateY(30px);
            opacity: 0;
            transition: transform 0.4s cubic-bezier(.2, .9, .2, 1), opacity 0.35s ease;
            position: relative;
            border: 2.5px solid var(--border-dark);
            box-shadow: 4px 4px 0px var(--border-dark);
        }

        .on .tc {
            opacity: 1;
            margin: 0 8px;
            transform: rotate(var(--r)) translateY(var(--y));
        }''',
    content
)

content = re.sub(
    r'\.row svg\s*\{[\s\S]*?\.on \.row svg\s*\{[\s\S]*?\}',
    '''.row svg {
            width: clamp(70px, 14vw, 150px);
            transform: scale(0.6);
            opacity: 0;
            transition: transform 0.4s cubic-bezier(.3, 1.5, .4, 1) 0.05s, opacity 0.3s ease;
        }

        .on .row svg {
            transform: none;
            opacity: 1;
        }''',
    content
)

# 6. Scene transition: instantaneous fade-in and smooth scene activation
content = re.sub(
    r'\.scene\s*\{[\s\S]*?\.scene\.out\s*\{[\s\S]*?\}',
    '''.scene {
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
            transform: scale(1.08);
            transition: clip-path 0.8s cubic-bezier(.7, 0, .2, 1), transform 0.8s cubic-bezier(.2, .8, .2, 1), opacity 0.35s ease;
        }

        .scene.on {
            opacity: 1;
            z-index: 3;
            pointer-events: auto;
            clip-path: circle(150% at var(--o, 50% 50%));
            transform: none;
        }

        .scene.out {
            opacity: 0;
            z-index: 2;
            clip-path: circle(150% at var(--o, 50% 50%));
            transform: scale(0.95);
            transition: transform 0.6s ease, opacity 0.3s ease;
        }''',
    content
)

# 7. JavaScript curtain and scene swap: trigger scene activation right at midpoint (220ms instead of waiting 450ms)
# and when scrolling in either direction, previous elements fade in instantly!
js_search = r'var d = 0;[\s\S]*?setTimeout\(function\(\) \{\s*sc\.forEach\(function\(e\) \{ e\.classList\.remove\("out"\); \};\s*\}, 1500\);\s*\}, d\);'
js_replace = '''var d = 0;
            if (prev >= 0) {
                d = 200; // Switch at curtain apex so elements are already fading in immediately
                cu.classList.remove("go");
                void cu.offsetWidth;
                cu.classList.add("go");
            }

            to = setTimeout(function() {
                sc.forEach(function(e, j) {
                    if (j === i) {
                        e.classList.remove("out");
                        e.classList.add("on");
                    } else if (j === prev) {
                        e.classList.remove("on");
                        e.classList.add("out");
                    } else {
                        e.classList.remove("on", "out");
                    }
                });
                setTimeout(function() {
                    sc.forEach(function(e, j) {
                        if (j !== cur) e.classList.remove("out");
                    });
                }, 600);
            }, d);'''

content = re.sub(js_search, js_replace, content)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(content)

print("Updated landing.html with instant element fade-in!")
