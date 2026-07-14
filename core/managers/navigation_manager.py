"""
=========================================================
AETHER
Navigation Manager
Version : 1.0.0
=========================================================
"""


class NavigationManager:

    def __init__(self):

        self.current_page = "dashboard"

        self.page_manager = None

    def connect(self, page_manager):

        self.page_manager = page_manager

    def navigate(self, page):

        self.current_page = page

        if self.page_manager:

            self.page_manager.show_page(page)

    def current(self):

        return self.current_page