import re

with open('docs/gazettes/5037.md', 'r') as f:
    lines = f.readlines()

new_lines = []
skip_lines = False

def process_row(line):
    # Split by | and strip whitespace
    parts = [p.strip() for p in line.split('|')]
    # Remove first and last empty strings (due to leading/trailing |)
    if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
        parts = parts[1:-1]
    return parts

for i, line in enumerate(lines):
    # Note: i is 0-indexed, so line 396 is lines[395]
    num = i + 1
    
    if num == 396:
        # |  |  | 101.7 MHz | Oshikoto | Tsumeb | Tsumeb Mine Tower | Own |  |
        new_lines.append("|  |  |  | 101.7 MHz | Oshikoto | Tsumeb | Tsumeb Mine Tower |  |  | Own |\n")
        continue
    if num == 397:
        # skip separator
        continue
    if 398 <= num <= 401:
        # |  |  | 99.8 MHz | Erongo | Walvis Bay | Telecom Tower |  | Own |
        parts = process_row(line)
        # It has 8 parts. We need 10.
        # col 1,2: empty
        # col 3: empty
        # col 4: freq
        # col 5: region
        # col 6: district
        # col 7: city
        # col 8: empty
        # col 9: empty
        # col 10: Own
        if len(parts) >= 8:
            new_lines.append(f"|  |  |  | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} |  |  | {parts[7]} |\n")
        continue

    if num == 402:
        new_lines.append("| Namibian Broadcasting Corporation |  |  |  |  |  |  | No | Public Broadcasting Service |  |\n")
        continue

    if num == 403:
        new_lines.append("| NBC - Afri- kaans | Namibia | 100% | 88.9 MHz | Omaheke | Gobabis | Aminius NBC Tower |  |  | Own |\n")
        continue

    if 404 <= num <= 428:
        # 8 columns
        parts = process_row(line)
        if len(parts) == 8:
            new_lines.append(f"| {parts[0]} |  |  | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} |  |  | {parts[7]} |\n")
        else:
            new_lines.append(line)
        continue

    if num == 429:
        new_lines.append("| NBC - Afri- kaans |  |  | 92.5 MHz | Karas | Karasburg | Aussenkehr NBC Tower |  |  | Own |\n")
        continue
    if num == 430 or num == 431:
        continue # skip
    if num == 433:
        continue # skip inner separator

    if 432 <= num <= 677 and num != 433:
        parts = process_row(line)
        if len(parts) == 6:
            new_lines.append(f"| {parts[0]} |  |  | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} |  |  | {parts[5]} |\n")
        elif len(parts) == 7 and parts[0] == "" and parts[1] == "kaans":
            # wait, line 520 and 521?
            pass
            new_lines.append(line)
        else:
            new_lines.append(line)
        continue

    new_lines.append(line)

with open('docs/gazettes/5037_fixed.md', 'w') as f:
    f.writelines(new_lines)
