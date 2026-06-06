import os
import re
from pathlib import Path

docs_dir = Path("/opt/cran_clean_mds/docs")
files_modified = 0

# Pattern: Starts with number, dot, space. Then a quote, words, quote, then "means", "is", "where", etc.
pattern = re.compile(r"^\d+\.\s+(['\"“‘][A-Za-z0-9\s-]+['\"”’]\s+(?:means|is|where).*)", re.MULTILINE)

for md_file in docs_dir.rglob("*.md"):
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content, count = pattern.subn(r"\1", content)
    
    if count > 0:
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        files_modified += 1
        print(f"Fixed {count} definitions in {md_file.name}")

print(f"Total files modified: {files_modified}")
