"""
AETHER Theme
"""

from ui.styles.colors import Colors


class Theme:

    @staticmethod
    def window():

        return f"""
        background:{Colors.WINDOW};
        """

    @staticmethod
    def sidebar():

        return f"""
        background:{Colors.SIDEBAR};
        border-right:1px solid {Colors.BORDER};
        """

    @staticmethod
    def card():

        return f"""
        background:{Colors.CARD};
        border:1px solid {Colors.BORDER};
        border-radius:12px;
        """

    @staticmethod
    def button():

        return f"""
        QPushButton{{

            background:{Colors.PRIMARY};

            color:white;

            border:none;

            border-radius:10px;

            padding:12px;

        }}

        QPushButton:hover{{

            background:{Colors.PRIMARY_HOVER};

        }}

        QPushButton:pressed{{

            background:{Colors.PRIMARY_PRESSED};

        }}
        """