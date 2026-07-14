"""
=========================================================
AETHER
Configuration Manager
=========================================================
"""

import json
from pathlib import Path


class ConfigManager:

    CONFIG_FILE = Path("config.json")

    def __init__(self):

        self.data = {}

        self.load()

    def load(self):

        if self.CONFIG_FILE.exists():

            with open(self.CONFIG_FILE, "r") as file:

                self.data = json.load(file)

    def save(self):

        with open(self.CONFIG_FILE, "w") as file:

            json.dump(self.data, file, indent=4)

    def get(self, key, default=None):

        return self.data.get(key, default)

    def set(self, key, value):

        self.data[key] = value