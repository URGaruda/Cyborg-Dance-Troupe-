

class IA_Loop:
    def __init__(self,ia,condition):
        self.ia=ia
        self.condition=condition
    
    def start(self):
        self.ia.start()

    def step(self):
        if self.ia.stop():
            self.ia.start()
            
        self.ia.step()

    def stop(self):
        return self.condition