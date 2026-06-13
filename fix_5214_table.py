import re

with open('docs/gazettes/5214.md', 'r') as f:
    lines = f.readlines()

new_lines = []
in_table = False

for i, line in enumerate(lines):
    # Fix orphaned sentences manually found
    if i == 3333 - 1: # Line 3333 is index 3332
        pass # Will handle
    
    if i >= 48 and i <= 1519:
        if line.strip() == "":
            continue
        if line.strip().startswith('|---'):
            if i != 48: # Line 49 is index 48
                continue
        
        if line.strip().startswith('|') and not line.strip().startswith('|---'):
            parts = [p.strip() for p in line.strip().split('|')]
            if len(parts) > 2 and parts[0] == '' and parts[-1] == '':
                parts = parts[1:-1]
            
            # Now we have parts
            if len(parts) == 4:
                # insert empty at 3rd index (4th col)
                parts.insert(3, "")
            elif len(parts) == 6:
                # Sometimes split. Just take first 5 or join?
                # Actually, let's just keep 5
                pass
            
            # We'll just rebuild
            pass

