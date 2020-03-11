from dataStore import DataStore
from sensorsThread import SensorsThread
from twitchThread import TwitchThread
import time
import threading

ds = DataStore.getInstance() #singleton

### INITIALIZE BACKGROUND PROCESSES ###

# Build and start the sensors thread - start recording data in the DataStore
sensorsThread = threading.Thread(target=SensorsThread.thread_function)
sensorsThread.start()
# Build and start the twitch stream thread - start streaming video to Twitch with overlaid data
twitchThread = threading.Thread(target=TwitchThread.thread_function)
twitchThread.start()

### MAIN ###

# every 10ms check the ds and print roll
while True:
	# print("Current orientation (degrees): " + repr(ds.getOrientation()))
	time.sleep(1)
