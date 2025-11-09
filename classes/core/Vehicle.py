from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self,license_plate,year):
        self.__license = license_plate
        self.__year = year

    def get_license_plate(self):
        return self.__license

    def get_year(self):
        return self.__year


    def set_license_plate(self,set1):
        if set1:
            self.__license = set1

    def set_year(self,set1):
        if set1:
            self.__year = set1

    @abstractmethod
    def calculate_annual_tax(self):
        pass
