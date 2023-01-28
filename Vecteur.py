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
    
    def soustraction(self, x=None, y=None, vecteur=None):
    if vecteur:
        self.x -= vecteur.x
        self.y -= vecteur.y
    else:
        self.x -= x
        self.y -= y
    return self

v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)
v1.addition(x=1, y=1) 
v1.addition(vecteur=v2)
v1.soustraction(x=1,y=1)
v1.soustraction(vecteur=v2)
    
