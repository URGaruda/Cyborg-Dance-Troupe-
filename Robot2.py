VMAX= 50
class Robot :
    def  __init__(self , x , y, v ,  R , theta):
        if v<0 or v>VMAX:
            raise ValueError("La vitesse doit etre entre 0 et {} ".format(VMAX))
        if theta < 0 or theta > 360:
            raise ValueError("L'angle doit être entre 0 et 360 degrés")
        self.x = x
        self.y = y
        self.v = v
        self.R = R
        self.theta = theta
        
        
        
        
try:
    robot=Robot(1,1,20,10,50)   
except valueError as erreur :
    print(erreur)