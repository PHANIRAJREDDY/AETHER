"""
=========================================================
AETHER
Workspace Manager
Version : 1.0.0
=========================================================
"""

from ui.components.workspace.workspace import Workspace


class WorkspaceManager:

    def __init__(self):

        self.workspace = Workspace()

    def register_page(self, name, page):

        self.workspace.register_page(name, page)

    def show_page(self, name):

        return self.workspace.show_page(name)

    def get_workspace(self):

        return self.workspace

    def page_names(self):

        return self.workspace.page_names()

    def page_count(self):

        return self.workspace.page_count()