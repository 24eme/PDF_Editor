from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
import io





def add_image():


    in_pdf_file = '../PDF_pool/signature.pdf'
    out_pdf_file = '../PDF_pool/with_image.pdf'
    img_file = '../images/img.png'

    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    x_start = 200
    y_start = 350
    can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.showPage()
    can.showPage()
    can.save()

    packet.seek(0)


    new_pdf = PdfReader(packet)
    # read the existing PDF
    existing_pdf = PdfReader(open(in_pdf_file, "rb"))
    output = PdfWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        page.merge_page(new_pdf.pages[i])
        output.add_page(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()

add_image()