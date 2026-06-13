import re

with open("docs/gazettes/5683.md", "r") as f:
    lines = f.readlines()

table_lines = lines[400:460]

rows = []
for line in table_lines:
    if line.strip() and not line.strip().startswith("|-"):
        cells = [c.strip() for c in line.strip().split("|")[1:-1]]
        rows.append(cells)

# Now we need to determine the dimensions.
max_cols = max(len(r) for r in rows)
for r in rows:
    while len(r) < max_cols:
        r.append("")

# Transpose
transposed = []
for c in range(max_cols):
    t_row = []
    for r in range(len(rows)):
        t_row.append(rows[r][c])
    transposed.append(t_row)

for r in transposed[:5]:
    print("| " + " | ".join(r) + " |")

