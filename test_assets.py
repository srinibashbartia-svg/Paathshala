import os

avatar_file = "/Users/srinibashbartia/.gemini/antigravity/scratch/leah_avatar.txt"
if os.path.exists(avatar_file):
    with open(avatar_file, "r") as f:
        avatar_b64 = f.read().strip()
    print("Leah avatar b64 length:", len(avatar_b64))
else:
    print("Avatar file not found")
