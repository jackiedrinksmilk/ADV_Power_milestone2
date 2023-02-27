# This class is for the mathematical values associated with
# ACSR Conductors that will be used to calculate impedences in other parts of the program

class ConductorData:
    def __init__(self, gmr: float, r: float, res: float):
        self.gmr: float = gmr  # geometric mean radius
        self.r: float = r  # inner radius
        self.res: float = res  # resistance