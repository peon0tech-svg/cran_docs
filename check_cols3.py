with open('docs/gazettes/5037.md', 'r') as f:
    for i, line in enumerate(f):
        if i < 34 or i > 220: continue
        if not line.strip().startswith('|'): continue
        if line.strip().startswith('|---'): continue
        
        parts = [p.strip() for p in line.split('|')]
        if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
            parts = parts[1:-1]
        
        if len(parts) != 8:
            print(f"Line {i+1} has {len(parts)} columns: {line.strip()}")
