import os
import re
from pathlib import Path

docs_dir = Path("docs")

for filepath in docs_dir.rglob("*.md"):
    with open(filepath, "r") as f:
        content = f.read()

    # Revert the roman numeral indentation issue from previous script
    # It changed "- (i)" to "        - (i)" incorrectly in some places where it should have been "    - (i)"
    # A safe bet: if we see "        - (i)", "        - (v)", "        - (x)", change it to "    - (i)"
    
    lines = content.split('\n')
    new_lines = []
    modified = False
    for line in lines:
        if re.match(r'^        - \(([ivx])\)$', line):
            new_line = re.sub(r'^        - \(([ivx])\)$', r'    - (\1)', line)
            new_lines.append(new_line)
            modified = True
        else:
            new_lines.append(line)

    if modified:
        with open(filepath, "w") as f:
            f.write('\n'.join(new_lines))

print("Roman numeral indentation fixed globally.")
