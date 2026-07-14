"""
=========================================================
AETHER
Workspace Component
Version : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
)


class Workspace(QWidget):
    """
    Central workspace for the AETHER Desktop Engine.

    All application pages (Dashboard, AI, Research,
    Projects, Documents, Settings...) are hosted here.
    """

    def __init__(self):
        super().__init__()

        self.pages = {}
        self.stack = QStackedWidget()

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)

        layout.addWidget(self.stack)

    def register_page(self, name: str, widget):

        if name in self.pages:
            return

        self.pages[name] = widget

        self.stack.addWidget(widget)

    def show_page(self, name: str):

        if name not in self.pages:
            return False

        self.stack.setCurrentWidget(self.pages[name])

        return True

    def get_page(self, name: str):

        return self.pages.get(name)

    def page_names(self):

        return list(self.pages.keys())

    def page_count(self):

        return self.stack.count()