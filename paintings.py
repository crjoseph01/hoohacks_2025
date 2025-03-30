import sys
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 215, 255)

WIDTH, HEIGHT = 800, 600

font = pygame.font.Font(None, 36)

def draw_button(x, y, screen, image_path):
    image = pygame.image.load(image_path) 
    imagex, imagey = image.get_size()
    button_rect = image.get_rect()
    button_rect.topleft = (x - (imagex // 2), y)

    screen.blit(image, button_rect)
    return button_rect

def paintings_page(game_state, screen, events, coins, locked):
    screen.fill(WHITE)
    title_text = font.render("My Paintings:", True, BLUE)
    title_textw, title_texth = title_text.get_size()
    screen.blit(title_text, ((WIDTH // 2) - (title_textw // 2), HEIGHT // 16))
    
    menu_button = draw_button(WIDTH // 2 , HEIGHT * 14 // 16, screen, "return_menu.png") # Go back to main menu
    
    if locked:
        drawings_button = draw_button(WIDTH // 2, HEIGHT * 20 // 160, screen, "locked_drawing.png")
    elif (locked == False):
        drawings_button = draw_button(WIDTH // 2, HEIGHT * 20 // 160, screen, "unlocked.png")

    if coins == 0:
        text = font.render("Complete Goals to Earn Coins!", True, BLUE)
        textw, texth = text.get_size()
        screen.blit(text, ((WIDTH // 2) - (textw // 2), HEIGHT * 10 // 16))
    elif coins != 0:
        text = font.render("Click on Painting to Begin!", True, BLUE)
        textw, texth = text.get_size()
        screen.blit(text, ((WIDTH // 2) - (textw // 2), HEIGHT * 10 // 16))

    for event in events:  # Use the events passed from main
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_button.collidepoint(event.pos):
                return "main_menu", locked
            elif coins > 0 and drawings_button.collidepoint(event.pos):
                locked = False
                return "draw_page", locked
    
    return game_state, locked