import pygame
import sys

# Initialize Pygame font module
pygame.font.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_GREEN = pygame.Color('lightgreen')
CADETBLUE = pygame.Color('cadetblue2')

# Fonts
small_font = pygame.font.Font(None, 24)
base_font = pygame.font.Font(None, 32)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
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

# Function to draw checkboxes
def draw_checkbox(surface, x, y, checked):
    rect = pygame.Rect(x, y, 20, 20)
    pygame.draw.rect(surface, BLACK, rect, 2)
    if checked:
        pygame.draw.line(surface, GREEN, (x, y), (x + 20, y + 20), 3)
        pygame.draw.line(surface, GREEN, (x + 20, y), (x, y + 20), 3)
    return rect

# Function to draw image for main menu button
def draw_image(x, y, screen, image_path):
    image = pygame.image.load(image_path) 
    imagex, imagey = image.get_size()
    button_rect = image.get_rect()
    button_rect.topleft = (x - (imagex // 2), y)

    screen.blit(image, button_rect)
    return button_rect

def get_user_input(screen, input_rect):
    user_text = ''
    active = True
    color = CADETBLUE
    clock = pygame.time.Clock()

    while active:
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
        screen.fill(WHITE)  # Clear the screen before drawing
        draw_text("Enter your goal:", base_font, BLACK, screen, (WIDTH // 2) - 150, HEIGHT * 2 // 5)
        pygame.draw.rect(screen, CADETBLUE, input_rect)
        screen.blit(base_font.render(user_text, True, BLACK), (input_rect.x + 5, input_rect.y + 5))

        cursor_img = pygame.image.load("cursor.png")  # Load a custom cursor image
        pygame.mouse.set_visible(False)  # Hide default cursor
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(cursor_img, (mouse_x, mouse_y))

        pygame.display.flip()
        clock.tick(60)

def health_goals_scene(screen, health_goals, token, event_list, coins):
    screen.fill(WHITE)
    draw_text("Health Goals", small_font, BLACK, screen, screen.get_width() // 2 - 80, 20)

    categories = ["fitness", "eating", "mental health"]
    column_width = screen.get_width() // 3
    y_offset = 60
    needs_refresh = False

    category_rects = []

    for i, category in enumerate(categories):
        x_offset = i * column_width + 20
        category_rect = draw_text(category.capitalize(), small_font, BLACK, screen, x_offset, y_offset)
        category_rects.append(pygame.Rect(x_offset, y_offset, category_rect.width, category_rect.height))
        y_offset_cat = y_offset + 30

        goals_to_remove = []

        for j, goal in enumerate(health_goals[category]):
            checkbox_x = x_offset + 20
            checkbox = draw_checkbox(screen, checkbox_x, y_offset_cat, goal["completed"])
            goal_text_x = checkbox_x + 30
            draw_text(goal["text"], small_font, BLACK, screen, goal_text_x, y_offset_cat)
            y_offset_cat += 30

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for j, goal in enumerate(health_goals[category]):
                    checkbox_x = x_offset + 20
                    checkbox = pygame.Rect(checkbox_x, y_offset + 30 * j, 20, 20)
                    if checkbox.collidepoint(event.pos):
                        goal["completed"] = not goal["completed"]
                        if goal["completed"]:
                            goals_to_remove.append((category, j))

        for cat, index in reversed(goals_to_remove):
            del health_goals[cat][index]
            needs_refresh = True

        add_button = draw_button(screen, GRAY, x_offset + column_width - 160, y_offset_cat, 100, 30, "Add Goal")

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if add_button.collidepoint(event.pos):
                    input_rect = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() // 2 - 25, 300, 50)
                    new_goal = get_user_input(screen, input_rect)
                    if new_goal:
                        health_goals[category].append({"text": new_goal, "completed": False})
                        needs_refresh = True
                if category_rect.collidepoint(event.pos):
                    print(f"Clicked on {category} category")

    all_completed = True
    for category in categories:
        for goal in health_goals[category]:
            if not goal["completed"]:
                all_completed = False
                break
        if not all_completed:
            break

    if all_completed and len([item for sublist in health_goals.values() for item in sublist]) > 0:
        token = True
        coins += 1
        draw_text("All goals completed! You earned a token!", small_font, GREEN, screen, screen.get_width() // 2 - 150, screen.get_height() - 50)
        puzzle_button = draw_button(screen, GREEN, screen.get_width() - 150, screen.get_height() - 60, 140, 50, "Color Puzzle")
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if puzzle_button.collidepoint(event.pos):
                    print("Go to color puzzle page")
    else:
        token = False
    return token, coins