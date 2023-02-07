import math

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
    def __init__(self, x, y, orientation, rayon_robot, rayon_roue, distance_roues):
        """
        Initialise un objet de la classe Robot avec les paramètres donnés.
        """
       
        self.x = x
        self.y = y
        self.orientation = orientation
        self.rayon_robot=rayon_robot
        self.rayon_roue = rayon_roue
        self.distance_roues = distance_roues
        self.vitesse_roue_gauche = 0
        self.vitesse_roue_droite = 0
        self.historique = []
    
    def set_vitesse(self, vitesse_roue_gauche, vitesse_roue_droite):
        """
        Définit les vitesses de la roue gauche et droite du robot.
        """
        self.vitesse_roue_gauche = vitesse_roue_gauche
        self.vitesse_roue_droite = vitesse_roue_droite

    def deplacement(self, delta_time):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses de ses roues.
        """
        vitesse_moyenne = (self.vitesse_roue_gauche + self.vitesse_roue_droite) / 2 
        vitesse_moyenne = vitesse_moyenne / (2 * math.pi * self.rayon_roue) #vitesse lineaire moyenne
        delta_x = vitesse_moyenne * math.cos(self.orientation) * delta_time #trignometry
        delta_y = vitesse_moyenne * math.sin(self.orientation) * delta_time #trigonometry
        self.x += delta_x
        self.y += delta_y
        
        
        vitesse_angulaire = (self.vitesse_roue_droite - self.vitesse_roue_gauche) / (2 * math.pi * self.distance_roues) #la vitesse de rotation du robot autour de son axe central
        delta_orientation = vitesse_angulaire * delta_time #calcule le changement d'orientation
        self.orientation += delta_orientation #calcule la nouvelle orientation
        
        self.historique.append((self.x, self.y))
    
    def check_collision(self, arene_xmax, arene_ymax, obstacles):
        """
        Vérifie s'il y a une collision entre le robot et les bords de l'arène/ obstacle
        """
        # Vérifie une collision avec les bords de l'arène
        if self.x - self.rayon_robot < 0 or self.x + self.rayon_robot > arene_xmax:
            return True
        if self.y - self.rayon_robot < 0 or self.y + self.rayon_robot > arene_ymax:
            return True
        
        # Vérifie une collision avec les obstacles
        for obstacle in obstacles:
            distance = math.sqrt((self.x - obstacle.x)**2 + (self.y - obstacle.y)**2)
            if distance < self.rayon_robot + obstacle.rayon:
                return True
        
        return False

    
    '''def senseur(self):
        """ Determine s'il y a un obstacle sur la direction du robot et renvoie le nombre de pas s'il l'a trouvé un
        obstacle ou sinon -1 s'il l'a rien trouvé """
        robot=self.dexter.copie() # crée une copie qui va faire des 
        pas=0
        while not(self.hors_terrain(robot)) :
            vect_v=self.dexter.dir.mult_par_un_scalaire((self.dexter.v*self.pas_temps))
            robot.x=vect_v.x
            robot.y=vect_v.y
            pas+=1
            if(self.collision(robot)):
                return pas 
        return -1 '''
    
    
    




