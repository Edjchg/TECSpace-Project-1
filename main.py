from calcs.rocket_engine import *


def main():
    motor1 = rocket_engine()
    motor1.set_external_diameter(0.0730)
    motor1.set_wall_thickness(0.0052)
    motor1.calc_internal_radius()
    print(motor1.get_internal_radius())


main()
