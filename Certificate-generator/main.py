import xml.etree.ElementTree as ET

def personalize_certificate(name, college):
    
    with open("template.svg", "r") as file:
        svg_content = file.read()

    root = ET.fromstring(svg_content)

   
    placeholders = {
        "participant_name": name,
        "participant_college": college,
    }

    for text_elem in root.iter("{http://www.w3.org/2000/svg}text"):
        if "id" in text_elem.attrib and text_elem.attrib["id"] in placeholders:
            text_elem.find("{http://www.w3.org/2000/svg}tspan").text = placeholders[text_elem.attrib["id"]]

    
    personalized_svg = ET.tostring(root, encoding='utf8').decode('utf8')

    with open("personalized_certificate.svg", "w") as output_file:
        output_file.write(personalized_svg)

 

    

if __name__ == "__main__":
    participant_name = "Somyajeet Chowdhury"  
    participant_college = "iitkgp" 
    personalize_certificate(participant_name, participant_college)
