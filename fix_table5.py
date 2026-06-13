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

    if num == 277:
        continue # skip separator

    if 276 <= num <= 316 and num != 277:
        if line.strip() == "":
            new_lines.append(line)
            continue
            
        parts = process_row(line)
        if len(parts) == 9:
            if "Omulunga Radio" in parts[0]:
                # line 297
                # parts: ['Omulunga Radio (Pty)Ltd', 'Namibia', '66.60%', '100.9 MHz', 'Khomas', 'Windhoek', 'Gross Herzog- Satcom Site No', 'Commercial Broadcasting', 'Own']
                city = parts[6].replace(" No", "")
                new_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {city} | No | Commercial Broadcasting Service | {parts[8]} |\n")
            elif "Trinity Broad-" in parts[0]:
                # line 313
                city = parts[6].replace(" No", "")
                new_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {city} | No | Community Broadcasting Service | {parts[8]} |\n")
            else:
                # others
                # parts: [' ', ' ', ' ', '92.1 MHz', 'Omaheke', 'Gobabis', 'Gobabis Water Tower', 'Service', 'Own']
                # we just insert an empty string before parts[8]
                new_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6]} |  |  | {parts[8]} |\n")
        else:
            new_lines.append(line)
        continue

    new_lines.append(line)

with open('docs/gazettes/5037_fixed5.md', 'w') as f:
    f.writelines(new_lines)
