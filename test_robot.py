import unittest 
from robot import Robot
from obstacle import Obstacle 
class TestRobot(unittest.TestCase):
    def setUp(self):
        self.r=Robot(2,3,4.2,1,6,8)
    def test_set_vitesse(self):
        self.r.set_vitesse(6,5)
    def test_check_collision(self):
        self.r.check_collision(50,50,[Obstacle(4,4,5),Obstacle(8,6,2)])
    def test_deplacement(self):
        self.r.deplacement(1.3)


    
    
    

        