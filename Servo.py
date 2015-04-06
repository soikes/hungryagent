class Servo
    from RPIO import PWM
    import time

    servo = PWM.Servo()

    def rotate(seconds):
        servo.set_servo(17, 1000)
        time.sleep(0.7)
        servo.stop_servo(17)
        return 0

    def rotate_forward(amount):
    
        return 0
    
    def rotate_backward(amount):
    
        return 0
