import pygame
from models.Constant import Direction

class Bullet:
    def __init__(self) -> None:
        self.image = pygame.image.load('./images/bullet/0.png')
        self.rect = self.image.get_rect()
        self.direction = Direction.left
        self.speed = 10
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        if self.direction == Direction.left:
            self.rect.x -= self.speed
        elif self.direction == Direction.right:
            self.rect.x += self.speed