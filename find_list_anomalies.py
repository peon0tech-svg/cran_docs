import os
import re
from pathlib import Path

def find_anomalies():
    docs_dir = Path("/opt/cran_clean_mds/docs")
    anomalies = []
    
    for md_file in docs_dir.rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        last_num = None
        last_line = -1
        in_list = False
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Match top-level list items like "1. ", "2. ", etc.
            match = re.match(r'^(\d+)\.\s', line)
            
            # also check if the line starts with some text and then a number?
            # No, standard lists start with "1. "
            if match:
                num = int(match.group(1))
                # If we are jumping down in numbers (e.g. from 6 to 2) 
                # or if we are skipping many numbers (e.g. 1 to 10)
                if last_num is not None and (i - last_line < 50): # If they are relatively close
                    if num <= last_num and num != 1: 
                        # Jumping backwards (e.g. 6 to 2) and it's not restarting at 1
                        anomalies.append(f"{md_file.name}: Line {i+1} jumps backwards from {last_num} to {num}")
                    elif num > last_num + 5:
                        # Jumping forward by a lot
                        anomalies.append(f"{md_file.name}: Line {i+1} jumps forwards from {last_num} to {num}")
                
                last_num = num
                last_line = i

    for a in anomalies:
        print(a)

if __name__ == "__main__":
    find_anomalies()
