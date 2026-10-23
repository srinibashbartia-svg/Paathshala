import os

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/leah_avatar.txt", "r") as f:
    avatar_b64 = f.read().strip()

print(f"Loaded avatar ({len(avatar_b64)} chars)")

# We will generate landing.html, homepage-section.html, and index.html
