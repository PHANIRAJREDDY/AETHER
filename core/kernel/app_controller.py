"""
=========================================================
AETHER
Application Controller
Version : 1.0.0
=========================================================
"""

from core.kernel.config_manager import ConfigManager
from core.kernel.logger import Logger
from core.kernel.event_bus import EventBus


class ApplicationController:

    def __init__(self):

        self.config = None
        self.logger = None
        self.events = None

    def initialize(self):

        self.config = ConfigManager()

        self.logger = Logger()

        self.events = EventBus()

        self.logger.info("Application Controller Initialized")