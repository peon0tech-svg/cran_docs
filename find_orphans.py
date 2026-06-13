import re

with open('docs/gazettes/5201.md', 'r') as f:
    lines = f.readlines()

for i in range(1, len(lines)):
    prev = lines[i-1].strip()
    curr = lines[i].strip()
    
    if prev and curr and not prev.startswith('#') and not curr.startswith('#') and not prev.startswith('|') and not curr.startswith('|'):
        if re.match(r'^[a-z]', curr) and prev[-1] not in ['.', '!', '?', ':', ';']:
            print(f"Line {i+1}: {prev} -> {curr}")
            
