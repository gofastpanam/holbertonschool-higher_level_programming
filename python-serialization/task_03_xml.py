#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    Parameters:
        dictionary (dict): Dictionary to serialize
        filename (str): Filename to save the XML data
    """
    # Create the root element
    root = ET.Element('data')

    # Iterate through the dictionary and create child elements
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)  # Ensure value is converted to string

    # Create the tree and write it to a file
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file to a Python dictionary.

    Parameters:
        filename (str): Filename of the XML file to deserialize

    Returns:
        dict: Dictionary representing the XML data
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Initialize the dictionary
    dictionary = {}

    # Iterate through the children of the root element
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
