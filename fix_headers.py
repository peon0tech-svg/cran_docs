import re

with open('docs/gazettes/5078.md', 'r') as f:
    content = f.read()

# Fix table 1
content = re.sub(
r"\| Licensee \| Licensee's citizenship or place of incopora- tion \| Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens \| List of radio frequencies or groups of radio applied for \| Description of geographic coverage area\(s\) \| Description of geographic coverage area\(s\) \| Description of geographic coverage area\(s\) \| License Fees Outstanding \| Service to be provided using frequency assigned \| Party providing Signal Distri- butio n \|\n\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|\n\n\| Licensee \| Licensee's citizenship or place of incopora- tion \| Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens \| List of radio frequencies or groups of radio applied for \| Region \| District \| City/Town \| License Fees Outstanding \| Service to be provided using frequency assigned \| Party providing Signal Distri- butio n \|\n\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|",
r"| Licensee | Licensee's citizenship or place of incorporation | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens | List of radio frequencies or groups of radio applied for | Region | District | City/Town | License Fees Outstanding | Service to be provided using frequency assigned | Party providing Signal Distribution |\n|---|---|---|---|---|---|---|---|---|---|",
content)

# Fix table 2
content = re.sub(
r"\| Applicant's Name \| Applicant's citizenship or place of incorporation \| Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens \| List of radio frequencies or groups of radio \| Description of geographic coverage area\(s\) \| Description of geographic coverage area\(s\) \| Description of geographic coverage area\(s\) \| License Fees Outstanding \| Service to be provided using frequency applied for \| Party providing Signal Distri- \|\n\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|-+\|\n\n\|  \| Applicant's citizenship or place of incorporation \| Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens \| List of radio frequencies or groups of radio \| Region \| District \| City/ Town \| License Fees Outstanding \| Service to be provided using frequency applied for \| bution \|\n\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|",
r"| Applicant's Name | Applicant's citizenship or place of incorporation | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens | List of radio frequencies or groups of radio | Region | District | City/ Town | License Fees Outstanding | Service to be provided using frequency applied for | Party providing Signal Distribution |\n|---|---|---|---|---|---|---|---|---|---|",
content)

with open('docs/gazettes/5078.md', 'w') as f:
    f.write(content)
