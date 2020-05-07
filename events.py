class Event:
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
    def __init__(self):
        self.name = "CPU Tick Event"

class QuitEvent(Event):
    def __init__(self):
        self.name = "Program Quit Event"

class GameStartEvent(Event):
    def __init__(self, game):
        self.name = "Game Start Event"
        self.game = game

class NextMoveEvent(Event):
    def __init__(self, players):
        self.name = "Next Move Event"
        self.players = players

class RotateDominoEvent(Event):
    def __init__(self, domino):
        self.name = "Rotate Domino Event"
        self.domino = domino

class MoveDominoEvent(Event):
    def __init__(self, domino):
        self.name = "Move Domino Event"
        self.domino = domino

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
