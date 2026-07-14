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

        self.buttons = {}

        self._build_ui()

    def _build_ui(self):

        self.setFixedWidth(240)

        self.setStyleSheet("""
        QFrame{
            background:#171717;
            border-right:1px solid #303030;
        }

        QLabel{
            color:white;
            font-size:22px;
            font-weight:bold;
            padding:20px;
        }

        QPushButton{
            background:transparent;
            color:white;
            border:none;
            text-align:left;
            padding:14px;
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

            ("Projects", "projects"),

            ("Innovation Lab", "innovation"),

            ("Documents", "documents"),

            ("Settings", "settings")

        ]

        for text, page in pages:

            button = QPushButton(text)

            button.setCheckable(True)

            button.clicked.connect(
                lambda checked, p=page: self.change_page(p)
            )

            self.buttons[page] = button

            layout.addWidget(button)

        layout.addStretch()

        self.change_page("dashboard")

    def change_page(self, page):

        for button in self.buttons.values():

            button.setChecked(False)

        if page in self.buttons:

            self.buttons[page].setChecked(True)

        self.page_requested.emit(page)