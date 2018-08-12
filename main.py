import RPi.GPIO as GPIO
from io import BytesIO
from PIL import Image
import time
import picamera

with picamera.PiCamera as camera:
  stream = BytesIO()
  camera.start_preview()
  GPIO.setmode(GPIO.BCM)
  out26 = GPIO.setup(26, GPIO.OUT)
  in19 = GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.output(26, True)
  while 1:
    if GPIO.input(19):
      print("BUTTON PRESSED")
      camera.capture()
      camera.capture(stream, format='jpeg')
      # "Rewind" the stream to the beginning so we can read its content
      stream.seek(0)
      image = Image.open(stream)

    time.sleep(0.5)


