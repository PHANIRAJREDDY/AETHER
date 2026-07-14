"""
=========================================================
AETHER
Workspace Component
Version : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget
)


class Workspace(QWidget):
    """
    Central workspace container.

    This component hosts all application pages.
    Future modules such as AI Team, Research,
    Projects, Innovation Lab, Documents, and
    Settings will be displayed here.
    """

    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)

        layout.addWidget(self.stack)

    def add_page(self, page):

        self.stack.addWidget(page)

    def set_page(self, page):

        self.stack.setCurrentWidget(page)

    def current_page(self):

        return self.stack.currentWidget()

    def page_count(self):

        return self.stack.count()