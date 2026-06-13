import re

with open('docs/gazettes/5201.md', 'r') as f:
    lines = f.readlines()

out_lines = []
for i, line in enumerate(lines):
    if line.startswith('|  | 20 9 27.5 S |  |  | 514 | 26 |  |  |  |  |'):
        continue
    if line.startswith('| Gam |  | 20 43 22.7 E | 3 | 546 | 30 | 50 | 16.99 | 11.3 | Vertical | 216.8 | Otjozondjupa |'):
        out_lines.append('| Gam | 20 9 27.5 S | 20 43 22.7 E | 3 | 514 | 26 | 50 | 16.99 | 11.3 | Vertical | 216.8 | Otjozondjupa |\n')
        out_lines.append('| Gam | 20 9 27.5 S | 20 43 22.7 E | 4 | 546 | 30 | 50 | 16.99 | 11.3 | Vertical | 216.8 | Otjozondjupa |\n')
        continue
    if line.startswith('| Gam Gibeon | 20 9 27.5 S 25 7 2.4 S | 20 43 22.7 E 17 56 22.7 E | 4 1 | 210 | 9 | 50 2000 | 16.99 33.01 | 11.3 | Vertical | 216.8 | Otjozondjupa 140 Hardap |'):
        out_lines.append('| Gibeon | 25 7 2.4 S | 17 56 22.7 E | 1 | 210 | 9 | 2000 | 33.01 | 11.5 | Vertical | 140 | Hardap |\n')
        continue

    # Fix combined Antenna Height and Region: "|  | 140 Hardap |" -> "| 140 | Hardap |"
    # General pattern: |  | [number] [Word] |
    if '|  |' in line and line.strip().endswith('|') and line.startswith('|'):
        # Let's split and fix
        parts = line.split('|')
        if len(parts) >= 3:
            second_last = parts[-2].strip()
            # check if it matches number and word
            m = re.match(r'^([\d\.]+)\s+([A-Za-z\s]+)$', second_last)
            if m and parts[-3].strip() == '':
                parts[-3] = ' ' + m.group(1) + ' '
                parts[-2] = ' ' + m.group(2) + ' '
                line = '|'.join(parts)

    out_lines.append(line)

with open('docs/gazettes/5201.md', 'w') as f:
    f.writelines(out_lines)

print("done")
