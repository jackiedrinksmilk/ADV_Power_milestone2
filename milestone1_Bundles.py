from milestone1_ConductorData import ConductorData
import math as m
import numpy as n


# class is for calculating dsl and dsc values depending on the number of bundles and conductor data class

class Bundles:
    def __init__(self, num: int, conductorData: ConductorData, d: float):

        if num < 1 or num > 4:
            print("invalid input for number of bundles. bundle not created")

        else:
            self.num: int = num     # number of bundles
            self.d: float = d       # bundle spacing
            self.conductorData: ConductorData = conductorData   # passed conductor data

            self.R = self.conductorData.r                   # conductor resistance
            self.gmr = self.conductorData.gmr               # conductor geometric mean radius
            self.res = conductorData.res / self.num         # conductor resistance, scaled by number of bundles

            self.dsl = Bundles.find_dsl(self)               # finds conductor dsl, based on number of bundles
            self.dsc = Bundles.find_dsc(self)               # finds conductor dsc, based on number of bundles

    # function for finding DSL depending on bundle number
    def find_dsl(self) -> float:

        if self.num == 1:       # 1 bundle
            dsl = self.gmr

        if self.num == 2:       # 2 bundles
            dsl = m.sqrt(self.gmr * self.d)

        if self.num == 3:       # 3 bundles
            dsl = n.cbrt(self.gmr * (self.d ** 2))

        if self.num == 4:       # 4 bundles
            dsl = 1.0941 * m.pow((self.gmr * (self.d ** 3)), (0.25))

        return dsl

    # function for finding DSC depending on bundle number
    def find_dsc(self) -> float:
        if self.num == 1:       # 1 bundle
            dsc = self.R

        if self.num == 2:       # 2 bundles
            dsc = m.sqrt(self.R * self.d)

        if self.num == 3:       # 3 bundles
            dsc = n.cbrt(self.R * (self.d ** 2))

        if self.num == 4:       # 3 bundles
            dsc = 1.0941 * m.pow((self.R * (self.d ** 3)), (0.25))

        return dsc