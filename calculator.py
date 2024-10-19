import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Máy Tính Bỏ Túi')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.display = QLineEdit(self)
        self.layout.addWidget(self.display)

        self.button_layout = QGridLayout()
        self.layout.addLayout(self.button_layout)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for btn_text, row, col in buttons:
            self.create_button(btn_text, row, col)

        self.clear_button = QPushButton('C', self)
        self.clear_button.clicked.connect(self.clear_display)
        self.button_layout.addWidget(self.clear_button, 4, 0, 1, 4)

    def create_button(self, text, row, col):
        button = QPushButton(text, self)
        button.clicked.connect(lambda: self.on_button_click(text))
        self.button_layout.addWidget(button, row, col)

    def on_button_click(self, char):
        if char == '=':
            self.calculate_result()
        else:
            self.display.setText(self.display.text() + char)

    def calculate_result(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error')

    def clear_display(self):
        self.display.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
