import pygame
import random

DIMENSIONS = (900, 900)
SQUARES_PER_ROW = 15
BLACK = (0,0,0)
WHITE = (255, 255, 255)
SILVER = (192,192,192)

def distribute_tiles():
    tiles = []
    for i in range(0,7):
        for j in range(i,7):
            tiles.append((i,j))
    random.shuffle(tiles)
    hands = [tiles[:len(tiles)//2], tiles[len(tiles)//2:]]
    return hands

def draw_background(surface):
    surface.fill(WHITE)
    tile_width, tile_length = DIMENSIONS[0] / SQUARES_PER_ROW, DIMENSIONS[1] / SQUARES_PER_ROW
    for x in range(0, SQUARES_PER_ROW):
        for y in range(0, SQUARES_PER_ROW):
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, SILVER, [tile_width * x, tile_length * y, tile_width, tile_length]) 

def main():
    pygame.init()
    logo = pygame.image.load("domino.jpeg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Dominos")
    screen = pygame.display.set_mode(DIMENSIONS)

    draw_background(screen)
    hands = distribute_tiles()
    player_tiles, computer_tiles = hands[0], hands[1]

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

if __name__=="__main__":
    main()
