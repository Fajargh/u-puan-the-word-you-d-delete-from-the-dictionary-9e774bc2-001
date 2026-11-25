"""Write the one word to delete from the dictionary to /output/entry.txt.

The pick: "onomatopoeia" — the word for words that sound like what they
mean, famously hard to spell and pronounce, and itself the prime example
of what it describes. Erasing it removes the word that names its own trick.
"""

import os

WORD = "onomatopoeia"


def main() -> None:
    if not WORD.isalpha():
        raise ValueError("entry must be a single word")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
