import IAs.ia as ia
import IAs.ia_tourner as ia_tourner 
from Robot_Arene_Obstacle.intermediaire import Intermediaire 
class IA_Seq:
    def __init__(self,liste_ia):
        self.liste=liste_ia
    def start(self):
        self.cur=0
        self.liste[self.cur].start()
    def step(self):
        if self.liste[self.cur].stop() :
            self.cur+=1
            if self.cur>=len(self.liste):
                return 
            print("switch")
            self.liste[self.cur].start()
        
        self.liste[self.cur].step()

    def stop(self):
        return self.cur>=len(self.liste)
    
    
        