#!/usr/bin/env python3

import os
import time

print("Exporting GPIO 40 as an input (Button 0)...")
os.system("echo 40 > /sys/class/gpio/export")
os.system("echo in > /sys/class/gpio/gpio40/direction")
print("Exporting GPIO 41 as an input... (Button 1)")
os.system("echo 41 > /sys/class/gpio/export")
os.system("echo in > /sys/class/gpio/gpio41/direction")

print("Exporting GPIO 42 as an output... (LED 0)")
os.system("echo 42 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio42/direction")

print("Exporting GPIO 43 as an output... (LED 1)")
os.system("echo 43 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio43/direction")

print("Exporting GPIO 44 as an output... (LED 2)")
os.system("echo 44 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio44/direction")

print("Exporting GPIO 45 as an output... (LED 3)")
os.system("echo 45 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio45/direction")
time.sleep(1)

print("")
print("Switching on LED0...")
os.system("echo 1 > /sys/class/gpio/gpio42/value")
time.sleep(1)

print("Switching on LED1...")
os.system("echo 1 > /sys/class/gpio/gpio43/value")
time.sleep(1)

print("Switching on LED2...")
os.system("echo 1 > /sys/class/gpio/gpio44/value")
time.sleep(1)

print("Switching on LED3...")
os.system("echo 1 > /sys/class/gpio/gpio45/value")
time.sleep(1)

print("Switching off LED0...")
os.system("echo 0 > /sys/class/gpio/gpio42/value")
time.sleep(1)

print("Switching off LED1...")
os.system("echo 0 > /sys/class/gpio/gpio43/value")
time.sleep(1)

print("Switching off LED2...")
os.system("echo 0 > /sys/class/gpio/gpio44/value")
time.sleep(1)

print("Switching off LED3...")
os.system("echo 0 > /sys/class/gpio/gpio45/value")
time.sleep(1)

print("")
print("Starting LED shift control scenario...")
time.sleep(1)
print("Switching on LED0...")
os.system("echo 1 > /sys/class/gpio/gpio42/value")
print("Press Button 0 to shift left and Button 1 to shift right")

currentLED = 0
button0State = False
button1State = False
while True:
    with open("/sys/class/gpio/gpio40/value", "r") as button0FileIn:
        button0State = (button0FileIn.readline().strip() == "1")
    if button0State:
        print("Button 0 pressed. Shifting left...")
        print("Switching off LED{}...".format(currentLED))
        os.system("echo 0 > /sys/class/gpio/gpio{}/value".format(currentLED + 42))
        currentLED = (currentLED - 1) % 4
        print("Switching on LED{}...".format(currentLED))
        os.system("echo 1 > /sys/class/gpio/gpio{}/value".format(currentLED + 42))
        while button0State:
            with open("/sys/class/gpio/gpio40/value", "r") as button0FileIn:
                button0State = (button0FileIn.readline().strip() == "1")
    with open("/sys/class/gpio/gpio41/value", "r") as button1FileIn:
        button1State = (button1FileIn.readline().strip() == "1")
    if button1State:
        print("Button 1 pressed. Shifting right...")
        print("Switching off LED{}...".format(currentLED))
        os.system("echo 0 > /sys/class/gpio/gpio{}/value".format(currentLED + 42))
        currentLED = (currentLED + 1) % 4
        print("Switching on LED{}...".format(currentLED))
        os.system("echo 1 > /sys/class/gpio/gpio{}/value".format(currentLED + 42))
        while button1State:
            with open("/sys/class/gpio/gpio41/value", "r") as button1FileIn:
                button1State = (button1FileIn.readline().strip() == "1")
    