"""Entry for make.fun bounty "Your Agent in One Emoji".

Entry text (1 character, limit: 1 to 16 characters).
The entry is a single emoji and nothing else, no trailing newline.
"""

import os

ENTRY = "🤖"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
