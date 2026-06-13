import os

filepath = "docs/gazettes/4962.md"
with open(filepath, "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_line = ""
    # We want to shift characters but leave markdown syntax alone.
    # The markdown syntax characters are at the beginning of lines or are | in tables.
    # Actually, let's just shift characters that are clearly part of the shifted text.
    # The shifted text only contains characters in range 33 to 94 basically, because +29 maps them to 62 to 123 (letters/numbers/symbols).
    # Wait, `+` is 43. 43+29 = 72 (H).
    # What if we just shift every char c where 33 <= ord(c) <= 95?
    # BUT we shouldn't shift `|` (124). That's fine, 124 > 95.
    # We shouldn't shift ` ` (32). That's fine, 32 < 33.
    # We shouldn't shift `#` (35) IF it's markdown.
    # We shouldn't shift `-` (45) IF it's markdown.
    
    # Let's tokenize the line to separate markdown from text.
    i = 0
    while i < len(line):
        c = line[i]
        
        # Skip markdown symbols at start of line
        if i < 10 and c in ['#', '-', '*'] and (i == 0 or line[i-1] == ' '):
            new_line += c
            i += 1
            continue
            
        # Skip table pipes
        if c == '|':
            new_line += c
            i += 1
            continue
            
        # Skip whitespace
        if c in [' ', '\n', '\t']:
            new_line += c
            i += 1
            continue
            
        # If it's a character that looks shifted, shift it.
        # Let's check if ord(c) + 29 makes sense.
        # We know the shifted text uses characters like A-Z, 0-9, some symbols like & (38), ( (40), ) (41).
        # What if it's already a correct character? (like `Applicability` if the agent typed it?)
        # The agent wrote "## Applicability" ? No, the grep showed `## $SSOLFDELOLW\`.
        
        # Let's shift everything except markdown formatting
        if 33 <= ord(c) <= 95 and c not in ['|']:
            new_line += chr(ord(c) + 29)
        else:
            new_line += c
        i += 1
        
    new_lines.append(new_line)

with open(filepath, "w") as f:
    f.writelines(new_lines)

print("Decoded 4962.md")
