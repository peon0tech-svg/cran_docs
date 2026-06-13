with open('docs/gazettes/5214.md', 'r') as f:
    content = f.read()

content = content.replace("equipment only if such person\n\nobtained the prior written consent", "equipment only if such person obtained the prior written consent")
with open('docs/gazettes/5214.md', 'w') as f:
    f.write(content)
