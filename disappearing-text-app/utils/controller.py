from PyQt6.QtCore import QTimer
from constants import *
import os
import json
        
class Controller:
    def __init__(self, view):
        self.view = view
        self.counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000) 
        self.timer.timeout.connect(self._on_timeout)

    def _on_timeout(self):
        if self.counter == 0:
            self.view.user_input.clear()
            self.stop_timer()
        else:      
            self.counter -= 1
            self.view.timer_label.setText(f"Remaining Seconds: {self.counter}")

        if self.counter < 2:
            self.view.user_input.setStyleSheet("""
                QTextEdit {
                    color: rgba(46, 61, 73, 30);
                }                                       
        """)
        elif self.counter < 4:
            self.view.user_input.setStyleSheet("""
                QTextEdit {
                    color: rgba(46, 61, 73, 65);
                }                                       
        """)
        elif self.counter < 6:
            self.view.user_input.setStyleSheet("""
                QTextEdit {
                    color: rgba(46, 61, 73, 125);
                }                                       
        """)
        else:
            self.view.user_input.setStyleSheet("""
                QTextEdit {
                    color: rgba(46, 61, 73, 250);
                }                                       
        """)

    def restart_timer(self):
        if self.timer.isActive():
            self.timer.stop()
        self.counter = 10
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def save_text(self):
        new_text = {
            "text": self.view.user_input.toPlainText()
            }
        
        data = []

        if os.path.exists(FILEPATH):
            with open(FILEPATH, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    pass
        
        data.append(new_text)

        with open(FILEPATH, "w") as file:
            json.dump(data, file, indent=4)
        
        self.view.user_input.clear()
        self.stop_timer()

        

        
