import csv
import os
from xml.etree import ElementTree as ET

def generate_svg(name, com, template_path, output_path):
    

    try:
        tree = ET.parse(template_path)
        root = tree.getroot()

        for element in root.iter():
            if  element.get("id") == "name":
                element.text = name
                print(element.text)
            elif element.get("id") == "com":
                element.text = com

        with open(output_path, "wb") as file:
            file.write(ET.tostring(root))

    except FileNotFoundError:
        print(f"Error: File not found: {template_path}")
    except Exception as e:
        print(f"Error generating SVG: {e}")

def main():
    

    csv_file = "input.csv"  
    template_path = "template.svg" 
    output_folder = "output" 
    count =0
 
    os.makedirs(output_folder, exist_ok=True)

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader) 

        for row in reader:
            Country,name,Teammate,com = row
            output_file = os.path.join(output_folder, f"{name}_{com}.svg")
            generate_svg(name, com, template_path, output_file)
            count+=1
            if Teammate and Teammate.strip().lower() !='none':
                generate_svg(Teammate, com, template_path, f"{Teammate}_{com}.svg")
                count+=1

    print(count)




if __name__ == "__main__":
    main()
