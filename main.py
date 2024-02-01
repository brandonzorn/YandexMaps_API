import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import Ui_Dialog
import requests

URL = 'http://static-maps.yandex.ru/1.x'
GEOCODE_URL = 'http://geocode-maps.yandex.ru/1.x/'


class Map:
    def __init__(self):
        self.lon = 40.109920
        self.lat = 44.601329
        self.zoom = 16
        self.type: str = 'map'
        self.types = ['map', 'sat,skl', 'sat']
        self.point = {}
        self.address: str = ''
        self.display_postal = False
        self.postal = None

    @property
    def ll(self):
        return f'{self.lon},{self.lat}'

    def get_map_file(self):
        params = {'ll': self.ll, 'z': self.zoom, 'l': self.type}
        params.update(self.point)
        response = requests.get(URL, params=params)
        with open('map.jpg', 'wb') as file:
            file.write(response.content)
        return 'map.jpg'

    def update_zoom(self, count: int):
        if self.zoom + count < 0 or self.zoom + count > 21:
            return
        self.zoom += count

    def shift_type(self):
        def shift(lst, steps):
            if steps < 0:
                steps = abs(steps)
                for i in range(steps):
                    lst.append(lst.pop(0))
            else:
                for i in range(steps):
                    lst.insert(0, lst.pop())
        shift(self.types, 1)
        self.type = self.types[0]

    def update_lat(self, count):
        self.lat += count

    def update_lon(self, count):
        self.lon += count

    def set_postal(self, cond):
        self.display_postal = cond

    def get_address(self):
        if self.postal and self.display_postal:
            return self.address + f' / {self.postal}'
        return self.address

    def set_geocode(self, text: str):
        params = {'apikey': '40d1649f-0493-4b70-98ba-98533de7710b', 'geocode': text, 'format': 'json'}
        response = requests.get(GEOCODE_URL, params=params)
        if response.status_code != 200 or not response.json()['response']['GeoObjectCollection']['featureMember']:
            return
        pos: str = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        self.lon, self.lat = [float(i) for i in pos.split()]
        self.point = {'pt': f'{self.ll},vkbkm'}
        self.address = [response.json()['response']['GeoObjectCollection']['featureMember'][0]
                        ['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']][0]
        self.postal = [response.json()['response']['GeoObjectCollection']['featureMember'][0]
                       ['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address'].get('postal_code')][0]


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.map = Map()
        self.turn_step = 0.001
        self.ui.pushButton.clicked.connect(self.change_type)
        self.ui.search.clicked.connect(self.search)
        self.ui.reset.clicked.connect(self.reset)
        self.ui.checkBox.clicked.connect(self.set_postal)
        self.update_image()
        self.setFixedSize(self.minimumSize())
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.map.update_lon(-self.turn_step)
        elif event.key() == Qt.Key_Right:
            self.map.update_lon(self.turn_step)
        elif event.key() == Qt.Key_Up:
            self.map.update_lat(self.turn_step)
        elif event.key() == Qt.Key_Down:
            self.map.update_lat(-self.turn_step)
        elif event.key() == Qt.Key_PageUp:
            self.map.update_zoom(1)
        elif event.key() == Qt.Key_PageDown:
            self.map.update_zoom(-1)
        else:
            return
        self.update_image()
        event.accept()

    def change_type(self):
        self.map.shift_type()
        self.update_image()

    def search(self):
        if not self.ui.lineEdit.text():
            return
        self.map.set_geocode(self.ui.lineEdit.text())
        self.update_image()

    def update_image(self):
        self.ui.img.setPixmap(QPixmap(self.map.get_map_file()))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'map.jpg')
        os.remove(path)
        self.ui.adress.setText(self.map.get_address())
        self.ui.checkBox.setCheckable(bool(self.map.postal))
        self.setFixedSize(self.minimumSize())

    def set_postal(self):
        self.map.set_postal(self.ui.checkBox.isChecked())
        self.ui.adress.setText(self.map.get_address())

    def reset(self):
        self.map.point = {}
        self.map.address = ''
        self.map.postal = None
        self.update_image()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec())
