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
        # Scape gass info
        self.heat_capacity_ratio = 1.043
        self.gas_constant = 196.14  # J/kg*K
        # Specific volumes
        self.combustion_chamber_volume = 0  # m**3/kg
        self.nozzle_volume = 0  # m**3/kg
        self.scape_volume = 0  # m**3/kg
        # Pressures
        self.nozzle_pressure = 0  # Pa
        self.scape_pressure = 101235  # Pa
        # Temperatures
        self.throat_temperature = 0  # K
        self.scape_temperature = 0  # K
        # Speeds
        self.throat_speed = 0  # m/s
        self.local_speed_sound_t = 0  # m/s
        self.mach_number_t = 0
        self.scape_speed = 0  # m/s
        self.local_speed_sound_2 = 0  # m/s
        self.mach_number_2 = 0
        self.characteristic_scape_speed = 0  # m/s
        # Performance
        self.fuel_volume = 0  # m**3
        self.fuel_mass = 0  # kg
        self.total_burn_time = 0  # s
        self.burn_area = 0  # m**2
        self.mass_flow = 0  # kg/s
        self.theoric_thrust_N = 0  # N
        self.theoric_thrust_kgf = 0  # kgf
        #self.average_expected_thrust_N = 0  # N
        #self.average_expected_thrust_kgf = 0
        #self.max_expected_thrust_N = 0  # N
        #self.max_expected_thrust_kgf = 0  # kgf
        self.theoric_specific_impulse = 0

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

    # End fuel data------------------------------------------------------ #
    # Scape gass info---------------------------------------------------- #
    def get_heat_capacity_ratio(self):
        return self.heat_capacity_ratio

    def set_heat_capacity_ratio(self, heat_capacity_ratio):
        self.heat_capacity_ratio = heat_capacity_ratio

    def get_gas_constant(self):
        return self.gas_constant

    def set_gas_constant(self, gas_constant):
        self.gas_constant = gas_constant

    # End Scape gass info------------------------------------------------ #
    # Specific volumes -------------------------------------------------- #
    def get_combustion_chamber_volume(self):
        return self.combustion_chamber_volume

    def calc_combustion_chamber_volume(self):
        self.combustion_chamber_volume = self.gas_constant * self.chamber_temperature_K / self.chamber_pressure_pa

    def get_nozzle_volume(self):
        return self.nozzle_volume

    def calc_nozzle_volume(self):
        self.nozzle_volume = self.combustion_chamber_volume * ((self.heat_capacity_ratio + 1) / 2) ** (
                1 / (self.heat_capacity_ratio - 1))

    def get_scape_volume(self):
        return self.scape_volume

    def calc_scape_volume(self):
        self.scape_volume = self.combustion_chamber_volume * (self.chamber_pressure_pa / self.scape_pressure) ** (
                1 / self.heat_capacity_ratio)

    # End specific volumes ---------------------------------------------- #
    # Pressures --------------------------------------------------------- #
    def get_nozzle_pressure(self):
        return self.nozzle_pressure

    def calc_nozzle_pressure(self):
        self.nozzle_pressure = self.chamber_pressure_pa * (
                self.combustion_chamber_volume / self.nozzle_volume) ** self.heat_capacity_ratio

    def get_scape_pressure(self):
        return self.scape_pressure

    # End pressures ----------------------------------------------------- #

    # Temperatures ------------------------------------------------------ #
    def get_throat_temperature(self):
        return self.throat_temperature

    def calc_throat_temperature(self):
        self.throat_temperature = self.chamber_temperature_K * (
                self.combustion_chamber_volume / self.nozzle_volume) ** (self.heat_capacity_ratio - 1)

    def get_scape_temperature(self):
        return self.scape_temperature

    def calc_scape_temperature(self):
        self.scape_temperature = self.chamber_temperature_K * (self.scape_pressure / self.chamber_pressure_pa) ** (
                (self.heat_capacity_ratio - 1) / self.heat_capacity_ratio)

    # End temperatures ----------------------------------------------- #
    # Speeds --------------------------------------------------------- #
    def get_throad_speed(self):
        return self.throat_speed

    def calc_throad_speed(self):
        self.throat_speed = math.sqrt((2 * self.heat_capacity_ratio / (
                self.heat_capacity_ratio + 1)) * self.gas_constant * self.chamber_temperature_K)

    def get_local_speed_sound_t(self):
        return self.local_speed_sound_t

    def calc_local_speed_sound_1(self):
        self.local_speed_sound_t = math.sqrt(self.heat_capacity_ratio * self.gas_constant * self.throat_temperature)

    def get_mach_number_t(self):
        return self.mach_number_t

    def calc_mach_number_t(self):
        self.mach_number_t = self.throat_speed / self.local_speed_sound_t

    def get_scape_speed(self):
        return self.scape_speed

    def calc_scape_speed(self):
        self.scape_speed = math.sqrt((2 * self.heat_capacity_ratio / (
                self.heat_capacity_ratio - 1)) * self.gas_constant * self.chamber_temperature_K * (
                                             1 - (self.scape_pressure / self.chamber_pressure_pa) ** (
                                             (self.heat_capacity_ratio - 1) / self.heat_capacity_ratio)))

    def get_local_speed_sound_2(self):
        return self.local_speed_sound_2

    def calc_local_speed_sound_2(self):
        self.local_speed_sound_2 = math.sqrt(self.gas_constant * self.heat_capacity_ratio * self.scape_temperature)

    def get_mach_number_2(self):
        return self.mach_number_2

    def calc_mach_number_2(self):
        self.mach_number_2 = self.scape_speed / self.local_speed_sound_2

    def get_characteristic_scape_speed(self):
        return self.characteristic_scape_speed

    def calc_characteristic_scape_speed(self):
        self.characteristic_scape_speed = math.sqrt(self.gas_constant * self.chamber_temperature_K / (
                    self.heat_capacity_ratio * (2 / (self.heat_capacity_ratio + 1)) ** (
                        (self.heat_capacity_ratio + 1) / (self.heat_capacity_ratio - 1))))

    # End Speeds ----------------------------------------------------- #
