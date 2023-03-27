import unittest 
from CDT.Simulation.robot import Robot
from CDT.Simulation.obstacle import Obstacle 
class TestRobot(unittest.TestCase):
    def test_set_vitesse(self):
        self.r.set_vitesse(6.4,5.6)
    def test_deplacement(self):
        self.r.deplacement(0.3)






    

        