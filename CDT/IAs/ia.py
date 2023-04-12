from .intermediaire import Intermediaire
import math

class IA:
    def __init__(self,dexter,distance,vitesse):
        self.distance=distance
        self.parcouru=0.0
        self.inter=dexter
        self.vitesse=vitesse
        self.limite=False
    def start(self):
        self.inter.distanceP=0.0
        self.inter.start_time_dist()
        self.inter.avancer(self.vitesse,self.vitesse)
    def step(self):
        #print("parcouru : ",self.parcouru)
        self.parcouru=self.inter.get_distance()
        if((self.parcouru/self.distance)*100>=85.0) and self.limite==False :
            self.inter.avancer(self.vitesse/1.3,self.vitesse/1.3)
            self.limite=True
        
    def stop(self):
        return self.parcouru>=self.distance 
