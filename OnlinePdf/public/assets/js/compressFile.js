// Fonction pour la compression extrême
function compressFileExtremely(fileContent) {
    return 'Contenu du fichier compressé (compression extrême)';
}

// Fonction pour la compression recommandée
function compressFileRecommended(fileContent) {
    return 'Contenu du fichier compressé (compression recommandée)';
}

// Fonction pour moins de compression
function compressFileLess(fileContent) {
    return 'Contenu du fichier compressé (moins de compression)';
}

compressFile(choix);{

    if (this.fileContent && this.compressionType) {
        let compressedFileContent = '';
        
        if (this.compressionType === 'Extreme') {
            compressedFileContent = compressFileExtremely(this.fileContent);
        } else if (this.compressionType === 'Recommandée') {
            compressedFileContent = compressFileRecommended(this.fileContent);
        } else if (this.compressionType === 'Moins') {
            compressedFileContent = compressFileLess(this.fileContent);
        }

        console.log('Fichier compressé avec succès.');
        console.log('Contenu du fichier compressé :', compressedFileContent);
    } else {
        console.log('Veuillez sélectionner un fichier et choisir un type de compression.');
    }
}
