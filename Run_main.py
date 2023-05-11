import pygame
from vector3D import Vecteur3D as v3d
from Particule import *
from Univers import *
from Generateur import *


# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Couleurs utilisées
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police de caractères
FONT = pygame.font.SysFont('arial', 30)

# Classe pour les onglets
class Tab:
    def __init__(self, text, x, y, width, height, color, highlighted_color, font_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.highlighted_color = highlighted_color
        self.font_color = font_color
        self.highlighted = False

    def draw(self, surface):
        # Dessin du rectangle de l'onglet
        if self.highlighted:
            pygame.draw.rect(surface, self.highlighted_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        # Dessin du texte de l'onglet
        text_surface = FONT.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        # Si l'utilisateur clique sur l'onglet
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Classe pour l'interface du menu principal
class MainMenu:
    def __init__(self):
        tab_height = 50
        self.tabs = [
            Tab("Menu 1: 2 particules", 100, 100, 200, 50, WHITE, BLACK, BLACK),
            Tab("Menu 2: Particule aléatoire", 100, 100 + tab_height, 200, 50, WHITE, BLACK, BLACK),
            Tab("Menu 3: Particule", 100, 100 + 2 * tab_height, 200, 50, WHITE, BLACK, BLACK)
        ]
        self.selected_tab = None

    def draw(self, surface):
        # Dessin des onglets
        for tab in self.tabs:
            tab.rect.centerx = WINDOW_WIDTH // 2  # Centrage horizontal
            tab.rect.top = (WINDOW_HEIGHT - len(self.tabs) * tab.rect.height) // 2 + self.tabs.index(tab) * tab.rect.height  # Centrage vertical
            tab.draw(surface)

    def handle_event(self, event):
        # Gestion des événements pour les onglets
        for tab in self.tabs:
            if tab.handle_event(event):
                self.selected_tab = tab.text

    def is_selected(self):
        # Renvoie le nom de l'onglet sélectionné
        return self.selected_tab

# Classe pour l'interface du menu 1
class Menu1:
    def __init__(self):
        self.title = FONT.render("Menu 1", True, BLACK)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = WINDOW_WIDTH // 2
        self.title_rect.top = 50

    def handle_event(self, event):
        pass

# Classe pour l'interface du menu 2
class Menu2:
    def __init__(self):
        self.title = FONT.render("Menu 2", True, BLACK)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = WINDOW_WIDTH // 2
        self.title_rect.top = 50

    def handle_event(self, event):
        pass
    
# Classe pour l'interface du menu 3
class Menu3:
    def __init__(self):
        self.title = FONT.render("Menu 3", True, BLACK)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = WINDOW_WIDTH // 2
        self.title_rect.top = 50

    def handle_event(self, event):
        pass
    
# Initialisation de la fenêtre Pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Création des interfaces
main_menu = MainMenu()
menu1 = Menu1()
menu2 = Menu2()
menu3 = Menu3()

# Boucle principale de Pygame
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            main_menu.handle_event(event)

    # Dessin de la fenêtre
    window.fill(WHITE)
    main_menu.draw(window)

    # Si un onglet est sélectionné, afficher l'interface correspondante
    selected_tab = main_menu.is_selected()
    
    ############################## MENU 1 #####################################
    if selected_tab == "Menu 1: 2 particules":
        noyau = Particule(pos=v3d(0.,0.),name='pivot',color='black',fix=True)  # fixe: déplacements bloqués
        masse2 = Particule(name='masse-2',pos=v3d(0.2,0.1),color='red')

        # Création du simulateur avec pas de temps de 1ms (nécessaire pour bien simuler le ressort)
        Monde = Univers(step=0.001)

        # Monde.addAgent(boule1,boule2)
        Monde.addAgent(noyau,masse2)
        
        Monde.addSource(Gravite(v3d(0,-10)), Viscosity(0.2),  Ressort(noyau,masse2,raideur=9000,amortissement=500,l0=0.1))

        # Initialiser l'affichage & lancer
        Monde.gameInit(1024,768,background='gray',scale=1000) # échelle 1000 -> 1 pixel = 1 mm
        
        while Monde.run:
            Monde.gameUpdate()
        sys.exit()
        
        
    ############################## MENU 2 #####################################
    elif selected_tab == "Menu 2: Particule aléatoire":
        menu2.draw(window)

    ############################## MENU 3 #####################################
    elif selected_tab == "Menu 3: Particule aléatoire":
        menu3.draw(window)

    # Actualisation de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()