"""
=========================================================
AETHER
Desktop Manager
Version : 1.0.0
=========================================================
"""

from core.managers.desktop.workspace_manager import WorkspaceManager
from core.managers.desktop.navigation_manager import NavigationManager


class DesktopManager:

    def __init__(self):

        self.workspace_manager = WorkspaceManager()

        self.navigation_manager = NavigationManager(
            self.workspace_manager
        )

    def workspace(self):

        return self.workspace_manager.get_workspace()

    def register_page(self, name, page):

        self.workspace_manager.register_page(name, page)

    def navigate(self, page):

        return self.navigation_manager.navigate(page)

    def current_page(self):

        return self.navigation_manager.current_page_name()