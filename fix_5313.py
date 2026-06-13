import re

with open('docs/gazettes/5313.md', 'r') as f:
    content = f.read()

# Fix &amp;
content = content.replace('&amp;', '&')

# Fix lLicencees
content = content.replace('Distribution lLicencees', 'Distribution licensees')

# Fix Adeviation
content = content.replace('Adeviation', 'A deviation')

# Fix lists in table cells
def fix_bullets(match):
    text = match.group(0)
    text = text.replace(' • ', '<br>• ')
    text = text.replace(' service A valid', ' service<br>A valid')
    text = text.replace(' writing. Where', ' writing.<br>Where')
    return text

content = re.sub(r'Include the following scenarios-.*?measurement purposes', fix_bullets, content)

# Fix line 172 bullets
def fix_bullets_172(match):
    text = match.group(0)
    text = text.replace(' • ', '<br>• ')
    return text

content = re.sub(r'A deviation from the normal porting procedures occurs when-.*?between operators', fix_bullets_172, content)

with open('docs/gazettes/5313.md', 'w') as f:
    f.write(content)

