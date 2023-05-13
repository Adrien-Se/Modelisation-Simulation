from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

import pygame
  
    
def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(name= 'sys2',step=0.01, W=10000, H=700)

    Monde.addSource(Gravite(v3d(0,-9.81)))
    
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))

    # Initialiser l'affichage & lancer
    Monde.gameInit(1000,700,background='white',scale=1000) # échelle 1000 -> 1 pixel = 1 mm
    
    
    while Monde.run:
        # On demande d'appuyer sur la barre d'espace pour déclencher l'ajout d'une particule
        # On vérifie si l'utilisateur appuie sur la barre d'espace:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # On crée une particule aléatoire:
                    name = 'Particule' + str(randint(0, 1000))
                    position = v3d(random(), random(), 0)
                    couleur = (random(), random(), random(), 1)
                    particule = Particule(pos=position, name=name, color=couleur, fix=False)
                    Monde.addAgent(particule)
                # On vérifie si l'utilisateur a cliqué sur la croix pour fermer la fenêtre:
                if event.key == pygame.K_ESCAPE:
                    Monde.run = False
        Monde.gameUpdate()
    
if __name__ == '__main__':
    run()