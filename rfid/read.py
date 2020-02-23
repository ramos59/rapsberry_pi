import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

try:
	print("RFID is ready to read")
	id, text = reader.read()
	print("The RFID ID: {}".format(id))
	print("The text on the RFID: {}".format(text))

finally:
	GPIO.cleanup()
	time.sleep(5)
