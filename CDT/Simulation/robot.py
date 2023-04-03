import math
import CDT.Weiter.constantes as constantes 
import time 
class Robot:
    """
    Classe pour représenter un robot.
    Attributs:
        x (float): la position x du robot.
        y (float): la position y du robot.
        orientation (float): orientation du robot en radians.
        rayon_robot(float): le rayon du robot.
        rayon_roue (float): le rayon des deux roues.
        distance_roues (float): la distance entre les deux roues du robot.
        vitesse_roue_gauche (float): vitesse angulaire de la roue gauche du robot en radians par seconde.
        vitesse_roue_droite (float): vitesse angulaire de la roue droite du robot en radians par seconde.
        historique (list): une liste de tuples de la position x, y du robot à chaque instant.
    """
    def __init__(self):
        """
        Initialise un objet de la classe Robot avec les paramètres donnés.
        """
        self.x=constantes.x
        self.y=constantes.y
        self.distanceP=0.0
        self.angleP=0.0
        self.tmp=0.0
        self.orientation = constantes.Orientation
        self.rayon_robot=constantes.Rayon_Robot
        self.rayon_roue = constantes.Rayon_Roue
        self.distance_roues = constantes.Distance_Roues
        self.vitesse_roue_gauche = 0.0
        self.vitesse_roue_droite = 0.0
        self.distance_sens=constantes.Distance_Max
        self.b=False
        
    
    def start_time(self):
        self.tmp=time.time()

    def set_vitesse(self, vitesse_roue_gauche, vitesse_roue_droite):
        """
        Définit les vitesses de la roue gauche et droite du robot.
        """
        self.vitesse_roue_gauche = vitesse_roue_gauche
        self.vitesse_roue_droite = vitesse_roue_droite

    #question 1.3 
    def dessine(self,b):
        self.b=b
        

    def deplacement(self, dt):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        #print(self.x," ",self.y)
        tmp_act=time.time()
        delta_time=tmp_act-self.tmp
        #print("dt =",delta_time)
        vitesse_moyenne = (self.vitesse_roue_gauche + self.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.rayon_roue) #vitesse lineaire moyenne
        self.distanceP=vitesse_moyenne*delta_time
        delta_x = vitesse_moyenne * math.cos(self.orientation) * delta_time 
        delta_y = vitesse_moyenne * math.sin(self.orientation) * delta_time 
        self.x += delta_x
        self.y += delta_y
        
        
        vitesse_angulaire = (self.vitesse_roue_droite - self.vitesse_roue_gauche) / (2 * math.pi * self.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * delta_time #calcule le changement d'orientation
        self.angleP=delta_orientation
        self.orientation += delta_orientation #calcule la nouvelle orientation 
        self.tmp=time.time()
   
    def senseur_distance(self, obstacles):
        angle = self.orientation
        inter = []
        m = math.tan(angle)  # calcul de la pente du capteur
        A = m
        B = -1
        C = -A * self.x + B * self.y

        for obs in obstacles:
            xc = obs.x
            yc = obs.y
            r = obs.rayon
            a = 1 + (A / B) ** 2
            b = 2 * ((A / B) * (C / B) - xc)
            c = xc ** 2 + (C / B - yc) ** 2 - r ** 2

            delta = b ** 2 - 4 * a * c

            if delta == 0:
                x = -b / (2 * a)
                y = (-A / B) * x - (C / B)
                inter.append((x, y))
            elif delta > 0:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                y1 = (-A / B) * x1 - (C / B)
                y2 = (-A / B) * x2 - (C / B)
                inter.append((x1, y1))
                inter.append((x2, y2))

        if len(inter) == 0:
            return -1
        else:
            premier_point = inter[0]
            px = premier_point[0]
            py = premier_point[1]
            res = math.sqrt((self.x - px)**2 + (self.y - py)**2)

            for (a, b) in inter[1:]:
                res_int = math.sqrt((self.x - a)**2 + (self.y - b)**2)
                if res_int < res:
                    res = res_int

            if res <= self.distance_sens :
                return res 
            else :
                return -1
