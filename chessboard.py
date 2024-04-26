import pygame
pygame.init()

# colours (check more on internet) (Format = R,G,B)
white = (255, 255, 255)
black = (0, 0, 0)

width = 400
height = 400
tile = height//8

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess")
pygame.display.update()  # updates the window

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    for row in range(0,8):
        for column in range(0,8):
            if (row + column) % 2 == 0:
                color = white
            else:
                color = black

            pygame.draw.rect(win, color, [row * tile, column * tile, tile, tile])

    

    pygame.display.update()

pygame.quit()
quit()
