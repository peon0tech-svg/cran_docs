import re

with open('/opt/cran_clean_mds/docs/gazettes/5460.md', 'r') as f:
    content = f.read()

# 1. Fix the top structure
header_to_remove = """## GOVERNMENT GAZETTE OF THE REPUBLIC OF NAMIBIA

N$4.00

WINDHOEK - 8 May 2014

No. 5460

## CONTENTS

Page

| GENERALNOTICES | GENERALNOTICES |  |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| No. 101 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding the Submissions of Interconnection Agreements and Tariffs | 1 |
| No. 102 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding the Submissions of Interconnection Agreements and Tariffs | 3 |
| No. 103 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding Licensing Procedures for Telecommunications and Broadcasting Service Licences and Spectrum Use Licences | 5 |
| No. 104 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding Licensing Procedures for Telecommunications and Broadcasting Service Licences and Spectrum Use Licences | 7 |
| No. 105 | Communications Regulatory Authority of Namibia: Notice of amendment in terms of Regulations 8(2) and 11 of the Regulations regarding Licensing Procedures for Telecommunications and Broadcasting Service Licences and Spectrum Use Licences | 8 |

---

## General Notices

## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA"""

content = content.replace(header_to_remove, "")

top_fixed = """# GOVERNMENT GAZETTE OF THE REPUBLIC OF NAMIBIA

N$4.00 WINDHOEK - 8 May 2014 No. 5460

## CONTENTS

**GENERAL NOTICES**

| No. | | Page |
|---|---|---|
| 101 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding the Submissions of Interconnection Agreements and Tariffs | 1 |
| 102 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding the Submissions of Interconnection Agreements and Tariffs | 3 |
| 103 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding Licensing Procedures for Telecommunications and Broadcasting Service Licences and Spectrum Use Licences | 5 |
| 104 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations regarding Licensing Procedures for Telecommunications and Broadcasting Service Licences and Spectrum Use Licences | 7 |
| 105 | Communications Regulatory Authority of Namibia: Notice of amendment in terms of Regulations 8(2) and 11 of the Regulations regarding Licensing Procedures for Telecommunications and Broadcasting Service Licences and Spectrum Use Licences | 8 |

---

## General Notices

## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

No. 101

2014

## NOTICE IN TERMS OF THE REGULATIONS REGARDING THE SUBMISSIONS OF INTERCONNECTION AGREEMENTS AND TARIFFS"""

# We'll regex replace from beginning up to the first ## NOTICE IN TERMS...
pattern = re.compile(r'^.*?## NOTICE IN TERMS OF THE REGULATIONS REGARDING THE SUBMISSIONS OF INTERCONNECTION AGREEMENTS AND TARIFFS', re.DOTALL)
content = pattern.sub(top_fixed, content)

# 2. Fix L.N. JACOBS
content = content.replace("L.N. JACOBS CHAIR PERSON OF THE BOARD COMMUNICATIONS REGULATORY AUTHORITY", "**L.N. JACOBS**\n**CHAIRPERSON OF THE BOARD**\n**COMMUNICATIONS REGULATORY AUTHORITY**")

