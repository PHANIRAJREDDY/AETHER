"""
=========================================================
AETHER
Toolbar Component
Version : 1.0.0
=========================================================
"""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy
)


class Toolbar(QWidget):

    new_project_requested = Signal()
    open_project_requested = Signal()
    save_project_requested = Signal()
    search_requested = Signal()

    def __init__(self):

        super().__init__()

        self._build_ui()

    def _button(self, text):

        button = QPushButton(text)

        button.setMinimumHeight(38)

        button.setCursor(Qt.PointingHandCursor)

        button.setStyleSheet("""
        QPushButton{
            background:#2A2A2A;
            color:white;
            border:1px solid #404040;
            border-radius:8px;
            padding-left:16px;
            padding-right:16px;
            font-size:13px;
        }

        QPushButton:hover{
            background:#3A3A3A;
        }

        QPushButton:pressed{
            background:#1565C0;
        }
        """)

        return button

    def _build_ui(self):

        self.setFixedHeight(60)

        self.setStyleSheet("""
        QWidget{
            background:#202020;
            border-bottom:1px solid #303030;
        }
        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(12, 10, 12, 10)

        layout.setSpacing(10)

        title = QLabel("AETHER")

        title.setStyleSheet("""
        color:white;
        font-size:18px;
        font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addSpacing(20)

        self.new_btn = self._button("New")

        self.open_btn = self._button("Open")

        self.save_btn = self._button("Save")

        self.search_btn = self._button("Search")

        layout.addWidget(self.new_btn)

        layout.addWidget(self.open_btn)

        layout.addWidget(self.save_btn)

        layout.addWidget(self.search_btn)

        spacer = QWidget()

        spacer.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )

        layout.addWidget(spacer)

        version = QLabel("Desktop Engine v1.0")

        version.setStyleSheet("""
        color:#A0A0A0;
        font-size:12px;
        """)

        layout.addWidget(version)

        self.new_btn.clicked.connect(
            self.new_project_requested.emit
        )

        self.open_btn.clicked.connect(
            self.open_project_requested.emit
        )

        self.save_btn.clicked.connect(
            self.save_project_requested.emit
        )

        self.search_btn.clicked.connect(
            self.search_requested.emit
        )