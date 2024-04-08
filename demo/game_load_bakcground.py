import pygame, sys

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Metal Slug')
clock = pygame.time.Clock()
bg_game = pygame.image.load('./images/bkgd.png')
bg_game = pygame.transform.scale(bg_game, (bg_game.get_width(), SCREEN_HEIGHT))
bg_rect = bg_game.get_rect()
x_scroll = bg_rect.x
running = True
while running:
    # FPS 60s/screen
    clock.tick(60)
    for event in pygame.event.get():
        # Xử lý thoát game
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        x_scroll -= 10
    elif key[pygame.K_a]:
        x_scroll += 10
    screen.blit(bg_game, (x_scroll, bg_rect.y))
    pygame.display.flip()

pygame.quit()
sys.exit()