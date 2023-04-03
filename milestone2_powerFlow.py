# Milestone 2: Produce Power Flow Input Data,
# Jacobian, and Injection Equations

# Given Bus Data
# Bus 1: SLACK      V = 1.0 pu      delta = 0
# Bus 2:            Pl = 0          QL = 0
# Bus 3:            PL = 110 MW     QL = 50 Mvar
# Bus 4:            PL = 100 MW     QL = 70 Mvar
# Bus 5:            PL = 100 MW     QL = 65 Mvar
# Bus 6:            PL = 0 MW       QL = 0 Mvar
# Bus 7:            PG = 200 MW     V = 1.0 pu      PL = QL = 0

import numpy as n
from main import Ybusmatrix
from main import Y_bus_list


class Powerflow:

    def __init__(self):

        # defining variable for number of busses
        num: int = len(Y_bus_list)

        # blank array initialized for values of P and Q at each bus
        self.P_final = []
        self.Q_final = []

        # given values for mismatch
        P_given = [0, 0, -1.10, -1.00, -1.00, 0, 2.00]
        Q_given = [0, 0, -0.50, -0.70, -0.65, 0, 0]

        # initial guess
        Voltages = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        deltas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        P_final = n.zeros(num)
        Q_final = n.zeros(num)

        # for mismatch
        for x in range(len(Y_bus_list)):
            #skipping slack bus
            if x == 0:
                continue

            for y in range(len(Y_bus_list)):
                P_final[x] += Voltages[x] * Voltages[y] * abs(Ybusmatrix[x, y]) * n.cos(deltas[x] - deltas[y] -
                                                                                        n.angle(Ybusmatrix[x, y]))
                Q_final[x] += Voltages[x] * Voltages[y] * abs(Ybusmatrix[x, y]) * n.sin(deltas[x] - deltas[y] -
                                                                                        n.angle(Ybusmatrix[x, y]))
        print(P_final)
        P_mm = P_given - P_final
        P_mm = P_mm[1:7]
        Q_mm = Q_given - Q_final
        Q_mm = Q_mm[1:7]

        #print(Q_mm)
        #print(P_mm)

        ### JACOBIAN MATRIX CALCULATIONS
        # initializing emtpy matrices size of busses - 1 (ignoring slack bus)
        J1 = n.zeros((num - 1, num - 1))
        J2 = n.zeros((num - 1, num - 1))
        J3 = n.zeros((num - 1, num - 1))
        J4 = n.zeros((num - 1, num - 1))



        skip = 0
        for row in range(num):
            if row == 0:
                skip = 1
                continue

            for col in range(num):
                if row == col:
                    for n_sum in range(num):
                        J2[row-skip, col-skip] += abs(Ybusmatrix[row, n_sum]) * Voltages[n_sum] * n.cos(
                            deltas[row] - deltas[n_sum] - n.angle(Ybusmatrix[row, n_sum]))
                        J4[row-skip, col-skip] += abs(Ybusmatrix[row, n_sum]) * Voltages[n_sum] * n.sin(
                            deltas[row] - deltas[n_sum] - n.angle(Ybusmatrix[row, n_sum]))

                        if n_sum == row:
                            continue

                        J1[row-skip, col-skip] += abs(Ybusmatrix[row, n_sum]) * Voltages[n_sum] * n.sin(
                            deltas[row] - deltas[n_sum] - n.angle(Ybusmatrix[row, n_sum]))
                        J3[row - skip, col - skip] += abs(Ybusmatrix[row, n_sum]) * Voltages[n_sum] * n.cos(
                            deltas[row] - deltas[n_sum] - n.angle(Ybusmatrix[row, n_sum]))

                    J1[row-skip, col-skip] = -1 * J1[row-skip, col-skip] * Voltages[row]
                    J2[row-skip, col-skip] = J2[row-skip, col-skip] + (Voltages[row] * abs(Ybusmatrix[row, col])
                                                                           * n.cos(n.angle(Ybusmatrix[row, col])))
                    J3[row-skip, col-skip] = J3[row-skip, col-skip] * Voltages[row]
                    J4[row-skip, col-skip] = J4[row-skip, col-skip] - (Voltages[row] * abs(Ybusmatrix[row, col])
                                                                           * n.sin(n.angle(Ybusmatrix[row, col])))

                else:
                    J1[row-skip, col-skip] = Voltages[row] * abs(Ybusmatrix[row,col]) * Voltages[col] * n.sin(
                            deltas[row] - deltas[col] - n.angle(Ybusmatrix[row, col]))

                    J2[row-skip, col-skip] = Voltages[row] * abs(Ybusmatrix[row,col]) * n.cos(
                            deltas[row] - deltas[col] - n.angle(Ybusmatrix[row, col]))

                    J3[row-skip, col-skip] = -1 * Voltages[row] * abs(Ybusmatrix[row, col]) * Voltages[col] * n.cos(
                            deltas[row] - deltas[col] - n.angle(Ybusmatrix[row, col]))

                    J4[row-skip, col-skip] = Voltages[row] * abs(Ybusmatrix[row, col]) * n.sin(
                            deltas[row] - deltas[col] - n.angle(Ybusmatrix[row, col]))


        J = n.block([[J1, J2], [J3, J4]])

        J_temp = n.delete(J, 11, 1)
        J = J_temp

        J_temp = n.delete(J, 11, 0)
        J = J_temp

        print("Jacobian Matrix")
        D = 0
        while D < len(J):
            E = 0
            print("\nRow " + str(D + 1))
            while E < len(J):
                print(J[D][E])
                E += 1
            D += 1

        J_inv = n.linalg.inv(J)
        Q_temp = n.delete(Q_mm, 5, 0)
        Q_mm = Q_temp

        mm = n.concatenate((P_mm, Q_mm)) #mismatch matrix
        cor = n.dot(J_inv, mm) # correction matrix

        deltas_cor = cor[:6]
        Voltages_cor = cor[6:]

        # angle for slack bus does not change
        deltas_cor = n.concatenate((deltas_cor[:0], [1], deltas_cor[0:]), axis=0)

        # angle for slack and voltage controlled bus do not change
        Voltages_cor = n.concatenate((Voltages_cor[:6], [0], Voltages_cor[6:]), axis=0)
        Voltages_cor = n.concatenate((Voltages_cor[:0], [0], Voltages_cor[0:]), axis=0)

        deltas += deltas_cor
        Voltages += Voltages_cor

        print("Delta Updated Data")
        print(deltas)
        print("Voltages Updated Data")
        print(Voltages)
