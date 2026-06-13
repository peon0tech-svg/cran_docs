with open('docs/gazettes/5037.md', 'r') as f:
    for i, line in enumerate(f):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
            parts = parts[1:-1]
        if len(parts) == 9:
            print(f"Line {i+1}: {line.strip()}")
