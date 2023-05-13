from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

import pygame

        
        
def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(step=0.001, W=10000, H=700)

    Monde.addSource(Gravite(v3d(0,-9.81)))
    
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))

    barre = Particule(pos=v3d(0.5, 0.5),name='pivot',color='black',fix=True)
    masse1 = Particule(pos=v3d(0.6, 0.5),name='masse1',color='red',fix=False)
    masse2 = Particule(pos=v3d(0.7, 0.5),name='masse2',color='green',fix=False)
    
    # Une barre se comporte comme un ressort avec une très grande raideur et un gros amortissement
    Monde.addSource(Ressort(barre, masse1, raideur=1000, amortissement=1000, l0=0.15))
    Monde.addSource(Ressort(masse1, masse2, raideur=1000, amortissement=1000., l0=0.1))

    
    # On ajoute un trait entre les masses et le pivot:

    
    # Initialiser l'affichage & lancer
    Monde.gameInit(1000,700,background='white',scale=1000) # échelle 1000 -> 1 pixel = 1 mm
    while Monde.run:
        
        # On vérifie si l'utilisateur appuie sur la barre d'espace:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # On lance la simulation:
                    Monde.addAgent(barre)
                    Monde.addAgent(masse1)
                    Monde.addAgent(masse2)
                
                # On vérifie si l'utilisateur a cliqué sur la croix pour fermer la fenêtre:
                if event.key == pygame.K_ESCAPE:
                    Monde.run = False
        Monde.gameUpdate()
    
if __name__ == '__main__':
    run()