# 3. Notice 103 table
bad_table_103 = """| Party providing Signal Distribution; | Own | Own | Own |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service to be provided using frequency applied for; | The radio frequencies applied for require a broadcasting service licence. Note however, that as per section 93 of the Act untill a date determined by the Minister, Chapter IV on broadcasting services is not applicable to the Namibian Broadcasting Corporation (NBC) or to any broadcasting activities carried out by the Namibian Broadcasting Corporation (NBC). | The radio frequencies applied for require a broadcasting service licence. Note however, that as per section 93 of the Act untill a date determined by the Minister, Chapter IV on broadcasting services is not applicable to the Namibian Broadcasting Corporation (NBC) or to any broadcasting activities carried out by the Namibian Broadcasting Corporation (NBC). | The radio frequencies applied for require a broadcasting service licence. Note however, that as per section 93 of the Act untill a date determined by the Minister, Chapter IV on broadcasting services is not applicable to the Namibian Broadcasting Corporation (NBC) or to any broadcasting activities carried out by the Namibian Broadcasting Corporation (NBC). |
| License Fees Outstanding; | Yes | Yes | Yes |
| Maximum Output power &Coordinates; | 4X5KW S 22 ° 31' 38'' E 14° 49' 21'' | 4X5KW S 22 ° 31' 38'' E 14° 49' 21'' | 4X5KW S 22 ° 31' 38'' E 14° 49' 21'' |
| Description of geographic coverage area(s) Region; District; City/ Town; | Swakop- mund | Swakop- mund | Swakop- mund |
| Description of geographic coverage area(s) Region; District; City/ Town; | Swakop- mund | Swakop- mund | Swakop- mund |
| Description of geographic coverage area(s) Region; District; City/ Town; | Erongo | Erongo | Erongo |
| List of radio frequencies or groups of radio frequencies being considered for assignment by the Authority; | 93.3 MHz Rukavango | 105.0 MHz Lozi | 106.9 MHz San |
| List of radio frequencies or groups of radio frequencies applied for; | - 108 MHz | - 108 MHz | - 108 MHz |
| Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens; | 100% | 100% | 100% |

| Applicant's citizenship or place of incorporation; | Namibia | Namibia | Namibia |
|---|---|---|---|
| Applicant's Name; | Namibian Broadcasting Corporation (NBC) | Namibian Broadcasting Corporation (NBC) | Namibian Broadcasting Corporation (NBC) |"""

good_table_103 = """| Applicant's Name | Applicant's citizenship or place of incorporation | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens | List of radio frequencies or groups of radio frequencies applied for | List of radio frequencies or groups of radio frequencies being considered for assignment by the Authority | Region | District | City/ Town | Maximum Output power & Coordinates | License Fees Outstanding | Service to be provided using frequency applied for | Party providing Signal Distribution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Namibian Broadcasting Corporation (NBC) | Namibia | 100% | 88 - 108 MHz | 93.3 MHz Rukavango<br>105.0 MHz Lozi<br>106.9 MHz San | Erongo | Swakopmund | Swakopmund | 4 X 5 KW S 22° 31' 38'' E 14° 49' 21'' | Yes | The radio frequencies applied for require a broadcasting service licence. Note however, that as per section 93 of the Act untill a date determined by the Minister, Chapter IV on broadcasting services is not applicable to the Namibian Broadcasting Corporation (NBC) or to any broadcasting activities carried out by the Namibian Broadcasting Corporation (NBC). | Own |"""

content = content.replace(bad_table_103, good_table_103)

# 4. Notice 105 table
bad_table_105 = """| Applicant's Name; | Applicant's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens; | Amendment; | Reasons for the proposed amendment; | Description of geographic coverage area(s) | Description of geographic coverage area(s) | Description of geographic coverage area(s) | License Fees Outstanding; |
|-----------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|-----------------------------------|
|  |  |  |  |  | Region; | District; | City/ Town; |  |
| Namibian Broadcasting Corporation | Namibia | 100% | Increase the output power of the following transmitters from 100 Watts to 1000 Watts: 1. Afrikaans 2. German 3. Damara/Nama 4. Setswana 5. Silozi 6. San Increase the output power of the following transmitters from 100 Watts to 5000 Watts: 1. Otjiherero 2. Rukavango | Applicant has conducted a study on populations demographics covered within the current output power limits and would like to increase increase coverage by increasing output power. | Oshana | Oshakati | Oshakati | Yes |"""

good_table_105 = """| Applicant's Name | Applicant's citizenship or place of incorporation | Percentage of Stock owned by Namibian Citizens or Namibian Companies controlled by Namibian Citizens | Amendment | Reasons for the proposed amendment | Region | District | City/ Town | License Fees Outstanding |
|---|---|---|---|---|---|---|---|---|
| Namibian Broadcasting Corporation | Namibia | 100% | Increase the output power of the following transmitters from 100 Watts to 1000 Watts:<br>1. Afrikaans<br>2. German<br>3. Damara/Nama<br>4. Setswana<br>5. Silozi<br>6. San<br><br>Increase the output power of the following transmitters from 100 Watts to 5000 Watts:<br>1. Otjiherero<br>2. Rukavango | Applicant has conducted a study on populations demographics covered within the current output power limits and would like to increase increase coverage by increasing output power. | Oshana | Oshakati | Oshakati | Yes |"""

content = content.replace(bad_table_105, good_table_105)

with open('/opt/cran_clean_mds/docs/gazettes/5460.md', 'w') as f:
    f.write(content)

