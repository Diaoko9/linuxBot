from gpiozero import OutputDevice, InputDevice
import time

start_time = 0
end_time = 0

###Ultrasonic sensor initialize
trig = OutputDevice(pin=17, active_high=True, initial_value=False)
echo = InputDevice(pin=27, pull_up=False)
while True:
	trig.on()
	time.sleep(1)
	trig.off()

###Reading echo Pulse
	
	echo_state = False

###Rising
	if echo_state==False and echo.is_active==True :
		echo_state = True
		start_time = time.perf_counter_ns()
		print(start_time)
	
###Falling
	if echo_state==True and echo.is_active==False :
		echo_state = False
		end_time = time.perf_counter_ns()
		print(end_time)

###Distance Calculating
	elapsed_time = end_time - start_time
	distance =(elapsed_time*340)/2
	print(elapsed_time)
	
	
	#rint(elapsed_time*340)
'''
distance =(elapsed_time*340)/2
print(distance)
'''
