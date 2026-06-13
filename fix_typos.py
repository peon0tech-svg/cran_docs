import re

with open('docs/gazettes/5313.md', 'r') as f:
    content = f.read()

content = content.replace('licensee Alog-in is successful', 'licensee<br>A log-in is successful')
content = content.replace('period Adata transmission', 'period<br>A data transmission')
content = content.replace('period | Adata transmission', 'period | A data transmission')
content = content.replace('licensee A log-in', 'licensee<br>A log-in')
content = content.replace('licensee Alog-in', 'licensee<br>A log-in')

with open('docs/gazettes/5313.md', 'w') as f:
    f.write(content)


with open('docs/gazettes/5313.md', 'r') as f:
    content = f.read()

content = content.replace('Authority Additional measurements', 'Authority<br>Additional measurements')
content = content.replace('Internet This measure', 'Internet<br>This measure')
content = content.replace('Internet Additional measurements', 'Internet<br>Additional measurements')
content = content.replace('service Additional measurements', 'service<br>Additional measurements')
content = content.replace('licensee Additional measurements', 'licensee<br>Additional measurements')

with open('docs/gazettes/5313.md', 'w') as f:
    f.write(content)


with open('docs/gazettes/5313.md', 'r') as f:
    content = f.read()

content = content.replace('057-4 Additional measurements', '057-4<br>Additional measurements')
content = content.replace('SMS\'s Additional measurements', 'SMS\'s<br>Additional measurements')

with open('docs/gazettes/5313.md', 'w') as f:
    f.write(content)

