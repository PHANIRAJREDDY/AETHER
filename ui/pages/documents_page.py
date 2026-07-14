from ui.components.page_template import PageTemplate


class DocumentsPage(PageTemplate):

    def __init__(self):
        super().__init__(
            "Documents",
            "View and organize documentation."
        )