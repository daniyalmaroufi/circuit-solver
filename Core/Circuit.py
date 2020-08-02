from .Resistance import *
from .IndepVoltage import *
from .Node import *
from .IndepCur import *
from .Solve import *
import numpy as np
from typing import List, Dict, Optional
from time import sleep
import math
import cmath


class Circuit():
    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.resistors: List[Resistance] = []
        self.indVolt: List[IndepVolt] = []
        self.independentCurrent = []

    def addResistor(self, rightNode: int, leftNode: int, resistance: int):
        res = Resistance(resistance, leftNode, rightNode, self.nodes)
        self.resistors.append(res)

    def addIndVolt(self, voltage, posTerm: int, negTerm: int):
        newIndVolt = IndepVolt(voltage, posTerm, negTerm, self.nodes)
        self.indVolt.append(newIndVolt)

    def addIndCur(self, comeInNode, comeOutNode, current):
        newIndCur = IndepCur(current, comeInNode, comeOutNode, self.nodes)
        self.independentCurrent.append(newIndCur)

    def calc(self):
        m = len(self.indVolt)
        n = len(self.nodes) - 1 #ignoring 0 node
        solver = Solve(m, n)
        solver.generateA(self.nodes, self.resistors, self.indVolt,
        self.independentCurrent)
        solver.generateZ(self.nodes, self.indVolt)
        results = solver.solveCircuit()
        self.addResultsToCircut(results)

    def addResultsToCircut(self, results):
        numberOfNodes = len(self.nodes)
        for i in range(1, numberOfNodes):
            self.nodes[i].volt = results[i - 1][0]

        numberOfIndVolts = len(self.indVolt)
        for i in range(0, numberOfIndVolts):
            self.indVolt[i].cur = results[i + numberOfNodes - 1][0]
      
        numbeOfResistors = len(self.resistors)
        for i in range(0, numbeOfResistors):
            self.resistors[i].setVoltageAndCur(self.nodes[self.resistors[i].leftNode],
            self.nodes[self.resistors[i].rightNode])

