from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

def turn_on_led():
    led.on()
    print("LED on!")
        
def turn_off_led():
    led.off()
    print("LED off!")

if __name__ == '__main__':
    button.when_pressed = turn_on_led
    button.when_released = turn_off_led

    pause()