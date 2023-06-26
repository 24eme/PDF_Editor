const puppeteer = require('puppeteer');

async function convertHtmlToPdf(htmlContent, outputFile) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Accéder à une page HTML temporaire
  await page.setContent(htmlContent, { waitUntil: 'networkidle0' });

  // Convertir la page en PDF
  await page.pdf({ path: outputFile, format: 'A4' });

  await browser.close();
  console.log(`Le fichier PDF a été créé : ${outputFile}`);
}

// TEST
const htmlContent = `
  <html>
    <body>
      <h1>Mon fichier HTML</h1>
      <p>Ceci est un exemple de contenu HTML.</p>
    </body>
  </html>
`;
const outputFile = 'htmlFile.pdf';

convertHtmlToPdf(htmlContent, outputFile);
