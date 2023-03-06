#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import time


def clear_screen():
    os.system('clear')


def draw_bottom_bar():
    print('\n\n\033[32mPress ctrl+C to quit\033[0m')


def print_colored(text, color):
    print(f'\033[{color}m{text}\033[0m', end='')


# Set the path for the RAM disk and the input file
ram_disk_path = "/run/user/1000/"
input_file = os.path.join(ram_disk_path, "its/sensors-api.json")

# Check if the input file exists
if not os.path.exists(input_file):
    print(f'{input_file} does not exist')
    exit()

# Loop indefinitely
while True:
    clear_screen()

    # Load the JSON file
    with open(input_file, 'r') as f:
        json_data = json.load(f)

    f.close()

    # Iterate through each key-value pair in the JSON object
    for key, value in json_data.items():
        # If the value is a nested object, format it as a table
        if isinstance(value, dict):
            print_colored(f'\n{key}:', 37)
            print('')
            for subkey, subvalue in value.items():
                print_colored(f'\t{subkey}:', 37)
                print_colored(f'\t{subvalue}', 36)
                print('')
        else:
            # If the value is not a nested object, output it as-is
            print_colored(f'{key}:', 37)
            print_colored(f'{value}', 36)

    # Draw the bottom bar
    draw_bottom_bar()


    time.sleep(1)

# Close the input file

