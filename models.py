import random
from events import *

ABOVE = 0
RIGHT = 1
BELOW = 2
LEFT = 3

class Game:
    
    WAITING = 'waiting'
    SETTING_UP = 'setting up'
    RUNNING = 'running'
    ENDED = 'ended'

    def __init__(self, event_manager):

        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        self.state = Game.WAITING

        self.map = Map(self.event_manager) 

        self.players = []
        self.deal_hands()
        self.end_dominos = []

        self.winner = None

    def deal_hands(self):
        dominos = []
        for i in range(0,7):
            for j in range(i,7):
                dominos.append(Domino(self.event_manager, (i,j)))
        random.shuffle(dominos)
        self.players.append(Player(self.event_manager, dominos[:len(dominos)//2], True)) 
        self.players.append(Player(self.event_manager, dominos[len(dominos)//2:], False))
        for domino in self.players[1].dominos:
            domino.human = False

    def is_game_over(self):
        # TODO check if either players can move
        return false

    def Notify(self, event):
        if isinstance(event, GameStartRequest) and self.state == Game.WAITING:
            self.state = Game.SETTING_UP
            self.event_manager.Post(GameStartEvent(self))
            self.state = Game.RUNNING
            for player in self.players:
                for domino in player.dominos:
                    if domino.values == (6,6):
                        player.to_move = False
                        self.event_manager.Post(PlaceDominoRequest(domino, self.map.sectors[len(self.map.sectors) // 2]))
                        break

        elif isinstance(event, PlaceDominoRequest):
            notification = None
            if event.domino.values == (6,6):
                notification = PlaceDominoEvent(event.domino)
                alpha_sector = event.sector # Make sure this is 
                self.end_dominos.append(event.domino)
            else:
                for i, open_domino in enumerate(self.end_dominos):
                    if event.sector in open_domino.neighbors and open_domino.values[1] in event.domino.values: 
                        if event.domino.values[0] != open_domino.values[1]:
                            notification = PlaceDominoEvent(event.domino, True)
                            for _ in range(2):
                                event.domino.rotate()
                        else:
                            notification = PlaceDominoEvent(event.domino)
                        
                        notification.domino.alpha_sector = open_domino.neighbors[RIGHT]\
                            if open_domino.orientation == Domino.Horizontal\
                            else open_domino.neighbors[BELOW]
                        
                        notification.domino.beta_sector = notification.domino.alpha_sector.neighbors[RIGHT]\
                            if notification.domino.orientation == Domino.HORIZONTAL\
                            else notification.domino.alpha_sector.neighbors[BELOW]
                        
                        if len(self.end_dominos) > 1:
                            self.end_dominos[i] = event.domino
                        else:
                            self.end_dominos.append(event.domino)
                        break

            if notification is None:
                notification = RejectPlacementEvent()
            self.event_manager.Post(notification)

class Map:
    def __init__(self, event_manager):
        self.sectors = []
        self.event_manager = event_manager

    def Build(self, sectors_per_row):
        for row in range(sectors_per_row):
            for column in range(sectors_per_row):
                self.sectors.append(Sector(self.event_manager, (row, column)))
        
        for sector in self.sectors:
            x = sector.coordinates[0]
            y = sector.coordinates[1]
            sector.neighbors[ABOVE] = None if y == 0 else self.sectors[((sectors_per_row * y) - 1) + x]
            sector.neighbors[RIGHT] = None if x == sectors_per_row - 1 else self.sectors[(sectors_per_row * y) + x + 1]
            sector.neighbors[BELOW] = None if y == sectors_per_row - 1 else self.sectors[((sectors_per_row * y) + 1) + x]
            sector.neighbors[LEFT] = None if y == 0 else self.sectors[(sectors_per_row * y) + x - 1]

           

class Sector:
    def __init__(self, event_manager, coordinates):
        self.coordinates = coordinates
        self.neighbors = [None] * 4
        self.event_manager = event_manager

class Player:

    def __init__(self, event_manager, dominos, human):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        self.dominos = dominos
        self.human = human

        self.to_move = True

    def Notify(self, event):
        return
        # if isinstance(event, NextTurnEvent):
            # TODO set has_next_move to opposite. Post another event? 
            # return


class Domino:

    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'

    def __init__(self, event_manager, values):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.values = values
        self.orientation = Domino.HORIZONTAL
        self.human = True
        self.alpha_sector = None
        self.beta_sector = None

    def rotate(self):
        if self.orientation == Domino.VERTICAL:
            self.values = (self.values[1], self.values[0])
        self.orientation = Domino.VERTICAL if self.orientation == Domino.HORIZONTAL else DOMINO.HORIZONTAL
    
    def Notify(self, event):
        if isinstance(event, TickEvent):
            return
        

