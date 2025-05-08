# ------------------------ Imports ------------------------- #
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTextEdit, QPushButton
from constants import *
from utils.controller import Controller
from PyQt6.QtGui import QPixmap

# ------------------------ Class ------------------------- #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GhostText")
        self.ui_setup()

    def ui_setup(self):
        self.logo_label = QLabel(self)
        pixmap_logo = QPixmap("disappearing-text-app/assets/logo.png")
        scaled_logo = pixmap_logo.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.logo_label.setPixmap(scaled_logo)
        self.logo_label.setFixedHeight(100)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.timer_label = QLabel("Remaining Seconds: 10")
        self.timer_label.setObjectName("timer")
        self.timer_label.setFixedHeight(50)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.user_input = QTextEdit()
        self.user_input.setPlaceholderText("Write a story, after 10 seconds without typing your text will disappear.")
        self.user_input.setFixedHeight(300)
        self.user_input.setFixedWidth(550)

        self.controller = Controller(self)
        self.user_input.textChanged.connect(self.controller.restart_timer)

        self.save_button = QPushButton("Save Text")
        self.save_button.setFixedHeight(50)
        self.save_button.setFixedWidth(200)
        self.save_button.clicked.connect(self.controller.save_text)

        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.user_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(20)

        container = QWidget()
        container.setLayout(layout)

        self.setFixedSize(QSize(750, 600))

        self.setCentralWidget(container)

        # ----------------------- Styling ------------------------- #

        self.setStyleSheet(f"""
        QWidget {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
            font-family: Roboto;
            font-size: 15px;
        }}
        QPushButton {{
            background-color: {BUTTON_BACKGROUND};
            color: {BUTTON_TEXT_COLOR};
            border-radius: 8px;
            padding: 8px;
        }}
        QPushButton:hover {{
            background-color: {HIGHLIGHT_COLOR};
        }}
        QPushButton:pressed {{
            background-color: {CLICKED_COLOR};
        }}
        QLabel#title {{
            font-size: 30px;
        }}
        QLabel#timer {{
            font-size: 20px;
        }}
        QTextEdit {{
            border: 1px solid {BORDER_COLOR};
            border-radius: 5px;
            padding: 5px;
            background: {INPUT_BACKGROUND};
        }}
        QScrollBar:vertical {{
            background: transparent;
            width: 10px;
            margin: 0px;
        }}

        QScrollBar::handle:vertical {{
            background: {SCROLL_BAR_COLOR};
            border-radius: 5px;
            min-height: 20px;
        }}

        QScrollBar::handle:vertical:hover {{
            background: {SCROLL_BAR_HOVER_COLOR};
        }}

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height: 0px;
        }}

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {{
            background: none;
        }}
        """)

    # ----------------------- Functions ------------------------- #

