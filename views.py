import pygame
from events import * 

# WINDOW
DIMENSIONS = (1100, 1100)
SECTORS_PER_ROW = 15
TRAY_WIDTH = 200
SECTOR_WIDTH = (DIMENSIONS[0] - TRAY_WIDTH) // SECTORS_PER_ROW
SECTOR_LENGTH = (DIMENSIONS[1] - TRAY_WIDTH) // SECTORS_PER_ROW

# COLORS
BLACK = (0,0,0)
SLATE = (112, 128, 144)
WHITE = (255, 255, 255)
SILVER = (192, 192, 192)

class DominoSprite(pygame.sprite.Sprite):
    def __init__(self, group=None, values = (6,6)):
        pygame.sprite.Sprite.__init__(self, group)
        surface = pygame.Surface((SECTOR_WIDTH * 2, SECTOR_LENGTH))
        surface.fill(BLACK)

        # TODO Make dots only appear if player's tiles
        self.draw_dots(surface, SECTOR_WIDTH, 0, values[0])
        self.draw_dots(surface, SECTOR_WIDTH, SECTOR_WIDTH, values[1])

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
        self.background = pygame.Surface(DIMENSIONS)

        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Dominos")

        self.draw_board()

        font = pygame.font.Font(None, 80)
        text = """Press SPACE BAR to begin"""
        text_img = font.render(text, 1, BLACK)
        self.background.blit(text_img, (120, 120))
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()

        self.sprites = pygame.sprite.RenderUpdates()

    def draw_board(self):
        # self.sprites.clear(self.screen, self.background)
        self.background.fill(SLATE)
        board = [0, 0, DIMENSIONS[0] - TRAY_WIDTH, DIMENSIONS[1] - TRAY_WIDTH] 
        pygame.draw.rect(self.background, WHITE, board)

        for x in range(0, SECTORS_PER_ROW):
            for y in range(0, SECTORS_PER_ROW):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.background, SILVER, [SECTOR_WIDTH * x, SECTOR_LENGTH * y, SECTOR_WIDTH, SECTOR_LENGTH]) 
        
        self.screen.blit(self.background, (0,0))

    def move_domino(self, domino):
        # TODO Move domino according to mouse drag
        return
    
    def place_domino(self, domino, game_map):
        # TODO Place domino onto the appropriate tiles on the board
        return

    def rotate_domino(self, domino):
        # TODO Rotate domino in tray clockwise 90 degrees
        return

    def game_over(self, game):
        # TODO Render results, prompt player to hit spacebar to play again
        return

    def Notify(self, event):
        if isinstance(event, TickEvent) :
            # TODO Draw everything, but if game hasn't started, only draw the prompt 
            return

        elif isinstance(event, GameStartEvent):
            self.draw_board()
            self.deal_hands(event.game.players)

        elif isinstance(event, MoveDominoEvent):
            self.move_domino(event.domino)
        
        elif isinstance(event, PlaceDominoEvent):
            self.place_domino(event.domino, event.game_map)

        elif isinstance(event, RotateDominoEvent):
            self.rotate_domino(event.domino)

        elif isinstance(event, GameOverEvent):
            self.game_over(event.game)
