from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

import pygame
import pylab


def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(name = 'sys6',step=0.001)

    Monde.addSource(Gravite(v3d(0,-9.81)))
    W = 1000
    H = 700
    scale = 1000
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))
    
    mur1 = Particule(pos=v3d(0.1, 0.),name='mur1',color='black',fix=True, rayon=0)
    mur2 = Particule(pos=v3d(0.9, 0.),name='mur2',color='black',fix=True, rayon=0)
    # Particule(masse, pos, vit, name, color, fix)

    masse1 = Particule(pos=v3d(0.3, 0.01),name='masse1',color='red',fix=False, rayon=10)
    masse2 = Particule(pos=v3d(0.4, 0.01),name='masse2',color='red',fix=False, rayon=10)
    
    l0 = (masse1.getPos()-mur1.getPos()).mod()
    l0_1 = (masse2.getPos()-masse1.getPos()).mod()
    l0_2 = (mur2.getPos()-mur2.getPos()).mod()
    
    Monde.addSource(Ressort(mur1, masse1, raideur=1000, amortissement=1, l0=l0))
    Monde.addSource(Ressort(masse1, masse2, raideur=1000, amortissement=1, l0=l0_1)) 
    Monde.addSource(Ressort(mur2, masse2, raideur=1000, amortissement=1, l0=l0_2)) 
    
    
    # Initialiser l'affichage & lancer
    Monde.gameInit(W=W,H=H,scale=scale) # échelle 1000 -> 1 pixel = 1 mm
    while Monde.run:
        
        # On vérifie si l'utilisateur appuie sur la barre d'espace:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    Monde.addAgent(masse1, masse2, mur1, mur2) # On lance la simulation:
                    
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
