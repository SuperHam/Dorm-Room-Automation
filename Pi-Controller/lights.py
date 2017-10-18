'''
@author: alex kaariainen
LAH version 0.1.1
COMMAND CONSOLE VERSION OF LEAH
Localized Automation Host
'''
#MAKE SURE THIS IS RUN IN PYTHON3
from _operator import pos
if __name__ == '__main__':
    pass
import os
import RPi.GPIO as GPIO  # @UnresolvedImport
import time
GPIO.setmode(GPIO.BOARD) #.BOARD specifies that we are using pin # references rather than BCM (channel references)
GPIO.setup(11, GPIO.OUT)    #set up pin 11
pwm = GPIO.PWM(11,50)    #pin 11, frequency 50 Hz, presume 50 bc of NA utility frequency
msPerCycle = 20    # milliseconds per cycle, dictated by 1000 / frequency, default frequency is 50 bc utility frequency 
left = .7    #levers most downward position
right = 1.4    #levers most upward position
middle = (right - left) / 2 + left   #lever arm will be middle position
posCycle = (middle, left, middle, right, middle)    #Goes through a full cycle, off -> on
posOn = (middle, right, middle)    #lights on
posOff = (middle, left, middle)    #lights off
posReset = (middle, middle)    #lever arm back to middle pos
status = "go"
os.system('clear')
#bluetoothSerial = serial.Serial("/dev/refomm0", baudrate=9600)
#comd = bluetoothSerial.readLine()

print("Welcome to L.E.A.H. Version: 0.1.2")
print("_________________________")
time.sleep(.25)
print("Localized")
time.sleep(.15)
print("Electronic")
time.sleep(.15)
print("Automation")
time.sleep(.15)
print("Host")
print("__________________________")
time.sleep(.15)
time.sleep(1.5)
os.system('clear') #clears screen, if this does not work try 'clr' or try 'print(chr(27) + "[2J") to clear the screen
breaker = 0
while (breaker == 0):
    print("Subsystems are as follows:")
    print("___________")
    time.sleep(.1)
    print("Lights")
    print("Settings")
    print("Stop")
    print("___________")
    time.sleep(.5)
    subsystem = input("Which subsystem would you like to access: ")
    if subsystem == "lights" or subsystem == "light" or subsystem == "Lights" or subsystem == "Light":
        print("Gotcha, accessing lights.")
        time.sleep(.75)
        os.system('clear')
        while (status != "stop"):    #if code above is uncommentded then indent this
            os.system('clear')
            print("______")
            print("On")
            print("Off")
            print("Reset")
            print("Stop")
            print("Go back")
            print("Crazy lights for the brave.")
            print("_______")
            comd = input("Ready for you command:")
            #work on adding code that after x amt of time if no user input is present, then rest the motor
            if comd =="crazy lights" or comd == "crazy light":
                for i in range(5):
                    for pos in posCycle:
                        dutyCyclePercentage = pos * 100 / msPerCycle
                        pwm.start(dutyCyclePercentage)
                        time.sleep(.3)
            if comd == "on" or comd == "ON" or comd == "On":
                for i in range(1):
                    for pos in posOn:
                        dutyCyclePercentage = pos * 100 / msPerCycle
                        pwm.start(dutyCyclePercentage)
                        time.sleep(.3)    #pauses the program, this is necessary for the servo to move
                        print("Lights are turning on.")
            if comd == "off" or comd == "OFF" or comd == "Off":
                for i in range(1):
                    for pos in posOff:
                        dutyCyclePercentage = pos * 100 / msPerCycle
                        pwm.start(dutyCyclePercentage)
                        time.sleep(.3)
                        print("Lights are turning off.")
            if comd == "reset":
                for i in range(1):
                    for pos in posReset:
                        dutyCyclePercentage = pos * 100 / msPerCycle
                        pwm.start(dutyCyclePercentage)
                        time.sleep(.3)
                        print("Lever is reseting.")
            if comd == "help":
                print("To turn the lights on, 'on'.")
                print("To turn the lights off, 'off'.")
                print("To reset the lever arm, 'reset'.")
            if comd == "stop" or comd == "Stop":
                print("Stopping in progress")
                print("Goodbye")
                time.sleep(.5)
                os.system('clear')
                pwm.stop
                status = "stop"
                breaker = 1
            if comd == "Go Back" or comd == "go back" or comd == "GO BACK":
                os.system('clear')
                status = "stop"
            else:
                print("Try again.")
    if subsystem == "Settings" or subsystem == "Setting" or subsystem == "setting" or subsystem == "settings":
        os.system('clear')
        print("Nothing here yet...")
        print("This will mostly hold bluetooth items.")
        comd = input("Type 'go back' to return to the previous menus.")
        if comd == "Go Back" or comd == "go back" or comd == "GO BACK":
                os.system('clear')
                status = "stop"
    if subsystem == "stop" or subsystem == "Stop":
        breaker = 1
os.system('clear')
pwm.stop()    #relaxes the motor
GPIO.cleanup()    #cleans any resources used and helps to avoid damage to pi, it un-sets pin/channel naming system in use
