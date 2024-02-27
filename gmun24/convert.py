import csv
import os
from xml.etree import ElementTree as ET


import csv

def create_name_set_from_csv(file_path, name_column_index=0):

   name_set = set()

   with open(file_path, 'r') as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
           if row:
             name = row[0]
             name = name.strip().lower()
             name_set.add(name)
             print(name)

   return name_set

file_path = "winners.csv"
winners = create_name_set_from_csv(file_path)
print(winners, len(winners))


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


check = set()


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
            output_file = os.path.join(output_folder, f"{name}.svg")
            if name.strip().lower() in winners:
                 check.add(name)
            else: 
                generate_svg(name, com, template_path, output_file)
                count+=1

            if Teammate and Teammate.strip().lower() !='none':
                output_file = os.path.join(output_folder, f"{Teammate}.svg")

                if name.strip().lower() in winners:
                   check.add(name)
                else: 
                    generate_svg(Teammate, com, template_path, output_file)
                    count+=1

    print(count)


if __name__ == "__main__":
    main()
    
    print("checking for winners.....")
    print(check)
    print("finished...............")
