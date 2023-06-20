import sys
import os
from PyPDF2 import PdfReader, PdfWriter


def unlock_pdf_file(input_path, password):
    reader = PdfReader(input_path)

    if reader.is_encrypted:
        writer = PdfWriter()
        if reader.decrypt(password):
            # Add all pages to the writer
            for page in reader.pages:
                writer.add_page(page)
            # Save the new PDF to a file
            decrypted_file_name = "decryted_" + os.path.basename(input_path)
            with open(decrypted_file_name, "wb") as f:
                writer.write(f)
        else:
            print("Wrong password.")
            exit()
    else:
        print("Your file is not encrypted.")
        exit()

    print("Your file is unlocked.")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(
            "Veuillez spécifier les noms du fichier d'entrée PDF et du fichier de sortie. Utilisation : python3 "
            "pdf_unlocker.py [input file] [password]")
    else:
        input_file = sys.argv[1]
        password = sys.argv[2]
        unlock_pdf_file(input_file, password)
