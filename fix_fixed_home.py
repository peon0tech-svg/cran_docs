import re

with open("docs/gazettes/5092.md", "r") as f:
    content = f.read()

bad_table = """| Fixed Broadband packages - Home | Fixed Broadband packages - Home | Fixed Broadband packages - Home | Fixed Broadband packages - Home | Fixed Broadband packages - Home | Fixed Broadband packages - Home | Fixed Broadband packages - Home | Fixed Broadband packages - Home | Fixed Broadband packages - Home |
|-------------------------------------------|---------------------------------------|---------------------------------------|-----------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| Package | 256k | 384k | 512k | 768k | 1024k | 1536k | 2048k | 3072k |"""

good_table = """### Fixed Broadband packages - Home

| Package | 256k | 384k | 512k | 768k | 1024k | 1536k | 2048k | 3072k |
|---|---|---|---|---|---|---|---|---|"""

content = content.replace(bad_table, good_table)

with open("docs/gazettes/5092.md", "w") as f:
    f.write(content)

