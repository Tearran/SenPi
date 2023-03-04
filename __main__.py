#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smbus2
import os, json, time
from modules import system_data
from modules import bme680_data
from modules import ina260_data
from modules import bmp280_data

# Set the path for the RAM disk and the output file
ram_disk_path = "/run/user/1000/"
output_file = os.path.join(ram_disk_path, "its/i2cSensors.json")


# Check if the directory exists and create it if it doesn't
if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))
print(f"""
	Json located at {output_file}
	Ctrl-C to exit
""")
# Set the I2C bus number
bus_num = 1

# Create an instance of the SMBus class
bus = smbus2.SMBus(bus_num)

# List of I2C addresses to scan
#addresses = [0x77, 0x76]
addresses = range(0x03, 0x78)
# Initialize an empty dictionary to store sensor data
data = {}
system_dump = json.loads(system_data.get_system_info())
data["system_dump"] = system_dump
cpu_dump = json.loads(system_data.get_system_data())
data["cpu_dump"] = cpu_dump
i=0

while True:
# Scan the I2C bus for connected devices
	for address in addresses:
	    try:
	        bus.read_byte(address)
	        # If the sensor is present at the address, retrieve data from it
	        if address == 0x77:
	            bme680_dump = json.loads(bme680_data.get_bme680_data())
	            data["bme680"] = bme680_dump
	        elif address == 0x76:
	            bmp280_dump = json.loads(bmp280_data.get_bmp280_data())
	            data["bmp280"] = bmp280_dump
	        elif address == 0x40:
	            ina260_data_dump = json.loads(ina260_data.get_ina260_data())
	            data["ina260_data"] = ina260_data_dump
	    except:
	        # If the sensor is not present at the address, skip it
	        pass

# Convert dictionary to JSON string
	json_data = json.dumps(data, indent=2)

# Write JSON string to file
	with open(output_file, 'w') as f:
		f.write(json_data)

	time.sleep(1)
