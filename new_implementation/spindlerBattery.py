from new_implementation.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_Service_Date):
        self.current_date = current_date
        self.last_Service_Date = last_Service_Date

    def needs_service(self):
        return (self.current_date - self.last_Service_Date).days / 365.2425 > 4
