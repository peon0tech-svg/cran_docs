with open('docs/gazettes/5214.md', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines[49:1519]):
    if not line.strip(): continue
    if line.strip().startswith('|---'): continue
    
    parts = [p.strip() for p in line.strip().split('|')]
    if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
        parts = parts[1:-1]
    
    if len(parts) < 4:
        print(f"Line {i+50} has {len(parts)} columns: {line.strip()}")
