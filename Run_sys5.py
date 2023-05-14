from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

import pygame
import pylab
        
        
def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(name= 'sys5',step=0.001)
    W = 1000
    H = 700
    scale = 1000
    Monde.addSource(Gravite(v3d(0,-9.81)))
    
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.5))

    barre = Particule(pos=v3d(0.5, 0.5),name='pivot',color='black',fix=True, rayon=0)
    masse1 = Particule(masse = 5, pos=v3d(0.6, 0.5),name='masse1',color='red',fix=False, rayon=10)
    masse2 = Particule(masse = 5,pos=v3d(0.7, 0.5),name='masse2',color='green',fix=False, rayon=10)
    
    # Une barre se comporte comme un ressort avec une très grande raideur et un gros amortissement
    Monde.addSource(Ressort(barre, masse1, raideur=10000, amortissement=3000, l0=0.15))
    Monde.addSource(Ressort(masse1, masse2, raideur=10000, amortissement=3000, l0=0.1))

    
    # On ajoute un trait entre les masses et le pivot:

    
    # Initialiser l'affichage & lancer
    Monde.gameInit(W=W,H=H,scale=scale) # échelle 1000 -> 1 pixel = 1 mm
    while Monde.run:
        
        # On vérifie si l'utilisateur appuie sur la barre d'espace:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # On lance la simulation:
                    Monde.addAgent(barre, masse1, masse2)
                
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

