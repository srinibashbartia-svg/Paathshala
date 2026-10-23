import sys, os

portal_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paathshala Guided Learning · Prototype Hub</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #5F5AF6;
            --coral: #FF5A36;
            --dark: #0F172A;
            --cream: #FAF8F5;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: #0B0F19;
            color: #F8FAFC;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* TOP HUB NAVIGATION */
        header.hub-header {
            background: #111827;
            border-bottom: 2px solid #1F2937;
            padding: 14px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }
        .hub-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .hub-logo {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            background: #5F5AF6;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            color: #FFFFFF;
            font-weight: 900;
        }
        .hub-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.25rem;
        }
        .hub-title span {
            color: #93C5FD;
            font-size: 0.85rem;
            font-weight: 600;
            margin-left: 6px;
            background: rgba(255, 255, 255, 0.08);
            padding: 2px 8px;
            border-radius: 6px;
        }

        /* PROTOTYPE TABS */
        .tab-switcher {
            display: flex;
            background: #1F2937;
            padding: 4px;
            border-radius: 12px;
            gap: 4px;
        }
        .tab-btn {
            background: none;
            border: none;
            color: #94A3B8;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 0.88rem;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.15s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .tab-btn:hover {
            color: #FFFFFF;
            background: rgba(255, 255, 255, 0.05);
        }
        .tab-btn.active {
            background: #5F5AF6;
            color: #FFFFFF;
            box-shadow: 0 2px 8px rgba(95, 90, 246, 0.4);
        }

        /* DEVICE CONTROLS */
        .hub-controls {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .device-toggle-group {
            display: flex;
            background: #1F2937;
            padding: 3px;
            border-radius: 10px;
            gap: 2px;
        }
        .device-btn {
            background: none;
            border: none;
            color: #94A3B8;
            font-size: 0.8rem;
            font-weight: 700;
            padding: 6px 12px;
            border-radius: 7px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s;
        }
        .device-btn:hover {
            color: #FFFFFF;
        }
        .device-btn.active {
            background: #374151;
            color: #FFFFFF;
        }
        .btn-open-external {
            background: #FF5A36;
            color: #FFFFFF;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.85rem;
            padding: 7px 14px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s;
        }
        .btn-open-external:hover {
            background: #E84D29;
            transform: translateY(-1px);
        }

        /* IFRAME STAGE */
        .preview-stage {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #0B0F19;
            padding: 16px;
            overflow: hidden;
            position: relative;
        }
        .iframe-container {
            width: 100%;
            height: calc(100vh - 120px);
            background: #FFFFFF;
            border-radius: 16px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
            overflow: hidden;
            transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
            display: block;
        }

        /* BOTTOM BRIEF INFO BAR */
        .info-strip {
            background: #111827;
            border-top: 1px solid #1F2937;
            padding: 10px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.82rem;
            color: #94A3B8;
            flex-wrap: wrap;
            gap: 10px;
        }
        .info-strip strong {
            color: #F8FAFC;
        }
        .info-strip a {
            color: #93C5FD;
            text-decoration: none;
        }
        .info-strip a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <!-- HUB HEADER -->
    <header class="hub-header">
        <div class="hub-brand">
            <div class="hub-logo">✦</div>
            <div class="hub-title">
                Paathshala Guided Learning <span>Prototype Portal</span>
            </div>
        </div>

        <!-- TABS TO SWITCH BETWEEN PROTOTYPES -->
        <div class="tab-switcher">
            <button class="tab-btn active" onclick="loadPrototype('/landing.html', this, 'Prototype #1 · Guided Learning Landing Page')">
                <span>🚀 Prototype #1: Landing Page</span>
            </button>
            <button class="tab-btn" onclick="loadPrototype('/homepage-section.html', this, 'Prototype #2 · Homepage Guided Learning Section')">
                <span>🏠 Prototype #2: Homepage Section</span>
            </button>
            <button class="tab-btn" onclick="loadPrototype('/paathshala-profile-prototype.html', this, 'Previous Profile Redesign')">
                <span>👤 Leah Alexander Profile</span>
            </button>
        </div>

        <!-- DEVICE VIEWPORT SELECTOR & OPEN BUTTON -->
        <div class="hub-controls">
            <div class="device-toggle-group">
                <button class="device-btn active" onclick="setDevice('100%', this)">🖥 Desktop</button>
                <button class="device-btn" onclick="setDevice('768px', this)">📱 Tablet</button>
                <button class="device-btn" onclick="setDevice('390px', this)">📲 Mobile</button>
            </div>
            <a href="/landing.html" target="_blank" class="btn-open-external" id="btnExternal">
                <span>Open in Tab</span>
                <span>↗</span>
            </a>
        </div>
    </header>

    <!-- PREVIEW STAGE -->
    <main class="preview-stage">
        <div class="iframe-container" id="iframeWrapper">
            <iframe src="/landing.html" id="previewIframe"></iframe>
        </div>
    </main>

    <!-- INFO BAR -->
    <footer class="info-strip">
        <div>
            <span id="activePrototypeLabel"><strong>Prototype #1: Guided Learning Landing Page</strong></span>
            <span>· Inspired by AI Predictor Bhavishya Page (`paathshala.app/ai-career-predictor`)</span>
        </div>
        <div style="display:flex; gap:16px;">
            <span>Reference Reel: <a href="https://paathshala.app/reels/6acca1a0fa97e5183b039237-r1" target="_blank">Nuclear Glue by Leah Alexander ↗</a></span>
            <span>Paathshala Production: <a href="https://paathshala.app/" target="_blank">paathshala.app ↗</a></span>
        </div>
    </footer>

    <script>
        function loadPrototype(url, btn, label) {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById('previewIframe').src = url;
            document.getElementById('btnExternal').href = url;
            document.getElementById('activePrototypeLabel').innerHTML = `<strong>${label}</strong>`;
        }

        function setDevice(width, btn) {
            document.querySelectorAll('.device-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const wrapper = document.getElementById('iframeWrapper');
            wrapper.style.width = width;
            if (width === '390px') {
                wrapper.style.borderRadius = '32px';
                wrapper.style.border = '8px solid #1E293B';
            } else if (width === '768px') {
                wrapper.style.borderRadius = '20px';
                wrapper.style.border = '6px solid #1E293B';
            } else {
                wrapper.style.borderRadius = '16px';
                wrapper.style.border = 'none';
            }
        }
    </script>
</body>
</html>
'''

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/index.html", "w") as f:
    f.write(portal_html)

print("Generated index.html successfully!")
