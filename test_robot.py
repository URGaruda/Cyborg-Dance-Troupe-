import unittest 
from robot import Robot 
class TestRobot(unittest.TestCase):
    def setUp(self):
        self.r=Robot(2,3,4.2,1,6,8)
    def test_set_vitesse(self):
        self.r.set_vitesse(6,5)
    

        