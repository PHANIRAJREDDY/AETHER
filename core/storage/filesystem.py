"""
=========================================================
AETHER
File System
Version : 1.0.0
=========================================================
"""

from pathlib import Path
import shutil


class FileSystem:
    """
    Handles all file and directory operations for AETHER.
    """

    @staticmethod
    def exists(path: str) -> bool:
        return Path(path).exists()

    @staticmethod
    def create_directory(path: str) -> Path:
        directory = Path(path)
        directory.mkdir(parents=True, exist_ok=True)
        return directory

    @staticmethod
    def create_file(path: str, content: str = "") -> Path:
        file = Path(path)

        if not file.parent.exists():
            file.parent.mkdir(parents=True, exist_ok=True)

        file.write_text(content, encoding="utf-8")

        return file

    @staticmethod
    def read_file(path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

    @staticmethod
    def write_file(path: str, content: str) -> None:
        Path(path).write_text(content, encoding="utf-8")

    @staticmethod
    def delete_file(path: str) -> bool:
        file = Path(path)

        if not file.exists():
            return False

        file.unlink()

        return True

    @staticmethod
    def delete_directory(path: str) -> bool:
        directory = Path(path)

        if not directory.exists():
            return False

        shutil.rmtree(directory)

        return True

    @staticmethod
    def list_files(path: str):
        directory = Path(path)

        if not directory.exists():
            return []

        return list(directory.iterdir())

    @staticmethod
    def copy_file(source: str, destination: str) -> None:
        shutil.copy2(source, destination)

    @staticmethod
    def move_file(source: str, destination: str) -> None:
        shutil.move(source, destination)

    @staticmethod
    def rename(source: str, destination: str) -> None:
        Path(source).rename(destination)