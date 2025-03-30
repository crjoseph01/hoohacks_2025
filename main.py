import sys
import pygame
import paintings
import goals_updated
import draw

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255, 255)

# Other constants
WIDTH, HEIGHT = 800, 600
health_goals = {"fitness": [], "eating": [], "mental health": []}
tokens = 0
locked = True

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Daily Habit Tracker!")

# Font
font = pygame.font.Font(None, 56)

def draw_button(x, y, image_path):
    button = pygame.image.load(image_path)
    buttonx, buttony = button.get_size()
    button_rect = button.get_rect()
    button_rect.topleft = (x - (buttonx // 2), y)

    screen.blit(button, button_rect)
    return button_rect

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect

# Function to draw token
def draw_token_counter(screen, token):
    draw_text(f"Tokens: {token}", pygame.font.Font(None, 36), BLACK, screen, WIDTH - 150, 5)

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
                if goals_updated.draw_image(WIDTH // 2, HEIGHT * 14 // 16, screen, "return_menu.png").collidepoint(event.pos):
                    game_state = "main_menu"

    # **Render Screens Based on game_state**
    if game_state == "main_menu":
        background = pygame.image.load("hoohacks_background.png")
        screen.blit(background, (0,0))

        main_title = pygame.image.load("title_main.png")
        main_titlex, main_titley = main_title.get_size()
        screen.blit(main_title, ((WIDTH // 2) - (main_titlex // 2), (HEIGHT * 3 // 10)))

        goals_button = draw_button(WIDTH // 2, HEIGHT // 2, "see_goals.png")
        paintings_button = draw_button((WIDTH // 2), (HEIGHT // 2) + 100, "see_paintings.png")
    elif game_state == "my_goals":
        tokens, game_state = goals_updated.health_goals_scene(screen, health_goals, events, 0, game_state)
        goals_updated.draw_image(WIDTH // 2, HEIGHT * 14 // 16, screen, "return_menu.png")
    elif game_state == "my_paintings":
        if tokens >> 0:
            locked = False
        game_state, locked = paintings.paintings_page(game_state, screen, events, tokens, locked)
    elif game_state == "draw_page":
        tokens -= 1
        locked = True
        game_state = draw.color_puzzle_scene(screen)

    # Get mouse position and draw custom cursor
    cursor_img = pygame.image.load("cursor.png")  # Load a custom cursor image
    pygame.mouse.set_visible(False)  # Hide default cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_x, mouse_y))

    draw_token_counter(screen, tokens)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


pygame.quit()