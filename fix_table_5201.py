import re

with open('/opt/cran_clean_mds/docs/gazettes/5201.md', 'r') as f:
    lines = f.readlines()

new_lines = []
in_table = False
table_header = None
for i, line in enumerate(lines):
    if line.startswith('| Site Name | Latitude |'):
        in_table = True
        new_lines.append(line)
        continue
    
    if in_table:
        if line.strip() == '':
            new_lines.append(line)
            continue
            
        if line.startswith('|--'):
            if i > 310: # This is a spurious separator
                continue
            new_lines.append(line)
            continue
            
        if line.startswith('|'):
            # Count columns
            cols = [c.strip() for c in line.split('|')][1:-1]
            if len(cols) == 12:
                new_lines.append(line)
            elif len(cols) == 10:
                # | 10 Horizontal | 125 Caprivi | -> | 10 | Horizontal | 125 | Caprivi |
                # The 9th col is "X Horizontal/Vertical"
                # The 10th col is "Y Region"
                new_cols = cols[:8]
                col9 = cols[8]
                col10 = cols[9]
                
                m9 = re.match(r'^([\d\.]+)\s+(Horizontal|Vertical)$', col9)
                m10 = re.match(r'^([\d\.]+)\s+(.*)$', col10)
                
                if m9 and m10:
                    new_cols.extend([m9.group(1), m9.group(2), m10.group(1), m10.group(2)])
                    new_lines.append('| ' + ' | '.join(new_cols) + ' |\n')
                elif col9 == '' and col10 == '':
                    # empty row?
                    new_lines.append(line)
                else:
                    # try to split by space anyway? Let's check other variations
                    m9_2 = re.split(r'\s+(Horizontal|Vertical)\s*', col9)
                    if len(m9_2) > 1:
                        new_cols.append(m9_2[0])
                        new_cols.append(m9_2[1])
                    else:
                        new_cols.append(col9)
                        new_cols.append('')
                        
                    m10_2 = re.split(r'\s+', col10, 1)
                    if len(m10_2) > 1:
                        new_cols.append(m10_2[0])
                        new_cols.append(m10_2[1])
                    else:
                        new_cols.append(col10)
                        new_cols.append('')
                    
                    if len(new_cols) == 12:
                        new_lines.append('| ' + ' | '.join(new_cols) + ' |\n')
                    else:
                        new_lines.append(line) # fallback
            elif len(cols) == 11:
                # Sometimes it might be 11 columns?
                # Check where the merge is
                if 'Horizontal' in cols[8] or 'Vertical' in cols[8]:
                    new_cols = cols[:8]
                    col9 = cols[8]
                    m9 = re.match(r'^([\d\.]+)\s+(Horizontal|Vertical)$', col9)
                    if m9:
                        new_cols.extend([m9.group(1), m9.group(2)])
                    else:
                        new_cols.extend([col9, ''])
                    new_cols.extend(cols[9:])
                    new_lines.append('| ' + ' | '.join(new_cols) + ' |\n')
                elif 'Horizontal' in cols[9] or 'Vertical' in cols[9]:
                    new_cols = cols[:9]
                    col10 = cols[9]
                    m10 = re.match(r'^([\d\.]+)\s+(Horizontal|Vertical)$', col10)
                    if m10:
                        new_cols.extend([m10.group(1), m10.group(2)])
                    else:
                        new_cols.extend([col10, ''])
                    new_cols.extend(cols[10:])
                    new_lines.append('| ' + ' | '.join(new_cols) + ' |\n')
                elif len(cols) >= 10 and len(cols[-1].split()) > 1:
                    new_cols = cols[:-1]
                    m10 = re.split(r'\s+', cols[-1], 1)
                    new_cols.extend([m10[0], m10[1]])
                    new_lines.append('| ' + ' | '.join(new_cols) + ' |\n')
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            in_table = False
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('/opt/cran_clean_mds/docs/gazettes/5201.md', 'w') as f:
    f.writelines(new_lines)
