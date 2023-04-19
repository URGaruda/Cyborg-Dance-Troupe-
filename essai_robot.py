from CDT.IAs.inter_robot import Inter_Robot
import CDT.IAs.ia as ia 
import CDT.IAs.ia_tourner as ia_tourner
import CDT.IAs.ia_seq as ia_seq 
import CDT.Weiter.constantes as constantes 
import robot2IN013 as Robot

dexter=None
inter=None
ruby=None
l_ia=[]
main_ia=None
def initiate(nb_obstacle):
    global dexter
    dexter=Robot.Robot2IN013()
    global inter
    inter=Inter_Robot(dexter)

def create_line(distance):
    global ruby
    ruby=ia.IA(inter,distance,constantes.Vitesse)
    global main_ia
    main_ia=ruby


def create_carre(distance):
    global l_ia
    for i in range(7):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ))
    ia_carre=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_carre

def create_rectangle(longueur,largeur):
    global l_ia
    b=True
    for i in range(7):
        if(i%2==0):
            if(b):
                l_ia.append(ia.IA(inter,longueur,constantes.Vitesse) )
                b=False
            else:
                l_ia.append(ia.IA(inter,largeur,constantes.Vitesse) )
                b=True

        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,90,constantes.Vitesse ))
    ia_rect=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_rect

def create_triangle_equilateral(distance):
    global l_ia
    l_ia.append(ia_tourner.Ia_Tourner(inter,60,constantes.Vitesse ))
    for i in range(5):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse) )
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,120,constantes.Vitesse ))
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi
def create_hexagone(distance):
    global l_ia
    l_ia.append(ia_tourner.Ia_Tourner(inter,60,constantes.Vitesse ))
    for i in range(11):
        if(i%2==0):
            l_ia.append(ia.IA(inter,distance,constantes.Vitesse) )
            
        else:
            l_ia.append( ia_tourner.Ia_Tourner(inter,60,constantes.Vitesse ))
            
    ia_equi=ia_seq.IA_Seq(l_ia)
    global main_ia
    main_ia=ia_equi

initiate(0)
create_carre(100)
main_ia.start()
inter.start_time_dist()
inter.start_time_angle()

while not main_ia.stop():
    main_ia.step()


dexter.stop()
print("fin")