import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def convert_json_to_xml(json_data, root_name="root"):
    """
    Converts a JSON object (dictionary) into a formatted XML string.
    :param json_data: Dictionary containing the data.
    :param root_name: Name of the XML root element.
    """
    # Create the root element
    root = ET.Element(root_name)

    # Function to recursively add elements
    for key, value in json_data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Convert to string and prettify (add indentation)
    xml_str = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="   ")
    
    return pretty_xml

# Example Usage
data = {"id": 101, "name": "Gemini", "role": "AI Assistant"}
print(convert_json_to_xml(data, "UserAccount"))
