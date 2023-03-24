import time
import math
class robotmockup:
    WHEEL_BASE_WIDTH         = 117  
    WHEEL_DIAMETER           = 66.5 
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi 
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi

    def __init__(self,controleur,fps=25):
        self.controleur=controleur
        self.fps=fps
        self.LED_LEFT_EYE = 15
        self.LED_RIGHT_EYE = 22
        self.LED_LEFT_BLINKER = 10
        self.LED_RIGHT_BLINKER = 10
        self.LED_WIFI = 0
        self.MOTOR_LEFT= 0
        self.MOTOR_RIGHT = 0

    
    def set_led(self, led, red = 0, green = 0, blue = 0):
        pass

    def get_voltage(self):
        pass

    def set_motor_dps(self, port, dps):
        pass



    def get_motor_position(self):
        return(73.4,46.8)
   
    def offset_motor_encoder(self, port, offset):
        pass

    def get_distance(self):
        return 30*4

    def servo_rotate(self,position):
        pass

    def stop(self):
        pass

    def get_image(self):
        return 500
    