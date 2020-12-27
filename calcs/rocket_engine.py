# TECSpace
# Computational rocketry
# Edgar Chaves González. edjchg@gmail.com
import math


class rocket_engine:
    def __init__(self):
        # Constants:
        self.atmospheric_pressure = 101325  # Pa
        self.speed_sound = 343.59  # m/s
        self.gravitational_accel = 9.81  # m/s**2
        # Pipe dimension:
        self.external_diameter = 0  # m
        self.wall_thickness = 0  # m
        self.internal_radius = 0  # m
        # Pipe material
        self.material = ""
        self.aleacion = 0
        self.modulo_elasticidad = 0  # Pa
        self.esfuerzo_cedencia_cortante = 0  # Pa
        self.esfuerzo_cedencia_tension = 0  # Pa
        self.esfuerzo_ultimo_cortante = 0  # Pa
        self.esfuerzo_ultimo_tension = 0  # Pa
        # Chamber
        self.chamber_pressure_psi = 800  # psi
        self.chamber_pressure_pa = 0  # Pa
        self.chamber_temperature_K = 1710  # K
        self.chamber_temperature_C = 0  # C
        # Grain
        self.grain_quantity = 0
        self.grain_internal_radius = 0  # m
        self.grain_external_radius = 0  # m
        self.grain_length = 0  # m
        self.grain_distance = 0  # m
        # desviación estandar?
        self.unit_volume = 0  # m**3
        self.unit_mass = 0  # g
        self.fuel_total_length = 0  # m
        self.port_area = 0  # m**2
        self.fuel_section_length = 0  # m
        # Fuel data
        self.const_burn_rate = 0.005
        self.pressure_e = 0.688
        self.burn_rate = 0  # m/s
        self.fuel_density = 0  # kg/m**3

    # Constants methods--------------------------------------------- #
    def get_atmospheric_pressure(self):
        return self.atmospheric_pressure

    def set_atmospheric_pressure(self, atm_pressure):
        self.atmospheric_pressure = atm_pressure

    def get_speed_sound(self):
        return self.speed_sound

    def set_speed_sound(self, new_speed):
        self.speed_sound = new_speed

    def get_gravitational_accel(self):
        return self.gravitational_accel

    def set_gravitational_accel(self, grav_accel):
        self.gravitational_accel = grav_accel

    # End constants methods--------------------------------------------- #
    # Pipe dimension --------------------------------------------------- #

    def get_external_diameter(self):
        return self.external_diameter

    def set_external_diameter(self, ext_diameter):
        self.external_diameter = ext_diameter

    def get_wall_thickness(self):
        return self.wall_thickness

    def set_wall_thickness(self, wall_thick):
        self.wall_thickness = wall_thick

    def get_internal_radius(self):
        return self.internal_radius

    def calc_internal_radius(self):
        self.internal_radius = (self.external_diameter - 2 * self.wall_thickness) / 2

    # End pipe dimension ------------------------------------------------ #
    # Pipe material------------------------------------------------------ #
    def get_material(self):
        return self.material

    def set_material(self, new_material):
        self.material = new_material

    def get_aleacion(self):
        return self.aleacion

    def set_aleacion(self, aleacion):
        self.aleacion = aleacion

    def get_modulo_elasticidad(self):
        return self.modulo_elasticidad

    def set_modulo_elasticidad(self, mod_elasticidad):
        self.modulo_elasticidad = mod_elasticidad

    def get_esfuerzo_cedencia_cortante(self):
        return self.esfuerzo_cedencia_cortante

    def set_esfuerzo_cedencia_cortante(self, esfuerzo_cedencia_cortante):
        self.esfuerzo_cedencia_cortante = esfuerzo_cedencia_cortante

    def get_esfuerzo_cedencia_tension(self):
        return self.esfuerzo_cedencia_tension

    def set_esfuerzo_cedencia_tension(self, esfuerzo_cedencia_tension):
        self.esfuerzo_cedencia_tension = esfuerzo_cedencia_tension

    def get_esfuerzo_ultimo_cortante(self):
        return self.esfuerzo_ultimo_cortante

    def set_esfuerzo_ultimo_cortante(self, esfuerzo_ultimo_cortante):
        self.esfuerzo_ultimo_cortante = esfuerzo_ultimo_cortante

    def get_esfuerzo_ultimo_tension(self):
        return self.esfuerzo_ultimo_tension

    def set_esfuerzo_ultimo_tension(self, esfuerzo_ultimo_tension):
        self.esfuerzo_ultimo_tension = esfuerzo_ultimo_tension

    # End Pipe material-------------------------------------------------- #
    # Chamber------------------------------------------------------------ #
    def get_chamber_pressure_psi(self):
        return self.chamber_pressure_psi

    def set_chamber_pressure_psi(self, chamber_pressure_psi):
        self.chamber_pressure_psi = chamber_pressure_psi
        self.chamber_pressure_pa = chamber_pressure_psi * 6894.757
        # There are some if to ask:

    def get_chamber_pressure_pa(self):
        return self.chamber_pressure_pa

    def set_chamber_pressure_pa(self, chamber_pressure_pa):
        self.chamber_pressure_pa = chamber_pressure_pa
        self.chamber_pressure_psi = chamber_pressure_pa / 6894.757
        # There are some if to ask:

    def get_chamber_temperature_k(self):
        return self.chamber_temperature_K

    def set_chamber_temperature_k(self, chamber_temperature_K):
        self.chamber_temperature_K = chamber_temperature_K

    def calc_chamber_temperature_C(self):
        self.chamber_temperature_C = self.chamber_temperature_K - 273.15

    def get_chamber_temperature_C(self):
        return self.chamber_temperature_C

    def set_chamber_temperature_C(self, chamber_temperature_C):
        self.chamber_temperature_C = chamber_temperature_C

    def calc_chamber_temperature_K(self):
        self.chamber_temperature_K = self.chamber_temperature_C + 273.15

    # End chamber-------------------------------------------------------- #
    # Grain-------------------------------------------------------------- #
    def get_grain_quantity(self):
        return self.grain_quantity

    def set_grain_quantity(self, grain_quantity):
        self.grain_quantity = grain_quantity

    def get_grain_internal_radius(self):
        return self.grain_internal_radius

    def set_grain_internal_radius(self, grain_internal_radius):
        self.grain_internal_radius = grain_internal_radius

    def get_grain_external_radius(self):
        return self.grain_external_radius

    def calc_grain_external_radius(self):
        self.grain_external_radius = self.internal_radius - 0.001

    def get_grain_length(self):
        return self.grain_length

    def set_grain_length(self, grain_length):
        self.grain_length = grain_length

    def get_grain_distance(self):
        return self.grain_distance

    def set_grain_distance(self, grain_distance):
        self.grain_distance = grain_distance

    def get_unit_volume(self):
        return self.unit_volume

    def calc_unit_volume(self):
        self.unit_volume = math.pi * self.grain_length * (
                self.grain_external_radius ** 2 - self.grain_internal_radius ** 2)

    def get_unit_mass(self):
        return self.unit_mass

    def calc_unit_mass(self):
        self.unit_mass = self.unit_volume * 1000 * self.fuel_density

    def get_fuel_total_length(self):
        return self.fuel_total_length

    def calc_fuel_total_length(self):
        self.fuel_total_length = self.grain_length * self.grain_quantity

    def get_port_area(self):
        return self.port_area

    def calc_port_area(self):
        self.port_area = math.pi * self.grain_internal_radius ** 2

    def get_fuel_section_length(self):
        return self.fuel_section_length

    def calc_fuel_section_length(self):
        self.fuel_section_length = self.grain_distance * (
                self.grain_quantity - 1) + self.grain_length * self.grain_quantity

    # End grain---------------------------------------------------------- #
    # Fuel data---------------------------------------------------------- #
    def get_const_burn_rate(self):
        return self.const_burn_rate

    def set_const_burn_rate(self, const_burn_rate):
        self.const_burn_rate = const_burn_rate

    def get_pressure_e(self):
        return self.pressure_e

    def set_pressure_e(self, pressure_e):
        self.pressure_e = pressure_e

    def get_burn_rate(self):
        return self.burn_rate

    def calc_burn_rate(self):
        self.burn_rate = (self.const_burn_rate * ((self.chamber_pressure_pa * 0.000145038) ** self.pressure_e)) * 0.0254

    def get_fuel_density(self):
        return self.fuel_density

    def set_fuel_density(self, fuel_density):
        self.fuel_density = fuel_density
