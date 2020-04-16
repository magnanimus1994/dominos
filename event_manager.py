from events import TickEvent

class EventManager:

    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        if listener in self.listeners:
            del self.listeners[listener]

    def Post(self, event):
        if isinstance(event, TickEvent):
            for listener in self.listeners:
                listener.Notify(event)
