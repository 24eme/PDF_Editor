import sys


def extract_text_to_pdf(fname, replacement_string, replacement_text):



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(
            "Veuillez spécifier le nom du fichier PDF, la chaîne de caractères à remplacer et la chaîne de caractères de remplacement.")
    else:
        fname = sys.argv[1]
        replacement_string = sys.argv[2]
        replacement_text = sys.argv[3]
        extract_text_to_pdf(fname, replacement_string, replacement_text)
