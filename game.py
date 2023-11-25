from pygame import *
window = display.set_mode((700, 500)) 
display.set_caption("TECLAS PRUEBA") 
 
height = 40 
width = 40 
 
x = 5 
y = 500 - height - 5 
 
character = draw.rect(window, (0, 0, 255), (x, y, width, height)) 
display.update() 
 
moving_left = False 
moving_right = False 
moving_up = False 
moving_down = False

tecla_a = False
tecla_d = False
tecla_w = False
tecla_S = False
 
running = True 
 
while running: 
    time.delay(50) 
 
    for e in event.get(): 
        if e.type == QUIT: 
            running = False 
        elif e.type == KEYDOWN: 
            if e.key == K_LEFT: 
                moving_left = True
            elif e.key == K_a:
                tecla_a = True
            elif e.key == K_RIGHT: 
                moving_right = True
            elif e.key == K_d:
                tecla_d = True
            elif e.key == K_UP: 
                moving_up = True
            elif e.key == K_w:
                tecla_w = True
            elif e.key == K_DOWN: 
                moving_down = True
            elif e.key == K_s:
                tecla_S = True
            elif e.key == K_x: 
                running = False 
        elif e.type == KEYUP: 
            if e.key == K_LEFT: 
                moving_left = False
            elif e.key == K_a:
                tecla_a = False
            elif e.key == K_RIGHT: 
                moving_right = False
            elif e.key == K_d:
                tecla_d = False
            elif e.key == K_UP: 
                moving_up = False
            elif e.key == K_w:
                tecla_w = False
            elif e.key == K_DOWN: 
                moving_down = False
            elif e.key == K_s:
                tecla_S = False
 
    if moving_left or tecla_a and character.left > 0: 
        x -= 5 
    if moving_right or tecla_d and character.right < window.get_width(): 
        x += 5 
    if moving_up  or tecla_w and character.top > 0: 
        y -= 5 
    if moving_down or tecla_S and character.bottom < window.get_height(): 
        y += 5 

    window.fill((255, 255, 255)) 
 
    # Dibujar el personaje en la nueva posición 
    character = draw.rect(window, (0, 0, 255), (x, y, width, height)) 
 
    # Actualizar la pantalla 
    display.update() 
 
quit()

    