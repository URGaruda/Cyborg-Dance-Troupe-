class IA_Cond:
    def __init__(self,ia_base,ia_alt,condition):
        self.ia_base=ia_base
        self.ia_alt=ia_alt
        self.condition=condition

    def start(self):
        self.ia_alt.stat()
        self.ia_base()

    def step(self):
        if self.condition :
            self.ia_base.step()
        else :
            self.ia_alt.step()


    def stop(self):
        return self.ia_base.stop() or self.ia_alt.stop() 
