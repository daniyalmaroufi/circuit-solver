import numpy as np
import numpy.linalg as linearAlg
from .Circuit import *
from .Node import *
from .Resistance import *


class Solve():
    def __init__(self, m, n):
        self.__A = np.zeros((m + n, m + n))
        self.__g = np.zeros((n, n))
        self.__b = np.zeros((n, m))
        self.__c = np.zeros((m, n))
        self.__d = np.zeros((m, m))

        self.__X = np.zeros((n + m, 1))
        self.__v = np.zeros((n, 1))
        self.__j = np.zeros((m, 1))

        self.__Z = np.zeros((n + m, 1))
        self.__i = np.zeros((n, 1))
        self.__e = np.zeros((m, 1))

    def generateG(self, nodes, resistors):
        for i in range(1, len(nodes)):
            sumr = 0
            for resistor in nodes[i].ResisConnented:
                sumr += 1/resistor
            self.__g[i-1][i-1] = sumr
        for res in resistors:
            left = res.leftNode - 1
            right = res.rightNode - 1
            
            if right == -1 or left == -1:
                continue
            self.__g[left][right] += -1/res.Resistance
            self.__g[right][left] += -1/res.Resistance

    def generateB(self, indVolts):
        numberOfIndVolts = len(indVolts)
        for i in range(0, numberOfIndVolts):
            posTerm = indVolts[i].PosTerm - 1
            negTerm = indVolts[i].NegTerm - 1
            import sys
            if posTerm != -1:
                self.__b[posTerm][i] = 1
            if negTerm != -1:
                self.__b[negTerm][i] = -1

    def generateC(self, indVolts):
        numberOfIndVolts = len(indVolts)
        for i in range(0, numberOfIndVolts):
            posTerm = indVolts[i].PosTerm - 1
            negTerm = indVolts[i].NegTerm - 1
            if posTerm != -1:
                self.__c[i][posTerm] = 1
            if negTerm != -1:
                self.__c[i][negTerm] = -1

    def generateA(self, nodes, resistors, indVolts, indCurs):
        self.generateG(nodes, resistors)
        self.generateB(indVolts)
        self.generateC(indVolts)
        leftSide = np.concatenate((self.__g, self.__c))
        rightSide = np.concatenate((self.__b, self.__d))
        self.__A = np.hstack((leftSide, rightSide))

    def generateI(self, nodes):
        for i in range(1, len(nodes)):
            self.__i[i - 1][0] = sum(nodes[i].comeInCurrents) - sum(nodes[i].comeOutCurrents)
        return self.__i

    def generateE(self, indepVolts):
        for i in range(0, len(indepVolts)):
            self.__e[i][0] = -indepVolts[i].Voltage
        return self.__e

    def generateZ(self, nodes, indepVolts):
        upSide = self.generateI(nodes)
        downSide = self.generateE(indepVolts)
        self.__Z = np.concatenate((upSide, downSide))
    
    def solveCircuit(self):
        return linearAlg.solve(self.__A, self.__Z)
