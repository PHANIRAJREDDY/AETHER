"""
=========================================================
AETHER
Projects Page
Version : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QMessageBox,
    QInputDialog,
)

from ui.components.project_explorer.project_explorer import ProjectExplorer
from core.project.manager import ProjectManager


class ProjectsPage(QWidget):

    def __init__(self):

        super().__init__()

        self.manager = ProjectManager()

        self.explorer = ProjectExplorer()

        self._build_ui()

        self._connect_signals()

        self.refresh_projects()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(self.explorer)

    def _connect_signals(self):

        self.explorer.new_project_requested.connect(
            self.create_project
        )

        self.explorer.refresh_requested.connect(
            self.refresh_projects
        )

        self.explorer.open_project_requested.connect(
            self.open_project
        )

        self.explorer.delete_project_requested.connect(
            self.delete_project
        )

    def refresh_projects(self):

        projects = self.manager.list_projects()

        self.explorer.set_projects(projects)

    def create_project(self):

        name, ok = QInputDialog.getText(
            self,
            "New Project",
            "Project Name:"
        )

        if not ok or not name.strip():

            return

        self.manager.create_project(name.strip())

        self.refresh_projects()

    def open_project(self):

        project = self.explorer.selected_project()

        if project is None:

            QMessageBox.information(
                self,
                "Open Project",
                "Please select a project."
            )

            return

        self.manager.open_project(project)

        QMessageBox.information(
            self,
            "Project Opened",
            f"Opened project:\n\n{project}"
        )

    def delete_project(self):

        project = self.explorer.selected_project()

        if project is None:

            QMessageBox.information(
                self,
                "Delete Project",
                "Please select a project."
            )

            return

        reply = QMessageBox.question(
            self,
            "Delete Project",
            f"Delete '{project}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:

            return

        self.manager.delete_project(project)

        self.refresh_projects()