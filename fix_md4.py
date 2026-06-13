import re

file_path = '/opt/cran_clean_mds/docs/gazettes/5535.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '- 7.5 MDB shall be required to submit to theAuthority lease agreements,interconnection and parties withinfourteen (14) daysprior to commencementof the studyperiod asstated in point 4.1 above.',
    '- 7.5 MDB shall be required to submit to the Authority lease agreements, interconnection and service agreements, as well as network diagrams of implementation concluded with other parties within fourteen (14) days prior to commencement of the study period as stated in point 4.1 above.'
)

content = content.replace(
    '- ii. The typeofservices offered and thespeed atwhich theservices are actually offered toallparties;\n- ii. Theinterfacesbetweenbackhaul solutionsanduser equipment;',
    '- ii. Theinterfacesbetweenbackhaul solutionsanduser equipment;\n- iii. The typeofservices offered and thespeed atwhich theservices are actually offered toallparties;'
)

content = content.replace(
    '- V. Any interferences and the performance of the equipment in the aforesaid spectrum band;',
    '- v. Any interferences and the performance of the equipment in the aforesaid spectrum band;'
)

content = content.replace(
    '- ii. Discontinuation of services pending the publication of regulations to be published in linewiththeITUregulationsforspectrumutilisation;',
    '- iii. Discontinuation of services pending the publication of regulations to be published in linewiththeITUregulationsforspectrumutilisation;'
)

content = content.replace(
    '- V. Ensure that all services offered during the study at all sites listed in"Annexure A" heretoarehandedovertoalicencedentityorsubstitutedbytelecommunications services already offered by suchlicensed entity after the completion of the study to ensurecontinuationoftheseservicesafterthestudy.',
    '- v. Ensure that all services offered during the study at all sites listed in"Annexure A" heretoarehandedovertoalicencedentityorsubstitutedbytelecommunications services already offered by suchlicensed entity after the completion of the study to ensurecontinuationoftheseservicesafterthestudy.'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
