from PyQt6.QtWidgets import QApplication
from draw_main import MainWindow

app = QApplication([])

start = MainWindow()
start.run()

app.exec()