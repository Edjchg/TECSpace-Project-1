# Tutorial: https://www.youtube.com/watch?v=Oy5saLTejtY
# Tutorial2: https://www.youtube.com/watch?v=DpSerOAZR9w
# Tutorial3: https://www.youtube.com/watch?v=Vl0Z_0DRs_Q

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface/prueba.ui", self)
        self.save_data_button.clicked.connect(self.function_save_data_first_tab)

        self.external_diameter_entry.setValidator(QDoubleValidator(99999, -99999, 8))
        self.wall_thickness_entry.setValidator(QDoubleValidator(99999, -99999, 8))

    def function_save_data_first_tab(self):
        external_diameter = self.external_diameter_entry.text()
        wall_thickness = self.wall_thickness_entry.text()

        if external_diameter == "" or wall_thickness == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Datos faltantes")
            msg.setInformativeText("Algunos de los campos se encuentran vacíos, todos los datos deben ser rellenados.")
            msg.exec_()
        else:

            external_diameter = external_diameter.replace(",", ".", 1)
            external_diameter = float(external_diameter)
            wall_thickness = wall_thickness.replace(",", ".", 1)
            wall_thickness = float(wall_thickness)
            print("Guardar Datos: ", external_diameter, wall_thickness)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Datos guardados correctamente")
            msg.setInformativeText("Todos los datos de la pestaña 'Constantes' han sido guardados exitosamente.")
            msg.exec_()





