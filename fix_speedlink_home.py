import re

with open("docs/gazettes/5092.md", "r") as f:
    content = f.read()

bad_table = """| Speedlink packages - Home | Speedlink packages - Home | Speedlink packages - Home | Speedlink packages - Home | Speedlink packages - Home |
|-----------------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Package | 384k | 512k | 1024k | 2048k |"""

good_table = """### Speedlink packages - Home

| Package | 384k | 512k | 1024k | 2048k |
|---|---|---|---|---|"""

content = content.replace(bad_table, good_table)

with open("docs/gazettes/5092.md", "w") as f:
    f.write(content)

