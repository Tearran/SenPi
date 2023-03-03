import json
import time
from .bmp_280 import BMP280
from .smbus2 import SMBus
from .bme680 import BME680
from .ina260 import INA260

i2c_addresses = {
    'bmp280': 0x76,
    'bme680': 0x77,
    'ina260': 0x40
}

def get_bmp280_data():
    bmp = BMP280(i2c_addr=i2c_addresses['bmp280'])

    data = {
        'timestamp': int(time.time()),
        'temperature': bmp.get_temperature(),
        'pressure': bmp.get_pressure(),
    }

    return json.dumps(data)

def get_bme680_data():
    bme = BME680(i2c_addr=i2c_addresses['bme680'])

    data = {
        'timestamp': int(time.time()),
        'temperature': bme.get_temperature(),
        'pressure': bme.get_pressure(),
        'humidity': bme.get_humidity(),
    }

    return json.dumps(data)

def get_ina260_data():
    ina = INA260(i2c_addr=i2c_addresses['ina260'])

    data = {
        'timestamp': int(time.time()),
        'voltage': ina.get_voltage(),
        'current': ina.get_current(),
        'power': ina.get_power(),
    }

    return json.dumps(data)

def get_system_data():
    data = {
        'timestamp': int(time.time()),
        'cpu_temp': get_cpu_temperature(),
        'ram_usage': get_ram_usage(),
    }

    return json.dumps(data)

def get_cpu_temperature():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp = float(f.read()) / 1000.0
    return temp

def get_ram_usage():
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()
        total_str = lines[0].split()[1]
        free_str = lines[1].split()[1]
        buffers_str = lines[2].split()[1]
        cached_str = lines[3].split()[1]
        total = int(total_str)
        free = int(free_str)
        buffers = int(buffers_str)
        cached = int(cached_str)
        used = total - free - buffers - cached
        usage = used / total * 100.0
    return usage

def get_sensor_data():
    sensor_data = {}
    
    try:
        sensor_data['bmp280'] = json.loads(get_bmp280_data())
    except:
        pass
    
    try:
        sensor_data['bme680'] = json.loads(get_bme680_data())
    except:
        pass
    
    try:
        sensor_data['ina260'] = json.loads(get_ina260_data())
    except:
        pass
    
    return json.dumps(sensor_data)
