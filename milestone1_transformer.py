import numpy as n

# This class is for Transformer elements
# they have two rated voltages, one high and low (v1 and v2)
# as well as a rated power, per unit impedance z and an x/r ratio
class Transformer:

    # constant values
    w = 377
    j = 1j
    s_base = 100.0

    def __init__(self, name: str, bus1: str, bus2: str, rated_power: float, v1: float, v2: float, z: float, xr: float):

        self.name: str = name                       # name of transformer
        self.rated_power: float = rated_power       # power rating of transformer
        self.v1: float = v1                         # rated voltage on side 1
        self.v2: float = v2                         # rated voltage on side 2
        self.z: float = z                           # transformer impedance (pu)
        self.xr: float = xr                         # transformer x/r ratio
        self.bus1: str = bus1                       # transformer bus connection 1
        self.bus2: str = bus2                       # tranformer bus connection 2

        self.v_base = v2                            # setting base voltage to high side voltage

        # calculating R + jX
        self.R = self.z * ((self.v2 ** 2) / self.rated_power)/(self.v_base * (self.v_base/Transformer.s_base)) * n.cos(n.arctan(self.xr))
        self.X = self.z * ((self.v2 ** 2) / self.rated_power)/(self.v_base * (self.v_base/Transformer.s_base)) * n.sin(n.arctan(self.xr))
