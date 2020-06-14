import pygame
from events import * 

# WINDOW
DIMENSIONS = (1300, 1300)
SECTORS_PER_ROW = 24
TRAY_WIDTH = 200

# BOARD
BOARD_WIDTH = DIMENSIONS[0] - TRAY_WIDTH
BOARD_LENGTH = DIMENSIONS[1] - TRAY_WIDTH
SECTOR_WIDTH =  BOARD_WIDTH // SECTORS_PER_ROW
SECTOR_LENGTH = BOARD_LENGTH // SECTORS_PER_ROW

# COLORS
BLACK = (0,0,0)
SLATE = (112, 128, 144)
WHITE = (255, 255, 255)
SILVER = (192, 192, 192)

class SectorSprite(pygame.sprite.Sprite):
    def __init__(self, sector, group=None):
        pygame.sprite.Sprite.__init__(self, group)
        self.sector = sector

        color = WHITE if (sector.coordinates[0] + sector.coordinates[1]) % 2 == 0 else SILVER
        surface = pygame.Surface((SECTOR_WIDTH, SECTOR_LENGTH))
        surface.fill(color)
        self.image = surface

class DominoSprite(pygame.sprite.Sprite):
    def __init__(self, domino, group=None, face_up=True):
        pygame.sprite.Sprite.__init__(self, group)
        
        self.domino = domino

        surfDimensions = (SECTOR_WIDTH * 2, SECTOR_LENGTH) 
        surface = pygame.Surface(surfDimensions)
        surface.fill(BLACK)

        if face_up:
            self.draw_dots(surface, 0, self.domino.values[0])
            self.draw_dots(surface, SECTOR_WIDTH, self.domino.values[1])
            pygame.draw.line(surface, WHITE, (SECTOR_WIDTH,0), (SECTOR_WIDTH, SECTOR_LENGTH))

        self.image = surface

    def draw_dots(self, surface, origin, n):
        radius = SECTOR_WIDTH // 10
        if n==1:
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 2), SECTOR_WIDTH // 2), radius)
        elif n==2:
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 4), 3 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * SECTOR_WIDTH // 4), SECTOR_WIDTH // 4), radius)
        elif n==3:
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 4), 3 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 2), SECTOR_WIDTH // 2), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * SECTOR_WIDTH // 4), SECTOR_WIDTH // 4), radius)
        elif n==4:
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 4), SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 4), 3 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * SECTOR_WIDTH // 4), SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * SECTOR_WIDTH // 4), 3 * SECTOR_WIDTH // 4), radius)
        elif n==5:
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 4), SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 4), 3 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * SECTOR_WIDTH // 4), SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (3 * SECTOR_WIDTH // 4), 3 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 2), SECTOR_WIDTH // 2), radius)
        elif n==6:
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 3), SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (2 * SECTOR_WIDTH // 3), SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 3), 2 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (2 * SECTOR_WIDTH // 3), 2 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (SECTOR_WIDTH // 3), 3 * SECTOR_WIDTH // 4), radius)
            pygame.draw.circle(surface, WHITE, (origin + (2 * SECTOR_WIDTH // 3), 3 * SECTOR_WIDTH // 4), radius)


class GameView:

    WAITING = 'waiting'
    RUNNING = 'running'
    ENDED = 'ended'

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        self.state = GameView.WAITING

        pygame.init()

        self.logo = pygame.image.load("domino.jpeg")
        self.screen = pygame.display.set_mode(DIMENSIONS)
        self.background = pygame.Surface(DIMENSIONS)
        self.background.fill(SLATE)

        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Dominos")

        font = pygame.font.Font(None, 80)
        text = """Press SPACE BAR to begin"""
        text_img = font.render(text, 1, BLACK)
        self.screen.blit(self.background, (0,0))
        self.screen.blit(text_img, (120, 120))
        pygame.display.flip()

        self.backSprites = pygame.sprite.RenderUpdates()
        self.frontSprites = pygame.sprite.RenderUpdates()

        self.selected_domino = None
        self.drag_start_x = None
        self.drag_start_y = None
        self.drag_offset_x = None
        self.drag_offset_y = None

    def draw_board(self, game_map):
        # self.sprites.clear(self.screen, self.background)
        self.screen.blit(self.background, (0,0))
        for sector in game_map.sectors:
            sprite = SectorSprite(sector, self.backSprites)
            sprite.rect = pygame.Rect((sector.coordinates[0] * SECTOR_WIDTH, sector.coordinates[1] * SECTOR_LENGTH, SECTOR_WIDTH, SECTOR_LENGTH))
        
    def deal_hands(self, players):
        for player in players:
            if player.human:
                for i, domino in enumerate(player.dominos):
                    sprite = DominoSprite(domino, self.frontSprites)
                    sprite.rect = pygame.Rect((\
                        (8 + ((i % 7) * ((SECTOR_WIDTH * 2) + 8))),\
                        (BOARD_LENGTH + 20 + ((i % 2) * (20 + SECTOR_LENGTH))),\
                        SECTOR_WIDTH * 2,\
                        SECTOR_LENGTH\
                    ))
            else:
                for i, domino in enumerate(player.dominos):
                    sprite = DominoSprite(domino, self.frontSprites, False)
                    sprite.rect = pygame.Rect((\
                        (BOARD_WIDTH + 20 + ((i % 2) * (SECTOR_WIDTH + 20))),\
                        (8 + ((i % 7) * (8 + SECTOR_LENGTH * 2))),\
                        SECTOR_WIDTH,\
                        SECTOR_LENGTH * 2\
                    ))
                    sprite.image = pygame.transform.rotate(sprite.image, 90)
                
    def game_over(self, game):
        # TODO Render results, prompt player to hit spacebar to play again
        return

    def return_to_tray(self):
        self.selected_domino.rect.x = self.drag_start_x
        self.selected_domino.rect.y = self.drag_start_y

    def deselect_domino(self):
        self.selected_domino = None
        self.drag_start_x = None
        self.drag_start_y = None
        self.drag_offset_x = None
        self.drag_offset_y = None

    def Notify(self, event):
        if isinstance(event, TickEvent):
            if self.state == GameView.RUNNING:
                self.backSprites.clear( self.screen, self.background )
                self.frontSprites.clear( self.screen, self.background )              

                self.backSprites.update()
                self.frontSprites.update()

                dirtyRects1 = self.backSprites.draw( self.screen )
                dirtyRects2 = self.frontSprites.draw( self.screen )
                
                dirtyRects = dirtyRects1 + dirtyRects2
                pygame.display.update( dirtyRects )


        elif isinstance(event, GameStartEvent):
            event.game.map.Build(SECTORS_PER_ROW)
            self.draw_board(event.game.map)
            self.deal_hands(event.game.players)
            self.state = GameView.RUNNING

        elif isinstance(event, LeftClickEvent):
            for sprite in self.frontSprites:
                if sprite.rect.collidepoint(event.pos):
                   self.selected_domino = sprite
                   self.drag_start_x = sprite.rect[0]
                   self.drag_start_y = sprite.rect[1]
                   mouse_x, mouse_y, = event.pos
                   self.drag_offset_x = self.drag_start_x - mouse_x
                   self.drag_offset_y = self.drag_start_y - mouse_y
        
        elif isinstance(event, MouseDragEvent):
            if self.selected_domino is not None:
                mouse_x, mouse_y, = event.pos
                self.selected_domino.rect.x = mouse_x + self.drag_offset_x
                self.selected_domino.rect.y = mouse_y + self.drag_offset_y

        elif isinstance(event, ReleaseMouseEvent):
            if self.selected_domino is not None:
                notification = None
                for sprite in self.backSprites:
                    if sprite.rect.collidepoint(event.pos):
                        notification = PlaceDominoRequest(self.selected_domino.domino, sprite.sector)
                        break
                if notification is None:
                    notification = RejectPlacementEvent()    
                self.event_manager.Post(notification)

        elif isinstance(event, PlaceDominoEvent):
#             for frontSprite in self.frontSprites:
#                 if frontSprite.domino.values == event.domino.values:
#                     for backSprite in self.backSprites:
#                         if backSprite.sector == event.domino.alpha_sector:
#                             destination = backSprite
#                             break
#                     frontSprite.rect.x = destination.rect.x
#                     frontSprite.rect.y = destination.rect.y
#                     if not frontSprite.domino.human:
#                         vertical = frontSprite.domino.orientation == 'vertical'
#                         frontSprite.draw_dots(frontSprite.image, 0, frontSprite.domino.values[0], vertical)
#                         frontSprite.draw_dots(frontSprite.image, SECTOR_WIDTH, frontSprite.domino.values[1], vertical)
#                     break
            self.deselect_domino()

        elif isinstance(event, RejectPlacementEvent):
            self.return_to_tray()
            self.deselect_domino()

        elif isinstance(event, GameOverEvent):
            self.state = GameView.ENDED
            self.game_over(event.game)
            
