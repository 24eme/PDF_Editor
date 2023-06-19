from reportlab.pdfgen import canvas

def create_pdf():
    pdf_file = 'Amal Hamdi Convention de stage.pdf'

    can = canvas.Canvas("../PDF_pool/"+pdf_file)

    can.drawString(250, 800, "Convention de Stage")
    can.showPage()

    can.drawString(20, 800, "Second Page")
    can.showPage()

    can.drawString(20, 800, "Third Page")
    can.showPage()

    can.save()

create_pdf()