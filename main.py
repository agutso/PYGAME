import pygame
from pygame import sprite, transform, key, image

class Car(sprite.Sprite):
    def __init__(self, image_path, x, y):  # Cambiado el nombre de la variable
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image_path), (80, 80))  # Utilizamos el nuevo nombre
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and self.rect.x < screen.get_width() - self.rect.width:
            self.rect.x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]  or keys[pygame.K_s] and self.rect.y < screen.get_height() - self.rect.height:
            self.rect.y += 5
        if keys[pygame.K_x]:
            pygame.quit()


# Ejemplo de uso
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

car_image_path = "cyborg.png" 

car = Car(car_image_path, 100, 100)

all_sprites = pygame.sprite.Group()
all_sprites.add(car)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(100)


pygame.quit()