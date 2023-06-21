from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green


def create_form():
    c = canvas.Canvas("../PDF_pool/"+'Amal Hamdi Convention de stage.pdf')

    c.setFont("Courier", 20)

    c.drawCentredString(300, 750, 'Convention de stage')
    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawCentredString(100, 700, " ENTREPRISE D'ACCUEIL : ")
    c.drawString(10, 650, 'Nom:')
    form.textfield(name='fname', tooltip='Nom',
                   x=120, y=635, borderStyle='inset',
                   borderColor=magenta, fillColor=pink,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 600, 'représentée par:')
    form.textfield(name='lname', tooltip='prénom',
                   x=150, y=585, borderStyle='inset',
                   borderColor=green, fillColor=magenta,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 550, 'Addresse:')
    form.textfield(name='address', tooltip='Address',
                   x=120, y=535, borderStyle='inset',
                   width=400, forceBorder=True)

    c.drawString(10, 500, 'Ville:')
    form.textfield(name='city', tooltip='City',
                   x=120, y=485, borderStyle='inset',
                   forceBorder=True)

    c.drawString(250, 500, 'Région:')
    form.textfield(name='state', tooltip='State',
                   x=350, y=485, borderStyle='inset',
                   forceBorder=True)

    c.drawString(10, 450, 'Code Postale:')
    form.textfield(name='zip_code', tooltip='Zip Code',
                   x=120, y=435, borderStyle='inset',
                   forceBorder=True)

    c.drawString(10, 400, 'N° SIRET:')
    form.textfield(name='entreprise', tooltip='entreprise',
                   x=120, y=385, borderStyle='inset',
                   borderColor=green, fillColor=green,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.save()

create_form()