# This file holds our sensors thread, which reads every sensor's data
# and updates the dataStore accordingly
from dataStore import DataStore
import time
import math
import board
import busio
import logging
import adafruit_lsm9ds1

# I2C connection, when we switch to SPI (Using GPIO pins just
# change how we set up the sensor here:
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

class SensorsThread:

	def thread_function():
		ds = DataStore.getInstance() #singleton
		logging.info("Sensors thread started.")
		while True:
			# Read acceleration, magnetometer, gyroscope, temperature.
			accel_x, accel_y, accel_z = sensor.acceleration
			mag_x, mag_y, mag_z = sensor.magnetic
			gyro_x, gyro_y, gyro_z = sensor.gyro
			temp = sensor.temperature
			# Update roll in the data store (complicated)
			normalizedZ = round(accel_z / 9.8, 2)
			normalizedY = round(accel_y / 9.8, 2)
			orientation = 0.0
			# This if block protects us from 0 division (edge cases)
			# we check the y accel and use its direction to choose from -90 or 90
			if normalizedZ == 0.00 and normalizedY > 0:
				orientation = -90.0
			elif normalizedZ == 0.00 and normalizedY < 0:
				orientation = 90.0
			else:
				orientation = round(math.degrees(math.atan(-normalizedY / normalizedZ)), 1)
				# adjusting for upside down cases
				if normalizedZ < 0 and normalizedY > 0:
					orientation = -180 + orientation
				elif normalizedZ < 0 and normalizedY < 0:
					orientation = 180 + orientation
			ds.setRoll(gyro_x)
			ds.setOrientation(orientation)
			time.sleep(0.01)
