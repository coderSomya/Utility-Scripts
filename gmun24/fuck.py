svg_file_path = './output/Aditi Garg.svg'
output_file_path = 'Aditi Garg.png'

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image


# Parse the SVG file
drawing = svg2rlg(svg_file_path)

# Render the drawing to an image
img_data = renderPM.drawToFile(drawing, output_file_path, fmt="PNG")  # Adjust format ("PNG" or "JPEG")

# Open and save the image using PIL
img = Image.open(output_file_path)
img.save(output_file_path)  # Overwrites with chosen format

print(f"SVG converted to {output_file_path} successfully!")

