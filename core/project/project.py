"""
=========================================================
AETHER
Project Model
Version : 1.0.0
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Project:
    """
    Represents an AETHER Project.
    """

    name: str

    project_id: str = field(default_factory=lambda: str(uuid4()))

    version: str = "1.0.0"

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    modified_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    author: str = ""

    modules: list[str] = field(
        default_factory=lambda: [
            "AI",
            "Research",
            "Innovation",
            "Documents",
            "Tasks",
            "Files",
            "Knowledge"
        ]
    )

    def rename(self, new_name: str):

        self.name = new_name

        self.touch()

    def touch(self):

        self.modified_at = datetime.now().isoformat()

    def to_dict(self):

        return {
            "project_id": self.project_id,
            "name": self.name,
            "version": self.version,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
            "author": self.author,
            "modules": self.modules,
        }

    @classmethod
    def from_dict(cls, data: dict):

        project = cls(
            name=data.get("name", "Untitled Project")
        )

        project.project_id = data.get(
            "project_id",
            project.project_id
        )

        project.version = data.get(
            "version",
            "1.0.0"
        )

        project.created_at = data.get(
            "created_at",
            project.created_at
        )

        project.modified_at = data.get(
            "modified_at",
            project.modified_at
        )

        project.author = data.get(
            "author",
            ""
        )

        project.modules = data.get(
            "modules",
            project.modules
        )

        return project

    def validate(self):

        return bool(self.name.strip())