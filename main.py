import pygame
from pygame import sprite, transform, key, image

class Personajes(sprite.Sprite):
    def __init__(self, image_path, x, y, controlable=True):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image_path), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.controlable = controlable

    def update(self, paredes):
        if self.controlable:
            keys = key.get_pressed()

            movimiento_x = 0
            movimiento_y = 0

            if (keys[pygame.K_LEFT]or keys[pygame.K_a]) and self.rect.x > 0:
                movimiento_x -= 3
            if (keys[pygame.K_RIGHT]or keys[pygame.K_d]) and self.rect.x < screen.get_width() - self.rect.width:
                movimiento_x += 3
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.y > 0:
                movimiento_y -= 3
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.y < screen.get_height() - self.rect.height:
                movimiento_y += 3

            position_x = self.rect.x
            self.rect.x += movimiento_x
            if self.check_collision(paredes):
                self.rect.x = position_x

            position_y = self.rect.y
            self.rect.y += movimiento_y
            if self.check_collision(paredes):
                self.rect.y = position_y

    def check_collision(self, paredes):
        for pared in paredes:
            if self.rect.colliderect(pared.rect):
                return True
        return False

class Pared:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)

    def dibujar(self):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

class Enemigo(Personajes):
    def __init__(self, image_path, x, y, punto_inicial, punto_final, movimiento):
        super().__init__(image_path, x, y, controlable=False)
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
        self.velocidad = 2
        self.movimiento = movimiento

    def mover_verticalmente(self):
        self.rect.y += self.velocidad
        if self.rect.y <= self.punto_inicial or self.rect.y >= self.punto_final:
            self.velocidad *= -1

    def mover_horizontalmente(self):
        self.rect.x += self.velocidad
        if self.rect.x <= self.punto_inicial or self.rect.x >= self.punto_final:
            self.velocidad *= -1

    def update(self, _):
        if self.movimiento == 'vertical':
            self.mover_verticalmente()
        elif self.movimiento == 'horizontal':
            self.mover_horizontalmente()


def mostrar_pantalla_perdida():
    pantalla_perdida = transform.scale(image.load(loss_image_path), (800, 600))
    screen.blit(pantalla_perdida, (0, 0))
    pygame.display.flip()
    pygame.time.wait(3000)

def mostrar_pantalla_ganada():
    pantalla_ganada = transform.scale(image.load(win_image_path), (800,600))
    screen.blit(pantalla_ganada,(0,0))
    pygame.display.flip()
    pygame.time.wait(3000)


# Ejemplo de uso
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

personaje_image_path = "hero.png"
enemies_image_path ="pac-1.png"
enemies2_image_path = "cyborg.png"
loss_image_path = "game-over-3.jpg"
win_image_path = "winner.jpg"

