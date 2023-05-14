
from vector3D import Vecteur3D as v3d
import pygame
from pylab import plot



class Particule(object):
    def __init__(self, masse=1., pos=v3d(), vit=v3d(), name='test', color='red', fix=False, rayon=1):
        self.masse = masse
        self.pos = [pos]
        self.vit = [vit] # Liste des vitesses de la particule
        self.accel = [v3d()] # Liste des accélérations de la particule
        self.name = name
        self.color = color
        self.fix = fix
        
        self.forces = [v3d()] # Liste des forces appliquées à la particule
        
        self. rayon = rayon # Rayon de la particule

    # def collision(self, other):
    #     """Détermine si cette particule entre en collision avec une autre particule 'other'"""
    #     dist = (self.getPos() - other.getPos()).norm() # distance entre les deux centres
    #     return dist < self.rayon + other.rayon # vérification de la condition de collision
        

    def __str__(self):
        return "Particule ("+str(self.masse)+', '+str(self.pos)+', '+str(self.vit)+', "'+self.name+'", "'+self.color+'")'
    
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

    # Il est à noter que dans le sujet on nous demande de mettre une fonction simule dans la classe Particule, 
    # mais dans le code fourni, il y a une fonction simule dans la classe Univers. Je ne sais pas si c'est une erreur ou si c'est voulu.
    # Je vais donc mettre la fonction simule dans la classe Univers.
    
    
    def PFD(self):
        """Applique le Principe Fondamental de la Dynamique"""
        a = v3d()
        if not self.fix:
            a = self.getForces()*(1/self.masse) # a = F/m
        self.accel.append(a)
  
            
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

    def plot_particule(self,screen,scale=1):
        H = screen.get_height()
        
        X = [p.x*scale for p in self.pos]
        Y = [p.y*scale for p in self.pos]
        
        return plot(X,Y,color=self.color,label=self.name)
    
        
        
    # def plot3D(self,screen,scale=1):
    #     X = int(scale*self.getPos().x)
    #     Y = int(scale*self.getPos().y)
    #     Z = int(scale*self.getPos().z)
    #     VX = int(scale*self.getVit().x) + X
    #     VY = int(scale*self.getVit().y) + Y
    #     VZ = int(scale*self.getVit().z) + Z
    #     size=2
        
    #     pygame.draw.circle(screen,self.color,(X,Y),size,size)
    #     pygame.draw.line(screen,self.color,(X,Y),(VX,VY))
    #     pygame.draw.line(screen,self.color,(X,Y),(VX,VZ))
    #     pygame.draw.line(screen,self.color,(X,Y),(VY,VZ))
        
        
    def gameDraw(self,screen,scale=1):
        H = screen.get_height()
        W = screen.get_width()
        X = int(scale*self.getPos().x)
        Y = H - int(scale*self.getPos().y)
        VX = int(scale*self.getVit().x) + X
        VY = - int(scale*self.getVit().y) + Y
        pygame.draw.circle(screen,self.color,(X,Y),self.rayon,self.rayon)
        pygame.draw.line(screen,self.color,(X,Y),(VX,VY))
    
        # On vérifie que la particule ne sorte pas de l'écran:
        if self.getPos().x*scale < self.rayon:
            self.getPos().x = self.rayon/scale
            self.getVit().x = -self.getVit().x
            
        if self.getPos().x*scale > W - self.rayon :
            self.getPos().x = (W - self.rayon)/scale
            self.getVit().x = -self.getVit().x
            
        if self.getPos().y*scale <= self.rayon:
            self.getPos().y = self.rayon/scale
            self.getVit().y = -self.getVit().y
            
        if self.getPos().y*scale > H - self.rayon:
            self.getPos().y = (H - self.rayon)/scale
            self.getVit().y = -self.getVit().y


    def gameDrawWall(self,screen,scale=1):
        # Pour dessiner les murs, on va utiliser la fonction même fonction que pour dessiner les particules,
        
        H = screen.get_height()
        X = int(scale*self.getPos().x)
        Y = H - int(scale*self.getPos().y)
        pygame.draw.line(screen,self.color,(X,Y),(X,Y-200.), width=5)

            


    
