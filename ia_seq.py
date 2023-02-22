import ia
import ia_tourner 
from intermediaire import Intermediaire 
class IA_Seq:
    def __init__(self,liste_ia):
        self.liste=liste_ia
    def start(self):
        self.cur=0

    def step(self):
        if self.liste[self.cur].stop() :
            self.cur+=1
            self.liste[self.cur].start()
        
        self.liste[self.cur].step()

    def stop(self):
        return self.cur>=len(self.liste)
    
    
        