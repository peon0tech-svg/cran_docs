import re

with open("docs/gazettes/5683.md", "r") as f:
    lines = f.readlines()

table_lines = lines[400:460]

# Parse markdown table
rows = []
for line in table_lines:
    if line.strip() and not line.strip().startswith("|-"):
        # Split by | and strip
        cells = [c.strip() for c in line.strip().split("|")[1:-1]]
        rows.append(cells)

# Now we need to handle the fact that some rows might be split across lines.
# Actually, looking at the output, the table lines might wrap.
