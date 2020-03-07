from dataStore import DataStore
from sensorsThread import SensorsThread
import time
import threading

ds = DataStore.getInstance() #singleton

# Build and start the sensors thread
sensorsThread = threading.Thread(target=SensorsThread.thread_function)
sensorsThread.start()

# every 10ms check the ds and print roll
while True:
	print("Current orientation (degrees): " + repr(ds.getOrientation()))
	time.sleep(0.01)
