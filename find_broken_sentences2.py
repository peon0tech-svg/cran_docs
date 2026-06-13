with open('docs/gazettes/5037.md', 'r') as f:
    lines = f.readlines()

for i in range(len(lines) - 1):
    curr = lines[i].strip()
    nxt = lines[i+1].strip()
    
    if curr and nxt and not curr.startswith('|') and not nxt.startswith('|') and not curr.startswith('#'):
        if curr[-1] not in ['.', ':', ';', '?', '!', '>']:
            if nxt[0].islower():
                print(f"Line {i+1}: {curr}")
                print(f"Line {i+2}: {nxt}")
                print("---")
