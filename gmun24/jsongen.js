const fs = require('fs');
const xlsx = require('xlsx');

const workbook = xlsx.readFile('merge/cq_delegates.xlsx');
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];

// Convert the worksheet to JSON
const jsonData = xlsx.utils.sheet_to_json(worksheet);

// Function to process each participant and create JSON structure
function processParticipant(participant) {
    const trimmedName = participant["Candidate's Name"].trim();
    const lowercaseName = trimmedName.toLowerCase().replace(/\s+/g, '');
    const certiPath = `../pdfs/${lowercaseName}.pdf`;

    return {
        name: trimmedName,
        email: participant["Candidate's Email"],
        certi: certiPath,
    };
}

// Create an array of participant details
const participantsArray = jsonData.map(processParticipant);

// Write the JSON array to a file
fs.writeFileSync('cq_delegates.json', JSON.stringify(participantsArray, null, 2));

console.log('JSON file created successfully.');
