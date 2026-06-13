import re

file_path = '/opt/cran_clean_mds/docs/gazettes/5535.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '- 8.2 Tocarryouttheresponsibilityofspectrumplanningandprovidinginformationonspectrum utilisedtodatebybroadcastingservicelicenseeintermsof theirspectrumuselicencesas well as any new spectrum use licenses thatmaybe awardedby the Authority during the study',
    '- 8.2 Tocarryouttheresponsibilityofspectrumplanningandprovidinginformationonspectrum utilisedtodatebybroadcastingservicelicenseeintermsof theirspectrumuselicencesas well as any new spectrum use licenses thatmaybe awardedby the Authority during the study period;'
)

content = content.replace(
    '- 10.4 reconsideranyorderordecisionthatit hasmadeinrespectofthisstudy,within90daysfrom dateofmakingtheorderordecision.',
    '- 10.4 The Authority may on its own motion or on a petition filed by any party to this study reconsider any order or decision that it has made in respect of this study, within 90 days from date of making the order or decision.'
)

content = content.replace('| likeloCS | 17°52\'43"S | 16°2401"E |', '| Iikelo CS | 17°52\'43"S | 16°24\'01"E |')

content = content.replace('- X. Conclusions', '- x. Conclusions')

# There might be spaces missing in the table, let's fix the first column:
content = content.replace('| EtsapaCS |', '| Etsapa CS |')
content = content.replace('| OmakondoCS |', '| Omakondo CS |')
content = content.replace('| OnanghuloCS |', '| Onanghulo CS |')
content = content.replace('| OnankaliNorthCs |', '| Onankali North CS |')
content = content.replace('| OupiliCS |', '| Oupili CS |')
content = content.replace('| ShikudeleCS |', '| Shikudele CS |')
content = content.replace('| Ekangolinene Cs |', '| Ekangolinene CS |')
content = content.replace('| EkwafoSs |', '| Ekwafo SS |')
content = content.replace('| OlukoloJS |', '| Olukolo JS |')
content = content.replace('| Euguwantale CS |', '| Euguwantale CS |') # Check if it's correct
content = content.replace('| OlunoCo |', '| Oluno CO |')
content = content.replace('| OlupanduPS |', '| Olupandu PS |')
content = content.replace('| OneeyaCS |', '| Oneeya CS |')
content = content.replace('| Epoli Cs |', '| Epoli CS |')
content = content.replace('| OnamahokaCS |', '| Onamahoka CS |')
content = content.replace('| UukeloCS |', '| Uukelo CS |')
content = content.replace('| 1545\'58E |', '| 15°45\'58"E |')
content = content.replace('| 1746\'08"S |', '| 17°46\'08"S |')
content = content.replace('| 1545\'56E |', '| 15°45\'56"E |')
content = content.replace('| 1746\'09"S |', '| 17°46\'09"S |')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
