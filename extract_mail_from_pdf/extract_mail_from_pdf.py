import re
from PyPDF2 import PdfReader

def extract_mail(path):

    pdf = PdfReader(open(path, 'rb'))
    email_pattern = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
    hidden_emails = []

    for page_num in range(len(pdf.pages)):
        page = pdf._get_page(page_num)
        text = page.extract_text()

        emails = re.findall(email_pattern, text)

        hidden_emails.extend(emails)

    for email in hidden_emails:
        print(email)

pdf_path = '../PDF_pool/mail_example.pdf'
extract_mail(pdf_path)
print('ici on verifie que l''information du mail est bien cachée ')
pdf_path = '../PDF_pool/redacted_Email_example.pdf'
extract_mail(pdf_path)