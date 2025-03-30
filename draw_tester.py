# color_puzzle_tester.py
import pygame
import sys
from draw_update import color_puzzle_scene

pygame.init()
print("Pygame initialized")

screen = pygame.display.set_mode((800, 600))  # Correct order: set_mode first
print("Display mode set")
pygame.display.set_caption("Color Puzzle Tester")

color_puzzle_scene(screen)
print("color_puzzle_scene finished")