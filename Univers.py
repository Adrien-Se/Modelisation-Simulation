import pygame
from vector3D import Vecteur3D as v3d
from Particule import *

class Univers(object) :
    
    def __init__(self,name="l'Univers",t0=0, step=0.1,*args):
        self.name = name
        self.temps=[t0]
        self.population=[]
        self.step=step
        self.sources=[]
        
    def addSource(self,*args):
        sources = list(args)
        self.sources += sources
        
    def addAgent(self,*args):
        agents = list(args)
        self.population+=agents
        
    def simule(self):
        for a in self.population:
            Ftot=v3d()
            for f in self.sources:
                Ftot += f.effect(a)
            
            a.setForces(Ftot)
            a.PFD()
            a.move(self.step)
            
        self.temps.append(self.temps[-1]+self.step)
    
    def plot(self):
        for a in self.population:
            a.plot()
        
    def gameInit(self,W,H,fps=60,background=(0,0,0),scale=1):
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()
        self.background=background
        self.fps=fps
        self.scale=scale
        self.run=True
                
        pygame.display.set_caption(self.name)
        self.gameKeys = pygame.key.get_pressed()

        
    def gameUpdate(self):
        
        now = self.temps[-1]
        while self.temps[-1] < (now + (1/self.fps)):
            self.simule()
            #print(self.temps[-1])
        
        font_obj = pygame.font.Font('freesansbold.ttf', 24)
        text_surface_obj = font_obj.render('Time: '+str(now)[:4] , True, 'red', self.background)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (25, 10)

        self.screen.fill(self.background)
        
        for p in self.population:
            p.gameDraw(self.screen,self.scale)
            
        self.screen.blit(text_surface_obj, (5,10))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        
        self.gameKeys = pygame.key.get_pressed()
        
        self.clock.tick(self.fps)