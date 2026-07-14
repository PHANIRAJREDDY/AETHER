"""
=========================================================
AETHER
Main Window
Version : 4.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from core.managers.navigation_manager import NavigationManager
from core.managers.page_manager import PageManager

from ui.components.sidebar import Sidebar
from ui.components.toolbar.toolbar import Toolbar
from ui.components.workspace.workspace import Workspace


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AETHER Workspace")

        self.resize(1600, 900)

        self.navigation = NavigationManager()

        self.page_manager = PageManager()

        self.navigation.connect(self.page_manager)

        self.workspace = Workspace()

        self.toolbar = Toolbar()

        self.build_ui()

        self.initialize_workspace()

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        root_layout = QHBoxLayout(central)

        root_layout.setContentsMargins(0, 0, 0, 0)

        root_layout.setSpacing(0)

        self.sidebar = Sidebar()

        self.sidebar.page_requested.connect(
            self.navigation.navigate
        )

        root_layout.addWidget(self.sidebar)

        right_container = QWidget()

        right_layout = QVBoxLayout(right_container)

        right_layout.setContentsMargins(0, 0, 0, 0)

        right_layout.setSpacing(0)

        right_layout.addWidget(self.toolbar)

        right_layout.addWidget(self.workspace)

        root_layout.addWidget(right_container)

    def initialize_workspace(self):

        for page_name in self.page_manager.page_names():

            page = self.page_manager.get_page(page_name)

            self.workspace.add_page(page)

        self.workspace.set_page(
            self.page_manager.get_page("dashboard")
        )