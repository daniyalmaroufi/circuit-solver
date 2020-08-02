from Core.Circuit import *
from Core import ShowResults
from Core.Ui import getInput


if __name__ == '__main__':
    circuit = [Circuit()]
    while True:
        statement = input()
        if statement.split()[0] in ['R', 'IC', 'IV']:
            getInput(circuit, statement)
        elif statement.split()[0] == 'calculate':
            circuit[0].calc()
            ShowResults.printResults(circuit[0])
            break
        else:
            print("Wrong input! Try agian.")
