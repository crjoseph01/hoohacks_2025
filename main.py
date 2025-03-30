import sys
import pygame
import paintings
import goal
import draw

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0, 255)

# Other constants
WIDTH, HEIGHT = 800, 600
health_goals = {"fitness": [], "eating": [], "mental health": []}
token = False
coins = 1
locked = True

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Daily Habit Tracker!")

# Font
font = pygame.font.Font(None, 36)

def draw_button(x, y, image_path):
    button = pygame.image.load(image_path)
    buttonx, buttony = button.get_size()
    button_rect = button.get_rect()
    button_rect.topleft = (x - (buttonx // 2), y)

    screen.blit(button, button_rect)
    return button_rect

# Track current screen
game_state = "main_menu"  # Start on the main menu

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "main_menu" and goals_button.collidepoint(event.pos):
                game_state = "my_goals"  # Switch to goals screen
            elif game_state == "main_menu" and paintings_button.collidepoint(event.pos):
                game_state = "my_paintings"
            elif game_state == "my_goals":
                token = goal.health_goals_scene(screen, health_goals, token, events)
                if goal.draw_button(screen, GREEN, 20, HEIGHT - 70, 100, 50, "Menu").collidepoint(event.pos):
                    game_state = "main_menu"

    # **Render Screens Based on game_state**
    if game_state == "main_menu":
        screen.fill(WHITE)
        title_text = font.render("Main Menu", True, BLUE)
        title_textw, title_texth = title_text.get_size()
        screen.blit(title_text, ((WIDTH // 2) - (title_textw // 2), HEIGHT // 4))

        goals_button = draw_button(WIDTH // 2, HEIGHT // 2, "see_goals.png")
        paintings_button = draw_button((WIDTH // 2), (HEIGHT // 2) + 100, "see_paintings.png")
    elif game_state == "my_goals":
        token = goal.health_goals_scene(screen, health_goals, token, events)
        goal.draw_button(screen, GREEN, 20, HEIGHT - 70, 100, 50, "Menu")
    elif game_state == "my_paintings":
        game_state = paintings.paintings_page(game_state, screen, events, coins, locked)
    elif game_state == "draw_page":
        draw.color_puzzle_scene(screen, events)

    # Get mouse position and draw custom cursor
    cursor_img = pygame.image.load("cursor.png")  # Load a custom cursor image
    pygame.mouse.set_visible(False)  # Hide default cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_x, mouse_y))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


pygame.quit()