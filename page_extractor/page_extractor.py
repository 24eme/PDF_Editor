from pypdf import PdfReader, PdfWriter

reader = PdfReader("../PDF_pool/chapitre2.pdf")
number_of_pages = len(reader.pages)
print(number_of_pages)
result = []
numero = -1
response = 'y'
while response == 'y' or response =='Y' :
    while (numero<0 or numero>=number_of_pages):
        print("Donner un num valide!")
        numero = int(input("Donner moi la page que tu veux : "))
    result.append(numero)
    numero = -1
    response = input("Voulez vous ajouter ajouter une autre page (repondre par y ou n ? ")


writer = PdfWriter()
for e in result:
    page = reader.pages[e]
    writer.add_page(page)



with open("../PDF_pool/MyPDF.pdf", "wb") as fp:
    writer.write(fp)

