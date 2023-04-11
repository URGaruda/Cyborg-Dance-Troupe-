import unittest 
from Simulation.arene import Arene

class TestArene(unittest.TestCase):
    def setUp(self):
        self.a=Arene()
    def test_check_collision(self):
        self.a.check_collision()
    def test_ajout_obstacle(self):
        self.a.ajout_obstacles(7)
    def test_arene_update(self):
        self.a.arene_update
if __name__ == '__main__':
    unittest.main()       


    