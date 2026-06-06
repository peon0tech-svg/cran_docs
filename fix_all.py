import os
import re
from pathlib import Path

docs_dir = Path("docs")
forms_file = Path("Reminder_Forms.txt")

# Regex to find annexures and forms
form_regex = re.compile(r'^(?:#+ )?(?:ANNEXURE\s+[A-Z].*|FORM\s+CRAN.*|Form\s+CRAN.*)', re.IGNORECASE)

# Helper to slugify a header for markdown links
def slugify(text):
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text

forms_found = []

for filepath in docs_dir.rglob("*.md"):
    with open(filepath, "r") as f:
        content = f.read()
    
    # 1. Forms Extraction
    lines = content.split('\n')
    file_forms = []
    for line in lines:
        if form_regex.search(line) and len(line) < 150:
            file_forms.append(line.strip('# ').strip())
    
    if file_forms:
        forms_found.append(f"Gazette/Doc {filepath.stem}:\n" + "\n".join([f"- {f}" for f in file_forms]) + "\n")
    
    # 2. TOC Linking
    # We look for a section likely to be a TOC (usually early in the document, list of sections)
    # A simple approach: If we find a list of items that exactly match headings later in the document.
    headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
    heading_titles = {h[1].strip(): h[1].strip() for h in headings}
    
    # We will look for lines like: "1. Definitions" or "- Definitions"
    # and if "Definitions" is a heading, we replace it with a link.
    new_lines = []
    toc_modified = False
    in_potential_toc = False
    
    for i, line in enumerate(lines):
        # Very basic TOC heuristic: lines near the top (e.g. before line 200)
        # that look like "1. Title" or "- Title" where "Title" is a known heading.
        if i < 300:
            m = re.match(r'^(\s*[-*]\s+|\s*\d+\.\s+)(.+)$', line)
            if m:
                prefix = m.group(1)
                title = m.group(2).strip()
                # Remove trailing dots or page numbers like "Title ...... 5"
                title_clean = re.sub(r'(?:\.+)?\s*\d+$', '', title).strip()
                
                # if title_clean is in heading_titles, and it's not already a link
                if title_clean in heading_titles and not title.startswith('['):
                    slug = slugify(title_clean)
                    new_line = f"{prefix}[{title}](#{slug})"
                    new_lines.append(new_line)
                    toc_modified = True
                    continue
        new_lines.append(line)
        
    if toc_modified:
        with open(filepath, "w") as f:
            f.write('\n'.join(new_lines))

if forms_found:
    with open(forms_file, "a") as f:
        f.write("\n" + "\n".join(forms_found))
print(f"Processed files. Forms appended to Reminder_Forms.txt")
