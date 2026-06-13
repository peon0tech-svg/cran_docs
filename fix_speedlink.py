with open("docs/gazettes/5683.md", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if "Speedlink - Professional | Speedlink - Professional" in lines[i]:
        # Need to split here
        lines[i] = "\n## Speedlink - Professional\n\n"
        # The next line is "| Package | 1024k | 2048k | 4096k | 6144k | 8192k | 10240k |"
        # We need to insert the separator AFTER the next line
        # wait, we will just insert the separator at i+2
        lines.insert(i+2, "|---|---|---|---|---|---|---|\n")
        break

for i in range(len(lines)):
    if "Speedlink Business | Speedlink Business" in lines[i]:
        lines[i] = "\n## Speedlink Business\n\n"
        break

for i in range(len(lines)):
    if "Speedlink Home | Speedlink Home" in lines[i]:
        lines[i] = "\n## Speedlink Home\n\n"
        break

with open("docs/gazettes/5683.md", "w") as f:
    f.writelines(lines)
