class Event:
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
    def __init__(self):
        self.name = "CPU Tick Event"

class QuitEvent(Event):
    def __init__(self):
        self.name = "Program Quit Event"

class PlaceTileEvent(Event):
    def __init__(self, tile, game_map):
        self.name = "Place Tile Event"
        self.tile = tile
        self.game_map = game_map


