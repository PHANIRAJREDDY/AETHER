"""
=========================================================
AETHER
Page Manager
Version : 2.0.0
=========================================================
"""

from PySide6.QtWidgets import QStackedWidget

from ui.pages.dashboard import DashboardPage
from ui.pages.ai_page import AIPage
from ui.pages.research_page import ResearchPage
from ui.pages.innovation_page import InnovationPage
from ui.pages.projects_page import ProjectsPage
from ui.pages.documents_page import DocumentsPage
from ui.pages.settings_page import SettingsPage


class PageManager(QStackedWidget):

    def __init__(self):

        super().__init__()

        self.pages = {}

        self._initialize_pages()

    def _initialize_pages(self):

        self.register("dashboard", DashboardPage())
        self.register("ai", AIPage())
        self.register("research", ResearchPage())
        self.register("innovation", InnovationPage())
        self.register("projects", ProjectsPage())
        self.register("documents", DocumentsPage())
        self.register("settings", SettingsPage())

    def register(self, name, page):

        self.pages[name] = page

        self.addWidget(page)

    def show_page(self, name):

        if name not in self.pages:
            return False

        self.setCurrentWidget(self.pages[name])

        return True

    def get_page(self, name):

        return self.pages.get(name)

    def has_page(self, name):

        return name in self.pages

    def page_names(self):

        return list(self.pages.keys())