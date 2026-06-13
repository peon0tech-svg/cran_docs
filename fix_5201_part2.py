import re

with open('docs/gazettes/5201.md', 'r') as f:
    lines = f.readlines()

out_lines = []
for line in lines:
    if "Rietfontein" in line and "1 2" in line and "650 626" in line:
        out_lines.append("| Rietfontein | 21 51 2.0 S | 20 45 21.0 E | 1 | 650 | 43 | 1000 | 30.00 | 12.6 | Vertical | 70.7 | Omaheke |\n")
        out_lines.append("| Rietfontein | 21 51 2.0 S | 20 45 21.0 E | 2 | 626 | 40 | 1000 | 30.00 | 12.6 | Vertical | 70.7 | Omaheke |\n")
        continue
    if "Rietfontein Rietfontein" in line and "594" in line:
        out_lines.append("| Rietfontein | 21 51 2.0 S | 20 45 21.0 E | 3 | 594 | 36 | 1000 | 30.00 | 12.6 | Vertical | 70.7 | Omaheke |\n")
        continue
        
    if "Tsumkwe Bay" in line and "3 4" in line and "658 562" in line:
        out_lines.append("| Tsumkwe Bay | 19 35 36.0 S | 20 30 8.0 E | 3 | 658 | 44 | 100 | 20.00 | 10.5 | Horizontal | 92.42 | Otjozondjupa |\n")
        out_lines.append("| Tsumkwe Bay | 19 35 36.0 S | 20 30 8.0 E | 4 | 562 | 32 | 100 | 20.00 | 10.5 | Horizontal | 92.42 | Otjozondjupa |\n")
        continue
    if "Tsumkwe Bay |  |" in line and "20 30 8.0 E" in line:
        # this line was an artifact
        continue
        
    if "Uis | 21 13 21.6 S | 14 53 5.1 E | 1 | 490" in line and "Horizontal |  |  |" in line:
        out_lines.append("| Uis | 21 13 21.6 S | 14 53 5.1 E | 1 | 490 | 23 | 100 | 20.00 | 10.5 | Horizontal | 62.42 | Erongo |\n")
        continue
        
    if "Uis | 21 13 21.6 S | 14 53 5.1 E | 2 | 594 | 36 | 100 | 20.00 | 10.5 | Horizontal | 62.42 | Erongo |" in line:
        out_lines.append(line)
        continue

    out_lines.append(line)

with open('docs/gazettes/5201.md', 'w') as f:
    f.writelines(out_lines)
print("done")
