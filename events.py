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
    def __init__(self, domino, game_map):
        self.name = "Place Domino Request"
        self.domino = domino
        self.game_map = game_map

class PlaceDominoEvent(Event):
    def __init__(self, domino, game_map):
        self.name = "Place Domino Event"
        self.domino = domino
        self.game_map = game_map

class GameOverEvent(Event):
    def __init_(self, game):
        self.name = "Game Over Event"
        self.game = game 
