with open('docs/gazettes/5037.md', 'r') as f:
    for i, line in enumerate(f):
        # Only process lines in the tables
        if not line.strip().startswith('|'): continue
        if line.strip().startswith('|---'): continue
        
        parts = [p.strip() for p in line.split('|')]
        if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
            parts = parts[1:-1]
        
        if len(parts) != 10:
            print(f"Line {i+1} has {len(parts)} columns: {line.strip()}")
