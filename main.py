from calcs.rocket_engine import *
from interface.main_window import *

def main():
    motor1 = rocket_engine()
    motor1.set_external_diameter(0.0730)
    motor1.set_wall_thickness(0.0052)
    motor1.calc_internal_radius()
    print(motor1.get_internal_radius())

    app = QApplication([])
    main_window_gui = main_window()
    main_window_gui.show()
    app.exec_()


main()
