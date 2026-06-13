with open('docs/gazettes/4962.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix 1: Lines 22-24
lines[21] = lines[21].strip() + " " + lines[23].strip() + "\n"
lines[22] = "DELETE\n"
lines[23] = "DELETE\n"

# Fix 2: Lines 53-55
lines[52] = lines[52].strip() + " " + lines[54].strip() + "\n"
lines[53] = "DELETE\n"
lines[54] = "DELETE\n"

# Fix 3: Lines 108-112
lines[107] = lines[107].strip() + " " + lines[111].strip() + "\n"
lines[108] = "DELETE\n"
lines[109] = "DELETE\n"
lines[110] = "DELETE\n"
lines[111] = "DELETE\n"

# Fix 4: Lines 250-252
lines[249] = lines[249].strip() + " " + lines[251].strip() + "\n"
lines[250] = "DELETE\n"
lines[251] = "DELETE\n"

# Fix 5: Lines 287-289
old_286 = lines[286]
old_288 = lines[288]

lines[285] = old_288
lines[286] = "\n"
lines[287] = old_286
lines[288] = "\n"

# Fix 6: Lines 312-314
old_340 = lines[340]
lines[311] = lines[311] + old_340
lines[340] = "DELETE\n"

final_lines = [line for line in lines if line != "DELETE\n"]

with open('docs/gazettes/4962.md', 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print("Done")
