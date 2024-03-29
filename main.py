from milestone1_ybus import YBus
from milestone1_ConductorData import ConductorData
from milestone1_geometry import Geometry
from milestone1_Bundles import Bundles

# this script inserts the specific line, generator, and transformer network connections
# for the purpose of this project

PartridgeData = ConductorData(0.2604, 0.321, 0.385)
BundledPartridgeData = Bundles(2, PartridgeData, 18.0)
PhaseGeometry = Geometry(0, 0, 19.5, 0, 40, 0)

Matrix = YBus("Matrix")

Matrix.addgenerator("G1", "B1", 100)
Matrix.addgenerator("G2", "B7", 100)

Matrix.addtransformer("T1", "B1", "B2", 125, 20, 230, 0.085, 10)
Matrix.addtransformer("T2", "B7", "B6", 200, 18, 230, 0.105, 12)

Matrix.addline("L1", 10, PhaseGeometry, BundledPartridgeData, "B2", "B4", 1.5)
Matrix.addline("L2", 25, PhaseGeometry, BundledPartridgeData, "B2", "B3", 1.5)
Matrix.addline("L3", 20, PhaseGeometry, BundledPartridgeData, "B3", "B5", 1.5)
Matrix.addline("L4", 20, PhaseGeometry, BundledPartridgeData, "B4", "B6", 1.5)
Matrix.addline("L5", 10, PhaseGeometry, BundledPartridgeData, "B5", "B6", 1.5)
Matrix.addline("L6", 35, PhaseGeometry, BundledPartridgeData, "B4", "B5", 1.5)

Matrix.setbustype("B1", "Slack", 0, 0)
Matrix.setbustype("B2", "Load", 0, 0)
Matrix.setbustype("B3", "Load", 110, 50)
Matrix.setbustype("B4", "Load", 100, 70)
Matrix.setbustype("B5", "Load", 100, 65)
Matrix.setbustype("B6", "Load", 0, 0)
Matrix.setbustype("B7", "Voltage Controlled", 200, 1)

Ybusmatrix = Matrix.calculate_Ybus_matrix()
Y_bus_list = Matrix.buses



