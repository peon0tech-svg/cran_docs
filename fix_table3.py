import re

with open('docs/gazettes/5037.md', 'r') as f:
    lines = f.readlines()

new_lines = []

def process_row(line):
    parts = [p.strip() for p in line.split('|')]
    if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
        parts = parts[1:-1]
    return parts

for i, line in enumerate(lines):
    num = i + 1

    if num == 152:
        continue # skip separator

    if 151 <= num <= 197 and num != 152:
        parts = process_row(line)
        if len(parts) == 7:
            if "Wireless" in parts[0]:
                # | Wireless Technologies Namibia (Pty) Ltd | Class ECS | Namibia | Namibia | 2505.000 - 2525.000 MHz | MOBILE ... | Yes |
                # Add 100% as 5th col
                new_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | 100% | {parts[4]} | {parts[5]} | {parts[6]} |\n")
            else:
                # | | | | | freq | service | |
                new_lines.append(f"|  |  |  |  |  | {parts[4]} | {parts[5]} | {parts[6]} |\n")
        else:
            new_lines.append(line)
        continue

    new_lines.append(line)

with open('docs/gazettes/5037_fixed3.md', 'w') as f:
    f.writelines(new_lines)
