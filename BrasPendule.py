# Tout comme pour la particule nous allons créer une classe BrasPendule qui permettra de contrôler le bras du pendule.
# Cette classe va modéliser une barre rigide de masse m et de longueur l, avec son inertie etc...
# Dans cette classe nous allons créer une méthode qui permettra de calculer la position du bras en fonction de l'angle.
# Il y aura la possibilité de coontrôler la masse, la longueur, l'angle, la position et la vitesse du bras.

from vector3D import Vecteur3D as v3d
import pygame
from pylab import plot

from math import sin, cos

class BrasPendule(object):
    """Classe BrasPendule
    Attributs:
    - masse: masse du bras
    - longueur: longueur du bras
    - angle: angle du bras
    - pos: position du bras
    - vit: vitesse du bras
    - name: nom du bras
    - color: couleur du bras
    - fix: booléen qui indique si le bras est fixe ou non
    - width: largeur du bras
    
    Méthodes:
    - setForces: ajoute une force à la liste des forces appliquées au bras
    - getForces: retourne la dernière force appliquée au bras
    

    """
    
    def __init__(self, masse=1., length=1., width=1., angle=0., pos=v3d(), vit=v3d(), ang_speed = v3d(), name='test', color='red', fix=False, k=12):
        self.masse = masse
        self.length = length # Longueur du bras
        self.width = width # Largeur du bras
        self.angle = angle
        self.pos = [pos]
        self.vit = [vit] # Liste des vitesses du bras
        self.ang_speed = [ang_speed] # Liste des vitesses angulaires du bras
        self.accel = [v3d()] # Liste des accélérations du bras
        self.name = name
        self.color = color
        self.fix = fix
        
        self.forces = [v3d()] # Liste des forces appliquées au bras

        
        # le moment d'inertie du bras est I = m*l**2
        self.k = k # coefficient inertiel du bras
        self.moment = (1/self.k)*self.masse*self.longueur**2

    def __str__(self):
        return "BrasPendule ("+str(self.masse)+', '+str(self.longueur)+', '+str(self.angle)+', '+str(self.pos)+', '+str(self.vit)+', "'+self.name+'", "'+self.color+'")'
    
    def setForces(self, force=v3d()):
        self.forces.append(force) # Ajoute une force à la liste des forces appliquées au bras
    
    def getForces(self):
        return self.forces[-1]
    
    def getPos(self):
        return self.pos[-1]
    
    def getVit(self):
        return self.vit[-1]
    
    def getAccel(self):
        return self.accel[-1]
    
    def PFD(self):
        """Applique le Principe Fondamental de la Dynamique"""
        a = v3d()
        if not self.fix:
            a = self.getForces()*(1/self.masse) # a = F/m
        self.accel.append(a)
  
            
    def move(self,step):
        self.vit.append(self.getVit() + self.getAccel()*step ) # v = v0 + a*t
        self.pos.append(self.getPos() + self.getVit()*step ) # x = x0 + v*t
        
    def calculePos(self):
        """Calcule la position du bras en fonction de l'angle"""
        self.pos.append(v3d(self.longueur*sin(self.angle), -self.longueur*cos(self.angle), 0))
        return self.pos[-1]
    