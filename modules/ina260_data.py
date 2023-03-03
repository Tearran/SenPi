import smbus
import json

def get_ina260_data(bus_num: int = 1, addr: int = 0x40) -> str:
    # Initialize I2C bus
    bus = smbus.SMBus(bus_num)

    # Configure INA260 for continuous mode with default settings
    bus.write_word_data(addr, 0x00, 0x7A18)

    # Read current, power, and voltage values
    current = bus.read_word_data(addr, 0x01)
    power = bus.read_word_data(addr, 0x03)
    voltage = bus.read_word_data(addr, 0x02)

    # Convert values to meaningful units
    current = round(current * 1.25 / 1000, 2) # mA
    power = round(power * 10 / 1000, 2) # mW
    voltage = round(voltage * 1.25 / 1000, 2) # V

    # Create a dictionary of the values
    data = {'current': current, 'power': power, 'voltage': voltage}

    # Return a JSON dump of the dictionary
    return json.dumps(data)
