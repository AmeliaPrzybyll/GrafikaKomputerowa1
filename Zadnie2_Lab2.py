import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2")
clock = pygame.time.Clock()
running = True

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Rysowanie kwadratu
square_size = 80
square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
pygame.draw.rect(square_surface, YELLOW, (0, 0, square_size, square_size))


# Rysowanie czarnego koła
circle_radius = 80
circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, BLACK, (circle_radius, circle_radius), circle_radius)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((255, 255, 255)) 

   
    win.blit(circle_surface, (200, 230))
    win.blit(square_surface, (240, 260))
    
    

    pygame.display.flip() 
    clock.tick(60) 

pygame.quit()
sys.exit()
