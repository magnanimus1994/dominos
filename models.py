import random
from events import TickEvent

class Game:
    
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.players = []

    def deal_tiles(self):
        tiles = []
        for i in range(0,7):
            for j in range(i,7):
                tiles.append(Tile(self.event_manager, (i,j)))
        random.shuffle(tiles)
        self.players.append(Player(self.event_manager, tiles[:len(tiles)//2], True)) 
        self.players.append(Player(self.event_manager, tiles[len(tiles)//2:], False))

    def Notify(self, event):
        if isinstance(event, TickEvent):
            return


class Player:

    def __init__(self, event_manager, tiles, human):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        self.tiles = tiles
        self.human = human

    def Notify(self, event):
        if isinstance(event, TickEvent):
            return


class Tile:

    def __init__(self, event_manager, values):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        self.values = values

    def Notify(self, event):
        if isinstance(event, TickEvent):
            return


