import pygame
from GameElements import Player, game_over, Ball


win = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Breakout")



clock = pygame.time.Clock()

player = Player()
ball = Ball()


def redrawGameWindow():


    player.draw(win=win)
    ball.draw(win=win)

    pygame.display.update()


while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.border_padding:
        player.left = True
        player.right = False
        player.x -= player.vel

    elif keys[pygame.K_RIGHT] and player.x < 600 - player.width - player.border_padding:
        player.right = True
        player.left = False
        player.x += player.vel

    else:
        player.left = False
        player.right = False

    redrawGameWindow()


