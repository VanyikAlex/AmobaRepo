import pygame

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Amőba")

letterX = pygame.image.load('AmobaRepo\Játék\proj\images')


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    window.fill((0, 0, 0))
    window.blit(letterX, (0, 0))
    pygame.display.flip()