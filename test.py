import pygame
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
        self.tabs = [
            Tab("Menu 1: 2 particules", 100, 100, 200, 50, WHITE, BLACK, BLACK),
            Tab("Menu 2", 400, 100, 200, 50, WHITE, BLACK, BLACK)
        ]
        self.selected_tab = None

    def draw(self, surface):
        # Dessin des onglets
        for tab in self.tabs:
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
        self.title = FONT.render("2 particules", True, BLACK)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = WINDOW_WIDTH // 2
        self.title_rect.top = 50

    def draw(self, surface):
        # Dessin du titre
        surface.blit(self.title, self.title_rect)

    def handle_event(self, event):
        pass

# Classe pour l'interface du menu 2
class Menu2:
    def __init__(self):
        self.title = FONT.render("Menu 2", True, BLACK)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = WINDOW_WIDTH // 2
        self.title_rect.top = 50

    def draw(self, surface):
        # Dessin du titre
        surface.blit(self.title, self.title_rect)

    def handle_event(self, event):
        pass
    
# Initialisation de la fenêtre Pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Création des interfaces
main_menu = MainMenu()
menu1 = Menu1()
menu2 = Menu2()

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
    if selected_tab == "Menu 1: 2 particules":
        menu1.draw(window)
    elif selected_tab == "Menu 2":
        menu2.draw(window)

    # Actualisation de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()