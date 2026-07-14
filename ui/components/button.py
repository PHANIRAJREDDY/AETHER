"""
==================================================
AETHER DESIGN SYSTEM
Component : Button
Version   : 1.0
==================================================
"""

from PySide6.QtWidgets import QPushButton
from ui.styles.theme import Theme


class AetherButton(QPushButton):

    def __init__(self, text):

        super().__init__(text)

        self.setMinimumHeight(48)
        self.setStyleSheet(Theme.button())