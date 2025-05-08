# ------------------------ Imports ------------------------- #
from gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

# ------------------------ Program Loop ------------------------- #

app = QApplication([])

window = MainWindow()
window.show()


app.exec()


# ------------------------ TODO's ------------------------------- #
# TODO: GUI erstellen

# TODO: Timer der nach 5 Sekunden nichts schreiben das Textfeld cleared
# TODO: Timer anzeigen / schönere Anzeige 