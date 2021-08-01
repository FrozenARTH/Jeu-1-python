import pygame
pygame.init()

#creer une premiere classe qui va representer notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()

# generer la fenetre de notre jeu
pygame.display.set_caption("Comete fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# charger notre joueur
player = Player()

running = True

# boucle tant que cette condition est vraie
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de mon joueur
    screen.blit(player.image, Player.rect)

    # mettre à joue l'arriere plan
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # pour detecter que la fenetre est fermé
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
