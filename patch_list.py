with open('docs/gazettes/5214.md', 'r') as f:
    content = f.read()

content = content.replace("approved telecommunications equipment;\n\nno significant changes are made", "approved telecommunications equipment;\n\n- (b) no significant changes are made")

with open('docs/gazettes/5214.md', 'w') as f:
    f.write(content)
