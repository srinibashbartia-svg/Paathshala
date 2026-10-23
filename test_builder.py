import os

with open("/Users/srinibashbartia/.gemini/antigravity/scratch/leah_avatar.txt", "r") as f:
    avatar_b64 = f.read().strip()

print("Avatar ready. Length:", len(avatar_b64))
