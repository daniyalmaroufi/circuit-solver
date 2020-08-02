from .Circuit import *


def printResults(circuit):
    for i in range(1, len(circuit.nodes)):
        print('\nNode Number: ', circuit.nodes[i].Number)
        print('     ', circuit.nodes[i].volt)
    for indVolt in circuit.indVolt:
        print('\nIndependent voltage source: posTerm, negTerm:', indVolt.PosTerm, ',', indVolt.NegTerm)
        print('     voltage:', indVolt.Voltage)
        print('     current:', indVolt.Current)

    for res in circuit.resistors:
        print('\nResistor: Left, Right:', res.leftNode, ', ', res.rightNode)
        print('     resistance:', res.Resistance, 'ohms')
        print('     voltage:', res.Voltage, 'V')
        print('     current:', res.Current, 'A')

def getShowResultAns(circuit):
    result = ""
    for i in range(1, len(circuit.nodes)):
        result += 'nodeNumber: ' + str(circuit.nodes[i].Number) + '<br>'
        result += str(circuit.nodes[i].volt) + '<br>'
    for indVolt in circuit.indVolt:
        result += 'Battery: '
        result += '&nbsp;&nbsp;posTerm, negTerm: ' + str(indVolt.PosTerm) + ', ' + str(indVolt.NegTerm) + '<br>'
        result += '&nbsp;&nbsp;&nbsp;volt: ' + str(round(indVolt.Voltage,4)) + '<br>'
        result += '&nbsp;&nbsp;&nbsp;current: ' + str(round(indVolt.Current,4)) + '<br><br>'

    for res in circuit.resistors:
        result += "Resistor:"
        result += "&nbsp;&nbsp;Left, Right: " + str(res.leftNode) + ', ' + str(res.rightNode) + '<br>'
        result += '&nbsp;&nbsp;&nbsp;resistance: ' + str(res.Resistance) + '<br>'
        result += '&nbsp;&nbsp;&nbsp;voltage: ' + str(round(res.Voltage,4)) + '<br>'
        result += '&nbsp;&nbsp;&nbsp;current: ' + str(round(res.Current,4)) + '<br><br>'

    return result
    