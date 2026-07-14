"""
=========================================================
AETHER
Navigation Manager
Version : 1.0.0
=========================================================
"""


class NavigationManager:

    def __init__(self, workspace_manager):

        self.workspace_manager = workspace_manager

        self.current_page = None

    def navigate(self, page_name):

        if self.workspace_manager.show_page(page_name):

            self.current_page = page_name

            return True

        return False

    def current_page_name(self):

        return self.current_page