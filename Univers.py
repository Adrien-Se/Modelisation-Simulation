import pygame
from vector3D import Vecteur3D as v3d
from Particule import *
from Generateur import *

class Univers(object) :
    
    def __init__(self,name="l'Univers",t0=0, step=0.1,W=800,H=600,*args):
        self.name = name
        self.temps=[t0]
        self.population=[]
        self.step=step
        self.sources=[]
        
        self.width=W
        self.height=H
        
        
    def addSource(self,*args):
        sources = list(args)
        self.sources += sources
        
        
    def addAgent(self,*args):
        agents = list(args)
        self.population+=agents
        
        
    def simule(self):
        for p in self.population:
            Ftot=v3d()
            for f in self.sources:
                if f.effect(p) is not None:
                    Ftot += f.effect(p)
            
            # On vérifie que les particules ne sortent pas de l'écran
            if p.getPos().x <= 0:
                p.getPos().x = 0
                p.getVit().x = -p.getVit().x
            elif p.getPos().x >= self.width:
                p.getPos().x = self.width
                p.getVit().x = -p.getVit().x
            if p.getPos().y <= 0:
                p.getPos().y = 0
                p.getVit().y = -p.getVit().y
            elif p.getPos().y >= self.height:
                p.getPos().y = self.height
                p.getVit().y = -p.getVit().y

                
            p.setForces(Ftot)
            p.PFD()
            p.move(self.step)
            
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

        
    def gameUpdate(self, *args):
        
        H = self.screen.get_height()
        W = self.screen.get_width()
        
        now = self.temps[-1]
        while self.temps[-1] < (now + (1/self.fps)):
            self.simule()
        
        font_obj = pygame.font.Font('freesansbold.ttf', 24)
        text_surface_obj = font_obj.render('Time: '+str(now)[:4] , True, 'red', self.background)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (25, 10)

        self.screen.fill(self.background)
        
        # Si un menu est lancé, on affiche un texte d'indications:
        if self.name: 
            text1 = font_obj.render("Appuyez sur la barre d'espace pour démarrer ou ajouter une particule", True, 'black', self.background)
            text_rect = text1.get_rect()
            text_rect.center = (500, 50)
            self.screen.blit(text1, text_rect)
        
        # for p in self.population:
        #     x, y = p.getPos().x, p.getPos().y
        #     x - p.rayon < 0 or x + p.rayon > W or y - p.rayon < 0 or y + p.rayon > H
            
        for p in self.population:
            if p.name == ("mur1" or "mur2") and self.name == "sys6":
                pass
            else:
                p.gameDraw(self.screen,self.scale)
            
        for m in self.population:
            if (m.name == "mur1" or m.name == "mur2") and self.name == "sys6":
                m.gameDrawWall(self.screen,self.scale)
        
        # On trace les traits:
        if self.name == "sys3" or self.name == "sys4":
            for p in self.population:
                if p.name == "pivot":
                    p0 = p
                else:
                    p1 = p
                    if p0 is not None and p1 is not None:
                        scale = 1000
                        pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
                
        if self.name == "sys5":
            # for p in self.population:
            #     if p.name == "pivot":
            #         p0 = p
            #     if p.name == "masse1":
            #         p1 = p
            #         if p0 is not None and p1 is not None:
            #             H = self.screen.get_height()
            #             scale = 1000
            #             pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
            #     if p.name == "masse1":
            #         p0 = p
            #     if p.name == "masse2":
            #         p1 = p
            #         if p0 is not None and p1 is not None:
            #             H = self.screen.get_height()
            #             scale = 1000
            #             pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
            
            # Une autre manière de l'écrire:
            
            # création d'un dictionnaire pour stocker les particules
            particules = {}

            # boucle sur la population pour trouver les particules
            for p in self.population:
                if p.name == "pivot": particules["pivot"] = p
                elif p.name == "masse1": particules["masse1"] = p
                elif p.name == "masse2": particules["masse2"] = p

            # check si toutes les particules sont présentes
            if all(key in particules for key in ["pivot", "masse1", "masse2"]):
                # Dessiner les traits entre les particules:
                p0 = particules["pivot"]
                p1 = particules["masse1"]
                p2 = particules["masse2"]
                H = self.screen.get_height()
                scale = 1000
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p2.getPos().x*scale, H-p2.getPos().y*scale), 2)
                
        if self.name == "sys6":
        
            # création d'un dictionnaire pour stocker les particules
            particules = {}

            # boucle sur la population pour trouver les particules
            for p in self.population:
                if p.name == "mur1": particules["mur1"] = p
                elif p.name == "masse1": particules["masse1"] = p
                elif p.name == "masse2": particules["masse2"] = p
                elif p.name == "mur2": particules["mur2"] = p

            # check si toutes les particules sont présentes
            if all(key in particules for key in ["mur1","mur2", "masse1", "masse2"]):
                # Dessiner les traits entre les particules:
                p0 = particules["mur1"]; p1 = particules["masse1"]; p2 = particules["masse2"]; p3 = particules["mur2"]
                H = self.screen.get_height()
                scale = 1000
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p1.getPos().x*scale, H-p1.getPos().y*scale), (p2.getPos().x*scale, H-p2.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p2.getPos().x*scale, H-p2.getPos().y*scale), (p3.getPos().x*scale, H-p3.getPos().y*scale), 2)
                # pygame.draw.line(self.screen, (0,0,0), (p2.getPos().x*scale, H-p2.getPos().y*scale), (p3.getPos().x*scale, H-p3.getPos().y*scale), 2)
                
        self.screen.blit(text_surface_obj, (5,10))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            
        self.gameKeys = pygame.key.get_pressed()
        self.clock.tick(self.fps)