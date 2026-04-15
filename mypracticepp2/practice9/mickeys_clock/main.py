import pygame
import math
from clock import MickeyClock

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 70)

mickey = MickeyClock("images/mickey_hand.png")

running = True
while running:
    screen.fill((240, 240, 240))

    center = (WIDTH // 2, HEIGHT // 2)

    #  большой круг
    pygame.draw.circle(screen, (200, 200, 200), center, 300)
    pygame.draw.circle(screen, (0, 0, 0), center, 300, 6)

    #  красные цифры
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = center[0] + 240 * math.cos(angle)
        y = center[1] + 240 * math.sin(angle)

        text = font.render(str(i), True, (255, 0, 0))
        screen.blit(text, (x - 20, y - 20))

    #  центр
    pygame.draw.circle(screen, (0, 0, 0), center, 12)

    #  стрелки
    mickey.draw(screen, center)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(1)

pygame.quit()