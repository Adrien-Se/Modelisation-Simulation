from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 1000 et une hauteur de 700
    Monde = Univers(name= 'sys1',step=0.01)
    W = 1000
    H = 700
    scale = 100
    
    Monde.addSource(Gravite(v3d(0,-9.81)))
    # Une particule pivot fixe au centre de l'écran:
    center = Particule(pos=v3d(0.5*int(W/scale), 0.5*int(H/scale), -5.),name='center',color='red',fix=True, rayon=10)
    Monde.addAgent(center)
    

    for i in range(10):
        name = 'Particule' + str(i)
        position = v3d(random()*int(W/scale) , random()*int(H/scale), 0)
        couleur = (random(), random(), random(), 1)
        particule = Particule(pos=position, name=name, color=couleur, fix=False, rayon=10)
        Monde.addAgent(particule)

    # On va ajouter une force de d'attraction entre center et les autres particules:
    for particule in Monde.population:
        if particule != center: Monde.addSource(ForceField(2.,center,particule))
        
    # Initialiser l'affichage & lancer
    Monde.gameInit(W=W,H=H,scale=scale) # échelle 1000 -> 1 pixel = 1 mm
    while Monde.run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Monde.run = False
                    pygame.display.flip()
        Monde.gameUpdate(scale=scale)
    
if __name__ == '__main__':
    run()