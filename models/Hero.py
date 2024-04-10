import pygame
from models.Constant import Status, Direction
from models.Bullet import Bullet

class Hero:
    def __init__(self) -> None:
        self.image = pygame.image.load('./images/right/hero/freeze/0.png')
        self.rect = self.image.get_rect()
        self.status = Status.freeze
        self.direction = Direction.right # True phải, False: trái
        self.frame = 0
        self.time_frame_start = 0
        self.speed = 5
        self.live = 5
        self.score = 0
        self.lst_bullet:list[Bullet] = []
        # Set up sự kiện nhảy
        self.speed_jump = -15 #Tốc độ nhảy
        self.gravity = 0.5 #Trọng lực 5
        self.jump_velocity = 0 #Vận tốc nhảy ban đầu
        self.jumping = False #Trạng thái đang nhảy
    
    def draw(self, screen:pygame.Surface):
        # Xử lý nhảy
        if self.jumping:
            self.jump_velocity += self.gravity
            self.rect.y += self.jump_velocity
            # chạm đất
            if self.rect.y > screen.get_height() - 250:
                self.jumping = False
                self.jump_velocity = 0
        # Load đạn
        for bullet in self.lst_bullet:
            bullet.draw(screen)
            bullet.move()
            if bullet.rect.x > screen.get_width() or bullet.rect.x < 0:
                self.lst_bullet.remove(bullet)
        
        # Thay đổi trạng thái
        time_frame_current = pygame.time.get_ticks()
        if time_frame_current - self.time_frame_start >= 300:
            self.frame += 1
            self.time_frame_start = time_frame_current
        self.update_status()
        # render mạng lên vị trí màn hình
        f_game = pygame.font.Font(None,48)
        title_live = f_game.render(f'Live: {self.live}', True, 'red')
        # Render điểm
        title_score = f_game.render(f'Score: {self.score}', True, 'red')
        screen.blit(title_live, (0,0))
        screen.blit(title_score, (screen.get_width() - title_score.get_width(),0))
        screen.blit(self.image, self.rect)
    
    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.jump_velocity = self.speed_jump
    
    def update_status(self):
        img_source = ''
        direction = 'right'
        if self.direction == Direction.left:
            direction = 'left'
        elif self.direction == Direction.right:
            direction = 'right'
        if self.status == Status.freeze: #freeze
            img_source = f'./images/{direction}/hero/freeze/{self.frame%3}.png'
        elif self.status == Status.attack: #attack
            img_source = f'./images/{direction}/hero/attack/{self.frame%4}.png'
        elif self.status == Status.move: #move
            img_source = f'./images/{direction}/hero/move/{self.frame%4}.png'
        elif self.status == Status.die: #die
            img_source = f'./images/{direction}/hero/die/{self.frame%19}.png'
        self.image = pygame.image.load(img_source)
    
    def move(self, direction):
        self.status = Status.move
        self.direction = direction
        if self.direction == Direction.left:
            self.rect.x -= self.speed
        elif self.direction == Direction.right:
            self.rect.x += self.speed
    
    def attack(self):
        # Thay đổi trạng thái thành bắn
        self.status = Status.attack
        # Tạo ra 1 viên đạn theo hướng của hero
        new_bullet = Bullet()
        new_bullet.direction = self.direction
        if self.direction == Direction.left:
            new_bullet.rect.x = self.rect.x
            new_bullet.rect.y = self.rect.y + self.rect.height / 2 - 15
        elif self.direction == Direction.right:
            new_bullet.rect.x = self.rect.x + self.rect.width
            new_bullet.rect.y = self.rect.y + self.rect.height / 2 - 15
        # Đưa đạn vào list
        self.lst_bullet.append(new_bullet)