const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
  service: "gmail",
  port: 587,
  secure: false,
  auth: {
    user: "isomya13@gmail.com",
    pass: "",
  },
});

const emails = [
  { email: "tyadi3110@gmail.com", name: "Aditya" },
  { email: "agrawalrashi73@gmail.com", name: "Rashi" },
  // {email: 'mananbagga7902@gmail.com', name: "Manan"}
];

const getCertificateData = (name) => {
  const filePath = `../output/Aditi Garg_UNHRC.svg`;
  const fs = require("fs");
  const certificateData = fs.readFileSync(filePath);
  return certificateData;
};

const sendCertificate = (email, name) => {
  const content = getCertificateData(name);

  const mailOptions = {
    from: "isomya13@gmail.com",
    to: email,
    subject: "Your Certificate",
    text: `Dear ${name}, Please find your attached certificate.`,
    attachments: [
      {
        filename: "certificate.svg",
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

emails.forEach((email) => {
  sendCertificate(email.email, email.name);
});

console.log("Server started!");
