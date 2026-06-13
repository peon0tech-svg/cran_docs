import re

with open("docs/gazettes/5683.md", "r") as f:
    lines = f.readlines()

# The table is from line 401 to 460
table_lines = lines[400:460]

rows = []
for line in table_lines:
    if line.strip() and not line.strip().startswith("|-"):
        cells = [c.strip() for c in line.strip().split("|")[1:-1]]
        rows.append(cells)

max_cols = max(len(r) for r in rows)
for r in rows:
    while len(r) < max_cols:
        r.append("")

transposed = []
for c in range(max_cols):
    t_row = []
    for r in range(len(rows)):
        t_row.append(rows[r][c])
    transposed.append(t_row)

new_table = []
for i, r in enumerate(transposed):
    new_table.append("| " + " | ".join(r) + " |\n")
    if i == 0:
        new_table.append("|" + "|".join(["---"] * len(r)) + "|\n")

lines = lines[:400] + new_table + lines[460:]

with open("docs/gazettes/5683.md", "w") as f:
    f.writelines(lines)

