import pygame, sys
from models.Hero import Hero
from models.Constant import Direction, Status

# Khởi tạo game
pygame.init()

# Set up chiều dài, chiều rộng khung hình
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Khởi tạo màn hình game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Tiêu đề game
pygame.display.set_caption('Metal Slug')

# Set up bộ đếm thời gian
clock = pygame.time.Clock()

# Tạo đối tượng hero từ class Hero
hero = Hero()
hero.rect.y = SCREEN_HEIGHT - 250

# Tạo background
bg_game = pygame.image.load('./images/bkgd.png')
bg_game = pygame.transform.scale(bg_game, (bg_game.get_width(), SCREEN_HEIGHT))
bg_rect = bg_game.get_rect()
x_scroll = bg_rect.x

# Tạo vòng lặp game
running = True
while running:
    # FPS 60s/screen
    clock.tick(60)
    
    for event in pygame.event.get():
        # Xử lý thoát game
        if event.type == pygame.QUIT:
            running = False
    # Start - Hero di chuyển
    key = pygame.key.get_pressed()
    if key[pygame.K_d] and x_scroll > - (bg_game.get_width() - SCREEN_WIDTH):
        hero.move(Direction.right)
        x_scroll -= hero.speed * 2.5
    elif key[pygame.K_a] and x_scroll < 0:
        hero.move(Direction.left)
        x_scroll += hero.speed * 2.5
    # Start - Hero tấn công
    elif key[pygame.K_j]: #j là phím bắn
        hero.attack()
    # End - Hero tấn công
    else:
        hero.status = Status.freeze
    # End - Hero di chuyển
    
    screen.blit(bg_game, (x_scroll, bg_rect.x))
    hero.draw(screen)
    pygame.display.flip()
    
pygame.quit()
sys.exit()