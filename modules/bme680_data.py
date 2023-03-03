import json
import time
import bme680


def get_bme680_data():
    # Create BME680 sensor object
	try:
		sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
	except (RuntimeError, IOError):
		sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    # These calibration data can safely be commented
    # out, if desired.
	calibration_data = {}
	for name in dir(sensor.calibration_data):
		if not name.startswith('_'):
			value = getattr(sensor.calibration_data, name)
			if isinstance(value, int):
				calibration_data[name] = value


	# Initialize sensor
	sensor.set_humidity_oversample(bme680.OS_2X)
	sensor.set_pressure_oversample(bme680.OS_4X)
	sensor.set_temperature_oversample(bme680.OS_8X)
	sensor.set_filter(bme680.FILTER_SIZE_3)
	sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

	# set heat profile
	sensor.set_gas_heater_temperature(320)
	sensor.set_gas_heater_duration(150)
	sensor.select_gas_heater_profile(0)

    # Get readings from sensor
	sensor.get_sensor_data()
	gas_resistance = sensor.data.gas_resistance
	temperature = sensor.data.temperature
	pressure = sensor.data.pressure
	humidity = sensor.data.humidity

    # Build dictionary of sensor data
	bme680_data = {}
	bme680_data['timestamp'] = time.time()
	bme680_data['temperature'] = temperature
	bme680_data['humidity'] = humidity
	bme680_data['pressure'] = pressure
	bme680_data['gas_resistance'] = gas_resistance

	# Return sensor information as JSON
	return json.dumps(bme680_data)
