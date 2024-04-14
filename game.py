import pygame, sys, random
from models.Hero import Hero
from models.Constant import Direction, Status
from models.Soldier import Soldier

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

# Tạo background
bg_game = pygame.image.load('./images/bkgd.png')
bg_game = pygame.transform.scale(bg_game, (bg_game.get_width(), SCREEN_HEIGHT))
bg_rect = bg_game.get_rect()
x_scroll = bg_rect.x

# Tạo list soldier cứ mỗi 5 giây thì sẽ append lính vào
arr_soldier: list[Soldier] = []
time_render_soldier_start = 0

# Thời gian bắt đầu chết
time_start_die = 0

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
    elif key[pygame.K_j]: #jjj là phím bắn
        hero.attack()
    # End - Hero tấn công
    else:
        hero.status = Status.freeze
    if key[pygame.K_k]:
        hero.jump()
    # End - Hero di chuyển
    
    # Render background
    screen.blit(bg_game, (x_scroll, bg_rect.x))
    # Random soldier ngẫu nhiên xuất hiện
    current_time_render_soldier = pygame.time.get_ticks()
    if current_time_render_soldier - time_render_soldier_start >= 5000:
        # Tạo lính
        new_soldier = Soldier()
        new_soldier.rect.y = SCREEN_HEIGHT - 250
        new_soldier.rect.x = random.randint(0, 2000)
        if new_soldier.rect.x > hero.rect.x:
            new_soldier.direction = Direction.left
        # Đưa soldier vào list
        arr_soldier.append(new_soldier)
        # gán lại mốc thời gian
        time_render_soldier_start = current_time_render_soldier
    # Render soldier
    for soldier in arr_soldier:
        soldier.draw(screen, hero)
    # Xử lý hero và soldier
    for bullet_hero in hero.lst_bullet:
        for soldier in arr_soldier:
            if bullet_hero.rect.colliderect(soldier.rect) and soldier.status != Status.die:
                soldier.status = Status.die
                hero.lst_bullet.remove(bullet_hero)
                hero.score += 10
    # Xử lý 3 giây cho nhân vật khi chết
    time_current_die = pygame.time.get_ticks()
    if time_current_die - time_start_die > 3000:
        # Xử lý chết
        for soldier in arr_soldier:
            if soldier.status == Status.die:
                arr_soldier.remove(soldier)
        # Gán lại mốc thời gian chết
        time_start_die = time_current_die
    
    # Render hero
    hero.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()