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

    parts = process_row(line)
    if len(parts) == 9:
        if line.strip().startswith('|---'):
            continue # skip separator
            
        if "Omulunga Radio" in parts[0]:
            city = parts[6].replace(" No", "")
            new_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {city} | No | Commercial Broadcasting Service | {parts[8]} |\n")
        elif "Trinity Broad-" in parts[0]:
            city = parts[6].replace(" No", "")
            new_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {city} | No | Community Broadcasting Service | {parts[8]} |\n")
        else:
            new_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6]} |  |  | {parts[8]} |\n")
        continue

    new_lines.append(line)

with open('docs/gazettes/5037_fixed6.md', 'w') as f:
    f.writelines(new_lines)
