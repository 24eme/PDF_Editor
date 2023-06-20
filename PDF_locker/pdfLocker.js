const { PDFDocument, StandardFonts, PDFSecurity } = require('pdf-lib');
const fs = require('fs');

async function lockPDFWithPassword(password) {
  try {
    const pdfBytes = fs.readFileSync('../PDF_pool/GNU_APGL.pdf');
    const pdfDoc = await PDFDocument.load(pdfBytes);

    // Créer une nouvelle sécurité PDF avec le mot de passe spécifié
    const security = PDFSecurity.createEmpty();

    // Ajouter un mot de passe au document PDF
    security.setPassword(password);

    // Appliquer la sécurité au document PDF
    pdfDoc.setSecurity(security);

    // Convertir le document PDF en tableau de bytes
    const lockedPdfBytes = await pdfDoc.save();

    fs.writeFileSync('../PDF_pool/GNU_APGL.pdf', lockedPdfBytes);
    console.log('Le fichier PDF a été verrouillé avec succès.');
  } catch (error) {
    console.error('Une erreur est survenue :', error);
  }
}

// Utilisation : Spécifiez le mot de passe pour verrouiller le PDF
const password = 'passe';

lockPDFWithPassword(password);
