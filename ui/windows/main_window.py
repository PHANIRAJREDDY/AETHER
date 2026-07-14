"""
=========================================================
AETHER
Main Window
Version : 3.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

from core.managers.navigation_manager import NavigationManager
from core.managers.page_manager import PageManager

from ui.components.sidebar import Sidebar


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AETHER Workspace")

        self.resize(1600, 900)

        self.navigation = NavigationManager()

        self.page_manager = PageManager()

        self.navigation.connect(self.page_manager)

        self.build_ui()

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)

        self.sidebar = Sidebar()

        self.sidebar.page_requested.connect(
            self.navigation.navigate
        )

        layout.addWidget(self.sidebar)

        layout.addWidget(self.page_manager)