import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2")
clock = pygame.time.Clock()
running = True

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Rysowanie okegu
circle_radius = 100
circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, BLACK, (circle_radius, circle_radius), circle_radius)

# Rysowanie kwadratu
square_size = 80
square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
pygame.draw.rect(square_surface, YELLOW, (0, 0, square_size, square_size))

# Obliczanie współrzędnych 
square_offset_x = circle_radius - square_size // 2
square_offset_y = circle_radius - square_size // 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((255, 255, 255))  

    # Wyśrodkowanie okręgu
    center_x = win.get_width() // 2
    center_y = win.get_height() // 2

    # Rysowanie okręgu i kwadratu
    win.blit(circle_surface, (center_x - circle_radius, center_y - circle_radius))
    win.blit(square_surface, (center_x - square_size // 2, center_y - square_size // 2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
