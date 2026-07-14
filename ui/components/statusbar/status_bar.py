"""
=========================================================
AETHER
Status Bar
Version : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)


class StatusBar(QWidget):

    def __init__(self):

        super().__init__()

        self._build_ui()

    def _build_ui(self):

        self.setFixedHeight(30)

        self.setStyleSheet("""
        QWidget{
            background:#1A1A1A;
            border-top:1px solid #303030;
        }

        QLabel{
            color:#A0A0A0;
            font-size:12px;
        }
        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(10, 0, 10, 0)

        self.version = QLabel("AETHER v0.3.0-alpha")

        self.workspace = QLabel("Workspace : Ready")

        self.status = QLabel("Status : Idle")

        layout.addWidget(self.version)

        layout.addStretch()

        layout.addWidget(self.workspace)

        layout.addSpacing(20)

        layout.addWidget(self.status)

    def set_status(self, text):

        self.status.setText(f"Status : {text}")

    def set_workspace(self, text):

        self.workspace.setText(f"Workspace : {text}")