const { PDFDocument, StandardFonts, rgb } = require('pdf-lib');

async function addAnnotationToPDF() {
  //lecture du fichier 
  const fs = require('fs');
  const pdfBytes = fs.readFileSync('../PDF_pool/GNU_APGL.pdf');

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
  fs.writeFileSync('../PDF_pool/GNU_APGL_annotated.pdf', modifiedPdfBytes);
  console.log('Le fichier PDF modifié a été enregistré.');
  
}

addAnnotationToPDF().catch((error) => {
  console.error('Une erreur est survenue :', error);
});
