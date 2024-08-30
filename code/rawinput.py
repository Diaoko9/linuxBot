import keyboard

while True :
    input1 = keyboard.read_event()
    

    while input1 == keyboard.KEY_DOWN :
        direction = input1.name
        print(direction)
        
    if direction == 'q' :
        break



