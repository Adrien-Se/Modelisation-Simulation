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
    raideur = 1000
    amortissement = 0.8
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))
    
    mur1 = Particule(pos=v3d(0.3, 0.01),name='mur1',color='black',fix=True, rayon=0)
    mur2 = Particule(pos=v3d(0.6, 0.01),name='mur2',color='black',fix=True, rayon=0)
    # Particule(masse, pos, vit, name, color, fix)

    masse1 = Particule(pos=v3d(0.4, 0.01),name='masse1',color='red',fix=False, rayon=10)
    masse2 = Particule(pos=v3d(0.5, 0.01),name='masse2',color='red',fix=False, rayon=10)
    
    l0 = (masse1.getPos()-mur1.getPos()).mod()
    l0_1 = (masse2.getPos()-masse1.getPos()).mod()
    l0_2 = (mur2.getPos()-masse2.getPos()).mod()
    
    Monde.addSource(Ressort(mur1, masse1, raideur=raideur, amortissement=amortissement, l0=l0))
    Monde.addSource(Ressort(masse1, masse2, raideur=raideur, amortissement=amortissement, l0=l0_1)) 
    Monde.addSource(Ressort(mur2, masse2, raideur=raideur, amortissement=amortissement, l0=l0_2)) 
    
    
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
                    
                    # On va maintenant tracer la position de la masse en fonction du temps:
                    # On va donc créer un tableau de temps et un tableau de position:
                    t = []
                    x1 = []; x2 = []
                    Vx1 = []; Vx2 = []
                    for i in range(len(masse1.pos)):
                        t.append(Monde.temps[i])
                        x1.append(masse1.pos[i].x)
                        x2.append(masse2.pos[i].y)
                        Vx1.append(masse1.vit[i].y)
                        Vx2.append(masse2.vit[i].y)
                    # # On va calculer la solution analytique:
                    # omega_0 = (raideur/masse1.masse)**0.5
                    # zeta = amortissement/(2*(raideur*masse1.masse)**0.5)
                    # tau = 2*masse1.masse/amortissement
                    # omega = omega_0*(1 - zeta**2)**0.5
                    # for i in range(len(t)):
                        # x_analytique = 0.1 + 0.1*(1 - (zeta**2))**0.5*np.exp(-zeta*omega_0*t[i])*np.cos(omega*t[i])
                    pylab.figure()
                    pylab.plot(t, x1, label='x_masse1(t)')
                    pylab.plot(t, x2, label='x_masse2(t)')
                    pylab.plot(t, Vx1, label='Vx_masse1(t)')
                    pylab.plot(t, Vx2, label='Vx_masse2(t)')
                    # pylab.plot(t, x_analytique, label='x_analytique(t)', linestyle='--', color='red', linewidth=0.2)
                    pylab.title('Position de la masse en fonction du temps')
                    pylab.legend()
                    pylab.show()
        Monde.gameUpdate(scale=scale)
        
if __name__ == '__main__':
    run()
