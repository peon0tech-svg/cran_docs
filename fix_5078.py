import re

with open('docs/gazettes/5078.md', 'r') as f:
    lines = f.readlines()

def fix_row(line):
    # Remove leading and trailing pipes for processing
    content = line.strip()
    if not content.startswith('|') or not content.endswith('|'):
        return line
        
    parts = [p.strip() for p in content.strip('|').split('|')]
    # the ideal length is 11
    # parts: 0: Site, 1: Lat, 2: Long, 3: Multiplex, 4: Freq, 5: Channel, 6: TX Power, 7: Gain, 8: Pol, 9: Height, 10: Region
    
    # We notice some cells have merged numbers like "40 20" for Channel "40" and TX Power "20".
    # Sometimes there is an empty column.
    
    # Clean up empty columns first
    new_parts = []
    
    # We will reconstruct the row by forcing exactly 11 columns, merging or splitting where obvious.
    # It's easier to strip out all the empty parts and then fix the numbers.
    clean_parts = [p for p in parts if p]
    
    # We know the types of the 11 columns:
    # 0: string
    # 1: string (lat)
    # 2: string (long)
    # 3: int
    # 4: int
    # 5: int
    # 6: int
    # 7: float
    # 8: string (Horizontal/Vertical)
    # 9: float or empty
    # 10: string (Region)
    
    # Some numbers are combined with a space.
    # Let's flatten everything from column 3 up to before Polarisation
    # Find Polarisation index
    pol_idx = -1
    for i, p in enumerate(clean_parts):
        if p in ['Horizontal', 'Vertical']:
            pol_idx = i
            break
            
    if pol_idx == -1:
        # maybe no polarisation? Check if we can just return
        # The Gross Hertzog lines have no Height/Region or are short.
        if len(parts) == 11:
            return line
            
    if pol_idx != -1:
        # Before pol, we should have 5 items: Multiplex, Freq, Channel, TX, Gain
        pre_pol = clean_parts[3:pol_idx]
        pre_pol_str = " ".join(pre_pol)
        # split by space
        pre_pol_nums = pre_pol_str.split()
        if len(pre_pol_nums) == 5:
            # perfect
            reconstructed = clean_parts[:3] + pre_pol_nums + clean_parts[pol_idx:]
            # We must ensure length is 11
            if len(reconstructed) == 10:
                # height is missing, region is last
                reconstructed.insert(9, '')
            elif len(reconstructed) == 9:
                # height and region missing
                reconstructed.extend(['', ''])
                
            if len(reconstructed) == 11:
                return "| " + " | ".join(reconstructed) + " |\n"
                
    return "| " + " | ".join(parts) + " |\n"

for i in range(193, 345):
    lines[i] = fix_row(lines[i])
    
with open('docs/gazettes/5078_fixed.md', 'w') as f:
    f.writelines(lines)
    
