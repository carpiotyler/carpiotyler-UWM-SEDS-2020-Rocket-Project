from __future__ import print_function
from twitchstream.outputvideo import TwitchBufferedOutputStream
from dataStore import DataStore
import picamera
import os
import datetime
import time

class TwitchThread:

	def thread_function():
		ds = DataStore.getInstance()
		tos = TwitchBufferedOutputStream(twitch_stream_key = os.environ['TWITCH_SECRET'], width=1280, height=720, fps=30, verbose=True)
		camera = picamera.PiCamera(1280, 720, framerate=24)
		camera.start_preview()
		camera.annotate_background = picamera.Color('black')
		camera.annotate_text = "Current orientation: " + ds.getOrientation()
		sleep(2)
		now = datetime.now()
		# Begine recording the video
		camera.start_recording('launches/launch-' + now.strftime("%m-%d-%H-%M-%S") +'.h264')

		while True:
			# Get current frame
			camera.annotate_text = "Current orientation: " + ds.getOrientation()
			frame = camera.frame
			tos.send_video_frame(frame)
			time.sleep(1/30)
