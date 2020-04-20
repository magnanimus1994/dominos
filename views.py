import pygame
from events import TickEvent

DIMENSIONS = (900, 1100)
SQUARES_PER_ROW = 15
TRAY_HEIGHT = 200
BLACK = (0,0,0)
SLATE = (112, 128, 144)
WHITE = (255, 255, 255)
SILVER = (192, 192, 192)

class GameView:

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        pygame.init()

        self.logo = pygame.image.load("domino.jpeg")
        self.screen = pygame.display.set_mode(DIMENSIONS)

        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Dominos")

        self.draw_background()

        font = pygame.font.Font(None, 80)
        text = """Press SPACE BAR to begin"""
        text_img = font.render(text, 1, BLACK)
        self.screen.blit(text_img, (120, 120))
        pygame.display.flip()


    def draw_background(self):
        self.screen.fill(WHITE)
        tile_width, tile_length = DIMENSIONS[0] / SQUARES_PER_ROW, (DIMENSIONS[1] - TRAY_HEIGHT) / SQUARES_PER_ROW
        for x in range(0, SQUARES_PER_ROW):
            for y in range(0, SQUARES_PER_ROW):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.screen, SILVER, [tile_width * x, tile_length * y, tile_width, tile_length]) 
        
        pygame.draw.rect(self.screen, SLATE, [0, DIMENSIONS[1] - TRAY_HEIGHT, DIMENSIONS[0], TRAY_HEIGHT])
        pygame.display.update()

    def Notify(self, event):
        if isinstance(event, TickEvent):
            return
        #     self.draw_background()
