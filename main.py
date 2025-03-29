"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
# Template from: http://programarcadegames.com/python_examples/f.php?file=pygame_base_template.py
 
import sys
import pygame

pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0, 255)

# Other constants
WIDTH, HEIGHT = 800, 600
 
# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dailt Habit Tracker!")

# Font
font = pygame.font.Font(None, 36)

def draw_button(x, y, text):
    text_surface = font.render(text, True, BLACK)
    textw, texth = text_surface.get_size()
    
    button_rect = pygame.Rect(x - ((textw + 100)// 2), y, textw + 100, texth + 50)
    pygame.draw.rect(screen, GOLD, button_rect)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect


# Track current screen
game_state = "main_menu"  # Start on the main menu

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "main_menu" and goals_button.collidepoint(event.pos):
                game_state = "my_goals"  # Switch to goals screen
            elif game_state == "main_menu" and paintings_button.collidepoint(event.pos):
                game_state = "my_paintings" # Switch to paintings screen
            elif game_state == "my_paintings" and menu_button.collidepoint(event.pos):
                game_state = "main_menu" # Switch to main menu screen
            elif game_state == "my_goals" and menu_button.collidepoint(event.pos):
                game_state = "main_menu"  # Switch to main menu screen
    
    # **Render Screens Based on game_state**
    if game_state == "main_menu":
        screen.fill(WHITE)
        title_text = font.render("Main Menu", True, GOLD)
        title_textw, title_texth = title_text.get_size()
        screen.blit(title_text, ((WIDTH // 2) - (title_textw // 2), HEIGHT // 4))
        
        goals_button = draw_button((WIDTH // 2), HEIGHT // 2, "See My Goals!")
        paintings_button = draw_button ((WIDTH // 2), (HEIGHT // 2) + 100, "See My Paintings!")
    elif game_state == "my_goals":
        screen.fill(WHITE)
        title_text = font.render("My Goals:", True, GOLD)
        title_textw, title_texth = title_text.get_size()
        screen.blit(title_text, ((WIDTH // 2) - (title_textw // 2), HEIGHT // 4))
        
        menu_button = draw_button(WIDTH // 2, HEIGHT // 2, "Back to Main Menu")
    elif game_state == "my_paintings":
        screen.fill(WHITE)
        title_text = font.render("My Paintings:", True, GOLD)
        title_textw, title_texth = title_text.get_size()
        screen.blit(title_text, ((WIDTH // 2) - (title_textw // 2), HEIGHT // 4))
        
        menu_button = draw_button(WIDTH // 2, HEIGHT // 2, "Back to Main Menu")
        

    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # --- Drawing code should go here

    # Get mouse position and draw custom cursor
    cursor_img = pygame.image.load("cursor.png")  # Load a custom cursor image
    pygame.mouse.set_visible(False)  # Hide default cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_x, mouse_y))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()