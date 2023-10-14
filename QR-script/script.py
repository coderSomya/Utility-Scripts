import os
import requests
import qrcode
from io import BytesIO
import json

# API endpoint URL
api_url = "http://localhost:5000/get-users"  # Replace with your API endpoint

# Create a folder to save QR codes
output_folder = "qrcodes"
os.makedirs(output_folder, exist_ok=True)

def get_api_data():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def generate_qr_code(data, output_path):
    json_data = json.dumps(data)  # Serialize JSON data to a string
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

def main():
    # Get data from the API
    api_data = get_api_data()

    if api_data:
        # Process each JSON object and generate QR code
        for i, obj in enumerate(api_data):
            output_path = os.path.join(output_folder, f"qrcode_{i + 1}.png")

            # Generate QR code with JSON data
            generate_qr_code(obj, output_path)
            print(f"QR code saved to: {output_path}")



if __name__ == "_main_":
    main()




