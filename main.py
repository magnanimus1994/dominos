import pygame
import random

DIMENSIONS = (900, 900)
SQUARES_PER_ROW = 15
BLACK = (0,0,0)
WHITE = (255, 255, 255)
SILVER = (192,192,192)

class Tile:

    def __init__(self, values):
        self.values = values

class Player:

    def __init__(self, tiles, human):
        self.tiles = tiles
        self.human = human

class Game:
    
    def __init__(self):
        tiles = []
        for i in range(0,7):
            for j in range(i,7):
                tiles.append(Tile((i,j)))
        random.shuffle(tiles)
        self.players = [
            Player(tiles[:len(tiles)//2], True), 
            Player(tiles[len(tiles)//2:], False)
        ]

class Controller:

    def __init__(self):
        self.game = Game()

    def Run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

class View:

    def __init__(self):
        self.logo = pygame.image.load("domino.jpeg")
        self.screen = pygame.display.set_mode(DIMENSIONS)

        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Dominos")
        
    
    def Render(self):
        self.screen.fill(WHITE)
        tile_width, tile_length = DIMENSIONS[0] / SQUARES_PER_ROW, DIMENSIONS[1] / SQUARES_PER_ROW
        for x in range(0, SQUARES_PER_ROW):
            for y in range(0, SQUARES_PER_ROW):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.screen, SILVER, [tile_width * x, tile_length * y, tile_width, tile_length]) 
        pygame.display.update()

def main():
    pygame.init()
    controller = Controller()
    view = View()

    running = True
    
    while running:
        if not controller.Run():
            return
        view.Render()

if __name__=="__main__":
    main()
