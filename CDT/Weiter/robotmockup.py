import time
import math
import CDT.Weiter.constantes as constantes 
class Robotmockup:
    WHEEL_BASE_WIDTH         = 117  
    WHEEL_DIAMETER           = 66.5 
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi 
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi

    def __init__(self,fps=25):
        self.fps=fps
        self.LED_LEFT_EYE = 15
        self.LED_RIGHT_EYE = 22
        self.LED_LEFT_BLINKER = 10
        self.LED_RIGHT_BLINKER = 10
        self.LED_WIFI = 0
        self.MOTOR_LEFT= constantes.Vitesse_Gauche
        self.MOTOR_RIGHT = constantes.Vitesse_Droite
        self.rayon_robot=Robotmockup.WHEEL_BASE_WIDTH/10
        self.dt=0.0 
        self.tmp=0.0
    


    def stop(self):
        pass
    
    def set_led(self, led, red = 0, green = 0, blue = 0):
        pass

    def get_voltage(self):
        pass

    def set_motor_dps(self, port, dps):
        pass

    def read_encoders(self):
        return [1,2,3,4,5]

    def get_motor_position(self):
        tmp_act=time.time()
        delta_time=tmp_act-self.tmp
        self.dt=delta_time
        self.tmp=time.time()
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
    
    
