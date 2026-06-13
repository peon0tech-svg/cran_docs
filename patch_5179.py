import re

with open('docs/gazettes/5179.md', 'r') as f:
    text = f.read()

# 1. Move "General Notices" and "COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA"
text = re.sub(
    r'\*\*L\. N\. JACOBS\*\*\s*\nCHAIRPERSON OF THE\s*\nCOMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA\s*\n\n## General Notices\s*\n\n## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA\s*\n\nWindhoek, 25 March 2013',
    '**L. N. JACOBS**  \nCHAIRPERSON OF THE BOARD  \nCOMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA\n\nWindhoek, 25 March 2013',
    text
)

text = re.sub(
    r'---\s*\n\nNo\. 109',
    '---\n\n## General Notices\n\n## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA\n\nNo. 109',
    text
)

# 2. Fix the misplaced Schedule 1 and No. 110 order
# Schedule 1 is currently from line 66 to 91, then No. 110 continuation.
# Wait, let's just find the text chunks.
no_110_header = """No. 110

## NOTICE OF INTENTION TO AMEND REGULATIONS REGARDING ADMINISTRATIVE AND LICENCE FEES FOR SERVICE LICENCES: COMMUNICATIONS ACT, 2009

The Communications Regulatory Authority of Namibia, in terms of regulation 4(3) of the Regulations Regarding Rule-Making Procedures as General Notice No. 334 of 17 December 2010 publishes this Notice of Intention to Amend the Regulations Regarding Administrative and Licence Fees for Service Licences published in General Notice No. 311 of 13 September 2012, which contains the following:

1. A draft of the proposed amended Regulations as set out in Schedule 1;"""

# Remove No 110 header from current position
text = text.replace(no_110_header + "\n\n", "")

# Add it back where it belongs
schedule_1_end = """- The product is applicable to new customers as well as current customers that want to migrate from Mobile Telecommunications (MTC) contract packages according to the rules defined in the terms and conditions.

---"""
new_schedule_1_end = schedule_1_end + "\n\n## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA\n\n" + no_110_header
text = text.replace(schedule_1_end, new_schedule_1_end)


# 3. Fix misplaced Schedule 2 inside No 112
schedule_2_block = """## SCHEDULE 2

## PURPOSE OF THE PROPOSED REGULATIONS SETTING OUT MINIMUM TECHNICAL STANDARDS FOR SET-TOP BOX DECODERS COMMUNICATIONS ACT, 2009

1. In terms of Section 129 (1)(f) of the Communications Act, 2009 (Act No. 8 of 2009), the Authority may make regulations prescribing anything that is necessary or expedient to prescribe in order to implement the provisions of the Act.
2. The purpose of these proposed regulations is to set out minimum technical standards for a set-top box decoder for digital terrestrial television, which will provide good quality video and sound for the viewer when used in conjunction with an analogue television receiver at the lowest possible cost. In addition, the set-top box decoder should be capable of providing interactive services and control features allowing decoders to be disabled to prevent them from being used outside the Republic of Namibia."""

text = text.replace(schedule_2_block + "\n\n", "")

no_112_marker = "No. 112\n\n## NOTICE IN TERMS OF THE REGULATIONS REGARDING LICENSING PROCEDURES"
text = text.replace(no_112_marker, schedule_2_block + "\n\n---\n\n## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA\n\n" + no_112_marker)


# 4. Fix quotes with `2.`
text = text.replace("2. '…The administrative fees", "'…The administrative fees")
text = text.replace("2. '…The annual licence fees", "'…The annual licence fees")


# 5. Fix No 113 signatures
sig_112 = """**L. N. JACOBS**  
CHAIRPERSON OF THE  
COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

Windhoek, 25 March 2
Windhoek, 25 March 2013

---

No. 113"""

new_sig_112 = """**L. N. JACOBS**  
CHAIRPERSON OF THE BOARD  
COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

Windhoek, 25 March 2013

---

## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

No. 113"""
text = text.replace(sig_112, new_sig_112)

# Fix No 114 signatures
sig_113 = """**L. N. JACOBS**  
CHAIRPERSON OF THE  
COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

---

Windhoek, 25 March 2013

No. 114"""

new_sig_113 = """**L. N. JACOBS**  
CHAIRPERSON OF THE BOARD  
COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

Windhoek, 25 March 2013

---

## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

No. 114"""
text = text.replace(sig_113, new_sig_113)

# Fix No 115 signatures
sig_114 = """**L. N. JACOBS**  
CHAIRPERSON OF THE  
COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

---

Windhoek, 25 March 2013

No. 115"""

new_sig_114 = """**L. N. JACOBS**  
CHAIRPERSON OF THE BOARD  
COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

Windhoek, 25 March 2013

---

## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

No. 115"""
text = text.replace(sig_114, new_sig_114)


# 6. Tables

table_113_old = """| No. |  | Licensee's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies Controlled by Namibian Citizens; | List of radio frequencies assigned (MHz) | Description of geographic coverage area(s); | Description of geographic coverage area(s); | Description of geographic coverage area(s); | Services to be provides using frequency assigned; |  |
|-------|--------------------------------------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|

| No. | Licensee; | Licensee's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies Controlled by Namibian Citizens; | List of radio frequencies assigned (MHz) | Region | District | City/Town |  | Proof of Application fees paid up to date submitted? |
|---|---|---|---|---|---|---|---|---|---|"""

table_113_new = """| No. | Licensee; | Licensee's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies Controlled by Namibian Citizens; | List of radio frequencies assigned (MHz) | Region | District | City/Town | Services to be provides using frequency assigned; | Proof of Application fees paid up to date submitted? |
|---|---|---|---|---|---|---|---|---|---|"""
text = text.replace(table_113_old, table_113_new)

table_114_old = """| Licensee; | Licensee's citizenship or place of incorpora- | Percentage of Stock owned by Namibian Citizens or Namibian Companies Controlled by Namibian Citizens; | List of radio frequencies assigned (MHz) | Description of geographic coverage area(s); | Description of geographic coverage area(s); | Description of geographic coverage area(s); | Services to be provided using frequency assigned; |  |  |  |
|-------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
|  |  |  |  | Region | District | City/ |  | Proof of Application fees paid up to date submit- | Proof of Application fees paid up to date submit- | Proof of Application fees paid up to date submit- |
|  | tion; |  |  |  |  |  |  | ted? | ted? | ted? |
|  |  |  |  |  |  | Town |  |  |  |  |
|  |  |  |  | Hardap | Rehoboth |  | Com- |  |  |  |
| Capricorn |  |  | 102.3 |  |  | Rehoboth | mercial | No | No | No |
|  | Namibia | 100% |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | Broadcast- |  |  |  |
|  |  |  |  |  |  |  | ing Service |  |  |  |
| Radio |  |  |  |  |  |  |  |  |  |  |"""

table_114_new = """| Licensee; | Licensee's citizenship or place of incorporation; | Percentage of Stock owned by Namibian Citizens or Namibian Companies Controlled by Namibian Citizens; | List of radio frequencies assigned (MHz) | Region | District | City/Town | Services to be provided using frequency assigned; | Proof of Application fees paid up to date submitted? |
|-------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------|--------|----------|-----------|---------------------------------------------------|------------------------------------------------------|
| Capricorn Radio | Namibia | 100% | 102.3 | Hardap | Rehoboth | Rehoboth | Commercial Broadcasting Service | No |"""
text = text.replace(table_114_old, table_114_new)


with open('docs/gazettes/5179.md', 'w') as f:
    f.write(text)

