import os
from datetime import datetime
import time 
import RPi.GPIO as GPIO
TRIGGER_VALUE = 25


GPIO.setmode(GPIO.BOARD)

relay = 7
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
os.system("bluetoothctl scan on > /dev/null 2>&1 &")

time.sleep(50)
os.system("bluetoothctl devices > list.txt")

prevReads = open("prevReads.txt", "a")

prevReads.write("\n")
prevReads.write(current_time)
prevReads.write("\n")

num_lines = sum(1 for line in open("list.txt"))

current_devices = open("list.txt", "r")

prevReads.write("Number of devices: ")
prevReads.write(str(num_lines))
prevReads.write("\n")
for line in current_devices:
	prevReads.write(line)

if num_lines >= TRIGGER_VALUE:
  GPIO.output(relay, GPIO.HIGH)
else:
  GPIO.output(relay, GPIO.LOW)

current_devices.close()
prevReads.close()
GPIO.cleanup()

print(current_time, ": Number of devices: ", num_lines)
