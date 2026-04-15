import pygame
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 40)

player = MusicPlayer()

running = True
while running:
    screen.fill((220, 220, 220))

    # 🎵 текст
    text = font.render(f"Track: {player.current}", True, (0, 0, 0))
    screen.blit(text, (150, 120))

    # 📋 подсказки
    controls = [
        "P - Play",
        "S - Stop",
        "N - Next",
        "B - Previous",
        "Q - Quit"
    ]

    for i, line in enumerate(controls):
        txt = font.render(line, True, (50, 50, 50))
        screen.blit(txt, (10, 10 + i * 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.prev()

            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()