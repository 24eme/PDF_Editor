const { PDFDocument, StandardFonts, rgb } = require('pdf-lib');
const fs = require('fs');
async function addAnnotationToPDF(fileName) {
  //lecture du fichier
  const pdfBytes = fs.readFileSync(fileName);

  const pdfDoc = await PDFDocument.load(pdfBytes);

  const page = pdfDoc.getPages()[1]; //la deuxieme page

  // Ajouter une annotation de texte
  const helveticaFont = await pdfDoc.embedFont(StandardFonts.Helvetica);
  const fontSize = 10;
  const annotationText = 'Ceci est une annotation';
  const annotationY = 200;
  const textWidth = helveticaFont.widthOfTextAtSize(annotationText, fontSize);
  const annotationX = page.getWidth() - textWidth - 5; // Ajuster la position X

  page.drawText(annotationText, {
    x: annotationX,
    y: annotationY,
    size: fontSize,
    font: helveticaFont,
    color: rgb(1, 0, 0), // Couleur du texte (rouge)
  });
  // Convertir le document PDF en tableau de bytes
  const modifiedPdfBytes = await pdfDoc.save();

  fs.writeFileSync(fileName, modifiedPdfBytes);
  console.log('Le fichier PDF d\'origine a été écrasé avec les modifications.');

  
}

addAnnotationToPDF('../PDF_pool/GNU_APGL.pdf').catch((error) => {
  console.error('Une erreur est survenue :', error);
});
