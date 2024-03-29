import pygame
from GameElements import Player, game_over, Ball, Obstacles


"""start_win = pygame.display.set_mode((600, 800))
start_game = False

#background = pygame.image.load("Bilder/Hintergrund.png")
#background = pygame.transform.scale(background, (600, 800))

def redraw_start_window():
    pygame.draw.rect(start_win, (255, 0, 0),(200, 200, 200, 200) )
    pygame.display.update()


while not start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = True
            pygame.quit()


    redraw_start_window()
"""




win = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()




player = Player()
ball = Ball()
obstacle_manager = Obstacles()



def redrawGameWindow():

    player.draw(win=win)
    ball.draw(win=win, player=player, obstacles=obstacle_manager.obstacles)
    obstacle_manager.draw(win=win)


    pygame.display.update()

#if start_game:
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


