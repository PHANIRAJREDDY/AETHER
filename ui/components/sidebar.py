"""
=========================================================
AETHER
Sidebar Component
Version : 1.0.0
=========================================================
"""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Sidebar(QFrame):

    page_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")

        self.setFixedWidth(260)

        self.buttons = {}

        self.build_ui()

    def build_ui(self):

        self.setStyleSheet("""
        QFrame#sidebar{
            background:#171717;
            border-right:1px solid #303030;
        }

        QLabel{
            color:white;
            font-size:24px;
            font-weight:bold;
            padding:20px;
        }

        QPushButton{
            color:white;
            background:transparent;
            border:none;
            padding:14px;
            text-align:left;
            font-size:14px;
        }

        QPushButton:hover{
            background:#2E7DFF;
        }

        QPushButton:checked{
            background:#1565C0;
        }
        """)

        layout = QVBoxLayout(self)

        title = QLabel("AETHER")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        pages = [
            ("Dashboard", "dashboard"),
            ("AI Team", "ai"),
            ("Research", "research"),
            ("Innovation Lab", "innovation"),
            ("Projects", "projects"),
            ("Documents", "documents"),
            ("Settings", "settings"),
        ]

        for text, page in pages:

            button = QPushButton(text)

            button.setCheckable(True)

            button.clicked.connect(
                lambda checked, p=page: self.select_page(p)
            )

            layout.addWidget(button)

            self.buttons[page] = button

        layout.addStretch()

        self.select_page("dashboard")

    def select_page(self, page):

        for button in self.buttons.values():

            button.setChecked(False)

        if page in self.buttons:

            self.buttons[page].setChecked(True)

        self.page_requested.emit(page)