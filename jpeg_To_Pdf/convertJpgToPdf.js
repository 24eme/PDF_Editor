const fs = require('fs');
const { PDFDocument } = require('pdf-lib');

async function convertImageToPdf(imagePath,outputFile) {
  const pdfDoc = await PDFDocument.create();
  const imageBytes = fs.readFileSync(imagePath);
  const image = await pdfDoc.embedJpg(imageBytes);
  const page = pdfDoc.addPage([image.width, image.height]);
  page.drawImage(image, {
    x: 0,
    y: 0,
    width: image.width,
    height: image.height,
  });
  const pdfBytes = await pdfDoc.save();

  const outputFilePath = './image.pdf';
  fs.writeFileSync(outputFile, pdfBytes);
  console.log(`Le fichier PDF a été créé : ${outputFile}`);
}

// TEST
convertImageToPdf('../Images_pool/marguerite.jpg','marguerite.pdf');
