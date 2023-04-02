import unittest
from Interfaces.affichage import Affichage
from Simulation.obstacle import Obstacle 
from Simulation.robot import Robot
class TestAffichage(unittest.TestCase):
    def test_updateaffichage(self):
        self.af.updateaffichage(Robot(),Obstacle(7,3,42))
        