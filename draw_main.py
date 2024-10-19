from PyQt6.QtWidgets import QWidget, QLabel, QMainWindow, QApplication, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.app = QApplication([])
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        indication = QLabel("Введите время от которого будем отсчитывать")
        self.meaning = QLineEdit()
        launch = QPushButton("Запустить таймер")
        launch.clicked.connect(self.program_launch)
        
        control_UI.addWidget(indication)
        control_UI.addWidget(self.meaning)
        control_UI.addWidget(launch)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)

    def run(self):
        self.show()

    def program_launch(self):
        try:
            self.res = int(self.meaning.text())  # Теперь self.res
        except:
            info = QMessageBox()
            info.setWindowTitle("Ошибка")
            info.setText("Вы ввели неверное значение")
            info.exec()
            return
        
        self.countdown = QMessageBox()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Задержка в 1 секунду

    def update_timer(self):
        if self.res != 0:
            self.countdown.setText(str(self.res))
            self.res -= 1
        else:
            self.countdown.exec()
            self.timer.stop()
