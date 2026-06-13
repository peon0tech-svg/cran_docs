import fitz

doc = fitz.open("/opt/cran_clean_docs/orig_pdfs/gazettes/5683.pdf")
text = ""
for i in range(13, 17):
    page = doc.load_page(i)
    text += page.get_text()

with open("table_text.txt", "w") as f:
    f.write(text)
