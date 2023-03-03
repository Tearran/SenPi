#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, json
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

if __name__ == '__main__':
    # Get sensor data
    bme680_dump = json.loads(bme680_data.get_bme680_data())
    system_dump = json.loads(system_data.get_system_info())
    cpu_dump = json.loads(system_data.get_system_data())
    ina260_dump = json.loads(ina260_data.get_ina260_data())
    bmp280_dump = json.loads(bmp280_data.get_bmp280_data())
    

    # Add sensor data and system information to final dictionary
    data = {
        "system": system_dump,
		"cpu": cpu_dump,
        "bme680": bme680_dump,
		"ina260": ina260_dump,
        "bmp280": bmp280_dump
    }

    # Convert dictionary to JSON string
    json_data = json.dumps(data)

    # Write JSON string to file
    with open(output_file, 'w') as f:
        f.write(json_data)