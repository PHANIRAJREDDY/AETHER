from ui.components.page_template import PageTemplate


class SettingsPage(PageTemplate):

    def __init__(self):
        super().__init__(
            "Settings",
            "Configure your AETHER workspace."
        )