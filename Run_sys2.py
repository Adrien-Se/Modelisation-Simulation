from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

import pygame
import pylab

   
    
def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(name= 'sys2',step=0.01)
    W = 1000
    H = 700
    scale = 10
    
    Monde.addSource(Gravite(v3d(0,-9.81)),Viscosity(0.1))

    # Initialiser l'affichage & lancer
    Monde.gameInit(W=W, H=H, scale=scale) # échelle 1000 pixels = 100 mètres -> 1 pixel = 10 cm
    
    while Monde.run:
        # On demande d'appuyer sur la barre d'espace pour déclencher l'ajout d'une particule
        # On vérifie si l'utilisateur appuie sur la barre d'espace ou escape:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # On crée une particule aléatoire:
                    name = 'Particule' + str(randint(0, 1000))
                    position = v3d(random()*int(W/scale) , random()*int(H/scale), 0)
                    couleur = (random(), random(), random(), 1)
                    particule = Particule(masse=2,pos=position, name=name, color=couleur, fix=False, rayon=10)
                    Monde.addAgent(particule)
                # On vérifie si l'utilisateur a cliqué sur la croix pour fermer la fenêtre:
                if event.key == pygame.K_ESCAPE:
                    Monde.run = False
                    pygame.display.flip()
                    
                    Monde.plot()
                    pylab.title(Monde.name)
                    pylab.legend()
                    pylab.show()
        Monde.gameUpdate(scale=scale)
    
if __name__ == '__main__':
    run()
