import re

with open("docs/gazettes/5092.md", "r") as f:
    content = f.read()

bad_table = """| Applicant's Name; | Applicant's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens; | List of radio frequencies or groups of radio; | Description of geographic coverage area(s); | Description of geographic coverage area(s); | Description of geographic coverage area(s); | Licence Fees Outstanding; | Service to be provided using frequency applied for; | Party providing Signal Distribution; |
|---------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------|-----------------------------------------------------------|--------------------------------------------|

| Applicant's Name; | Applicant's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens; | List of radio frequencies or groups of radio; | Region | District | City/Town | Licence Fees Outstanding; | Service to be provided using frequency applied for; | Party providing Signal Distribution; |
|---|---|---|---|---|---|---|---|---|---|
| Capricorn Radio | Namibia | 100% | 102.3 MHz | Hardap | Rehoboth | Rehoboth | Yes | Commercial Broadcasting Service | Own |"""

good_table = """| Applicant's Name; | Applicant's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens; | List of radio frequencies or groups of radio; | Description of geographic coverage area(s) Region | Description of geographic coverage area(s) District | Description of geographic coverage area(s) City/Town | Licence Fees Outstanding; | Service to be provided using frequency applied for; | Party providing Signal Distribution; |
|---|---|---|---|---|---|---|---|---|---|
| Capricorn Radio | Namibia | 100% | 102.3 MHz | Hardap | Rehoboth | Rehoboth | Yes | Commercial Broadcasting Service | Own |"""

content = content.replace(bad_table, good_table)

with open("docs/gazettes/5092.md", "w") as f:
    f.write(content)

