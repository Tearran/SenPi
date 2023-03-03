import json
import time
from bmp_280 import BMP280

def get_bmp280_data():
    bmp = BMP280(port=1, mode=BMP280.FORCED_MODE, oversampling_p=BMP280.OVERSAMPLING_P_x16, oversampling_t=BMP280.OVERSAMPLING_T_x1,
           filter=BMP280.IIR_FILTER_OFF, standby=BMP280.T_STANDBY_1000)

    data = {
        'timestamp': int(time.time()),
        'temperature': bmp.read_temperature(),
        'pressure': bmp.read_pressure(),
    }


    return json.dumps(data)
