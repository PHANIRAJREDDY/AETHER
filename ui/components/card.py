"""
==================================================
AETHER DESIGN SYSTEM
Component : Card
Version   : 1.0
==================================================
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from ui.styles.colors import Colors
from ui.styles.fonts import Fonts


class AetherCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setStyleSheet(f"""
            QFrame {{
                background:{Colors.CARD};
                border:1px solid {Colors.BORDER};
                border-radius:12px;
            }}

            QLabel {{
                color:{Colors.TEXT};
                border:none;
            }}
        """)

        layout = QVBoxLayout(self)

        title_label = QLabel(title)

        title_label.setStyleSheet(f"""
            color:{Colors.TEXT_SECONDARY};
            font-size:{Fonts.CARD_TITLE}px;
        """)

        value_label = QLabel(value)

        value_label.setStyleSheet(f"""
            font-size:{Fonts.CARD_VALUE}px;
            font-weight:bold;
        """)

        layout.addWidget(title_label)
        layout.addWidget(value_label)