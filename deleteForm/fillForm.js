const { PDFDocument } = require('pdf-lib');
const fs = require('fs');

async function fillPdfForm(fileName,fields) {
    try {
        const pdfBytes = fs.readFileSync(fileName);
        const pdfDoc = await PDFDocument.load(pdfBytes);
      
        const form = pdfDoc.getForm()  
        for(const field of fields){
            const fieldName = form.getTextField(field);
            fieldName.setText("hello");
        }
        //recuperer le text sur les champs
        /*const nameField = form.getTextField('CharacterName 2')
        const ageField = form.getTextField('Age')
        const heightField = form.getTextField('Height')
        const weightField = form.getTextField('Weight')
        const eyesField = form.getTextField('Eyes')
        const skinField = form.getTextField('Skin')
        const hairField = form.getTextField('Hair')

        //modifier le text des champs 
        nameField.setText('Hello')
        ageField.setText('4 years')
        heightField.setText(`4' 2"`)
        weightField.setText('196 lbs')
        eyesField.setText('red')
        skinField.setText('black')
        hairField.setText('brown')*/

        // Convertir le document PDF en tableau de bytes
        const modifiedPdfBytes = await pdfDoc.save();

        fs.writeFileSync(fileName, modifiedPdfBytes);
        console.log('Le formulaire est bien rempli.');
       
    } catch (error) {
    console.error('Une erreur est survenue :', error);
    }
}

//test 
fields = ['CharacterName 2','Age','Height']
fillPdfForm('../PDF_pool/fill_form.pdf',fields);