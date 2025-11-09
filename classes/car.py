from classes.core.Vehicle import Vehicle
from classes.core.engine import Engine

class Car(Vehicle):

    def __init__(self,license_plate,year,engine : Engine):
        super().__init__(license_plate,year)
        self.engine = engine
        self.license_plate = license_plate
        self.year = year

    def calculate_annual_tax(self):
        return f"The car tax is: {(self.engine.horsepower + self.year) * 0.18} IL"