personaje1 = Personajes(personaje_image_path, 50, 30, controlable=True)
objeto = Personajes("football.png",770,550,controlable=False)
enemigo1 = Enemigo(enemies_image_path, 430,560,100,570,movimiento='vertical')
enemigo2 = Enemigo(enemies2_image_path,390,100,100,570, movimiento='vertical')
enemigo3 = Enemigo(enemies2_image_path,270,40,10,140, movimiento='vertical')
enemigo4 = Enemigo(enemies2_image_path,10,90,10,260,movimiento='horizontal')
enemigo5 = Enemigo(enemies2_image_path,10,340,10,200,movimiento='horizontal')
enemigo6 = Enemigo(enemies2_image_path,140,175,140,330,movimiento='horizontal')
enemigo7 = Enemigo(enemies2_image_path,10,425,10,330,movimiento='horizontal')
enemigo9 = Enemigo(enemies2_image_path,30,410,410,570,movimiento='vertical')
enemigo11 = Enemigo(enemies2_image_path,310,40,310,770,movimiento='horizontal')
enemigo12 = Enemigo(enemies2_image_path,750,10,10,130,movimiento='vertical')
enemigo13 = Enemigo(enemies2_image_path,470,90,470,770,movimiento='horizontal')
enemigo14 = Enemigo(enemies2_image_path,490,100,100,210,movimiento='vertical')
enemigo15 = Enemigo(enemies2_image_path,490,160,490,770,movimiento='horizontal')
enemigo16 = Enemigo(enemies2_image_path,750,170,170,280,movimiento='vertical')
enemigo17 = Enemigo(enemies2_image_path,490,250,490,770,movimiento='horizontal')
enemigo18 = Enemigo(enemies2_image_path,490,260,260,360,movimiento='vertical')
enemigo19 = Enemigo(enemies2_image_path,490,330,490,770,movimiento='horizontal')
enemigo20 = Enemigo(enemies2_image_path,750,330,330,460,movimiento='vertical')
enemigo21 = Enemigo(enemies2_image_path,490,450,490,770,movimiento='horizontal')
enemigo22 = Enemigo(enemies2_image_path,490,420,420,570,movimiento='vertical')
enemigos=[enemigo1,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7
,enemigo9,enemigo11,enemigo12,enemigo13,enemigo14,enemigo15
,enemigo16,enemigo17,enemigo18,enemigo19,enemigo20,enemigo21,enemigo22]
pared1 = Pared(0,0,10,600)
pared2 = Pared(0,590,800,10)
pared3 = Pared(0,0,800,10)
pared4 = Pared(790,0,10,500)
pared5 = Pared(0,80,200,10)
pared6 = Pared(300,0,10,160)
pared7 = Pared(130,160,240,10)
pared8 = Pared(130,160,10,180)
pared9 = Pared(370,160,10,335)
pared10 = Pared(100,485,270,10)
pared11 = Pared(465,80,10,510)
pared12 = Pared(370,80,330,10)
pared13 = Pared(560,150,230,10)
pared14 = Pared(470,230,230,10)
pared15 = Pared(560,310,230,10)
pared16 = Pared(470,400,230,10)
pared17 = Pared(560,490,230,10)
pared18 = Pared(0,400,230,10)
pared19 = Pared(220,230,10,170)
pared20 = Pared(220,230,90,10)
pared21 = Pared(270,280,100,10)
pared22 = Pared(220,320,100,10)
pared23 = Pared(270,360,100,10)
pared24 = Pared(220,400,100,10)
pared25 = Pared(100,530,25,70)
pared26 = Pared(155,490,25,70)
pared27 = Pared(210,530,25,70)
pared28 = Pared(265,490,25,70)
pared29 = Pared(325,530,25,70)
pared30 = Pared(560,500,25,60)
pared31 = Pared(615,530,25,70)
pared32 = Pared(670,500,25,60)
pared33 = Pared(725,530,25,70)
pared34 = Pared(50,160,90,10)
pared35 = Pared(0,200,100,10)
pared36 = Pared(50,240,90,10)
pared37 = Pared(0,280,100,10)
pared38 = Pared(50,330,90,10)
pared39 = Pared(180,230,50,10)
pared40 = Pared(130,270,50,10)
pared41 = Pared(180,310,50,10)
pared42 = Pared(130,270,50,10)

all_sprites = pygame.sprite.Group()
all_sprites.add(personaje1)
all_sprites.add(objeto)
all_sprites.add(enemigo1)
all_sprites.add(enemigo2)
all_sprites.add(enemigo3)
all_sprites.add(enemigo4)
all_sprites.add(enemigo5)
all_sprites.add(enemigo6)
all_sprites.add(enemigo7)
all_sprites.add(enemigo9)
all_sprites.add(enemigo11)
all_sprites.add(enemigo12)
all_sprites.add(enemigo13)
all_sprites.add(enemigo14)
all_sprites.add(enemigo15)
all_sprites.add(enemigo16)
all_sprites.add(enemigo17)
all_sprites.add(enemigo18)
all_sprites.add(enemigo19)
all_sprites.add(enemigo20)
all_sprites.add(enemigo21)
all_sprites.add(enemigo22)
paredes=[pared1,pared2,pared3,pared4,pared5,pared6,pared7,pared8
,pared9,pared10,pared11,pared12,pared13,pared14,pared15,pared16
,pared17,pared18,pared19,pared20,pared21,pared22,pared23,pared24,pared25
,pared26,pared27,pared28,pared29,pared30,pared31,pared32,pared33,pared34
,pared35,pared36,pared37,pared38,pared39,pared40,pared41,pared42]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    all_sprites.update(paredes)
    for pare in paredes:
        if personaje1.rect.colliderect(pare.rect):
            mostrar_pantalla_perdida()
    for enemigo in enemigos:
        if personaje1.rect.colliderect(enemigo):
            mostrar_pantalla_perdida()
            running=False
    if personaje1.rect.colliderect(objeto.rect):
        mostrar_pantalla_ganada()
        running=False
    screen.fill((255, 255, 255))
    for pared in paredes:
        pared.dibujar()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(100)
    

pygame.quit()
