import tkinter as tk
import xml.etree.ElementTree as ET
import os

tree = ET.parse('task02.xml')
xml_root = tree.getroot()

for action in xml_root.iter('step_item1'):

    suchstring = str(action.text.strip())
    print("suchen", suchstring)


print("congratulation")