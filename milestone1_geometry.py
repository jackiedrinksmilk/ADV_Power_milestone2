import math as m
import numpy as n

# This class calculates the equivelent distance, deq, between three
# phases of a particular conductor, depending on the coordinates for
# each phase passed through the class
class Geometry:
    def __init__(self, phasea_x: float, phasea_y: float, phaseb_x: float,
                 phaseb_y: float, phasec_x: float, phasec_y: float):

        self.phasea_x: float = phasea_x         # x position of phase a
        self.phaseb_x: float = phaseb_x         # x position of phase b
        self.phasec_x: float = phasec_x         # x position of phase c
        self.phasea_y: float = phasea_y         # y position of phase a
        self.phaseb_y: float = phaseb_y         # y position of phase b
        self.phasec_y: float = phasec_y         # y position of phase c

        self.deq = Geometry.find_deq(self)      # finding equivalent distance, deq for this phase geometry

    # finding DEQ and returning it as a class variable
    def find_deq(self):
        dab_x = self.phasea_x - self.phaseb_x       # distance between phase a and b, x coordinates
        dab_y = self.phasea_y - self.phaseb_y       # distance between phase a and b, y coordinates
        dab = m.sqrt((dab_x ** 2) + (dab_y ** 2))   # distance between phase a and b

        dbc_x = self.phaseb_x - self.phasec_x       # distance between phase b and c, x coordinates
        dbc_y = self.phaseb_y - self.phasec_y       # distance between phase b and c, y coordinates
        dbc = m.sqrt((dbc_x ** 2) + (dbc_y ** 2))   # distance between phase b and c

        dca_x = self.phasec_x - self.phasea_x       # distance between phase c and a, x coordinates
        dca_y = self.phasec_y - self.phasea_y       # distance between phase c and a, y coordinates
        dca = m.sqrt((dca_x ** 2) + (dca_y ** 2))   # distance between phase c and a

        deq = n.cbrt(dab * dbc * dca)       # equivalent distance
        return deq