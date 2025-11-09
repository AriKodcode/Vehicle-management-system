from classes.core.electric_mixin import ElectircMixin
from classes.car import Car
from classes.core.luxury_mixin import LuxuryMixin

class ElectricCar(ElectircMixin,Car,LuxuryMixin):
    def calculate_annual_tax(self):
        return "The electric car tax: 250 IL"