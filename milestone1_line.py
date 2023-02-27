from milestone1_geometry import Geometry
from milestone1_Bundles import Bundles
import math as m


class Line:
    # Constants in the particular system we are solving
    w = 377         # angular freq associated with f = 60 Hz
    j = 1j          # defining j
    s_base = 100    # power base of 100 MVA

    def __init__(self, name: str, length: float, linegeometry: Geometry, linebundle: Bundles, bus1: str, bus2: str,
                 v_base: float):

        self.name: str = name                   # name of line
        self.length: float = length             # length of line
        self.bus1: str = bus1                   # name of the first bus the line is connected to
        self.bus2: str = bus2                   # name of the second bus the line is connected to
        self.v_base: float = v_base             # voltage base of the line


        # pulling equivalent distance associated with the line's phase geometry from passed geometry class
        self.deq = linegeometry.deq * 12        # converting to ft

        # pulling transmission line parameters from line's bundle data
        self.dsl = linebundle.dsl
        self.dsc = linebundle.dsc

        self.L = Line.findL(self)  # finds inductance in H
        self.C = Line.findC(self)  # finds capacitance in F

        # calculating base impedance from base voltage and power rating
        Zbase = (self.v_base ** 2) / Line.s_base


        self.Rpu = (linebundle.res / Zbase) * self.length           # Resistance in per unit
        self.Xpu = ((self.L * Line.w) / Zbase)                      # X in per unit
        self.Bpu = ((self.C * Line.w) * Zbase)                      # B in per unit


    # calculates line's inductance in H
    def findL(self):
        Din = self.deq / self.dsl                                           # calculating the quotient that goes inside of log(Deq/Dsl)
        L = (2 * (10 ** (-7)) * m.log(Din)) * self.length * 1609.344        # formula for inductance
        return L

    # calculates line's capactitance in C
    def findC(self):
        Din = self.deq / self.dsc                                           # calculating the quotient that goes inside of log(Deq/Dsc)
        e0 = 8.854187812 * (10 ** (-12))                                    # definition of e0
        C = ((2) * (m.pi) * (e0)) / (m.log(Din)) * self.length * 1609.344   # formula for capacitance
        return C