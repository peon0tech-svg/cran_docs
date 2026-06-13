with open("docs/gazettes/5201.md", "r") as f:
    lines = f.readlines()

out = []
for line in lines:
    if line.startswith("| CONTENTS Page | CONTENTS Page | CONTENTS Page |"):
        out.append("| | CONTENTS | Page |\n")
    elif line.startswith("| GENERALNOTICES | GENERALNOTICES | GENERALNOTICES |"):
        out.append("| | GENERAL NOTICES | |\n")
    elif line.startswith("| General Notices | General Notices | General Notices |"):
        out.append("## General Notices\n")
    else:
        out.append(line)

with open("docs/gazettes/5201.md", "w") as f:
    f.writelines(out)
