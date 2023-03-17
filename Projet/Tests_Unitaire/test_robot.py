import unittest 
from Robot_Arene_Obstacle.robot import Robot
from Robot_Arene_Obstacle.obstacle import Obstacle 
class TestRobot(unittest.TestCase):
    def test_set_vitesse(self):
        self.r.set_vitesse(6.4,5.6)
    def test_deplacement(self):
        self.r.deplacement(0.3)
    def test_senseur_distance(self):
        self.r.senseur_distance([Obstacle(4.0,4.0,5.0),Obstacle(8.0,6.0,2.0)])






    

        