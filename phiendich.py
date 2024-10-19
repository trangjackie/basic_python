import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QLabel, QWidget
from googletrans import Translator

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vietnamese to German Translator')
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText('Nhập văn bản bằng tiếng Việt...')
        self.input_text.textChanged.connect(self.translate_text)
        self.layout.addWidget(self.input_text)

        self.translated_label = QLabel('Dịch sang tiếng Đức sẽ hiện ở đây', self)
        self.layout.addWidget(self.translated_label)

        self.translator = Translator()

    def translate_text(self):
        text = self.input_text.text()
        if text:
            translation = self.translator.translate(text, src='vi', dest='de')
            self.translated_label.setText(translation.text)
        else:
            self.translated_label.setText('Dịch sang tiếng Đức sẽ hiện ở đây')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec())
