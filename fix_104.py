import re

with open('/opt/cran_clean_mds/docs/gazettes/5460.md', 'r') as f:
    content = f.read()

bad_table_104 = """| Applicant's Name; | Applicant's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens; | List of radio frequencies or groups of radio frequencies applied for; | Description of geographical coverage area(s); | Service intended to be provided using frequency applied for; | Type of Service Licence (s); | Proof of Licence Fees paid up to date submitted? Yes/no |
|-------------------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------|
| Telecom Namibia Limited | Namibian | 100% | 3447.000 - 3468.000 MHz / 3547.000 - 3569.000 MHz | National | FIXED | Individual Comprehensive Telecommunications Service Licence (ECS/ECNS) 1 | Yes |"""

good_table_104 = """| Applicant's Name | Applicant's citizenship or place of incorporation | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens | List of radio frequencies or groups of radio frequencies applied for | Description of geographical coverage area(s) | Service intended to be provided using frequency applied for | Type of Service Licence(s) | Proof of Licence Fees paid up to date submitted? Yes/no |
|---|---|---|---|---|---|---|---|
| Telecom Namibia Limited | Namibian | 100% | 3447.000 - 3468.000 MHz / 3547.000 - 3569.000 MHz | National | FIXED | Individual Comprehensive Telecommunications Service Licence (ECS/ECNS)¹ | Yes |

¹ Deemed Telecommunications Service Licence in terms of Section 45 of the Communications Act, 2009 (Act No. 8 of 2009)"""

content = content.replace(bad_table_104, good_table_104)

with open('/opt/cran_clean_mds/docs/gazettes/5460.md', 'w') as f:
    f.write(content)

