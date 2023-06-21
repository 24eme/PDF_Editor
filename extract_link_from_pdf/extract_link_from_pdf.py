import PyPDF2
import re
import fitz
from PyPDF2.generic import IndirectObject
from bs4 import BeautifulSoup
import requests


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

    def extract_hidden_links(self):
        with open(self.path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)

            hidden_links = set()

            for page_num in range(len(pdf.pages)):
                page = pdf._get_page(page_num)
                page_links = page.get('/Annots')

                if page_links:
                    for link in page_links:
                        link_obj = link.get_object()

                        if link_obj.get('/Subtype') == '/Link':
                            if '/A' in link_obj.keys():
                                if isinstance(link_obj.get('/A'), IndirectObject):
                                    link_object = link_obj.get('/A').get_object()

                                    if '/URI' in link_object:
                                        uri = link_object.get('/URI')
                                        hidden_links.add(uri)

                                else :
                                    if '/URI' in link_obj.get('/A'):
                                        uri = link_obj.get('/A').get('/URI')
                                        hidden_links.add(uri)


            return hidden_links




if __name__ == "__main__":
    # replace it with name of the pdf file
    #path = '../PDF_pool/mail_example.pdf'
    path = '../PDF_pool/GetPDF.pdf'
    linkExtractor = LinkExtractor(path)
    print("hidden link : ", linkExtractor.extract_hidden_links())
    print("link", linkExtractor.extract_href_links())
    path = '../PDF_pool/PDF_from_Image.pdf'
    linkExtractor = LinkExtractor(path)
    print("hidden link : ", linkExtractor.extract_hidden_links())
    print("link", linkExtractor.extract_href_links())


