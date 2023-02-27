class Bus:

    counter = 0     # number of busses

    def __init__(self, name: str):

        self.name: str = name           # name of bus
        self.index: int = Bus.counter   # index of bus

        Bus.counter = Bus.counter + 1   # increasing bus number, when bus is added

    def bustype(self, bustype: str, value1: float, value2: float):

        # Swing/Slack bus.
        # Voltage at this point is the reference so V = 1.0 pu and delta = 0 degrees
        # Power Flow should calculate real and reactive power
        if bustype == "Swing":
            self.V = 1.0

        # Load (PQ) Bus
        # Input 1 will be real power, Input 2 will be reactive power
        # Power Flow should calculate bus Voltage and angle (delta)
        elif bustype == "Load":
            self.P = value1
            self.Q = value2

        # Voltage Controlled (PV) Bus
        # Input 1 will be real power rating, Input 2 will be Voltage rating
        # Power Flow should calculate bus voltage angle (delta) and reactive power
        elif bustype == "Voltage Controlled":
           self.V = value2
           self.P = value1

        # check if valid input for bus type
        else:
            print("Invalid type enter. Please enter one of the following: 1) Swing, 2) Load, or 3) Voltage Controlled")