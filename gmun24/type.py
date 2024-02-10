from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import Drawing
from PIL import Image
import os

folder_path = "output"

final_folder = os.path.join(folder_path, "final")
if not os.path.exists(final_folder):
    os.makedirs(final_folder)

def convert_svg_to_jpeg(svg_file):
   

    filename, _ = os.path.splitext(svg_file)

    with open(svg_file, "rb") as f:
        svg_data = f.read()
    drawing = svg2rlg(svg_data)

    img = Image.frombytes("RGB", drawing.getSize(), drawing.render())
    output_path = os.path.join(final_folder, f"{filename}.jpg")

    img.save(output_path, "JPEG")
    print(f"Converted '{svg_file}' to '{output_path}'")

for svg_file in os.listdir(folder_path):
    if svg_file.endswith(".svg"):
        convert_svg_to_jpeg(os.path.join(folder_path, svg_file))

print("All SVG files converted and saved in the 'final' folder!")
