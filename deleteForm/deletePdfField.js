const { PDFDocument, StandardFonts, rgb } = require('pdf-lib');
const fs = require('fs');

async function removeFormFields(fileName, fieldNames) {
  const pdfBytes = fs.readFileSync(fileName);
  const pdfDoc = await PDFDocument.load(pdfBytes);

  const form = pdfDoc.getForm();

  fieldNames.forEach((fieldName) => {
   const field = form.getFields().find(x => x.getName() === fieldName);
   form.removeField(field);

  });

  const modifiedPdfBytes = await pdfDoc.save();
  fs.writeFileSync(fileName, modifiedPdfBytes);
}

const fieldNames = ['name', 'agree']

removeFormFields('../PDF_pool/form.pdf', fieldNames);
