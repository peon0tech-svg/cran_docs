import re

with open('docs/gazettes/5214.md', 'r') as f:
    content = f.read()

# 1. Fix the table separators (misaligned tables)
table_start = content.find("| ITU Region 1 allocations")
table_end = content.find("## ITU DEFINITIONS")

table_content = content[table_start:table_end]

lines = table_content.split('\n')
new_lines = []
separator_found = False
for line in lines:
    if line.strip().startswith('|---'):
        if not separator_found:
            new_lines.append(line)
            separator_found = True
    elif line.strip() == "":
        continue
    else:
        if line.strip().startswith('|'):
            parts = [p.strip() for p in line.strip().split('|')]
            if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
                parts = parts[1:-1]
            if len(parts) == 4:
                parts.insert(3, " ")
            elif len(parts) < 5:
                while len(parts) < 5:
                    parts.append(" ")
            elif len(parts) > 5:
                # join the extra parts into the 5th column so data isn't lost
                parts[4] = " ".join(parts[4:]).strip()
                parts = parts[:5]
            new_line = "| " + " | ".join(parts) + " |"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

fixed_table = '\n'.join(new_lines)
content = content[:table_start] + fixed_table + "\n\n" + content[table_end:]

with open('docs/gazettes/5214.md', 'w') as f:
    f.write(content)

