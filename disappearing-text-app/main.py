# ------------------------ Imports ------------------------- #
from gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, Qt

# ------------------------ Splash Class ------------------------- #

class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

# ------------------------ Program Loop ------------------------- #

app = QApplication([])

pixmap = QPixmap("disappearing-text-app/assets/logo.png").scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
splash = SplashScreen(pixmap)
splash.show()

QTimer.singleShot(2000, splash.close)


window = MainWindow()

QTimer.singleShot(2000, window.show)

app.exec()


# ------------------------ TODO's ------------------------------- #
# TODO: GUI erstellen

# TODO: Timer der nach 5 Sekunden nichts schreiben das Textfeld cleared
# TODO: Timer anzeigen / schönere Anzeige 