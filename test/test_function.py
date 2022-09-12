import unittest
from datetime import datetime

from new_implementation.capulet_engine import CapuletEngine
from new_implementation.willoughbyEngine import WilloughbyEngine
from new_implementation.sternmanEngine import SternmanEngine
from new_implementation.spindlerBattery import SpindlerBattery
from new_implementation.nubbinBattery import NubbinBattery
from new_implementation.carriganTire import CarriganTire
from new_implementation.octoprimeTire import OctoprimeTire


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)

        self.assertFalse(engine.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 4)

        battery = SpindlerBattery(today, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)

        battery = SpindlerBattery(today, last_service_date)

        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 5)

        battery = NubbinBattery(today, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(today.year - 1)

        battery = NubbinBattery(today, last_service_date)

        self.assertFalse(battery.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_sensors = ["1", "0", "0.9", "0.4"]

        tire = CarriganTire(wear_sensors)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wear_sensors = ["0.8", "0", "0.8", "0.4"]

        tire = CarriganTire(wear_sensors)

        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_sensors = ["1", "1", "0.9", "0.4"]

        tire = OctoprimeTire(wear_sensors)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wear_sensors = ["0.1", "0", "0.3", "0.4"]

        tire = OctoprimeTire(wear_sensors)

        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
