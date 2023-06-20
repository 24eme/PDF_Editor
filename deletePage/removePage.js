const { PDFDocument } = require('pdf-lib');
const fs = require('fs');

async function removePageFromPDF(fileName,pageIndexToRemove) {
     try {
        const pdfBytes = fs.readFileSync(fileName);
        const pdfDoc = await PDFDocument.load(pdfBytes);

        // Vérifier si l'index de page à supprimer est valide
        if (pageIndexToRemove < 0 || pageIndexToRemove >= pdfDoc.getPageCount()) {
        console.error('Index de page invalide.');
        return;
        }

        // Supprimer la page spécifiée
        pdfDoc.removePage(pageIndexToRemove);

        // Convertir le document PDF en tableau de bytes
        const modifiedPdfBytes = await pdfDoc.save();

        fs.writeFileSync(fileName, modifiedPdfBytes);
        console.log('La page a été supprimée avec succès.');
  } catch (error) {
    console.error('Une erreur est survenue :', error);
  }
}

//test de suppresion de la 3eme page du fichier
const pageIndexToRemove = 2; 

removePageFromPDF('../PDF_pool/GNU_APGL.pdf',pageIndexToRemove);