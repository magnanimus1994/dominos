import pygame
from events import TickEvent

DIMENSIONS = (900, 1100)
SQUARES_PER_ROW = 15
TRAY_HEIGHT = 200
TILE_WIDTH = DIMENSIONS[0] // SQUARES_PER_ROW
TILE_LENGTH = (DIMENSIONS[1] - TRAY_HEIGHT) // SQUARES_PER_ROW
BLACK = (0,0,0)
SLATE = (112, 128, 144)
WHITE = (255, 255, 255)
SILVER = (192, 192, 192)

class DominoSprite(pygame.sprite.Sprite):
    def __init__(self, group=None, values = (6,6)):
        pygame.sprite.Sprite.__init__(self, group)
        surface = pygame.Surface((TILE_WIDTH * 2, TILE_LENGTH))
        surface.fill(BLACK)

        self.draw_dots(surface, TILE_WIDTH, 0, values[0])
        self.draw_dots(surface, TILE_WIDTH, TILE_WIDTH, values[1])

        self.image = surface
        self.rect = surface.get_rect()

    def draw_dots(self, surface, width, origin, n):
        radius = width // 10
        if n==0:
            return
        elif n==1:
            pygame.draw.circle(surface, WHITE, (origin + (width // 2), width // 2), radius)
            return
        elif n==2:
            pygame.draw.circle(surface, WHITE, (origin + (width // 4), 3 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * width // 4), width // 4), radius)
            return
        elif n==3:
            pygame.draw.circle(surface, WHITE, (origin + (width // 4), 3 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (width // 2), width // 2), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * width // 4), width // 4), radius)
            return
        elif n==4:
            pygame.draw.circle(surface, WHITE, (origin + (width // 4), width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (width // 4), 3 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * width // 4), width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * width // 4), 3 * width // 4), radius)
            return
        elif n==5:
            pygame.draw.circle(surface, WHITE, (origin + (width // 4), width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (width // 4), 3 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * width // 4), width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * width // 4), 3 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (width // 2), width // 2), radius)
            return
        elif n==6:
            pygame.draw.circle(surface, WHITE, (origin + (width // 3), width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (2 * width // 3), width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (width // 3), 2 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (2 * width // 3), 2 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (width // 3), 3 * width // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (2 * width // 3), 3 * width // 4), radius)
            return


class GameView:

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        pygame.init()

        self.logo = pygame.image.load("domino.jpeg")
        self.screen = pygame.display.set_mode(DIMENSIONS)

        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Dominos")

        self.sprites = pygame.sprite.RenderUpdates()
        self.draw_background()

        font = pygame.font.Font(None, 80)
        text = """Press SPACE BAR to begin"""
        text_img = font.render(text, 1, BLACK)
        self.screen.blit(text_img, (120, 120))
        pygame.display.flip()



    def draw_background(self):
        self.screen.fill(WHITE)
        for x in range(0, SQUARES_PER_ROW):
            for y in range(0, SQUARES_PER_ROW):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.screen, SILVER, [TILE_WIDTH * x, TILE_LENGTH * y, TILE_WIDTH, TILE_LENGTH]) 
        
        tray = [0, DIMENSIONS[1] - TRAY_HEIGHT, DIMENSIONS[0], TRAY_HEIGHT] 
        pygame.draw.rect(self.screen, SLATE, tray)
        
        # TESTING SPRITE
        # newSprite = DominoSprite(self.sprites, (0,6))
        # self.screen.blit(newSprite.image, (450, 450))

        pygame.display.update()


    def Notify(self, event):
        if isinstance(event, TickEvent):
            return
        #     self.draw_background()
