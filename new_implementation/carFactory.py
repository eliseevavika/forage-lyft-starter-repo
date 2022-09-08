import datetime

from capuletEngine import CapuletEngine
from spindlerBattery import SpindlerBattery
from nubbinBattery import NubbinBattery
from car import Car
from willoughbyEngine import WilloughbyEngine
from sternmanEngine import SternmanEngine


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
