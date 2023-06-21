import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

def draw_shapes():
    in_pdf_file = '../PDF_pool/PDF_from_Image.pdf'
    out_pdf_file = '../PDF_pool/PDF_from_Image_new.pdf'

    packet = io.BytesIO()
    c = canvas.Canvas(packet)
    c.setStrokeColorRGB(1,1,1)
    c.setFillColorRGB(1, 1, 1)
    c.rect(485, 9, 100, 40, stroke=1, fill=1)
    #c.ellipse(10, 680, 100, 630, stroke=1, fill=1)
    #c.wedge(10, 600, 100, 550, 45, 90, stroke=1, fill=0)
    #c.circle(300, 600, 50)
    c.showPage()
    c.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)

    existing_pdf = PdfReader(open(in_pdf_file, "rb"))
    output = PdfWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ == '__main__':
    draw_shapes()