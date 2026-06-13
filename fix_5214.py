import re

with open('docs/gazettes/5214.md', 'r') as f:
    lines = f.readlines()

in_table = False
bad_cols = 0
total_table_lines = 0

for i, line in enumerate(lines):
    if "| ITU Region 1" in line:
        in_table = True
        continue
    if in_table and line.strip() == "":
        continue
    if in_table and line.strip().startswith('|'):
        if line.strip().startswith('|---'):
            continue
        parts = [p.strip() for p in line.split('|')]
        if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
            parts = parts[1:-1]
        
        total_table_lines += 1
        if len(parts) != 5:
            bad_cols += 1

print(f"Total table lines: {total_table_lines}")
print(f"Bad column lines: {bad_cols}")
