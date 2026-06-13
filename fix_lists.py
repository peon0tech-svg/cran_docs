import re

with open("docs/gazettes/5092.md", "r") as f:
    content = f.read()

# Fix Applicability
content = content.replace("- (1) Licensees; and\n\n- (2) Persons", "- (1) Licensees; and\n- (2) Persons")

# Fix Decisions
content = content.replace("- (5) grant the relief sought in the dispute, either wholly or partly;\n\n- (6) impose", "- (5) grant the relief sought in the dispute, either wholly or partly;\n- (6) impose")

# Fix Confidential information
content = content.replace("- (1) Any person providing information or documentation may designate information as confidential, provided, however, if the Authority is of the opinion that the information is not confidential, it must inform the person that he may withdraw the information, agree that it will not be treated as confidential, or request a hearing on the issue of confidentiality to be conducted in terms of section 28 of the Act.\n\n- (2)", "- (1) Any person providing information or documentation may designate information as confidential, provided, however, if the Authority is of the opinion that the information is not confidential, it must inform the person that he may withdraw the information, agree that it will not be treated as confidential, or request a hearing on the issue of confidentiality to be conducted in terms of section 28 of the Act.\n- (2)")

# Fix Amendment of Regulation 4
content = content.replace("- (a) Commercial;\n\n- (b) Community;", "- (a) Commercial;\n- (b) Community;")

with open("docs/gazettes/5092.md", "w") as f:
    f.write(content)

