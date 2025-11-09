from classes.car import Car
from classes.truck import Truck
from classes.electric_car import ElectricCar
from classes.core.engine import Engine

if __name__ == '__main__':
    engine_car = Engine(1800, "95")
    toyota = Car(5335966, 2009, engine_car)

    truck = Truck(5500, 70252398, 2022)

    engine_electric = Engine(3000, "electric")
    tesla = ElectricCar(5335897, 2025, engine_electric)

    car_list = [
        toyota,
        truck,
        tesla
    ]
    for vehicle in car_list:
        print(vehicle.calculate_annual_tax())

    print("before change:", toyota.get_year())
    toyota.set_year(2019)
    print("after change:", toyota.get_year())
    print(tesla.charge())
    print(tesla.get_luxury_features())