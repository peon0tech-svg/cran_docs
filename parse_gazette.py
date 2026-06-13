import re

with open('extracted_6888.txt') as f:
    text = f.read()

# Remove page headers and footers
# e.g., "6888                          Government Gazette 29 April 2019                                    3"
# or "2                             Government Gazette 29 April 2019                       6888"
# and form feed (\x0c)
lines = text.split('\n')
cleaned_lines = []
for line in lines:
    # check for page headers
    if re.search(r'^\s*\d+\s+Government Gazette\s+\d+\s+\w+\s+\d+\s+\d+\s*$', line):
        continue
    if re.search(r'^\s*\d+\s+Government Gazette\s+\d+\s+\w+\s+\d+\s*\d*\s*$', line):
        continue
    if re.search(r'^\s*\d+\s+Government Gazette\s+29 April 2019\s+\d+\s*$', line):
        continue
    if re.search(r'^\s*\d+\s+Government Gazette\s+29 April 2019\s+6888\s*$', line):
        continue
    if re.search(r'^\s*6888\s+Government Gazette\s+29 April 2019\s+\d+\s*$', line):
        continue
    cleaned_lines.append(line)

cleaned_text = '\n'.join(cleaned_lines)
cleaned_text = cleaned_text.replace('\x0c', '\n')

with open('cleaned_body.txt', 'w') as f:
    f.write(cleaned_text)

print("Page headers/footers removed.")
