import re

with open('docs/gazettes/5313.md', 'r') as f:
    content = f.read()

content = content.replace('days and 100%', 'days<br>and<br>100%')
content = content.replace('days 100%', 'days<br>100%')
content = content.replace('reported 100%', 'reported<br>100%')
content = content.replace('reported 100%', 'reported<br>100%')
content = content.replace('repaired within 24 elapsed hours from time reported 100%', 'repaired within 24 elapsed hours from time reported<br>100%')

# Let's also check for Applicability column which has missing line breaks
# "Individual licensees Class Comprehensive ECS/ECNS licensees Class ECS licensees"
# Let's fix missing line breaks in Applicability column
content = content.replace('Individual licensees Class', 'Individual licensees<br>Class')
content = content.replace('ECS/ECNS licensees Class', 'ECS/ECNS licensees<br>Class')
content = content.replace('Class ECS licensees Class', 'Class ECS licensees<br>Class')
content = content.replace('Class ECNS licensees Class', 'Class ECNS licensees<br>Class')
content = content.replace('Class ECS Licensees', 'Class ECS Licensees<br>')
content = content.replace('Class ECNS Licensees', 'Class ECNS Licensees<br>')
content = content.replace('Signal Distribution licensees Class', 'Signal Distribution licensees<br>Class')
content = content.replace('licensees Commercial', 'licensees<br>Commercial')
content = content.replace('Distribution licensees Commercial', 'Distribution licensees<br>Commercial')
content = content.replace('Broadcasting licensees Public', 'Broadcasting licensees<br>Public')
content = content.replace('Broadcasting licensee Community', 'Broadcasting licensee<br>Community')
content = content.replace('Class ECS licensee', 'Class ECS licensee<br>')
content = content.replace('Multiplex Licensees Signal', 'Multiplex Licensees<br>Signal')

with open('docs/gazettes/5313.md', 'w') as f:
    f.write(content)

