 # WRITE YOUR SOLUTION HERE:

import pygame
import random

window = pygame.display.set_mode((640, 480))
window.fill((0,0,0))

robot = pygame.image.load('robot.png')

for i in range(1000):
    window.blit(robot, (random.randint(0, 640), random.randint(0, 480)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()