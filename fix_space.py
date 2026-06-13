with open('/opt/cran_clean_mds/docs/gazettes/5311.md', 'r') as f:
    content = f.read()

content = content.replace("notice in the Gazette .", "notice in the Gazette.")

with open('/opt/cran_clean_mds/docs/gazettes/5311.md', 'w') as f:
    f.write(content)
