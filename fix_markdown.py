with open('docs/gazettes/5037.md', 'r') as f:
    text = f.read()

# Fix ** issue
text = text.replace("**L.N.JACOBS**\nCHAIRPERSON\n**\nBOARD OF DIRECTORS", "**L.N.JACOBS**\nCHAIRPERSON\nBOARD OF DIRECTORS")
text = text.replace("CHAIRPERSON OF THE BOARD BOARD", "CHAIRPERSON OF THE BOARD")

with open('docs/gazettes/5037.md', 'w') as f:
    f.write(text)
