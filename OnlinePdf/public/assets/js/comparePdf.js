// Spécifier l'emplacement du script du worker de PDF.js
pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.6.347/pdf.worker.min.js";

// Chargement des fichiers PDF avec la bibliothèque PDF.js
function loadPdf(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = function (e) {
      const pdfData = new Uint8Array(e.target.result);
      pdfjsLib
        .getDocument({ data: pdfData })
        .promise.then((pdf) => {
          resolve(pdf);
        })
        .catch((error) => {
          reject(error);
        });
    };
    reader.readAsArrayBuffer(file);
  });
}

// Comparaison des fichiers PDF
function comparePDF() {
  const fileInput = document.getElementById("file-input");
  const files = fileInput.files;

  if (files.length === 2) {
    const file1 = files[0];
    const file2 = files[1];

    Promise.all([loadPdf(file1), loadPdf(file2)])
      .then((results) => {
        const pdf1 = results[0];
        const pdf2 = results[1];

        // Récupérer le nombre total de pages des fichiers PDF
        const numPages1 = pdf1.numPages;
        const numPages2 = pdf2.numPages;

        // Comparaison des pages de chaque fichier PDF
        let differentPages = [];
        let currentPage = 1;
        compareNextPage();

        function compareNextPage() {
          if (currentPage > Math.min(numPages1, numPages2)) {
            console.log("Comparaison terminée !");
            if (differentPages.length === 0) {
              displayPopup("Les deux fichiers sont identiques.");
            } else {
              displayPopup(
                `Les fichiers diffèrent sur les pages suivantes: ${differentPages.join(
                  ", "
                )}`
              );
            }
            return;
          }

          comparePdfPages(pdf1, pdf2, currentPage, (pageNumber) => {
            differentPages.push(pageNumber);
          }).finally(() => {
            currentPage++;
            compareNextPage();
          });
        }
      })
      .catch((error) => {
        console.error(
          "Une erreur s'est produite lors du chargement des fichiers PDF.",
          error
        );
      });
  } else {
    console.log("Veuillez sélectionner deux fichiers PDF à comparer.");
  }
}

// Comparaison des pages de fichiers PDF individuels
function comparePdfPages(pdf1, pdf2, pageNumber, onDifferenceFound) {
  return new Promise((resolve, reject) => {
    Promise.all([pdf1.getPage(pageNumber), pdf2.getPage(pageNumber)])
      .then((results) => {
        const page1 = results[0];
        const page2 = results[1];

        // Conversion des pages en images pour faciliter la comparaison
        const canvas1 = document.createElement("canvas");
        const context1 = canvas1.getContext("2d");
        const viewport1 = page1.getViewport({ scale: 1.0 });
        canvas1.height = viewport1.height;
        canvas1.width = viewport1.width;
        page1.render({ canvasContext: context1, viewport: viewport1 });

        const canvas2 = document.createElement("canvas");
        const context2 = canvas2.getContext("2d");
        const viewport2 = page2.getViewport({ scale: 1.0 });
        canvas2.height = viewport2.height;
        canvas2.width = viewport2.width;
        page2.render({ canvasContext: context2, viewport: viewport2 });

        const image1 = canvas1.toDataURL("image/png");
        const image2 = canvas2.toDataURL("image/png");

        // Comparaison des images des pages
        if (image1 !== image2) {
          onDifferenceFound(pageNumber);
        }
        resolve();
      })
      .catch((error) => {
        console.error(
          `Une erreur s'est produite lors de la comparaison de la page ${pageNumber}.`,
          error
        );
        reject(error);
      });
  });
}

function displayPopup(message, width = "300px", height = "100px") {
  const popup = document.createElement("div");
  popup.classList.add("popup");

  const content = document.createElement("div");
  content.classList.add("popup-content"); 
  content.innerText = message;

  popup.appendChild(content);

  const closeButton = document.createElement("span");
  closeButton.classList.add("popup-close");
  closeButton.innerHTML = "&times;";
  closeButton.addEventListener("click", () => {
    popup.remove();
  });
  popup.appendChild(closeButton);

  document.body.appendChild(popup);
}
