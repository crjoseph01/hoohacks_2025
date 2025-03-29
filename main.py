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
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

button_color = (0, 255, 0)
button_rect = pygame.Rect(300, 250, 200, 50)  # (x, y, width, height)

habits = {"Exercise": 0, "Reading": 0, "Meditation": 0}
habit_buttons = []

# Create button positions
for i, habit in enumerate(habits):
    rect = pygame.Rect(300, 150 + (i * 100), 200, 50)
    habit_buttons.append((habit, rect))
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Habit Tracker Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def get_reward(points):
    if points >= 10:
        return "Gold Medal!"
    elif points >= 5:
        return "Silver Medal!"
    return "Bronze Medal!"
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    # Draw button
    pygame.draw.rect(screen, button_color, button_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):  # Check if button clicked
                print("Habit Completed!")  # Replace with habit tracking logic
    
    for habit, rect in habit_buttons:
        pygame.draw.rect(screen, (0, 255, 0), rect)
        font = pygame.font.Font(None, 36)
        text = font.render(f"{habit}: {habits[habit]}", True, (255, 255, 255))
        screen.blit(text, (rect.x + 10, rect.y + 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for habit, rect in habit_buttons:
                if rect.collidepoint(event.pos):
                    habits[habit] += 1  # Increment habit count
    
    reward_text = font.render(get_reward(habits["Exercise"]), True, (255, 0, 0))
    screen.blit(reward_text, (500, 500))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()