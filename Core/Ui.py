from .Circuit import *
import Core.ShowResults as ShowResults

def getInput(circuit, statement):
    element = statement.split()
    if element[0] == 'R':
        leftNode = int(element[1])
        rightNode = int(element[2])
        resistance = float(element[3])
        circuit[0].addResistor(rightNode, leftNode, resistance)
    elif element[0] == 'IV':
        posTerm = int(element[1])
        negTerm = int(element[2])
        voltage = float(element[3])
        circuit[0].addIndVolt(voltage, posTerm, negTerm)
    elif element[0] == 'IC':
        comeIn = int(element[1])
        comeOut = int(element[2])
        current = float(element[3])
        circuit[0].addIndCur(comeIn, comeOut, current)
    elif element[0] == 'calculate':
        circuit[0].calc()
        return ShowResults.getShowResultAns(circuit[0])

