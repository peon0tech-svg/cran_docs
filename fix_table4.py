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

    if num == 58:
        continue # skip separator
    if num == 112:
        continue # skip separator

    if 57 <= num <= 110 and num != 58:
        parts = process_row(line)
        if len(parts) == 6:
            if "PowerCom" in parts[0]:
                new_lines.append(f"| {parts[0]} | {parts[1]} | Namibia | Namibia | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} |\n")
            else:
                new_lines.append(f"|  |  |  |  |  | {parts[3]} | {parts[4]} | {parts[5]} |\n")
        else:
            new_lines.append(line)
        continue

    new_lines.append(line)

with open('docs/gazettes/5037_fixed4.md', 'w') as f:
    f.writelines(new_lines)
