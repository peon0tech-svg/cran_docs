import re

with open("docs/gazettes/5092.md", "r") as f:
    content = f.read()

bad_table1 = """| Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages |
| Package | 512k | 1024k | 2048k | 4096k | 6144k | 8192k | 10240k |"""

good_table1 = """### Online Broadband Packages

| Package | 512k | 1024k | 2048k | 4096k | 6144k | 8192k | 10240k |
|---|---|---|---|---|---|---|---|"""

content = content.replace(bad_table1, good_table1)

bad_table2 = """| Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages | Online Broadband Packages |
|-----------------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Package | 512k | 1024k | 2048k | 4096k | 6144k | 8192k | 10240k |"""

good_table2 = """### Online Broadband Packages

| Package | 512k | 1024k | 2048k | 4096k | 6144k | 8192k | 10240k |
|---|---|---|---|---|---|---|---|"""

content = content.replace(bad_table2, good_table2)

with open("docs/gazettes/5092.md", "w") as f:
    f.write(content)

