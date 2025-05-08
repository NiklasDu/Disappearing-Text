# ------------------------ Imports ------------------------- #
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTextEdit, QPushButton
from constants import *
from utils.controller import TimerController

# ------------------------ Class ------------------------- #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GhostText")
        self.ui_setup()

    def ui_setup(self):
        self.title_label = QLabel("GhostText")
        self.title_label.setObjectName("title")
        self.title_label.setFixedHeight(50)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.timer_label = QLabel("10")
        self.timer_label.setObjectName("timer")
        self.timer_label.setFixedHeight(50)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.user_input = QTextEdit()
        self.user_input.setPlaceholderText("Write a story.\nAfter 10 seconds without typing your text will disappear.")
        self.user_input.setFixedHeight(300)
        self.user_input.setFixedWidth(550)

        self.controller = TimerController(self.update_label, self)
        self.user_input.textChanged.connect(self.controller.restart_timer)

        self.save_button = QPushButton("Save Text")
        self.save_button.setFixedHeight(50)
        self.save_button.setFixedWidth(200)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
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

    def update_label(self, text):
        self.timer_label.setText(text)
