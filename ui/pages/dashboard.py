from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QFrame,
    QPushButton
)
from PySide6.QtCore import Qt


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def create_card(self, title, value):

        card = QFrame()

        card.setStyleSheet("""
            QFrame{
                background:#252525;
                border:1px solid #3A3A3A;
                border-radius:12px;
            }

            QLabel{
                color:white;
            }
        """)

        layout = QVBoxLayout(card)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size:14px;
            color:#AAAAAA;
        """)

        value_label = QLabel(value)
        value_label.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        return card

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(30,30,30,30)
        root.setSpacing(25)

        title = QLabel("Dashboard")
        title.setStyleSheet("""
            color:white;
            font-size:34px;
            font-weight:bold;
        """)

        subtitle = QLabel("Welcome back to AETHER")
        subtitle.setStyleSheet("""
            color:#B0B0B0;
            font-size:16px;
        """)

        root.addWidget(title)
        root.addWidget(subtitle)

        grid = QGridLayout()
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        cards = [

            ("AI Models","6"),

            ("Projects","3"),

            ("Research Papers","0"),

            ("Patents","0"),

            ("Documents","0"),

            ("Tasks","0")

        ]

        row = 0
        col = 0

        for title,value in cards:

            grid.addWidget(self.create_card(title,value),row,col)

            col += 1

            if col == 3:
                col = 0
                row += 1

        root.addLayout(grid)

        quick = QLabel("Quick Actions")

        quick.setStyleSheet("""
            color:white;
            font-size:22px;
            font-weight:bold;
        """)

        root.addWidget(quick)

        buttons = QGridLayout()

        names = [

            "New Project",
            "Research",
            "Patent Studio",
            "Open Workspace"

        ]

        row = 0
        col = 0

        for name in names:

            btn = QPushButton(name)

            btn.setMinimumHeight(50)

            btn.setStyleSheet("""

                QPushButton{

                    background:#2E7DFF;

                    color:white;

                    border:none;

                    border-radius:10px;

                    font-size:15px;

                }

                QPushButton:hover{

                    background:#4A91FF;

                }

            """)

            buttons.addWidget(btn,row,col)

            col += 1

            if col == 2:

                row += 1
                col = 0

        root.addLayout(buttons)

        root.addStretch()