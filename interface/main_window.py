# Tutorial: https://www.youtube.com/watch?v=Oy5saLTejtY
# Tutorial2: https://www.youtube.com/watch?v=DpSerOAZR9w
# Tutorial3: https://www.youtube.com/watch?v=Vl0Z_0DRs_Q

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from calcs.rocket_engine import *


class main_window(QMainWindow):
    def __init__(self):
        self.engine = rocket_engine()
        super().__init__()
        uic.loadUi("interface/prueba.ui", self)
        self.save_data_button.clicked.connect(self.function_save_data_first_tab)

        self.external_diameter_entry.setValidator(QDoubleValidator(99999, -99999, 8))
        self.wall_thickness_entry.setValidator(QDoubleValidator(99999, -99999, 8))
        self.modulo_elasticidad_entry.setValidator(QDoubleValidator(999999999, -99999999, 8))
        self.esfuerzo_cedencia_cortante_entry.setValidator(QDoubleValidator(999999999, -99999999, 8))
        self.esfuerzo_cedencia_tension_entry.setValidator(QDoubleValidator(999999999, -99999999, 8))
        self.esfuerzo_ultimo_cedencia_entry.setValidator(QDoubleValidator(999999999, -99999999, 8))
        self.esfuerzo_ultimo_tension_entry.setValidator(QDoubleValidator(999999999, -99999999, 8))

        self.chamber_pressure_entry.setValidator(QDoubleValidator(999999999, -99999999, 8))
        self.chamber_temperature_entry.setValidator(QDoubleValidator(999999999, -99999999, 8))

    def function_save_data_first_tab(self):
        external_diameter = self.external_diameter_entry.text()
        wall_thickness = self.wall_thickness_entry.text()
        material = self.material_entry.text()
        aleacion = self.aleacion_entry.text()
        modulo_elasticidad = self.modulo_elasticidad_entry.text()
        esfuerzo_cedencia_c = self.esfuerzo_cedencia_cortante_entry.text()
        esfuerzo_cedencia_t = self.esfuerzo_cedencia_tension_entry.text()
        esfuerzo_ultimo_c = self.esfuerzo_ultimo_cedencia_entry.text()
        esfuerzo_ultimo_t = self.esfuerzo_ultimo_tension_entry.text()

        if external_diameter == "" or wall_thickness == "" or material == "" or aleacion == "" or modulo_elasticidad == "" or esfuerzo_cedencia_c == "" or esfuerzo_cedencia_t == "" or esfuerzo_ultimo_c == "" or esfuerzo_ultimo_t == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Datos faltantes")
            msg.setInformativeText("Algunos de los campos se encuentran vacíos, todos los datos deben ser rellenados.")
            msg.exec_()
        else:

            external_diameter = external_diameter.replace(",", ".", 1)
            external_diameter = float(external_diameter)
            self.engine.set_external_diameter(external_diameter)

            wall_thickness = wall_thickness.replace(",", ".", 1)
            wall_thickness = float(wall_thickness)
            self.engine.set_wall_thickness(wall_thickness)

            self.engine.set_material(material)
            self.engine.set_aleacion(aleacion)

            modulo_elasticidad = modulo_elasticidad.replace(",", ".", 1)
            modulo_elasticidad = float(modulo_elasticidad)
            self.engine.set_modulo_elasticidad(modulo_elasticidad)

            esfuerzo_cedencia_c = esfuerzo_cedencia_c.replace(",", ".", 1)
            esfuerzo_cedencia_c = float(esfuerzo_cedencia_c)
            self.engine.set_esfuerzo_cedencia_cortante(esfuerzo_cedencia_c)

            esfuerzo_cedencia_t = esfuerzo_cedencia_t.replace(",", ".", 1)
            esfuerzo_cedencia_t = float(esfuerzo_cedencia_t)
            self.engine.set_esfuerzo_cedencia_tension(esfuerzo_cedencia_t)

            esfuerzo_ultimo_c = esfuerzo_ultimo_c.replace(",", ".", 1)
            esfuerzo_ultimo_c = float(esfuerzo_ultimo_c)
            self.engine.set_esfuerzo_ultimo_cortante(esfuerzo_ultimo_c)

            esfuerzo_ultimo_t = esfuerzo_ultimo_t.replace(",", ".", 1)
            esfuerzo_ultimo_t = float(esfuerzo_ultimo_t)
            self.engine.set_esfuerzo_ultimo_tension(esfuerzo_ultimo_t)

            print("Guardar Datos: ", external_diameter, wall_thickness)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Datos guardados correctamente")
            msg.setInformativeText("Todos los datos de la pestaña 'Constantes' han sido guardados exitosamente.")
            msg.exec_()





