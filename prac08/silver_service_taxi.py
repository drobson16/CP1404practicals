"""
SilverServiceTaxi class
"""

from prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.fare_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                    self.flag_fall)

    def get_fare(self):
        return self.flag_fall + super().get_fare()