import pygame
from vector3D import Vecteur3D as v3d
from Particule import *
from Generateur import *

class Univers(object) :
    '''Classe Univers
    Attributs:
    - name: nom de l'univers
    - temps: liste des temps
    - population: liste des particules
    - step: pas de temps
    - sources: liste des sources de force
    
    Méthodes:
    - addSource: ajoute une source de force
    - removeSource: retire une source de force
    - addAgent: ajoute une particule
    - simule: simule l'univers
    - gameInit: initialise l'affichage
    - gameUpdate: met à jour l'affichage
    - plot: plot la position en fonction du temps
    - plotx_temps: plot la position en fonction du temps
    '''
    
    def __init__(self,name="l'Univers",t0=0, step=0.1,*args):
        self.name = name
        self.temps=[t0]
        self.population=[]
        self.step=step
        self.sources=[]

    def addSource(self,*args):
        sources = list(args)
        self.sources += sources
        
    def removeSource(self,*args):
        sources = list(args)
        print(sources)
        for s in sources:
            self.sources.remove(s)
        
        
    def addAgent(self,*args):
        agents = list(args)
        self.population+=agents
        
        
    def simule(self):
        for p in self.population:
            Ftot=v3d()
            for f in self.sources:
                if f.effect(p) is not None:
                    Ftot += f.effect(p)
                                
            p.setForces(Ftot)
            p.PFD()
            p.move(self.step)
            
        self.temps.append(self.temps[-1]+self.step)
        
        
    def gameInit(self,W=1000,H=700,fps=60,background='white',scale=1):
        '''Initialise l'affichage du jeu
        W: largeur de la fenêtre
        H: hauteur de la fenêtre
        fps: nombre d'images par seconde
        background: couleur de fond
        scale: échelle de la simulation'''
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()
        self.background=background
        self.fps=fps
        self.scale=scale
        self.run=True
                
        pygame.display.set_caption(self.name)
        self.gameKeys = pygame.key.get_pressed()

        
    def gameUpdate(self, scale, *args):
        
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

        for p in self.population:
            if p.name == ("mur1" or "mur2") and self.name == "sys6": # on dessine les murs dans le système 6
                pass
            else:
                p.gameDraw(self.screen,self.scale)
            
        for m in self.population:
            if (m.name == "mur1" or m.name == "mur2") and self.name == "sys6":
                m.gameDrawWall(self.screen,self.scale)
        
        # On trace les traits:
        if self.name == "sys3":
            particules = {} # création d'un dictionnaire pour stocker les particules

            for p in self.population: # boucle sur la population pour trouver les particules
                if p.name == "pivot": particules["pivot"] = p
                elif p.name == "masse1": particules["masse1"] = p

            if all(key in particules for key in ["pivot", "masse1"]): # check si toutes les particules sont présentes
                # Dessiner les traits entre les particules:
                p0 = particules["pivot"];p1 = particules["masse1"]
                H = self.screen.get_height()
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*self.scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*self.scale), 2)
                
        if self.name == "sys4":
            particules = {}
            for p in self.population:
                if p.name == "pivot": particules["pivot"] = p
                elif p.name == "masse1": particules["masse1"] = p
                elif p.name == "masse2": particules["masse2"] = p
                elif p.name == "masse3": particules["masse3"] = p

            if all(key in particules for key in ["pivot", "masse1", "masse2", "masse3"]):
                p0 = particules["pivot"];p1 = particules["masse1"]
                p2 = particules["masse2"];p3 = particules["masse3"]
                H = self.screen.get_height()
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p2.getPos().x*scale, H-p2.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p3.getPos().x*scale, H-p3.getPos().y*scale), 2)

                
        if self.name == "sys5":
            particules = {}
            for p in self.population:
                if p.name == "pivot": particules["pivot"] = p
                elif p.name == "masse1": particules["masse1"] = p
                elif p.name == "masse2": particules["masse2"] = p

            if all(key in particules for key in ["pivot", "masse1", "masse2"]):
                p0 = particules["pivot"]
                p1 = particules["masse1"]
                p2 = particules["masse2"]
                H = self.screen.get_height()
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p1.getPos().x*scale, H-p1.getPos().y*scale), (p2.getPos().x*scale, H-p2.getPos().y*scale), 2)
                
        if self.name == "sys6":
            particules = {}
            for p in self.population:
                if p.name == "mur1": particules["mur1"] = p
                elif p.name == "masse1": particules["masse1"] = p
                elif p.name == "masse2": particules["masse2"] = p
                elif p.name == "mur2": particules["mur2"] = p
                
            if all(key in particules for key in ["mur1","mur2", "masse1", "masse2"]):
                p0 = particules["mur1"]; p1 = particules["masse1"]; p2 = particules["masse2"]; p3 = particules["mur2"]
                H = self.screen.get_height()
                pygame.draw.line(self.screen, (0,0,0), (p0.getPos().x*scale, H-p0.getPos().y*scale), (p1.getPos().x*scale, H-p1.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p1.getPos().x*scale, H-p1.getPos().y*scale), (p2.getPos().x*scale, H-p2.getPos().y*scale), 2)
                pygame.draw.line(self.screen, (0,0,0), (p2.getPos().x*scale, H-p2.getPos().y*scale), (p3.getPos().x*scale, H-p3.getPos().y*scale), 2)
                
        self.screen.blit(text_surface_obj, (5,10)) # affichage du temps
        pygame.display.update() # mise à jour de l'affichage
        
        for event in pygame.event.get(): # gestion des évènements
            if event.type == pygame.QUIT: # si l'utilisateur clique sur la croix
                self.run = False # on arrête la simulation
            
        self.gameKeys = pygame.key.get_pressed() # on récupère les touches appuyées
        self.clock.tick(self.fps) # on attend pour avoir un fps constant
        
        
    def plot(self): # plot de la position en fonction du temps
        for a in self.population:
            a.plot_particule(screen=self.screen,scale=self.scale)
            
    def plotx_temps(self): # plot de la position en fonction du temps
        for a in self.population:
            a.plotx_temps(screen=self.screen,scale=self.scale)