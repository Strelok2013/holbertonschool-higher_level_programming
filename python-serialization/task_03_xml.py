#!/usr/bin/python3
import xml.etree.ElementTree as ET
""""""


def serialize_to_xml(dictionary, filename):
    """"""
    data = ET.Element('data')
    for k in dictionary.keys():
        ET.SubElement(data, k).text = dictionary[k]
    tree = ET.ElementTree(data)
    tree.write(filename)

def deserialize_from_xml(filename):
    """"""
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {} 
    for child in root:
        data[child.tag] = child.text

    return data
   
def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()