import pygame
from events import *

class CPUController:

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.running = 1

    def Run(self):
        while self.running:
            self.event_manager.Post(TickEvent())
        
    def Notify(self, event):
        if isinstance(event, QuitEvent):
            self.running = 0

class MouseController:

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

    def Notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                notification = None
                if event.type == pygame.QUIT:
                    notification = QuitEvent()

                if notification:
                    self.event_manager.Post(notification)
