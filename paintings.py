import sys
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 215, 255)

WIDTH, HEIGHT = 800, 600

font = pygame.font.Font(None, 36)

def draw_button(x, y, screen):
    return_menu = pygame.image.load("return_menu.png") 
    return_menux, return_menuy = return_menu.get_size()
    button_rect = return_menu.get_rect()
    button_rect.topleft = (x - (return_menux // 2), y)

    screen.blit(return_menu, button_rect)
    return button_rect

def paintings_page(game_state, screen):
    screen.fill(WHITE)
    title_text = font.render("My Paintings:", True, BLUE)
    title_textw, title_texth = title_text.get_size()
    screen.blit(title_text, ((WIDTH // 2) - (title_textw // 2), HEIGHT // 16))
    
    menu_button = draw_button(WIDTH // 2 , HEIGHT * 14 // 16, screen) # Go back to main menu

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu_button.collidepoint(event.pos):
                game_state = "main_menu"
                return game_state
    
    return game_state