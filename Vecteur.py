class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
     def addition(self, x=None, y=None, vecteur=None):
        if vecteur:
            self.x += vecteur.x
            self.y += vecteur.y
        else:
            self.x += x
            self.y += y
        return self 