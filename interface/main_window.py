# Tutorial: https://www.youtube.com/watch?v=Oy5saLTejtY
# Tutorial2: https://www.youtube.com/watch?v=DpSerOAZR9w

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic


Form, Window = uic.loadUiType("prueba.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()


'''
# Instance of the main app, is singleton so just call it once:
rocket_designer_gui = QApplication([])

# Instance of the main window
window = QMainWindow()
window.setFixedSize(700, 500)
window.setWindowTitle("TECSpace: Rocket engine designer")

label1 = QLabel("Prueba", window)
label1.setStyleSheet("background:#424242; color:#fff")

# Shows the window
window.show()

# Start a event cycle, main thread:
rocket_designer_gui.exec_()
'''