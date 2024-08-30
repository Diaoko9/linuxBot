#!/usr/bin/python

from gpiozero import LED
from time import sleep

#setup LEDs
led1 = LED(27)
led2 = LED(22)

#getting values
a = input("Input Value: ")
b = input("Input second Value: ")

#LED1 blinks
led1.on()
sleep(5)
led1.off()
sleep(5)

#Calculating
c = a + b

#Print
print(int(a)+int(b))
