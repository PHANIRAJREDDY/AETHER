"""
=========================================================
AETHER
JSON Database
Version : 1.0.0
=========================================================
"""

import json
from pathlib import Path


class JsonDatabase:
    """
    Lightweight JSON database used by AETHER.

    Provides safe loading and saving of JSON files.
    """

    def __init__(self, database_path: str):

        self.database_path = Path(database_path)

        if not self.database_path.exists():

            self.database_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            self.database_path.write_text(
                "{}",
                encoding="utf-8"
            )

    def load(self) -> dict:

        try:

            with open(
                self.database_path,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except Exception:

            return {}

    def save(self, data: dict):

        with open(
            self.database_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def exists(self) -> bool:

        return self.database_path.exists()

    def clear(self):

        self.save({})

    def delete(self):

        if self.database_path.exists():

            self.database_path.unlink()