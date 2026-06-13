import re

with open("docs/gazettes/5683.md", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    # Check lowercase continuation
    if i > 0 and len(line) > 0 and line[0].islower() and not line.startswith("http") and not line.startswith("|"):
        prev = lines[i-1].strip()
        # ignore previous lines that are headers or tables
        if prev and not prev.endswith((".", ":", ";", "!", "?", ">", "|", "-", "*")) and not prev.startswith("#"):
            print(f"Broken: Line {i}: {prev}")
            print(f"        Line {i+1}: {line}\n")
