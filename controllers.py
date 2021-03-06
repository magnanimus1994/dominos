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

class InputController:

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.dragging = False

    def Notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                notification = None
                if event.type == pygame.QUIT:
                    notification = QuitEvent()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    notification = GameStartRequest()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.dragging = True
                    notification = LeftClickEvent(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP and self.dragging and event.button == 1:
                    self.dragging = False
                    notification = ReleaseMouseEvent(event.pos)
                elif event.type == pygame.MOUSEMOTION and self.dragging:
                    notification = MouseDragEvent(event.pos)
                if notification:
                    self.event_manager.Post(notification)



