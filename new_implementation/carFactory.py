from new_implementation.capulet_engine import CapuletEngine
from new_implementation.spindlerBattery import SpindlerBattery
from new_implementation.nubbinBattery import NubbinBattery
from new_implementation.car import Car
from new_implementation.willoughbyEngine import WilloughbyEngine
from new_implementation.sternmanEngine import SternmanEngine


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   SpindlerBattery(current_date, last_service_date))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   SpindlerBattery(current_date, last_service_date))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(current_date, last_service_date))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   NubbinBattery(current_date, last_service_date))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))
