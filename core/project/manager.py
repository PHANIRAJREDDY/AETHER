"""
=========================================================
AETHER
Project Manager
Version : 1.0.0
=========================================================
"""

from core.project.project import Project
from core.storage.storage_manager import StorageManager


class ProjectManager:
    """
    Handles creation, loading and management of
    AETHER projects.
    """

    def __init__(self):

        self.storage = StorageManager()

        self.current_project = None

    def create_project(self, name: str):

        project = Project(name=name)

        self.storage.create_project(project.name)

        self.current_project = project

        return project

    def open_project(self, name: str):

        data = self.storage.open_project(name)

        if not data:

            return None

        project = Project.from_dict(data)

        self.current_project = project

        return project

    def current(self):

        return self.current_project

    def has_project(self):

        return self.current_project is not None

    def close_project(self):

        self.current_project = None

    def list_projects(self):

        return self.storage.list_projects()

    def delete_project(self, name: str):

        if (
            self.current_project
            and self.current_project.name == name
        ):
            self.current_project = None

        return self.storage.delete_project(name)

    def rename_project(self, new_name: str):

        if not self.current_project:

            return False

        old_name = self.current_project.name

        self.current_project.rename(new_name)

        self.storage.delete_project(old_name)

        self.storage.create_project(new_name)

        return True