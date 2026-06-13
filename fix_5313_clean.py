import re

with open('docs/gazettes/5313.md', 'r') as f:
    content = f.read()

# Fix text issues
content = content.replace('&amp;', '&')
content = content.replace('Distribution lLicencees', 'Distribution licensees')
content = content.replace('Adeviation', 'A deviation')

# Fix bullet points
content = content.replace(' • ', '<br>• ')

# Fix missing linebreaks in measurement cell
content = content.replace(' service A valid', ' service<br>A valid')
content = content.replace(' writing. Where', ' writing.<br>Where')
content = content.replace('days and 100%', 'days<br>and<br>100%')
content = content.replace('days 100%', 'days<br>100%')
content = content.replace('reported 100%', 'reported<br>100%')

# Fix applicability column
content = content.replace('Individual licensees Class', 'Individual licensees<br>Class')
content = content.replace('ECS/ECNS licensees Class', 'ECS/ECNS licensees<br>Class')
content = content.replace('ECS licensees Class', 'ECS licensees<br>Class')
content = content.replace('ECNS licensees Class', 'ECNS licensees<br>Class')
content = content.replace('ECS Licensees', 'ECS Licensees')  # Leave as is
content = content.replace('Distribution licensees Class', 'Distribution licensees<br>Class')
content = content.replace('licensees Commercial', 'licensees<br>Commercial')
content = content.replace('Broadcasting licensees Public', 'Broadcasting licensees<br>Public')
content = content.replace('Broadcasting licensee Community', 'Broadcasting licensee<br>Community')
content = content.replace('ECS/ECNS licensees Class', 'ECS/ECNS licensees<br>Class') # duplicate
content = content.replace('ECNS Licensees Class', 'ECNS Licensees<br>Class')
content = content.replace('ECS licensee |', 'ECS licensee |')

# Just do a targeted regex replace for Applicability classes
def fix_applicability(match):
    text = match.group(0)
    # Replace spaces with <br> before capitalized categories
    text = re.sub(r' (Class|Commercial|Public|Community|Signal|Multiplex|Individual)', r'<br>\1', text)
    # Undo it if it matches "Class Comprehensive"
    text = text.replace('<br>Class Comprehensive', '<br>Class Comprehensive') # this is correct
    return text

# We can find all lines starting with | and ending with | and apply the fix to the last column
lines = content.split('\n')
for i, line in enumerate(lines):
    if line.startswith('|') and line.endswith('|') and 'Applicability' not in line and '---' not in line:
        parts = line.split('|')
        if len(parts) >= 6: # 5 columns + empty start and end
            last_col = parts[-2]
            # fix missing linebreaks before categories
            last_col = re.sub(r'(?<=licensees) (Class|Commercial|Public|Community|Signal|Multiplex)', r'<br>\1', last_col)
            last_col = re.sub(r'(?<=licensee) (Class|Commercial|Public|Community|Signal|Multiplex)', r'<br>\1', last_col)
            last_col = re.sub(r'(?<=Licensees) (Class|Commercial|Public|Community|Signal|Multiplex)', r'<br>\1', last_col)
            parts[-2] = last_col
            lines[i] = '|'.join(parts)

content = '\n'.join(lines)

with open('docs/gazettes/5313.md', 'w') as f:
    f.write(content)

