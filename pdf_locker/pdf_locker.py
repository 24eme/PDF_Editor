import sys
import os
import fitz


def lock_pdf_file(input_file, password):
    doc = fitz.open(input_file)
    perm = int(fitz.PDF_PERM_ACCESSIBILITY)
    user_pass = password
    encrypt_meth = fitz.PDF_ENCRYPT_AES_256
    encrypted_file_name = "encrypted_" + os.path.basename(input_file)
    doc.save(encrypted_file_name, encryption=encrypt_meth, user_pw=user_pass, permissions=perm)
    print("Your file has been encrypted.")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(
            "Veuillez spécifier les noms du fichier d'entrée PDF et du fichier de sortie. Utilisation : python3 "
            "pdf_unlocker.py [input file] [new password]")
    else:
        input_file = sys.argv[1]
        password = sys.argv[2]
        lock_pdf_file(input_file, password)
