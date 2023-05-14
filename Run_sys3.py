from Generateur import *
from Particule import *
from Univers import *

from random import random, randint

from math import cos, sin
import pygame
import pylab

def run():
    # Création du simulateur avec pas de temps de 10ms, une largeur de 10000 et une hauteur de 700
    Monde = Univers(name= 'sys3',step=0.01)
    W = 1000
    H = 700
    scale = 1000
    Monde.addSource(Gravite(v3d(0,-9.81)))
    
    # Ajout d'une force de viscosité:
    Monde.addSource(Viscosity(0.1))

    barre = Particule(pos=v3d(0.5, 0.5),name='pivot',color='black',fix=True, rayon = 0)
    
    masse1 = Particule(pos=v3d(0.5, 0.4),name='masse1',color='red',fix=False, rayon = 10)

    Fc = ForceConst(v3d(), masse1)
    
    # Initialiser l'affichage & lancer
    Monde.gameInit(W=W,H=H,scale=scale) # échelle 1000 -> 1 pixel = 1 mm
    while Monde.run:
        
        # On vérifie si l'utilisateur appuie sur la barre d'espace:
        for event in pygame.event.get():
            if Fc in Monde.sources: # Lorsqu'on ajoutera les forces on veut qu'elle soient temporaires et non actives constamment
                Monde.removeSource(Fc)
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    # On lance la simulation:
                    Monde.addAgent(barre, masse1)
                    
                    raideur = 100; amortissement = 0.1 
                    l0 = (barre.getPos()-masse1.getPos()).mod() + 0.2
                    Monde.addSource(Fc,Ressort(barre, masse1, raideur=raideur, amortissement=amortissement, l0=l0))        
                    
                # si l'utilisateur appuie sur les touvhes fléchées, on applique une force sur la masse:
                if event.key == pygame.K_UP:
                    Fc = ForceConst(v3d(0, 1), masse1)
                    Monde.addSource(Fc)

                if event.key == pygame.K_DOWN:
                    Fc = ForceConst(v3d(0, -1), masse1)
                    Monde.addSource(Fc)
                    
                if event.key == pygame.K_LEFT:
                    Fc = ForceConst(v3d(-1, 0), masse1)
                    Monde.addSource(Fc)
                    
                if event.key == pygame.K_RIGHT:
                    Fc = ForceConst(v3d(1, 0), masse1)
                    Monde.addSource(Fc)

                if event.key == pygame.K_ESCAPE:
                    Monde.run = False
                    pygame.display.flip()
                    
                    pylab.figure()
                    Monde.plot()
                    pylab.title(Monde.name)
                    pylab.legend()
                    pylab.show()

                    # On va maintenant tracer la position de la masse en fonction du temps:
                    # On va donc créer un tableau de temps et un tableau de position:
                    t = []
                    x = []
                    Vy = []
                    y_analytique = []
                    y = []
                    for i in range(len(masse1.pos)):
                        t.append(Monde.temps[i])
                        # print('t = ', t[i], 's')
                        # print()
                        x.append(masse1.pos[i].x)
                        y.append(masse1.pos[i].y)
                        Vy.append(masse1.vit[i].y)
                    # On va calculer la solution analytique:
                    omega_0 = (raideur/masse1.masse)**0.5
                    zeta = amortissement/(2*(raideur*masse1.masse)**0.5)
                    tau = 2*masse1.masse/amortissement
                    omega = omega_0*(1 - zeta**2)**0.5
                    for i in range(len(t)):
                        y_analytique.append(pylab.exp(-t[i]/tau) * ((y[i])*cos(omega*t[i]) + ((1/omega)*(Vy[i]+y[i]/tau))*sin(omega*t[i])) + 0.1)
                    pylab.figure()
                    pylab.plot(t, x, label='x(t)')
                    pylab.plot(t, y, label='y(t)')
                    pylab.plot(t, y_analytique, label='y_analytique(t)', linestyle='--', color='red', linewidth=0.2)
                    pylab.title('Position de la masse en fonction du temps')
                    pylab.legend()
                    pylab.show()
        
        Monde.gameUpdate(scale=scale)
    
if __name__ == '__main__':
    run()
  