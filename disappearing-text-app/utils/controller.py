from PyQt6.QtCore import QTimer
        
class TimerController:
    def __init__(self, update_callback, view):
        self.view = view
        self.counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000) 
        self.timer.timeout.connect(self._on_timeout)

        # Callback zum GUI z. B. Label aktualisieren
        self.update_callback = update_callback

    def _on_timeout(self):
        if self.counter == 0:
            self.view.user_input.clear()
            self.stop_timer()
        else:      
            self.counter -= 1
            self.update_callback(f"{self.counter}")

    def restart_timer(self):
        if self.timer.isActive():
            self.timer.stop()
        self.counter = 10
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()
        
