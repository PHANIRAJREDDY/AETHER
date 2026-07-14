"""
=========================================================
AETHER
Logger
=========================================================
"""

from datetime import datetime


class Logger:

    def info(self, message):

        print(
            f"[INFO] {datetime.now().strftime('%H:%M:%S')} | {message}"
        )

    def warning(self, message):

        print(
            f"[WARNING] {datetime.now().strftime('%H:%M:%S')} | {message}"
        )

    def error(self, message):

        print(
            f"[ERROR] {datetime.now().strftime('%H:%M:%S')} | {message}"
        )