const fs = require('fs');
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  service: 'gmail',
  port: 587,
  secure: false,
  auth: {
    user: 'isomya13@gmail.com',
    pass: '',
  },
});

const getCertificateData = (certi) => {
  const filePath = certi; // Update the path accordingly
  const fs = require('fs');
  try{
    const certificateData = fs.readFileSync(filePath);
    return certificateData;
  }
  catch(err){
    return undefined
  }

  
};

const sendCertificate = (email, name, certi) => {
  const content = getCertificateData(certi);
  if(content === undefined){
    console.log("No certificate for", name)
    const logMessage = `Failed to send mail to ${name}.`;
      fs.appendFileSync('log.txt', logMessage);
    return;
  }

  const mailOptions = {
    from: 'isomya13@gmail.com',
    to: email,
    subject: 'GMUN 2024 Participation Certificate',
    text: `Dear ${name},

    We hope this message finds you well!
    
    It is with great pleasure that we present to you your participation certificate for the Global Model United Nations 2024 hosted by IIT Kharagpur. Your dedication, enthusiasm, and thoughtful contributions have greatly enriched the conference, making it a memorable experience for everyone involved.

    We appreciate your active participation and the positive impact you had on the conference. Your insights and commitment to diplomacy have truly contributed to the success of GMUN 2024.

    Thank you once again for being an integral part of GMUN 2024. If you have any feedback or suggestions, feel free to share them with us. We value your input as we strive to make each GMUN edition better than the last.
    
    Best wishes for your future endeavors, and we hope to welcome you back for GMUN 2025!
    
    Please find attached your participation certificate.

    Warm regards,
    
    Somyajeet Gupta Chowdhury
    Governor, Communiqué
    9113340204
    Global Model United Nations 2024
    IIT Kharagpur`,
    attachments: [
      {
        filename: 'certificate.pdf',
        content: content,
      },
    ],
  };

  console.log(mailOptions);

  transporter.sendMail(mailOptions, (err, info) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`Email sent to ${email}`);
    }
  });
};

// Read participant details from participants.json
const participantsData = fs.readFileSync('../kgp_participants.json', 'utf-8');
const participantsArray = JSON.parse(participantsData);

// Send emails to participants
participantsArray.forEach((participant) => {
  sendCertificate(participant.email, participant.name, participant.certi);
});

console.log('Emails sent to all participants!');
