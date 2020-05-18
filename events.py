class Event:
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
    def __init__(self):
        self.name = "CPU Tick Event"

class QuitEvent(Event):
    def __init__(self):
        self.name = "Program Quit Event"

class GameStartRequest(Event):
    def __init__(self):
        self.name = "Game Start Request"

class GameStartEvent(Event):
    def __init__(self, game):
        self.name = "Game Start Event"
        self.game = game

class LeftClickEvent(Event):
    def __init__(self, pos):
        self.name = "Left Click Event"
        self.pos = pos

class MouseDragEvent(Event):
    def __init__(self, pos):
        self.name = "Mouse Drag Event"
        self.pos = pos

class ReleaseMouseEvent(Event):
     def __init__(self, pos):
        self.name = "Mouse Drag Event"
        self.pos = pos

class PlaceDominoRequest(Event):
    def __init__(self, domino, sector):
        self.name = "Place Domino Request"
        self.domino = domino
        self.sector = sector

class PlaceDominoEvent(Event):
    def __init__(self, domino, sector, rotate=False):
        self.name = "Place Domino Event"
        self.domino = domino
        self.sector = sector
        self.rotate = rotate

class RejectPlacementEvent(Event):
    def __init__(self):
        self.name = "Reject Placement Event"

class GameOverEvent(Event):
    def __init__(self, game):
        self.name = "Game Over Event"
        self.game = game 
