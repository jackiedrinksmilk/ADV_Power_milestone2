class Generator:

    # This class is for Generator components
    # Generators have one bus they are connected to and a power rating
    def __init__(self, name: str, bus: str, power_rating: float):
        self.name: str = name                       # generator name
        self.bus: str = bus                         # generator bus connection
        self.power_rating: float = power_rating     # generator power rating, MVA