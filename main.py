import sys

from PySide6.QtWidgets import QApplication
import qdarktheme

from core.kernel.startup import startup
from ui.windows.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setStyleSheet(qdarktheme.load_stylesheet())

    controller = startup()

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()