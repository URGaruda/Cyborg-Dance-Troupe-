import unittest 
from CDT.Simulation.robot import Robot
from CDT.Simulation.obstacle import Obstacle 
class TestRobot(unittest.TestCase):
    def setUp(self):
        self.r=Robot()
    def test_start_time(self):
        self.r.start_time()
    def test_set_vitesse(self):
        self.r.set_vitesse(6.4,5)
    def test_deplacement(self):
        self.r.deplacement(0.3)
    def test_senseur_distance(self):
        self.r.senseur_distance([Obstacle(4.0,4.0,5.0),Obstacle(8.0,6.0,2.0)])

if __name__ == '__main__':
    unittest.main()       