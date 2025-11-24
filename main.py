import pygame
import os
pygame.init()

screen = pygame.display.set_mode((854, 480))

#importar assets
asset_path = os.path.join("..","assets") #<- variable de la ruta a assets
cursor_image = pygame.image.load(asset_path + "/tile_0027.png")
#Esconder cursor en la pantalla para que esté el pixelado
pygame.mouse.set_visible(False)
# Mantener la ventana corriendo hasta que se presione la X
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cursor_cords = pygame.mouse.get_pos()
    screen.blit(cursor_image, cursor_cords)
    pygame.display.flip()

pygame.quit()

#TODO add delta time and a clock, of course