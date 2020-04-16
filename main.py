from models import Game
from views import GameView
from controllers import *
from event_manager import EventManager

def main():
    event_manager = EventManager()

    cpu_controller = CPUController(event_manager)
    mouse_controller = MouseController(event_manager)
    view = GameView(event_manager)
    game = Game(event_manager)

    cpu_controller.Run()

if __name__=="__main__":
    main()
