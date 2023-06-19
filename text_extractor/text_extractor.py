import sys
from PyPDF2 import PdfReader

def extract_text_to_file(input_path, output_path):
    reader = PdfReader(input_path)
    output_file = open(output_path, 'w')
    for page in reader.pages:
        text = page.extract_text()
        output_file.write(text)

    output_file.close()
    print("Extraction terminée. Le texte a été enregistré dans '{output_path}'.")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Veuillez spécifier les noms du fichier d'entrée PDF et du fichier de sortie. Utilisation : python3 text_extractor.py [input file] [output file]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        extract_text_to_file(input_file, output_file)