import smbus2
import json

def get_ina260_data():
    # Initialize SMBus
    bus = smbus2.SMBus(1)

    # Address of the INA260 device
    address = 0x40

    # Register addresses for configuring the device
    config_reg = 0x00
    shunt_reg = 0x01
    bus_reg = 0x02
    power_reg = 0x03

    # Configure the device to operate in continuous mode with default settings
    bus.write_word_data(address, config_reg, 0x0187)

    # Read the data from the device
    shunt_voltage = bus.read_word_data(address, shunt_reg)
    bus_voltage = bus.read_word_data(address, bus_reg)
    power = bus.read_word_data(address, power_reg)

    # Convert the raw data to human-readable units
    shunt_voltage = shunt_voltage * 0.00001  # Shunt voltage is in units of 10 uV
    bus_voltage = bus_voltage * 0.001  # Bus voltage is in units of 1 mV
    power = power * 0.0001  # Power is in units of 100 uW

    # Create a dictionary to store the data
    data = {
        'shunt_voltage': shunt_voltage,
        'bus_voltage': bus_voltage,
        'module_power': power
    }

    return json.dumps(data)

