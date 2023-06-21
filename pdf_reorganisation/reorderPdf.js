const { PDFDocument, PDFPage } = require('pdf-lib');
const fs = require('fs');

async function reorganizePDFPages(fileName, outputName, pagesOrder) {

  try{
    const inputBytes = fs.readFileSync(fileName);
    const pdfDoc = await PDFDocument.load(inputBytes);

    // Vérification de l'ordre des pages spécifié 
    if (pagesOrder.length !== pdfDoc.getPageCount()) {
      throw new Error("L'ordre des pages spécifié est invalide !");
    }

    const newPages = [];

    // Réorganiser les pages du document
    for (const pageIndex of pagesOrder) {
      const page = pdfDoc.getPage(pageIndex);
      newPages.push(page);
    }

    while (pdfDoc.getPageCount() > 0) {
      pdfDoc.removePage(0);
    }

    // Ajouter les nouvelles pages réorganisées au document
    for (const newPage of newPages) {
      pdfDoc.addPage(newPage);
    }

    const outputBytes = await pdfDoc.save();

    fs.writeFileSync(outputName, outputBytes);

    console.log('Les pages du PDF ont été réorganisées avec succès !');
  }catch(error) {
    console.error('Une erreur s\'est produite lors de la réorganisation des pages du PDF :', error);
  }
  
}

//TEST
const fileName = '../PDF_pool/cyrilic_text.pdf';
const outputName = 'reoderedPDF.pdf';
const pagesOrder = [1, 0, 2, 3]; // Réorganiser dans l'ordre 2, 1, 3, 4

reorganizePDFPages(fileName, outputName, pagesOrder);
