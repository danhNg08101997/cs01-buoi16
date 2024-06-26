import pygame, random
from models.Constant import Status, Direction, arr_random_status_soldier
from models.Bullet import Bullet

class Soldier:
    def __init__(self) -> None:
        self.image = pygame.image.load('./images/left/soldier/freeze/0.png')
        self.rect = self.image.get_rect()
        self.status = Status.freeze
        self.direction = Direction.left # True phải, False: trái
        self.frame = 0
        self.time_frame_start = 0
        self.time_change_status = 0
        self.speed = 2
        self.time_attack = 0
        self.lst_bullet:list[Bullet] = []
    
    def draw(self, screen,hero):
        if hero.rect.x > self.rect.x:
            self.direction = Direction.right
        else:
            self.direction = Direction.left
        # Thay đổi trạng thái
        current_change_status = pygame.time.get_ticks()
        if current_change_status - self.time_change_status >= 1000:
            status = random.choice(arr_random_status_soldier)
            self.status = status
            self.time_change_status = current_change_status
        if self.status == Status.move:
            self.move()
        elif self.status == Status.attack:
            current_time_attack = pygame.time.get_ticks()
            if current_time_attack - self.time_attack >= 1000:
                self.attack()
                self.time_attack = current_time_attack
        for bullet in self.lst_bullet:
            bullet.draw(screen)
            bullet.move()
            if bullet.rect.x > screen.get_width() or bullet.rect.x < 0:
                self.lst_bullet.remove(bullet)
            if bullet.rect.colliderect(hero.rect):
                hero.live -= 1
                self.lst_bullet.remove(bullet)
        self.update_status()
        
        # Thay đổi frame của trạng thái
        time_frame_current = pygame.time.get_ticks()
        if time_frame_current - self.time_frame_start >= 300:
            self.frame += 1
            self.time_frame_start = time_frame_current
        self.update_status()
        screen.blit(self.image, self.rect)
    
    def update_status(self):
        img_source = ''
        direction = 'left'
        if self.direction == Direction.left:
            direction = 'left'
        elif self.direction == Direction.right:
            direction = 'right'
        if self.status == Status.freeze: #freeze
            img_source = f'./images/{direction}/soldier/freeze/{self.frame%4}.png'
        elif self.status == Status.attack: #attack
            img_source = f'./images/{direction}/soldier/attack/{self.frame%5}.png'
        elif self.status == Status.move: #move
            img_source = f'./images/{direction}/soldier/move/{self.frame%7}.png'
        elif self.status == Status.die: #die
            if direction == 'left':
                img_source = f'./images/{direction}/soldier/die/{self.frame%15}.png'
            elif direction == 'right':
                img_source = f'./images/{direction}/soldier/die/{self.frame%9}.png'
        self.image = pygame.image.load(img_source)
    
    def move(self):
        self.status = Status.move
        if self.direction == Direction.left:
            self.rect.x -= self.speed
        elif self.direction == Direction.right:
            self.rect.x += self.speed
    
    def attack(self):
        # Thay đổi trạng thái thành bắn
        self.status = Status.attack
        # Tạo ra đạn đưa vào lst_bullet
        new_bullet = Bullet(bullet_type=1, speed=5)
        self.lst_bullet.append(new_bullet)
        if self.direction == Direction.left:
            new_bullet.rect.x = self.rect.x
            new_bullet.rect.y = self.rect.y + self.rect.height/2
        elif self.direction == Direction.right:
            new_bullet.rect.x = self.rect.x + self.rect.width
            new_bullet.rect.y = self.rect.y + self.rect.height/2