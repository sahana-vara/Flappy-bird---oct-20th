import pygame
from random import randint
pygame.init()

pygame.display.set_caption("Car OOPs") 
width=600
height=600
screen=pygame.display.set_mode((width,height))

coin=pygame.image.load("/Users/sahana/Desktop/Home /coding - python projects/Homework oct 20th/assets/money.png")
x=randint(0,600)
y=randint(0,600)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/sahana/Desktop/Home /coding - python projects/Homework oct 20th/assets/car.png")
        #self.image=pygame.image.transform.scale(self.image,(80,50))
        self.rect=self.image.get_rect()

    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)

sprites=pygame.sprite.Group()

def start_game():
    player=Car()
    sprites.add(player)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        pressed_keys=pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.blit(coin,(x,y))
        if coin.colliderect(player):
            print("You win!")
        sprites.draw(screen)
        pygame.display.update()

start_game()