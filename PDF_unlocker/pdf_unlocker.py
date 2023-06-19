import sys
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("../PDF_pool/locked.pdf")
if reader.is_encrypted:
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt("")

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save the new PDF to a file
    with open("decrypted-pdf.pdf", "wb") as f:
        writer.write(f)
