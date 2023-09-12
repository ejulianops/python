# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
window.fill((0,0,0))

robot = pygame.image.load('robot.png')
width = robot.get_width()
height = robot.get_height()

robots_count = 9
window.blit(robot, (width, height))

repeted_robot_position = width + width

while robots_count > 0:    
    window.blit(robot, (repeted_robot_position, height))
    robots_count -= 1
    repeted_robot_position += width

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()