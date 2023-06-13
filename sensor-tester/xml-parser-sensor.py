'''
XML Parser based on the ElementTree XML API.
Reference documentation: https://docs.python.org/3/library/xml.etree.elementtree.html
'''

import xml.etree.ElementTree as et
import subprocess
import pdb

ns = {'Sensor': 'https://iot-sensor.org/iot/Sensor'}

tree = et.parse('sensor_data.xml')

root = tree.getroot()

name = root.find('Sensor:name', ns).text
description = root.find('Sensor:description', ns).text
temperature = root.find('Sensor:temperature', ns).text
humidity = root.find('Sensor:humidity', ns).text

data = {
    'name': name,
    'description': description,
    'temperature': temperature,
    'humidity': humidity
}

print('SENSOR XML DATA PARSER - PARSING DATA FROM XML FILE AND CREATING NGSI-LD ENTITY')
print('PARSED XML SENSOR DATA:')
print(data)
print('\n')

print('CREATING NGSI-LD ENTITY GIVEN PARSED DATA...')
# Runs create-sensor-entity.py script passing parsed XML data as arguments.
subprocess.run(["python3.9", "create-sensor-entity.py", name, description, temperature, humidity])

# pdb.set_trace()