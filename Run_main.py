import pygame
import keyboard

from vector3D import Vecteur3D as v3d
from Particule import * 
from Univers import *
from Generateur import *




# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# Couleurs utilisées
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREY = (192,192,192)

# Police de caractères
FONT = pygame.font.SysFont('arial', 30)

# Classe pour les onglets
class Tab:
    def __init__(self, text, x=0, y=0, width=0, height=0, color=WHITE, highlighted_color=BLACK, font_color=BLACK):
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
            Tab("Une fois dans un menu, appuyez sur Esc pour revenir au menu principal",height=70,color=WHITE, highlighted_color= RED, font_color=RED),
            Tab("Menu 1: 10 particules", 100, 100, 200, 50, highlighted_color=BLACK, font_color=BLACK),
            Tab("Menu 2: Particule aléatoire et viscosité", 100, 100 + tab_height, 200, 50, highlighted_color=BLACK, font_color=BLACK),
            Tab("Menu 3: Système masse+ressort+amortisseur", 100, 100 + 2 * tab_height, 200, 50, highlighted_color=BLACK, font_color=BLACK),
            Tab("Menu 4: Trois pendules", 100, 100 + 3 * tab_height, 200, 50, highlighted_color=BLACK, font_color=BLACK),
            Tab("Menu 5: Pendule double", 100, 100 + 4 * tab_height, 200, 50, highlighted_color=BLACK, font_color=BLACK),
            Tab("Menu 6: Système 2ddl (2 masses+3 ressorts)", 100, 100 + 5 * tab_height, 200, 50, highlighted_color=BLACK, font_color=BLACK),
            Tab("Menu 7: Pendule inverse", 100, 100 + 6 * tab_height, 200, 50, highlighted_color=BLACK, font_color=BLACK)
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
    
        
    
# Initialisation de la fenêtre Pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Création des interfaces
main_menu = MainMenu()


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
    if selected_tab == "Menu 1: 10 particules":
        '''Exemple de simulation avec 10 particules de masse et de position (x,y) aléatoires en chute libre selon -z 
        avec une force de gravité et une force attractive placé au centre à z=-5m'''
        
        import Run_sys1
        Run_sys1.run()
        
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        main_menu = MainMenu() # Retour à l'interface principale
        
        
    ############################## MENU 2 #####################################
    elif selected_tab == "Menu 2: Particule aléatoire et viscosité":

        import Run_sys2
        Run_sys2.run()
        
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        main_menu = MainMenu() # Retour à l'interface principale


    ############################## MENU 3 #####################################
    elif selected_tab == "Menu 3: Système masse+ressort+amortisseur":
        import Run_sys3
        Run_sys3.run()
        
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        main_menu = MainMenu() # Retour à l'interface principale
        
        
    ############################## MENU 4 #####################################
    elif selected_tab == "Menu 4: Trois pendules":
        import Run_sys4
        Run_sys4.run()
        
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        main_menu = MainMenu() # Retour à l'interface principale
        
    ############################## MENU 5 #####################################
    elif selected_tab == "Menu 5: Pendule double":
        import Run_sys5
        Run_sys5.run()
        
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        main_menu = MainMenu() # Retour à l'interface principale
        
    ############################## MENU 6 #####################################
    elif selected_tab == "Menu 6: Système 2ddl (2 masses+3 ressorts)":
        import Run_sys6
        Run_sys6.run()
        
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        main_menu = MainMenu() # Retour à l'interface principale
        
    # ############################## MENU 7 #####################################
    # elif selected_tab == "Menu 7: Pendule inverse":
        

    # Actualisation de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
sys.exit()