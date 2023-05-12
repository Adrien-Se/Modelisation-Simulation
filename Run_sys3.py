from Generateur import *
from Particule import *
from Univers import *

from random import random, randint
import pygame

'''Dans ce fichier nous allons créer un système masse+ressort+amortisseur, avec une application au clavier
d'une force constante ou d'une force harmonique'''

def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(step=0.01, W=10000, H=700)

    Monde.addSource(Gravite(v3d(0,-9.81)))
    
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))

    FONT = pygame.font.SysFont('arial', 300) # Police de caractères
    BLACK = (0, 0, 0)
        
    # Initialiser l'affichage & lancer
    Monde.gameInit(1000,700,background='white',scale=1000) # échelle 1000 -> 1 pixel = 1 mm
    while Monde.run:
        # On demande d'appuyer sur la barre d'espace pour déclencher l'ajout d'une particule
        # et on ajoute un texte pour indiquer à l'utilisateur qu'il faut appuyer sur la barre d'espace:
        
        text_surface = FONT.render("Appuyez sur la barre d'espace pour ajouter une particule", True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (50, 50)
        text_surface.blit(text_surface, text_rect)
        
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
    