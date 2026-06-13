import re

with open("docs/gazettes/5092.md", "r") as f:
    content = f.read()

bad_table = """| Speedlink packages - Business | Speedlink packages - Business | Speedlink packages - Business | Speedlink packages - Business | Speedlink packages - Business | Speedlink packages - Business | Speedlink packages - Business | Speedlink packages - Business |
|-----------------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| Package | 512k | 1024k | 2048k | 4096k | 6144k | 8192k | 10240k |"""

good_table = """### Speedlink packages - Business

| Package | 512k | 1024k | 2048k | 4096k | 6144k | 8192k | 10240k |
|---|---|---|---|---|---|---|---|"""

content = content.replace(bad_table, good_table)

with open("docs/gazettes/5092.md", "w") as f:
    f.write(content)

