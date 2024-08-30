from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(echo=27, trigger=17, max_distance=0.5, 
			threshold_distance=0.3)

led = LED(22)

while True:
	print('Distance: ', sensor.distance*100)
	
	sensor.when_in_range = led.on()
	sensor.when_out_of_range = led.off()
	sleep(1)

