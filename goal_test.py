# goal_tester.py
import pygame
import sys
import goal

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goal Tester")

# Global variables
health_goals = {"fitness": [], "eating": [], "mental health": []}
token = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    token = goal.health_goals_scene(screen, health_goals, token)
    pygame.display.flip()