import re

file_path = '/opt/cran_clean_mds/docs/gazettes/5535.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('| HashiyanaPS |', '| Hashiyana PS |')
content = content.replace('1545′56E', '15°45\'56"E')
content = content.replace('17°4619"S', '17°46\'19"S')
content = content.replace('17°34*29"S', '17°34\'29"S')
content = content.replace('15°39\'16E', '15°39\'16"E')
content = content.replace('15°35′40.992"', '15°35\'40.992"E')
content = content.replace('17°2513"S', '17°25\'13"S')
content = content.replace('15°2021"E', '15°20\'21"E')
content = content.replace('15°1713"E', '15°17\'13"E')
content = content.replace('| BrakwaterNorth |', '| Brakwater North |')
content = content.replace('17°21.29"E', '17° 2\'1.29"E')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
