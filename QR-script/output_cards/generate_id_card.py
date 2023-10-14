import xml.etree.ElementTree as ET
import base64
import os
import csv
import qrcode

if not os.path.exists("output_cards"):
    os.makedirs("output_cards")

def update_text(element_id, new_text, root):
    element = root.find(".//*[@id='" + element_id + "']")
    if element is not None:
        element.text = new_text


def update_qr(png_path, root):
    with open(png_path, "rb") as png_file:
        encoded_png = base64.b64encode(png_file.read()).decode("utf-8")

    image_element = root.find(".//*[@id='qr_shaurya']")
    if image_element is not None:
        image_element.set("{http://www.w3.org/1999/xlink}href", f"data:image/png;base64,{encoded_png}")


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)  # Add the data you want to encode
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    return qr_image


def update_card_data(input_file, output_file, participant_data):
    tree = ET.parse(input_file)
    root = tree.getroot()

    update_text("P_NAME", participant_data["name"], root)
    update_text("P_COLLEGE", participant_data["institute"], root)
    update_text("SHPS000000", participant_data["user_id"], root)
    update_text("P_ACCO", participant_data["accomodation"], root)

    qr_code = generate_qr_code(participant_data)
    if qr_code is not None:
        college_folder = os.path.join("output_qr", participant_data["institute_code"])
        if not os.path.exists(college_folder):
            os.makedirs(college_folder)

        qr_code_path = os.path.join(college_folder, f"{participant_data['user_id']}_qr.png")
        qr_code.save(qr_code_path)
        update_qr(qr_code_path, root)

    tree.write(output_file)


with open("participants.csv", mode="r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        output_folder = os.path.join("output_qr", row["college"])
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_file = os.path.join(output_folder, f"{row['sh_id']}_card.svg")
        update_card_data("participant_template.svg", output_file, row)




