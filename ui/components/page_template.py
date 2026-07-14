from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from ui.styles.colors import Colors


class PageTemplate(QWidget):

    def __init__(self, title: str, subtitle: str):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(10)


        title_label = QLabel(title)

        title_label.setStyleSheet(f"""
            color:{Colors.TEXT};
            font-size:32px;
            font-weight:bold;
        """)

        subtitle_label = QLabel(subtitle)

        subtitle_label.setStyleSheet(f"""
            color:{Colors.TEXT_SECONDARY};
            font-size:15px;
        """)

        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)

        layout.addStretch()