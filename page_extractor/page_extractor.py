from pypdf import PdfReader, PdfWriter

reader = PdfReader("../PDF_pool/chapitre2.pdf")
number_of_pages = len(reader.pages)
print(number_of_pages)
numero = -1
while (numero<0 or numero>=number_of_pages):
    print("Donner un num valide!")
    numero = int(input("Donner moi la page que tu veux : "))

page = reader.pages[numero]

writer = PdfWriter()
writer.add_page(page)
with open("../PDF_pool/MyPDF.pdf", "wb") as fp:
    writer.write(fp)

