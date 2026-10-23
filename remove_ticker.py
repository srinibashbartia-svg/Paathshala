import re

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "r") as f:
    content = f.read()

# 1. Remove the entire .hero-ticker-section markup
content = re.sub(
    r'\s*<!-- =========================================================================\s*HIGHLIGHT REELS TICKER[\s\S]*?<\/section>',
    '\n    </section>',
    content
)

# 2. Clean up ticker CSS
content = re.sub(
    r'\/\* =========================================================================\s*HIGHLIGHT REELS TICKER[\s\S]*?\/\* =========================================================================\s*DEFAULT \/ ORIGINAL CURTAIN TRANSITION ENGINE',
    '/* =========================================================================\n           DEFAULT / ORIGINAL CURTAIN TRANSITION ENGINE',
    content
)

# 3. Clean up video JS
content = re.sub(
    r'\/\/ 3\. Autoplay All Muted Videos[\s\S]*?window\.addEventListener\(\'load\', initMutedVideos\);',
    '',
    content
)

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/paathshala-guided-learning/landing.html", "w") as f:
    f.write(content)

print("Ticker completely removed from landing.html!")
