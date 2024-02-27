const fs = require('fs');
const path = require('path');
const jsPDF = require('jspdf'); // Assuming you've installed jsPDF

const inputFolder = './output';
const outputFolder = './output2';

fs.readdir(inputFolder, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }

  files.forEach(file => {
    if (path.extname(file) === '.svg') {
      const svgFilePath = path.join(inputFolder, file);
      const pdfFilePath = path.join(outputFolder, path.basename(file, '.svg') + '.pdf');

      fs.readFile(svgFilePath, 'utf8', (err, svgData) => {
        if (err) {
          console.error(err);
          return;
        }

        const doc = new jsPDF();
        doc.html(svgData, {
          callback: (doc) => {
            doc.save(pdfFilePath);
            console.log(`${file} converted to PDF`);
          }
        });
      });
    }
  });
});
