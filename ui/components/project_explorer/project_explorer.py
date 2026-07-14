"""
=========================================================
AETHER
Project Explorer
Version : 1.0.0
=========================================================
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QHBoxLayout,
)


class ProjectExplorer(QWidget):

    new_project_requested = Signal()
    open_project_requested = Signal()
    delete_project_requested = Signal()
    refresh_requested = Signal()

    def __init__(self):

        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Projects")

        title.setStyleSheet("""
            color:white;
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.project_list = QListWidget()

        self.project_list.setStyleSheet("""
            QListWidget{
                background:#252525;
                color:white;
                border:1px solid #404040;
                border-radius:8px;
                padding:5px;
            }
        """)

        layout.addWidget(self.project_list)

        buttons = QHBoxLayout()

        self.new_btn = QPushButton("New")

        self.open_btn = QPushButton("Open")

        self.delete_btn = QPushButton("Delete")

        self.refresh_btn = QPushButton("Refresh")

        for button in [
            self.new_btn,
            self.open_btn,
            self.delete_btn,
            self.refresh_btn
        ]:

            button.setMinimumHeight(40)

            buttons.addWidget(button)

        layout.addLayout(buttons)

        self.new_btn.clicked.connect(
            self.new_project_requested.emit
        )

        self.open_btn.clicked.connect(
            self.open_project_requested.emit
        )

        self.delete_btn.clicked.connect(
            self.delete_project_requested.emit
        )

        self.refresh_btn.clicked.connect(
            self.refresh_requested.emit
        )

    def set_projects(self, projects):

        self.project_list.clear()

        self.project_list.addItems(projects)

    def selected_project(self):

        item = self.project_list.currentItem()

        if item is None:

            return None

        return item.text()