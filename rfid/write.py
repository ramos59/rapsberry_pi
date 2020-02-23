import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()

try:
	text = input('data: ')
	print("Put RFID chip near reader.")
	reader.write(text)
	print("Wrote "{}" to RFID chip".format(text))
finally:
	GPIO.cleanup()
