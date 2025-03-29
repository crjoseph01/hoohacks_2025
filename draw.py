# color_puzzle.py
import pygame
import sys
import os

pygame.init()

# Application Size
WIDTH, HEIGHT = 800, 600

# Colors (Adjust as needed)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
PINK = (255, 192, 203)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BEIGE = (245, 245, 220)
LIGHT_BLUE = (173, 216, 230)

# Color Palette (Adjust to match your image)
palette = {
    1: GREEN,
    2: PINK,
    3: BLUE,
    4: YELLOW,
    5: BEIGE,
    6: LIGHT_BLUE,
    7: BLACK,
    8: WHITE,
}

def color_puzzle_scene(screen):
    # Image Loading - Using relative path
    image_path = "puzzle_frog.png"

    if os.path.exists(image_path):
        print(f"Image found at: {image_path}")
        try:
            puzzle_image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f"Error loading image: {e}")
            sys.exit()
    else:
        print(f"Image not found at: {image_path}")
        sys.exit()

    # Scale the image to fit within the application size
    image_width, image_height = puzzle_image.get_size()
    scale_factor = min((WIDTH - 100) / image_width, HEIGHT / image_height)
    puzzle_image = pygame.transform.scale(puzzle_image, (int(image_width * scale_factor), int(image_height * scale_factor)))

    # Color Selection Boxes
    color_boxes = []
    box_width = 50
    box_height = 50
    box_x = WIDTH - 90
    box_y = 50

    for color_num, color in palette.items():
        color_rect = pygame.Rect(box_x, box_y, box_width, box_height)
        color_boxes.append((color_rect, color_num))
        box_y += box_height + 10

    current_color = None

    running = True
    pixels = pygame.PixelArray(puzzle_image)
    color_area_size = 9

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    for color_rect, color_num in color_boxes:
                        if color_rect.collidepoint(mouse_pos):
                            current_color = color_num
                            break
                    else:
                        if current_color is not None:
                            try:
                                clicked_pixel = puzzle_image.get_at(mouse_pos)
                                if clicked_pixel in palette.values():
                                    for x in range(-color_area_size, color_area_size + 1):
                                        for y in range(-color_area_size, color_area_size + 1):
                                            try:
                                                pixels[mouse_pos[0] + x, mouse_pos[1] + y] = palette[current_color]
                                            except IndexError:
                                                pass
                            except IndexError:
                                pass

        del pixels
        screen.fill(WHITE)
        screen.blit(puzzle_image, (0, 0))

        for color_rect, color_num in color_boxes:
            pygame.draw.rect(screen, palette[color_num], color_rect)
            pygame.draw.rect(screen, BLACK, color_rect, 2)
            font = pygame.font.Font(None, 36)
            number_text = font.render(str(color_num), True, BLACK)
            screen.blit(number_text, (color_rect.x + 15, color_rect.y + 10))

        pygame.display.flip()
        pixels = pygame.PixelArray(puzzle_image)

    del pixels
    pygame.quit()
    sys.exit()