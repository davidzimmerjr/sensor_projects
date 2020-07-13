# fifth
from gpiozero import Button
from signal import pause

# i = 0

def say_hello():
#     i = i + 1
    print("Hello!")
    
    
button = Button(2)

button.when_pressed = say_hello

pause()

# fourth
# from gpiozero import Button
# 
# 
# button = Button(2)
# 
# button.wait_for_press()
# print("Button was pressed")


# third attempt
# from gpiozero import Button
# 
# button = Button(2)
# 
# while True:
#     if button.is_pressed:
#         print("Button is pressed")
#     else:
#         print("Button is not pressed")

# first attempt
# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# second attempt
# from gpiozero import Button
# from signal import pause
# 
# button = Button(2)
# if button.is_pressed:
#     print("Pressed")
# 
# pause()