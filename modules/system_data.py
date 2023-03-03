import os, platform, json, time

def get_system_info():
    # Get system information
    system_info = {}
    system_info['system'] = platform.system()
    system_info['node'] = platform.node()
    system_info['release'] = platform.release()
    system_info['version'] = platform.version()


    # Return system information as JSON
    return json.dumps(system_info)

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