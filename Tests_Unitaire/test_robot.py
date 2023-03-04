import unittest 
from robot import Robot
from obstacle import Obstacle 
class TestRobot(unittest.TestCase):
    def setUp(self):
        self.r=Robot(2,3,4.2,1,6,8)
    def test_set_vitesse(self):
        self.r.set_vitesse(6.4,5.6)
    def test_check_collision(self):
        self.r.check_collision(50.0,50.0,[Obstacle(4.0,4.0,5.0),Obstacle(8.0,6.0,2.0)])
    def test_deplacement(self):
        self.r.deplacement(0.3)






    

        