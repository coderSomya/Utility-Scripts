import os
from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import Drawing
from PIL import Image

# Folder paths (replace with your actual paths)
input_folder = "output"
output_folder = "final"

# Check if output folder exists, create it if necessary
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("Created the 'final' folder for converted JPEGs.")

# Function to handle individual SVG conversion
def convert_svg_to_jpeg(svg_file):
    """Converts an SVG file to JPEG and saves it in the output folder."""

    filename, _ = os.path.splitext(svg_file)  # Extract filename without extension

    # Read and parse the SVG
    with open(svg_file, "rb") as f:
        svg_data = f.read()
    drawing = svg2rlg(svg_data)

    # Render as a PNG and convert to JPEG
    img = Image.frombytes("RGB", drawing.getSize(), drawing.render())

    # Create output path within the final folder
    output_path = os.path.join(output_folder, f"{filename}.jpg")

    # Save the JPEG
    img.save(output_path, "JPEG")
    print(f"Converted '{svg_file}' to '{output_path}'")

# Loop through SVG files in the input folder
for svg_file in os.listdir(input_folder):
    if svg_file.endswith(".svg"):
        convert_svg_to_jpeg(os.path.join(input_folder, svg_file))

print("All SVG files converted successfully and saved in the 'final' folder!")
