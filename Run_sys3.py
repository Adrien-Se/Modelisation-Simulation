from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

import pygame

def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(name= 'sys3',step=0.01)

    Monde.addSource(Gravite(v3d(0,-9.81)))
    
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))

    barre = Particule(pos=v3d(0.5, 0.5),name='pivot',color='black',fix=True, rayon = 0)
    
    masse1 = Particule(pos=v3d(0.5, 0.5),name='masse1',color='red',fix=False, rayon = 10)

    
    # Initialiser l'affichage & lancer
    Monde.gameInit(1000,700,scale=1000) # échelle 1000 -> 1 pixel = 1 mm
    while Monde.run:
        
        # On vérifie si l'utilisateur appuie sur la barre d'espace:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # On lance la simulation:
                    Monde.addAgent(barre, masse1)
                    
                    l0 = (barre.getPos()-masse1.getPos()).mod() +0.2
                    Monde.addSource(Ressort(barre, masse1, raideur=1000, amortissement=0.1, l0=l0))           
                # On vérifie si l'utilisateur a cliqué sur la croix pour fermer la fenêtre:
                if event.key == pygame.K_ESCAPE:
                    Monde.run = False
                    pygame.display.flip()
        Monde.gameUpdate(scale=1000)
        
if __name__ == '__main__':
    run()