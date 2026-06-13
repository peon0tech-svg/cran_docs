import re

with open("docs/gazettes/5092.md", "r") as f:
    content = f.read()

bad_table = """| Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business | Fixed Broadband packages - Business |
|-------------------------------------------|-----------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Package | SME 256k | 256k | 384k | 512k | 768k | 1024k | 1536k | 2048k | 3072k |"""

good_table = """### Fixed Broadband packages - Business

| Package | SME 256k | 256k | 384k | 512k | 768k | 1024k | 1536k | 2048k | 3072k |
|---|---|---|---|---|---|---|---|---|---|"""

content = content.replace(bad_table, good_table)

with open("docs/gazettes/5092.md", "w") as f:
    f.write(content)

