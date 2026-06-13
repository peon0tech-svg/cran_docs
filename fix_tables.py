import re

with open('/opt/cran_clean_mds/docs/gazettes/5311.md', 'r') as f:
    content = f.read()

# Fix the Netherlands split in PostPaid
content = content.replace(
    "| Netherlands,Sweden,Switzerland, | Peak | 4.05 | 3.65 |\n| Spain, Australia, France, &Kenya (Fixed) | Off Peak | 3.25 | 2.99 |",
    "| Netherlands,Sweden,Switzerland, Spain, Australia, France, & Kenya (Fixed) | Peak | 4.05 | 3.65 |\n| Netherlands,Sweden,Switzerland, Spain, Australia, France, & Kenya (Fixed) | Off Peak | 3.25 | 2.99 |"
)

# Fix &Kenya to & Kenya
content = content.replace("&Kenya", "& Kenya")
# Fix &Mobile to & Mobile
content = content.replace("&Mobile", "& Mobile")
# Fix &Portugal to & Portugal
content = content.replace("&Portugal", "& Portugal")

# Split the tables
content = content.replace(
    "| International call charges (PrePaid) | Time Period | Current N$/Minute | New N$/Minute |",
    "\n| International call charges (PrePaid) | Time Period | Current N$/Minute | New N$/Minute |\n|---|---|---|---|"
)

with open('/opt/cran_clean_mds/docs/gazettes/5311.md', 'w') as f:
    f.write(content)
