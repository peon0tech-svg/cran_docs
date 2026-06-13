import re

with open('/opt/cran_clean_mds/docs/gazettes/5311.md', 'r') as f:
    content = f.read()

# First, remove the displaced stuff:
displaced = """## GOVERNMENT GAZETTE OF THE REPUBLIC OF NAMIBIA

N$4.00

WINDHOEK - 11 October 2013

No. 5311

## CONTENTS"""

content = content.replace(displaced, "")

# The text "Telecom Namibia Limited may submit..." should be directly after the Gazette sentence.
# Let's fix the extra spaces too.
content = content.replace("in the Gazette .\n\n\n\nTelecom Namibia", "in the Gazette.\n\nTelecom Namibia")

# Replace the beginning
new_header = """# GOVERNMENT GAZETTE OF THE REPUBLIC OF NAMIBIA

N$4.00 WINDHOEK - 11 October 2013 No. 5311

## CONTENTS

**GENERAL NOTICES**

| No. | | Page |
|---|---|---|
| 403 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations Regarding the Submission of Interconnection Agreements and Tariffs | 1 |
| 404 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations Regarding the Submission of Interconnection Agreements and Tariffs | |
| 405 | Communications Regulatory Authority of Namibia: Notice in terms of the Regulations Regarding Transitional Procedures for Telecommunications and Broadcasting Service Licences and Spectrum Use Licence | |

---

## General Notices

## COMMUNICATIONS REGULATORY AUTHORITY OF NAMIBIA

No. 403

2013

## NOTICE IN TERMS OF THE REGULATIONS REGARDING THE SUBMISSION OF INTERCONNECTION AGREEMENTS AND TARIFFS"""

# We need to replace everything from the start of the file up to "## NOTICE IN TERMS..."
# Wait, let's just use regex to replace up to that heading.

pattern = re.compile(r'^.*?## NOTICE IN TERMS OF THE REGULATIONS REGARDING THE SUBMISSION OF INTERCONNECTION AGREEMENTS AND TARIFFS', re.DOTALL)
content = pattern.sub(new_header, content)

with open('/opt/cran_clean_mds/docs/gazettes/5311.md', 'w') as f:
    f.write(content)
