import unittest
from Interfaces.affichage import Affichage
from Robot_Arene_Obstacle.obstacle import Obstacle 
from Robot_Arene_Obstacle.robot import Robot
class TestAffichage(unittest.TestCase):
    def test_updateaffichage(self):
        self.af.updateaffichage(Robot(),Obstacle(7,3,42))
        