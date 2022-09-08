from battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_Service_Date):
        self.current_date = current_date
        self.last_Service_Date = last_Service_Date

    def needs_service(self):
        return int((self.current_date - self.last_Service_Date).days / 365.2425) > 2
