import sys, pathlib, fitz


def extract_text_to_file(fname, replacement_string, replacement_text):
    with fitz.open(fname) as doc:
        text = chr(12).join([page.get_text() for page in doc])

    # Remplace la chaîne de caractères spécifiée par l'utilisateur
    text = text.replace(replacement_string, replacement_text)

    # Écrit comme un fichier binaire pour prendre en charge les caractères non-ASCII
    pathlib.Path(fname + ".txt").write_bytes(text.encode())


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Veuillez spécifier le nom du fichier PDF, la chaîne de caractères à remplacer et la chaîne de caractères de remplacement. Utilisation : python3 text_exctractor_v2.py [chaine a remplacer] [chaine de remplacement]")
    else:
        fname = sys.argv[1]
        replacement_string = sys.argv[2]
        replacement_text = sys.argv[3]
        extract_text_to_file(fname, replacement_string, replacement_text)