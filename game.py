import pygame, sys

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

# Tạo vòng lặp game
running = True
while running:
    # FPS 60s/screen
    clock.tick(60)
    
    screen.fill((255,255,255))
    for event in pygame.event.get():
        # Xử lý thoát game
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    
pygame.quit()
sys.exit()