const PDFLib = require('pdf-lib');
const fs = require('fs');

async function mergePDFs(file1Name, file2Name, outputFile) {
    try {

        const file1Bytes = fs.readFileSync(file1Name);
        const file2Bytes = fs.readFileSync(file2Name);

        const file1Doc = await PDFLib.PDFDocument.load(file1Bytes);
        const file2Doc = await PDFLib.PDFDocument.load(file2Bytes);

        // Créer un nouveau document PDF
        const mergedDoc = await PDFLib.PDFDocument.create();

        // Copie des pages du premier fichier dans le nouveau document
        const file1Pages = await mergedDoc.copyPages(file1Doc, file1Doc.getPageIndices());
        file1Pages.forEach((page) => {
            mergedDoc.addPage(page);
        });

        // Copie des pages du deuxième fichier dans le nouveau document
        const file2Pages = await mergedDoc.copyPages(file2Doc, file2Doc.getPageIndices());
        file2Pages.forEach((page) => {
            mergedDoc.addPage(page);
        });

        const mergedBytes = await mergedDoc.save();

        await fs.writeFileSync(outputFile, mergedBytes);

        console.log('Les fichiers PDF ont été combinés avec succès.');
    }catch(error){
        console.error('Une erreur s\'est produite lors de la combinaison des fichiers PDF :', error);
    }
}

// TEST
mergePDFs('../PDF_pool/cyrilic_text.pdf', '../PDF_pool/chapitre2.pdf', 'mergedPDF.pdf');