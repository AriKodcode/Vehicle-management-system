from classes.core.engine import Engine
from classes.core.Vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self,max_load,license_plate,year):
        super().__init__(license_plate,year)
        self.max_load = max_load
        self.license_plate = license_plate
        self.year = year


    def calculate_annual_tax(self):
        return f"The truck tax is: {(self.max_load + self.year) * 0.18} IL"