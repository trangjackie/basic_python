import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chuyển Chuỗi Thành In Hoa')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText('Nhập chuỗi vào đây...')
        self.layout.addWidget(self.input_text)

        self.process_button = QPushButton('Xử lý', self)
        self.process_button.clicked.connect(self.process_text)
        self.layout.addWidget(self.process_button)

        self.result_label = QLabel('Kết quả sẽ hiển thị ở đây', self)
        self.layout.addWidget(self.result_label)

    def process_text(self):
        input_text = self.input_text.text()
        upper_text = input_text.upper()
        self.result_label.setText(upper_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
