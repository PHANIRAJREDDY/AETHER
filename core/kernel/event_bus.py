"""
=========================================================
AETHER
Event Bus
=========================================================
"""


class EventBus:

    def __init__(self):

        self.events = {}

    def subscribe(self, event, callback):

        if event not in self.events:

            self.events[event] = []

        self.events[event].append(callback)

    def emit(self, event, data=None):

        if event not in self.events:

            return

        for callback in self.events[event]:

            callback(data)