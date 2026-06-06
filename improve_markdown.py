import os
import re
from pathlib import Path

docs_dir = Path("docs")

def slugify(text):
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text

for filepath in docs_dir.rglob("*.md"):
    with open(filepath, "r") as f:
        content = f.read()

    # Find all headings
    headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
    
    # We will do case-insensitive exact matching for titles
    heading_titles = {h[1].strip().lower(): h[1].strip() for h in headings}
    
    lines = content.split('\n')
    new_lines = []
    modified = False
    
    # 1. Fix roman numeral indentations (like we did in 5983)
    # If a line starts with exactly 8 spaces, hyphen, and (i), (v), (x), reduce to 4 spaces
    # Actually it's safer to just fix anything that is 8 spaces but preceded by 0-space indent? 
    # Let's be safe and just do TOC linking with case insensitivity first
    
    for i, line in enumerate(lines):
        # 1. TOC Linking
        if i < 400: # Only check first 400 lines for TOC
            m = re.match(r'^(\s*[-*]\s+|\s*\d+\.\s+)(.+)$', line)
            if m:
                prefix = m.group(1)
                title = m.group(2).strip()
                title_clean = re.sub(r'(?:\.+)?\s*\d+$', '', title).strip().lower()
                
                # Check if it matches a heading
                if title_clean in heading_titles and not title.startswith('['):
                    actual_heading = heading_titles[title_clean]
                    slug = slugify(actual_heading)
                    new_line = f"{prefix}[{title}](#{slug})"
                    new_lines.append(new_line)
                    modified = True
                    continue
        
        new_lines.append(line)

    if modified:
        with open(filepath, "w") as f:
            f.write('\n'.join(new_lines))

print("TOC linking improved.")
