import sys
import pygame

pygame.init()
pygame.font.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CADETBLUE = pygame.Color('cadetblue2')
WIDTH, HEIGHT = 800, 600

# Fonts
small_font = pygame.font.Font(None, 24)
base_font = pygame.font.Font(None, 32)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect

# Function to draw buttons
def draw_button(surface, color, x, y, width, height, text):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, color, rect)
    draw_text(text, small_font, BLACK, surface, x + 10, y + 5)
    return rect

# Function to draw image for main menu button
def draw_image(x, y, screen, image_path):
    image = pygame.image.load(image_path) 
    imagex, imagey = image.get_size()
    button_rect = image.get_rect()
    button_rect.topleft = (x - (imagex // 2), y)

    screen.blit(image, button_rect)
    return button_rect

# Function to draw checkboxes
def draw_checkbox(surface, x, y, checked):
    rect = pygame.draw.rect(surface, BLACK, (x, y, 20, 20), 2)
    if checked:
        pygame.draw.line(surface, GREEN, (x, y), (x + 20, y + 20), 3)
        pygame.draw.line(surface, GREEN, (x + 20, y), (x, y + 20), 3)
    return rect

def get_user_input(screen, input_rect):
    user_text = ''
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_text
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        enter_background = pygame.image.load("enter_background.png")  # Clear the screen before drawing
        screen.blit(enter_background, (0,0))
        draw_text("Enter your goal:", base_font, BLACK, screen, (WIDTH // 2) - 150, HEIGHT * 2 // 5)
        pygame.draw.rect(screen, CADETBLUE, input_rect)
        screen.blit(base_font.render(user_text, True, BLACK), (input_rect.x + 5, input_rect.y + 5))

        cursor_img = pygame.image.load("cursor.png")  # Load a custom cursor image
        pygame.mouse.set_visible(False)  # Hide default cursor
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(cursor_img, (mouse_x, mouse_y))

        pygame.display.flip()
        clock.tick(60)


def health_goals_scene(screen, health_goals, event_list, tokens, game_state):
    screen.fill(WHITE)
    draw_text("Health Goals", base_font, BLACK, screen, (WIDTH // 2) - 80, 20)

    categories = ["fitness", "eating", "mental health"]
    column_width = WIDTH // len(categories)

    for i, category in enumerate(categories):
        x_offset = i * column_width + 20
        y_offset_cat = 90
        category_rect = draw_text(category.capitalize(), small_font, BLACK, screen, x_offset, 60)

        for j, goal in enumerate(health_goals[category]):
            checkbox = draw_checkbox(screen, x_offset + 20, y_offset_cat, goal["completed"])
            draw_text(goal["text"], small_font, BLACK, screen, x_offset + 50, y_offset_cat)
            y_offset_cat += 30

            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and checkbox.collidepoint(event.pos):
                        goal["completed"] = not goal["completed"]


        add_button = draw_button(screen, CADETBLUE, x_offset + column_width - 160, y_offset_cat, 100, 30, "Add Goal")

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if add_button.collidepoint(event.pos):
                    input_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 25, 300, 50)
                    new_goal = get_user_input(screen, input_rect)
                    if new_goal:
                        health_goals[category].append({"text": new_goal, "completed": False})

# Ensure there are goals before checking completion
    has_goals = any(health_goals[category] for category in categories)
    all_completed = has_goals and all(
        goal["completed"] for category in categories for goal in health_goals[category]
    )

    if all_completed:
        tokens += 1
        draw_text("All goals completed! You earned a token!", base_font, GREEN, screen, WIDTH // 2 - 200, HEIGHT - 100)
        paintings_button = draw_image((WIDTH // 2), (HEIGHT // 2) + 100, screen, "see_paintings.png")
        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and paintings_button.collidepoint(event.pos):
                game_state = "my_paintings"
                return tokens, game_state

    return tokens, game_state
