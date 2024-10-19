import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Map Viewer')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.view = QWebEngineView()
        self.layout.addWidget(self.view)

        self.pin_button = QPushButton('Pin Location')
        self.pin_button.clicked.connect(self.pin_location)
        self.layout.addWidget(self.pin_button)

        self.rectangle_button = QPushButton('Draw Rectangle')
        self.rectangle_button.clicked.connect(self.draw_rectangle)
        self.layout.addWidget(self.rectangle_button)

        self.save_button = QPushButton('Save Map Image')
        self.save_button.clicked.connect(self.save_map_image)
        self.layout.addWidget(self.save_button)

        self.init_map()

    def init_map(self):
        self.m = folium.Map(location=[10.762622, 106.660172], zoom_start=13)
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())

    def pin_location(self):
        folium.Marker([10.762622, 106.660172], popup='Pinned Location').add_to(self.m)
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())

    def draw_rectangle(self):
        bounds = [[10.762622, 106.660172], [10.762722, 106.660272]]
        folium.Rectangle(bounds=bounds, color='blue', fill=True, fill_opacity=0.1).add_to(self.m)
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())

    def save_map_image(self):
        self.view.grab().save('map_snapshot.png')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())
