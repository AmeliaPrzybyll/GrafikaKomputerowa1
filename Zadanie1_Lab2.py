import pygame
import sys
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadnie 1")
clock = pygame.time.Clock()
running = True
dt = 0

# Deklarowanie kolorów
NIEBIESKI = (0, 0, 255)

N = 9  # Liczba boków dziewięciokąta
R = 150  # Promień koła
CENTER = (300, 300)

def draw_polygon(screen, center, n, rx, ry, rotation=0, offset_x=0, offset_y=0):
    points = []
    for i in range(n):
        angle = 2 * math.pi * i / n + math.radians(rotation)
        x = center[0] + int(rx * math.cos(angle))
        y = center[1] + int(ry * math.sin(angle))
        points.append((x, y))
    
    # Dodanie przesunięcia dla lewego górnego rogu i prawego dolnego rogu
    points[0] = (points[0][0] - offset_x, points[0][1] - offset_y)
    points[-1] = (points[-1][0] + offset_x, points[-1][1] + offset_y)

    pygame.draw.polygon(screen, NIEBIESKI, points)

def shear_polygon(color, center, size, shear_amount_x, shear_amount_y):
    n = 9
    angle = 360 / n
    coordinates = []
    for i in range(n):
        x = center[0] + size * math.cos(math.radians(i * angle))
        y = center[1] + size * math.sin(math.radians(i * angle))
        x_sheared = x + shear_amount_x * (y - center[1]) / size
        y_sheared = y + shear_amount_y * (x - center[0]) / size
        coordinates.append((x_sheared, y_sheared))
    return coordinates

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((255, 255, 255))

    # Obsługa klawiszy numerycznych 1-9
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:  # Przywrócenie początkowych ustawień
        draw_polygon(win, CENTER, N, R, R)
    elif keys[pygame.K_2]:  # Powiększony i obrócony o 45 stopni
        side_length = 180
        rotated_center = CENTER
        rotated_points = []
        for i in range(N):
            angle = 2 * math.pi * i / N + math.radians(45)  # Obrót o 45 stopni
            x = rotated_center[0] + int(side_length * math.cos(angle))
            y = rotated_center[1] + int(side_length * math.sin(angle))
            rotated_points.append((x, y))
        pygame.draw.polygon(win, NIEBIESKI, rotated_points)
    elif keys[pygame.K_3]:  # Obrócenie do góry nogami
        draw_polygon(win, CENTER, 9, R * 0.8, R * 1.2, rotation=180)
    elif keys[pygame.K_4]:  # Przesunięcie lewego górnego rogu i prawego dolnego rogu
        points = shear_polygon(NIEBIESKI, CENTER, R, 50, 0)
        pygame.draw.polygon(win, NIEBIESKI, points, 0)
    elif keys[pygame.K_5]:  # Przesunięcie na góre i spłaszczenie
        draw_polygon(win, (300,125), N, R*1.2, R*0.8)   
    elif keys[pygame.K_6]: # Obrócenie przycisku 4
        points = shear_polygon(NIEBIESKI, CENTER, R, 50, 0)
        surface = pygame.Surface((600, 600), pygame.SRCALPHA)
        pygame.draw.polygon(surface, NIEBIESKI, points, 0)
        rotated_surface = pygame.transform.rotate(surface, 45)
        rotated_rect = rotated_surface.get_rect(center=(300, 300))
        win.blit(rotated_surface, rotated_rect)
    elif keys[pygame.K_7]: # odwrócenie o 180 stopni i spłaszczenie
        points = shear_polygon(NIEBIESKI, CENTER, R * 0.6, R * 1.4, 0)
        surface = pygame.Surface((600, 600), pygame.SRCALPHA)
        pygame.draw.polygon(surface, NIEBIESKI, points, 0)
        rotated_surface = pygame.transform.rotate(surface, 180)
        rotated_rect = rotated_surface.get_rect(center=(300, 300))
        win.blit(rotated_surface, rotated_rect)
    elif keys[pygame.K_8]:  # Obrót pierwszego wielokąta o 30 stopni
        side_length = 180
        rotated_center = CENTER
        rotated_points = []
        for i in range(N):
            angle = 2 * math.pi * i / N + math.radians(30) 
            x = rotated_center[0] + int(side_length * math.cos(angle))
            y = rotated_center[1] + int(side_length * math.sin(angle))
            rotated_points.append((x, y))
        pygame.draw.polygon(win, NIEBIESKI, rotated_points)
    elif keys[pygame.K_9]:
        points = shear_polygon(NIEBIESKI, CENTER, R, 50, 0)
        surface = pygame.Surface((600, 600), pygame.SRCALPHA)
        pygame.draw.polygon(surface, NIEBIESKI, points, 0)
        rotated_surface = pygame.transform.rotate(surface, 45)
        rotated_rect = rotated_surface.get_rect(center=(300, 300))
        win.blit(rotated_surface, rotated_rect)

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()
