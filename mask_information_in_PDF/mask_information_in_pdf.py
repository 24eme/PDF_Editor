# imports
import fitz
import re


class Redactor:
    @staticmethod
    def get_sensitive_data(lines):

        """ Function to get all the lines """

        # email regex
        EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
        for line in lines:

            # matching the regex to each line
            if re.search(EMAIL_REG, line, re.IGNORECASE):
                search = re.search(EMAIL_REG, line, re.IGNORECASE)
                yield search.group(1)

    # constructor
    def __init__(self, path):
        self.path = path

    def redaction(self):

        """ main redactor code """

        # opening the pdf
        doc = fitz.open(self.path)

        for page in doc:

            page.wrap_contents()

            # getting the rect boxes which consists the matching email regex
            sensitive = self.get_sensitive_data(page.get_text("text")
                                                .split('\n'))
            for data in sensitive:
                areas = page.search_for(data)

                # drawing outline over sensitive datas
                [page.add_redact_annot(area, fill=(0, 0, 0)) for area in areas]

            # applying the redaction
            page.apply_redactions()

        # saving it to a new pdf
        doc.save('../PDF_pool/redacted_PDF_From_Image.pdf')
        print("Successfully redacted")

if __name__ == "__main__":
    # replace it with name of the pdf file
    path = '../PDF_pool/mail_example.pdf'
    redactor = Redactor(path)
    redactor.redaction()