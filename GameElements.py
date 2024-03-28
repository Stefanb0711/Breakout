import pygame
from PIL import Image
import random
import math


game_over = False

RED = (255, 0, 0)
BLUE = (0, 255, 0)
WHITE = (255, 255, 255)

background = pygame.image.load("Bilder/Hintergrund.png")
background = pygame.transform.scale(background, (600, 800) )

def calculate_bounce_angle(incoming_angle, surface_angle):
    incoming_angle_rad = math.radians(incoming_angle)
    surface_angle_rad = math.radians(surface_angle)

    surface_normal = (math.cos(surface_angle_rad), math.sin(surface_angle_rad))

    incidence_angle = math.acos(
        surface_normal[0] * math.cos(incoming_angle_rad) + surface_normal[1] * math.sin(incoming_angle_rad))

    # Berechne den reflektierten Winkel basierend auf dem Reflexionsgesetz
    reflected_angle = 2 * surface_angle_rad - incoming_angle_rad + math.pi

    # Konvertiere den Winkel in Grad zurück und stelle sicher, dass er im Bereich [0, 360) liegt
    reflected_angle_deg = math.degrees(reflected_angle) % 360

    return reflected_angle_deg


def abprallwinkel_berechnen(einfallswinkel, wandwinkel):
    einfallswinkel %= 360
    wandwinkel %= 360

    winkeldifferenz = einfallswinkel - wandwinkel
    ausfallwinkel = wandwinkel - winkeldifferenz
    ausfallwinkel = (ausfallwinkel + 360) % 360

    return ausfallwinkel



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

        pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        """if self.left:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        elif self.right:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        else:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))
"""


class Ball:
    def __init__(self):

        self.x = 400
        self.y = 500
        self.start_position = [self.x, self.y]
        self.heading_degrees = random.randrange(20, 160)

        self.vel = 5



        self.heading_rad = math.radians(self.heading_degrees)





        self.radius = 25




    def draw(self, win):
        global game_over


        velocity_x = self.vel * math.cos(self.heading_rad)
        velocity_y = self.vel * math.sin(self.heading_rad)


        self.x += velocity_x
        self.y += velocity_y


        if self.x >= 600 - self.radius or self.x <= 0 + self.radius:
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 90)

            self.heading_rad = math.radians(self.heading_degrees)

            #self.heading_angle = math.radians(self.heading_angle)


        elif self.y >= 800 - self.radius or self.y <=0 + self.radius:
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 180)
            #self.heading = math.degrees(self.heading_angle)
            self.heading_rad = math.radians(self.heading_degrees)

            game_over = True
            #pygame.quit()

        elif self.y <= 0:
            pass


        pygame.draw.circle(surface=win, color=RED, center=(self.x, self.y), radius=self.radius)




class Obstacles:
    def __init__(self):
        pass


