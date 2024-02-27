const svgToPdf = require('svg-to-pdf'); 

const inputFolder = './output'; 
const outputFolder = './output3';

const fs = require('fs'); 

if (!fs.existsSync(outputFolder)) {
  fs.mkdirSync(outputFolder);
}

fs.readdirSync(inputFolder).forEach(file => {
  if (file.endsWith('.svg')) {
    const inputFilePath = `${inputFolder}/${file}`;
    const outputFilePath = `${outputFolder}/${file.replace('.svg', '.pdf')}`;

    svgToPdf(inputFilePath, outputFilePath)
      .then(() => {
        console.log(`Converted ${file} to ${outputFilePath}`);
      })
      .catch(error => {
        console.error(`Error converting ${file}:`, error);
      });
  }
});
