from ui.components.page_template import PageTemplate


class ProjectsPage(PageTemplate):

    def __init__(self):
        super().__init__(
            "Projects",
            "Manage all AETHER projects."
        )