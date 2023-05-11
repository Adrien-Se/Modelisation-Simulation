
from vector3D import Vecteur3D as v3d
import pygame
from pylab import plot, show, legend


# from Generateur import ForceConst, Gravite, Viscosite, Ressort
import sys


class Particule(object):
    def __init__(self, masse=1., pos=v3d(), vit=v3d(), name='test', color='red', fix=False):
        self.masse = masse
        self.pos = [pos]
        self.vit = [vit] # Liste des vitesses de la particule
        self.accel = [v3d()] # Liste des accélérations de la particule
        self.name = name
        self.color = color
        self.fix = fix
        
        self.forces = [v3d()] # Liste des forces appliquées à la particule
        
    def __str__(self):
        return "Particule ("+str(self.masse)+', '+str(self.pos)+', '+str(self.vit)+', "'+self.name+'", "'+self.color+'")'
    
    # def __repr__(self):
    #     return str(self) # 
    
    def setForces(self, force=v3d()):
        self.forces.append(force) # Ajoute une force à la liste des forces appliquées à la particule
    
    def getForces(self):
        return self.forces[-1]
    
    def getPos(self):
        return self.pos[-1]
    
    def getVit(self):
        return self.vit[-1]
    
    def getAccel(self):
        return self.accel[-1]
    
    # def simule(self,step):
    #     self.pos.append(self.pos[-1]+self.vit[-1]*step)
    #     ### A COMPLETER
    #     #Comment utiliser getPostion() et getVit() ?
    # Il est à noter que dans le sujet on nous demande de mettre une fonction simule dans la classe Particule, 
    # mais dans le code fourni, il y a une fonction simule dans la classe Univers. Je ne sais pas si c'est une erreur ou si c'est voulu.
    # Je vais donc mettre la fonction simule dans la classe Univers.
    
    
    def PFD(self):
        """Applique le Principe Fondamental de la Dynamique"""
        a = v3d()
        if not self.fix:
            a = self.getForces()*(1/self.masse) # a = F/m
        self.accel.append(a)
        
    # def simulation(self,step):
        
    
            
    def move(self,step):
        self.vit.append(self.getVit() + self.getAccel()*step ) # v = v0 + a*t
        self.pos.append(self.getPos() + self.getVit()*step + 0.5*(self.getAccel()*step**2)) # x = x0 + v*t + 1/2*a*t**2


    def gameInit(self, W, H, fps=60, background=(0,0,0), scale=1):
        pygame.init()
        self.time = pygame.time.clock()
        self.screen = pygame.display.set_mode((W,H))
        self.fps = fps
        self.background = background
        self.scale = scale


    def plot2D(self,screen,scale=1):
        X = int(scale*self.getPos().x)
        Y = int(scale*self.getPos().y)
        VX = int(scale*self.getVit().x) + X
        VY = int(scale*self.getVit().y) + Y
        size=2
        
        pygame.draw.circle(screen,self.color,(X,Y),size*2,size)
        pygame.draw.line(screen,self.color,(X,Y),(VX,VY))
        
        
    def plot3D(self,screen,scale=1):
        X = int(scale*self.getPos().x)
        Y = int(scale*self.getPos().y)
        Z = int(scale*self.getPos().z)
        VX = int(scale*self.getVit().x) + X
        VY = int(scale*self.getVit().y) + Y
        VZ = int(scale*self.getVit().z) + Z
        size=2
        
        pygame.draw.circle(screen,self.color,(X,Y),size*2,size)
        pygame.draw.line(screen,self.color,(X,Y),(VX,VY))
        pygame.draw.line(screen,self.color,(X,Y),(VX,VZ))
        pygame.draw.line(screen,self.color,(X,Y),(VY,VZ))
        
    def gameDraw(self,screen,scale=1):
        H = screen.get_height()
        X = int(scale*self.getPos().x)
        Y = H - int(scale*self.getPos().y)
        VX = int(scale*self.getVit().x) + X
        VY = - int(scale*self.getVit().y) + Y
        size=2
        
        pygame.draw.circle(screen,self.color,(X,Y),size*2,size)
        pygame.draw.line(screen,self.color,(X,Y),(VX,VY))
        # if self.getPos().z == 0:
        #     self.plot2D(screen,scale)
        # else:
        #     self.plot3D(screen,scale)
            
        
        
        
                      
if __name__ == "__main__":
    
    boule1 = Particule(1, pos=v3d(0.5,0.5,0), vit=v3d(0,0,0), name='boule1', color='red', fix=True)
    boule2 = Particule(1, v3d(0.1,0.1,0), v3d(0,0,0), 'boule2', 'blue', False)
    
    #Affichage des particules:
    print(boule1)
    
    #Test de la fonction setForces:
    boule1.setForces(v3d(0,0,0))
    print(boule1.getForces())
    
    #Test de la fonction getPos:
    print(boule1.getPos())
    
    #Test de la fonction getVit:
    print(boule1.getVit())
    
    #Test de la fonction getAccel:
    print(boule1.getAccel())
    
    #Test de la fonction PFD:
    boule1.PFD()
    
    #Test de la fonction move:
    boule1.move(1)
    print(boule1.getPos())
    print(boule1.getVit())
    print(boule1.getAccel())
    
    # #Test de la fonction plot2D:
    # boule1.plot2D(screen,scale=1)
    
    # #Test de la fonction plot3D:
    # boule1.plot3D(screen,scale=1)
    
    # #Test de la fonction gameDraw:
    # boule1.gameDraw(screen,scale=1)

    
