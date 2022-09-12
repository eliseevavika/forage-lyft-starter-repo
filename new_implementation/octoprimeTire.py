from new_implementation.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        result = sum(self.wear_sensors)

        if result >= 3:
            return True
        else:
            return False
