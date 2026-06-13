import re

with open("docs/gazettes/5092.md", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    # If a line starts with a lowercase letter and previous line doesn't end with punctuation
    if i > 0 and len(line) > 0 and line[0].islower() and not line.startswith("http"):
        prev = lines[i-1].strip()
        if prev and not prev.endswith((".", ":", ";", "!", "?", ">", "|", "-", "*")):
            # It might be a broken sentence
            print(f"Line {i}: {prev}")
            print(f"Line {i+1}: {line}\n")

