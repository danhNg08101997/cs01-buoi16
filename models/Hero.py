import pygame
from models.Constant import Status, Direction

class Hero:
    def __init__(self) -> None:
        self.image = pygame.image.load('./images/right/hero/freeze/0.png')
        self.rect = self.image.get_rect()
        self.status = Status.freeze
        self.direction = Direction.right # True phải, False: trái
        self.frame = 0
        self.time_frame_start = 0
        self.speed = 1
    
    def draw(self, screen):
        time_frame_current = pygame.time.get_ticks()
        if time_frame_current - self.time_frame_start >= 300:
            self.frame += 1
            self.time_frame_start = time_frame_current
        self.update_status()
        screen.blit(self.image, self.rect)
    
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