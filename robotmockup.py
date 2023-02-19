import time
import math
class robotmockup:
    WHEEL_BASE_WIDTH         = 117  
    WHEEL_DIAMETER           = 66.5 
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi 
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi

    def __init__(self,controleur,fps=25,resolution=None,servoPort ="SERVO1",motionPort="AD1"):
        self._gpg= EasyGoPiGo3()
        self.controleur=controleur
        self.fps=fps
        self.LED_LEFT_EYE = self._gpg.LED_LEFT_EYE
        self.LED_RIGHT_EYE = self._gpg.LED_RIGHT_EYE
        self.LED_LEFT_BLINKER = self._gpg.LED_LEFT_BLINKER
        self.LED_RIGHT_BLINKER = self._gpg.LED_RIGHT_BLINKER
        self.LED_WIFI = self._gpg.LED_WIFI
        self.MOTOR_LEFT= self._gpg.MOTOR_LEFT
        self.MOTOR_RIGHT = self._gpg.MOTOR_RIGHT

        try:
            self.camera=picamera.PICamera()
            if resolution:
                self.camera.resolution =resolution
        except Exception as e:
            print("Camera not found", e)
        try:
            self.servo =Servo(servoPort,self._gpg)
        except Exception as e:
            print("servo not found",e)
        try:
            self.distanceSensor = ds_sensor.DistanceSensor()
        except Exception as e:
            print("Distance Sensor not found",e)
        try:
            self.imu = imu.inertial_measurement_unit()
        except Exception as e:
            print("IMU sensor not found",e)
        self._gpg.set_motor_limits(self._gpg.MOTOR_LEFT+self._gpg.MOTOR_RIGHT,0)
    
    def set_led(self, led, red = 0, green = 0, blue = 0):
        pass

    def get_voltage(self):
        pass

    def set_motor_dps(self, port, dps):
        pass


    def get_motor_position(self):
        pass
   
    def offset_motor_encoder(self, port, offset):
        pass

    def get_distance(self):
        pass

    def servo_rotate(self,position):
        pass

    def stop(self):
        pass

    def get_image(self):
        pass
    