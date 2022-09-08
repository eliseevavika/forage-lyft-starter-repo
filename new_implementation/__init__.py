import datetime
from carFactory import CarFactory


def main():
    current_date = datetime.datetime.now()
    last_service_date = current_date - datetime.timedelta(5 * 366)  # 5 years ago

    current_mileage = int(31000)
    last_service_mileage = int(0)

    car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    need_service = car.needs_service()
    print("Is the car in need of service?", need_service)


if __name__ == "__main__": main()
