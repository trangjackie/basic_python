import sys
import cv2
import numpy as np
import pyautogui
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QLabel, QRadioButton, QWidget
from PyQt6.QtCore import Qt, QRect, QPoint
from PyQt6.QtGui import QPainter, QPen

class RecorderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Screen Recorder')
        self.setGeometry(100, 100, 300, 200)

        self.is_recording = False
        self.selecting_area = False
        self.start_point = QPoint()
        self.end_point = QPoint()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.full_screen_radio = QRadioButton('Full Screen', self)
        self.full_screen_radio.setChecked(True)
        self.layout.addWidget(self.full_screen_radio)

        self.custom_area_radio = QRadioButton('Custom Area', self)
        self.custom_area_radio.clicked.connect(self.enable_area_selection)
        self.layout.addWidget(self.custom_area_radio)

        self.record_button = QPushButton('Record', self)
        self.record_button.clicked.connect(self.start_recording)
        self.layout.addWidget(self.record_button)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_recording)
        self.layout.addWidget(self.stop_button)

    def enable_area_selection(self):
        self.selecting_area = True
        self.repaint()

    def paintEvent(self, event):
        if self.selecting_area:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.GlobalColor.red, 3, Qt.PenStyle.SolidLine))
            rect = QRect(self.start_point, self.end_point)
            painter.drawRect(rect)

    def mousePressEvent(self, event):
        if self.selecting_area:
            self.start_point = event.globalPosition().toPoint()
            self.end_point = self.start_point
            self.update()

    def mouseMoveEvent(self, event):
        if self.selecting_area:
            self.end_point = event.globalPosition().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.selecting_area:
            self.end_point = event.globalPosition().toPoint()
            self.selecting_area = False
            self.update()

    def start_recording(self):
        self.is_recording = True
        self.record_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        output_file, _ = QFileDialog.getSaveFileName(self, "Save Video", "", "MP4 Files (*.mp4)")

        if output_file:
            if self.custom_area_radio.isChecked():
                screen_size = (self.end_point.x() - self.start_point.x(), self.end_point.y() - self.start_point.y())
                screen_area = (self.start_point.x(), self.start_point.y(), screen_size[0], screen_size[1])
            else:
                screen_size = pyautogui.size()
                screen_area = (0, 0, screen_size.width, screen_size.height)

            codec = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(output_file, codec, 10.0, screen_size)

            def record_screen():
                while self.is_recording:
                    img = pyautogui.screenshot(region=screen_area)
                    frame = np.array(img)
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Update color conversion order
                    out.write(frame)

            self.recording_thread = threading.Thread(target=record_screen)
            self.recording_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        if hasattr(self, 'recording_thread'):
            self.recording_thread.join()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecorderApp()
    window.show()
    sys.exit(app.exec())
