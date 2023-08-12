import pygame

#Set SCALAR to 1 for smaller screens and 2 for larger screens
SCALAR = 1

WIDTH, HEIGHT = 400*SCALAR, 400*SCALAR
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
GREEN = (0, 255, 0)

WHITE_CROWN = pygame.transform.scale(pygame.image.load('assets/crown2.png'), (22*SCALAR, 12.5*SCALAR))
RED_CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (22*SCALAR, 12.5*SCALAR))
