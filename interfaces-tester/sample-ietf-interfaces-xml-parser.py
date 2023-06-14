'''
XML Parser based on the ElementTree XML and lxml libraries.
Reference documentation:
* ElementTree: https://docs.python.org/3/library/xml.etree.elementtree.html
* lxml: https://lxml.de/
'''

import xml.etree.ElementTree as et
import subprocess
import pdb

ns = {}

tree = et.parse('sample-ietf-interfaces.xml')

root = tree.getroot()

'''
name = root.find('Sensor:name', ns).text
description = root.find('Sensor:description', ns).text
temperature = root.find('Sensor:temperature', ns).text
humidity = root.find('Sensor:humidity', ns).text
'''

data = {}

# pdb.set_trace()
