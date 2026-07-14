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
    QSizePolicy,
)


class Toolbar(QWidget):

    new_project_clicked = Signal()
    open_project_clicked = Signal()
    save_project_clicked = Signal()
    ai_clicked = Signal()
    research_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.build_ui()

    def create_button(self, text):

        button = QPushButton(text)

        button.setMinimumHeight(38)

        button.setCursor(Qt.PointingHandCursor)

        button.setStyleSheet("""
        QPushButton{

            background:#2A2A2A;
            color:white;
            border:1px solid #404040;
            border-radius:8px;
            padding-left:14px;
            padding-right:14px;
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

    def build_ui(self):

        self.setFixedHeight(60)

        self.setStyleSheet("""
        QWidget{

            background:#202020;
            border-bottom:1px solid #333333;

        }
        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(12,10,12,10)

        layout.setSpacing(10)

        title = QLabel("AETHER")

        title.setStyleSheet("""

            color:white;

            font-size:18px;

            font-weight:bold;

        """)

        layout.addWidget(title)

        layout.addSpacing(20)

        self.new_btn = self.create_button("New Project")
        self.open_btn = self.create_button("Open")
        self.save_btn = self.create_button("Save")
        self.ai_btn = self.create_button("AI Team")
        self.research_btn = self.create_button("Research")

        layout.addWidget(self.new_btn)
        layout.addWidget(self.open_btn)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.ai_btn)
        layout.addWidget(self.research_btn)

        spacer = QWidget()
        spacer.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )

        layout.addWidget(spacer)

        status = QLabel("Desktop Framework v0.3.0")

        status.setStyleSheet("""

            color:#AAAAAA;

            font-size:12px;

        """)

        layout.addWidget(status)

        self.new_btn.clicked.connect(
            self.new_project_clicked.emit
        )

        self.open_btn.clicked.connect(
            self.open_project_clicked.emit
        )

        self.save_btn.clicked.connect(
            self.save_project_clicked.emit
        )

        self.ai_btn.clicked.connect(
            self.ai_clicked.emit
        )

        self.research_btn.clicked.connect(
            self.research_clicked.emit
        )