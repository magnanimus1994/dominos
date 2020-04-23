import random
from events import TickEvent

class Game:
    
    WAITING = 'waiting'
    RUNNING = 'running'
    ENDED = 'ended'

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.state = Game.WAITING
        self.players = []
        self.winner = None


    def deal_hands(self):
        dominos = []
        for i in range(0,7):
            for j in range(i,7):
                dominos.append(Domino(self.event_manager, (i,j)))
        random.shuffle(dominos)
        self.players.append(Player(self.event_manager, dominos[:len(dominos)//2], True)) 
        self.players.append(Player(self.event_manager, dominos[len(dominos)//2:], False))

    def is_game_over(self):
        # TODO check if either players can move
        return false

    def Notify(self, event):
        if isinstance(event, TickEvent):
            return


class Player:

    def __init__(self, event_manager, dominos, human):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

        self.dominos = dominos
        self.human = human

        self.has_next_move = False

    def Notify(self, event):
        if isinstance(event, NextTurnEvent):
            # TODO set has_next_move to opposite. Post another event? 
            return


class Domino:

    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'

    def __init__(self, event_manager, values):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.values = values
        self.orientation = Domino.HORIZONTAL
    
    def rotate(self)
        if self.orientation == Domino.VERTICAL:
            self.values = (self.values[1], self.values[0])
        self.orientation = Domino.VERTICAL if self.orientation == Domino.HORIZONTAL else DOMINO.HORIZONTAL

    def Notify(self, event):
        if isinstance(event, TickEvent):
            return
        
        elif isinstance(event, RotateDominoEvent):
            self.rotate()
            # TODO This will make all dominos rotate. Need to move it one layer above 

