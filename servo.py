# module for turning a servo motor using pulse-width modulation

from RPIO import PWM
import time

def rotate(seconds):
    servo = PWM.Servo()
    
    servo.set_servo(17, 1000)
    time.sleep(seconds)
    servo.stop_servo(17)
    return 0
