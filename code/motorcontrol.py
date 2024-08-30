from gpiozero import Motor


rmotor = Motor(2, 3)
lmotor = Motor(14, 15)

def forward():
	rmotor.forward(speed = 0.5)
	lmotor.forward(speed = 0.5)
	
def reverse():
	rmotor.backward(speed = 0.5)
	lmotor.backward(speed = 0.5)
	
def stop():
	rmotor.stop()
	lmotor.stop()
	
def right():
	rmotor.forward(speed = 0.25)
	lmotor.backward(speed = 0.1 )
	
def left():
	rmotor.backward(speed = 0.1 )
	lmotor.forward(speed = 0.25)
	
while True:
		
	#command = input("w(forward) d(right) a(left) s(reverse)")
	#if len(command) == 1:
	#	command.append("enter")
	#	direction = command[0]
	#	command = ""
	direction = getkey()
	print(direction)
	if direction == "w":
		forward()
	
	if direction == "d":
		right()
		
	if direction == "a":
		left()
	
	if direction == "s":
		reverse()
	
	else:
		stop()
	
	
