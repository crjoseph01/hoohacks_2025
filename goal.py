# goal.py
import pygame
import sys

# Initialize Pygame font module
pygame.font.init()
pygame.init()

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

def get_user_input(screen, input_rect, hide_rects):
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

        for rect in hide_rects:
            pygame.draw.rect(screen, WHITE, rect)

        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, BLACK)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()
        clock.tick(60)

def health_goals_scene(screen, health_goals, token):
    screen.fill(WHITE)
    draw_text("Health Goals", small_font, BLACK, screen, screen.get_width() // 2 - 80, 20)

    categories = ["fitness", "eating", "mental health"]
    column_width = screen.get_width() // 3
    y_offset = 60
    needs_refresh = False

    event_list = pygame.event.get()

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
                    hide_rects = []
                    #correct hide rect calculation.
                    for k, rect in enumerate(category_rects):
                        if k != i:
                            hide_rects.append(pygame.Rect(rect.x - 10, 0, column_width, input_rect.y - 10)) #changed height.
                            hide_rects.append(pygame.Rect(rect.x - 10, input_rect.bottom + 10, column_width, screen.get_height()))

                    new_goal = get_user_input(screen, input_rect, hide_rects)
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
        draw_text("All goals completed! You earned a token!", small_font, GREEN, screen, screen.get_width() // 2 - 150, screen.get_height() - 50)
        puzzle_button = draw_button(screen, GREEN, screen.get_width() - 150, screen.get_height() - 60, 140, 50, "Color Puzzle")
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if puzzle_button.collidepoint(event.pos):
                    print("Go to color puzzle page")
    else:
        token = False
    if needs_refresh:
        return token
    else:
        return token