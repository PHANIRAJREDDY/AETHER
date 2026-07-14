"""
=========================================================
AETHER
Storage Manager
Version : 1.0.0
=========================================================
"""

from pathlib import Path

from core.storage.filesystem import FileSystem
from core.storage.json_database import JsonDatabase


class StorageManager:
    """
    Central storage manager for AETHER.

    Responsible for creating project structures,
    loading project metadata and saving project data.
    """

    def __init__(self):

        self.workspace_root = Path("storage/projects")

        FileSystem.create_directory(
            str(self.workspace_root)
        )

    def create_project(self, project_name: str):

        project_path = self.workspace_root / project_name

        FileSystem.create_directory(str(project_path))

        folders = [
            "AI",
            "Research",
            "Innovation",
            "Documents",
            "Tasks",
            "Files",
            "Knowledge"
        ]

        for folder in folders:

            FileSystem.create_directory(
                str(project_path / folder)
            )

        database = JsonDatabase(
            str(project_path / "project.aether")
        )

        database.save(
            {
                "name": project_name,
                "version": "1.0.0",
                "modules": folders
            }
        )

        return project_path

    def open_project(self, project_name: str):

        project_path = self.workspace_root / project_name

        database = JsonDatabase(
            str(project_path / "project.aether")
        )

        return database.load()

    def list_projects(self):

        projects = []

        for item in self.workspace_root.iterdir():

            if item.is_dir():

                projects.append(item.name)

        return sorted(projects)

    def delete_project(self, project_name: str):

        project_path = self.workspace_root / project_name

        return FileSystem.delete_directory(
            str(project_path)
        )