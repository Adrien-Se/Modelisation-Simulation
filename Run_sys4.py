from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

import pygame

def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(step=0.01, W=10000, H=700)

    Monde.addSource(Gravite(v3d(0,-9.81)))
    
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))

    barre = Particule(pos=v3d(0.5, 0.5),name='pivot',color='black',fix=True)
    
    masse1 = Particule(pos=v3d(0.6, 0.5),name='masse1',color='red',fix=False)
    masse2 = Particule(pos=v3d(0.7, 0.5),name='masse2',color='green',fix=False)
    masse3 = Particule(pos=v3d(0.8, 0.5),name='masse3',color='blue',fix=False)
    
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
                    Monde.addAgent(masse3)
                    
                    Monde.addSource(Ressort(barre, masse1, raideur=1000, amortissement=0.1, longueur=0.1))
                    Monde.addSource(Ressort(barre, masse2, raideur=1000, amortissement=0.1, longueur=0.2))
                    Monde.addSource(Ressort(barre, masse3, raideur=1000, amortissement=0.1, longueur=0.3))
                
                # On vérifie si l'utilisateur a cliqué sur la croix pour fermer la fenêtre:
                if event.key == pygame.K_ESCAPE:
                    Monde.run = False
        Monde.gameUpdate()
    