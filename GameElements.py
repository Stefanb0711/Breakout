import pygame
from PIL import Image

game_over = False

RED = (255, 0, 0)
BLUE = (0, 255, 0)
WHITE = (255, 255, 255)

background = pygame.image.load("Bilder/Hintergrund.png")
background = pygame.transform.scale(background, (600, 800) )

def calculate_bounce_angle(incidence_angle, wall_angle ):
    pass

class Player:
    def __init__(self):
        self.x = 300
        self.y = 750
        self.width = 80
        self.height = 20
        self.border_padding = 5
        self.vel = 5
        self.left = False
        self.right = False



    def draw(self, win):
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))

        if self.left:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        elif self.right:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        else:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))



class Ball:
    def __init__(self):
        pass

class Obstacles:
    def __init__(self):
        pass


