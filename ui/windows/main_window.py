"""
=========================================================
AETHER
Main Window
Version : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)

from core.managers.desktop.desktop_manager import DesktopManager

from ui.components.sidebar.sidebar import Sidebar
from ui.components.toolbar.toolbar import Toolbar
from ui.components.statusbar.status_bar import StatusBar

from ui.pages.dashboard import DashboardPage
from ui.pages.ai_page import AIPage
from ui.pages.research_page import ResearchPage
from ui.pages.innovation_page import InnovationPage
from ui.pages.projects_page import ProjectsPage
from ui.pages.documents_page import DocumentsPage
from ui.pages.settings_page import SettingsPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AETHER")

        self.resize(1600, 900)

        self.desktop = DesktopManager()

        self.sidebar = Sidebar()

        self.toolbar = Toolbar()

        self.statusbar = StatusBar()

        self.workspace = self.desktop.workspace()

        self._register_pages()

        self._build_ui()

        self._connect_signals()

        self.desktop.navigate("dashboard")

    def _register_pages(self):

        self.desktop.register_page(
            "dashboard",
            DashboardPage()
        )

        self.desktop.register_page(
            "ai",
            AIPage()
        )

        self.desktop.register_page(
            "research",
            ResearchPage()
        )

        self.desktop.register_page(
            "innovation",
            InnovationPage()
        )

        self.desktop.register_page(
            "projects",
            ProjectsPage()
        )

        self.desktop.register_page(
            "documents",
            DocumentsPage()
        )

        self.desktop.register_page(
            "settings",
            SettingsPage()
        )

    def _build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        root = QHBoxLayout(central)

        root.setContentsMargins(0, 0, 0, 0)

        root.setSpacing(0)

        root.addWidget(self.sidebar)

        right = QWidget()

        right_layout = QVBoxLayout(right)

        right_layout.setContentsMargins(0, 0, 0, 0)

        right_layout.setSpacing(0)

        right_layout.addWidget(self.toolbar)

        right_layout.addWidget(self.workspace)

        right_layout.addWidget(self.statusbar)

        root.addWidget(right)

    def _connect_signals(self):

        self.sidebar.page_requested.connect(
            self.desktop.navigate
        )