from PyPDF2 import PdfReader, PdfWriter
import fitz
from reportlab.pdfgen import canvas

path = "../PDF_pool/chapitre2.pdf"
result = "../PDF_pool/pdf_edite.pdf"
out = '../PDF_pool/test.pdf'

old_text = "relationnel"
new_text = "relational"

pdf = fitz.open(path)

elem = []
heigth = pdf[0].rect.height
for page_num in range(len(pdf)):
    page = pdf[page_num]
    text_instances = page.search_for(old_text)

    elem.append(text_instances)
    [page.add_redact_annot(area, fill=(1, 1, 1)) for area in text_instances]


    page.apply_redactions()
pdf.save(out)

c = canvas.Canvas("temp.pdf")
for page in elem:
    for area in page:

        c.setFont("Helvetica", 12)
        c.setFillColorRGB(1, 0, 0)
        c.drawString(area.x0, heigth - area.y1 +2.5, new_text)
    c.showPage()
c.save()

temp = PdfReader("temp.pdf")
# read the existing PDF
existing_pdf = PdfReader(out)
output = PdfWriter()

for i in range(len(existing_pdf.pages)):
    page = existing_pdf.pages[i]
    page.merge_page(temp.pages[i])
    output.add_page(page)

outputStream = open(result, "wb")
output.write(outputStream)
outputStream.close()






