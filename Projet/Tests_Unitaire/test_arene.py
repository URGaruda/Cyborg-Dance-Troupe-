import unittest 
from Robot_Arene_Obstacle.arene import Arene

class TestArene(unittest.TestCase):
    def test_check_collision(self):
        self.a.check_collision()
    def test_ajout_obstacle(self):
        self.a.ajout_obstacles(7)

    