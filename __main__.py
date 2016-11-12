from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(480, 80))         # Устанавливаем размеры
        self.setWindowTitle("Line Edit IP Address") # Устанавливаем заголовок окна
        central_widget = QWidget(self)              # Создаём центральный виджет
        self.setCentralWidget(central_widget)       # Устанавливаем центральный виджет

        grid_layout = QGridLayout(self)         # Создаём QGridLayout
        central_widget.setLayout(grid_layout)   # Устанавливаем данное размещение в центральный виджет

        grid_layout.addWidget(QLabel("Введите IP-адрес", self), 0, 0)

        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # Часть регулярного выржение
        # Само регулярное выражение
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)   # Валидатор для QLineEdit

        lineEdit = QLineEdit()
        lineEdit.setValidator(ipValidator)      # Устанавливаем валидатор
        grid_layout.addWidget(lineEdit, 0, 1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())