import sys
import numpy as np
import pygame
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt

class PianoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Virtual Piano')
        self.setGeometry(100, 100, 1000, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.keys = [
            ('C', 261.63), ('C#', 277.18), ('D', 293.66), ('D#', 311.13),
            ('E', 329.63), ('F', 349.23), ('F#', 369.99), ('G', 392.00),
            ('G#', 415.30), ('A', 440.00), ('A#', 466.16), ('B', 493.88),
        ]

        pygame.mixer.init()

        for key, freq in self.keys:
            button = QPushButton(key)
            button.setFixedSize(80, 200)
            if '#' in key:  # Sharp keys are black
                button.setStyleSheet('background-color: black; color: white;')
            else:  # Natural keys are white
                button.setStyleSheet('background-color: white; color: black;')
            button.clicked.connect(lambda _, f=freq: self.play_sound(f))
            self.button_layout.addWidget(button)

    def play_sound(self, frequency, duration=1.0, samplerate=44100):
        t = np.linspace(0, duration, int(samplerate * duration), False)
        note = np.sin(frequency * t * 2 * np.pi)
        stereo_note = np.column_stack((note, note))  # Make it 2-dimensional
        sound = pygame.sndarray.make_sound((stereo_note * 32767).astype(np.int16))
        sound.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PianoApp()
    window.show()
    sys.exit(app.exec())
