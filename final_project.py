# importing libraries
import RPi.GPIO as GPIO # manages rpi pins
import drivers          # manages lcd
import time             # to use sleep function 

display = drivers.Lcd() # creating lcd object

# defining GPIO pins in Raspberry pi
L1 = 25
L2 = 8
L3 = 7
L4 = 1

C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Initializing the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Pull-down resistors

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Detecting key pressed by sending a single pulse

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        #print(characters[0])
        display.lcd_display_string(characters[0],1)
    if(GPIO.input(C2) == 1):
        #print(characters[1])
        display.lcd_display_string(characters[1],1)
    if(GPIO.input(C3) == 1):
        #print(characters[2])
        display.lcd_display_string(characters[2],1)
    if(GPIO.input(C4) == 1):
        #print(characters[3])
        display.lcd_display_string(characters[3],1)
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # calling the readLine function for each row of the keypad
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")
