import PyPDF2
import re
import fitz
from bs4 import BeautifulSoup


class LinkExtractor:
    def __init__(self, path):
        self.path = path

    def extract_href_links(self):
        href_links = []

        with open(self.path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page_num in range(len(reader.pages)):
                page = reader._get_page(page_num)
                content = page.extract_text()

                # Extract image links using regular expressions
                pattern = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
                matches = re.findall(pattern, content)

                for match in matches:
                    url = match[0]
                    href_links.append(url)

        return href_links

if __name__ == "__main__":
    # replace it with name of the pdf file
    path = '../PDF_pool/mail_example.pdf'
    linkExtractor = LinkExtractor(path)
    print(linkExtractor.extract_href_links())

