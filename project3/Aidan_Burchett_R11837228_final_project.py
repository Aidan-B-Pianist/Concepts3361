import argparse
import os.path
from multiprocessing import *

#Parse arguments for input and output
parser = argparse.ArgumentParser(description="Project 3 Multiprocessor Parameters")

parser.add_argument('-i', '--input', required=True)
parser.add_argument('-o', '--output', required=True)
parser.add_argument('-p', '--processor', required=False, type=int)

args = parser.parse_args()

if not os.path.exists(args.input):
    parser.error("The file %s does not exist" % args.input)

if args.processor is None:
    #automatically set to 1
    args.processor = 1
elif args.processor <= 0:
    parser.error("You must put a value greater than 0")

#Command line arguments
cmdline = args.input
outputFile = args.output

if outputFile is None:
    parser.error("Must have an output file name")

inputFile = open(cmdline, "r")

#list of prime numbers
listofPrimeNumbers = [2, 3, 5, 7, 11, 13]

#list of power numbers
listofPowerNumbers = [1, 2, 4, 8, 16]

#Convert string file into 2d array with integers
def StringToIntArray(file):
    text = file.read()
    def checkCase(input):
        if input == 'O':
            return 2
        elif input == 'o':
            return 1
        elif input == '.':
            return 0
        elif input == 'x':
            return -1
        elif input == 'X':
            return -2
    matrix = [[
        checkCase(char) for char in line
    ] for line in text.split('\n')]

    return matrix


def getAdjenctCells(matrix, i , j):

    neighbors = []

    rowLimit = len(matrix)
    columnLimit = len(matrix[i])

    def checkNeighbor(x, y):
        #check boundaries to see if neighbor is legit
        return (0 <= x < rowLimit) and (0 <= y < columnLimit) and ((x, y) != (i, j))
    
    #iterate through the 2d matrix using conditional max and min statements to 
    #get each neighbor up down and diagonally
    for x in range (max(0, i-1), min(rowLimit, i+2)):
        for y in range (max(0, j-1), min(columnLimit, j+2)):
            if checkNeighbor(x, y):
                neighbors.append(matrix[x][y])

    return neighbors

#Do the transforming
def Compute(iterativeTuple):
    #create tuple from iterable
    i, matrix = tuple(iterativeTuple)
    #print(f"Row: {i}, matrix: {matrix}\n")
    result = []
    #do row transforms by iterating j, and let pool workers do the rest
    for j in range(len(matrix[i])):
        neighbors = getAdjenctCells(matrix, i, j)
        result.append(Rules(matrix[i][j], neighbors))
    return result

def powerOfTwo(value):
    return value in listofPowerNumbers

def primeNumber(value):
    return value in listofPrimeNumbers

def Rules(value, neighbors):
    #print(neighbors)
    total = sum(neighbors)
    if value == 2:
        if powerOfTwo(total):
            return 0
        elif total < 10:
            return 1
        return 2
    elif value == 1:
        if total <= 0:
            return 0
        elif total >= 8:
            return 2
        return 1
    elif value == 0:
        if primeNumber(total):
            return 1
        elif primeNumber(abs(total)):
            return -1
        return 0
    elif value == -1:
        if total >= 1:
            return 0
        elif total <= -8:
            return -2
        return -1
    elif value == -2:
        if powerOfTwo(abs(total)):
            return 0
        elif total > -10:
            return -1
        return -2
    

def IntToStringArray(matrix):
    with open(str(outputFile), "w") as fileOutput:
        def checkCase(input):
            if input == 2:
                return 'O'
            elif input == 1:
                return 'o'
            elif input == 0:
                return '.'
            elif input == -1:
                return 'x'
            elif input == -2:
                return 'X'
    
        lines = [''.join(checkCase(num) for num in line) for line in matrix]

        lines = '\n'.join(lines)
        fileOutput.write(lines)


def main():

    #Print out R number
    print("Project :: R11837228")


    #change the file from strings to numbers
    result = StringToIntArray(inputFile)
    #print(f"the result is {result}")
    for i in range(100):

        with Pool(processes=args.processor) as pool:
            result = pool.map(Compute, [(i, result) for i in range(len(result))])

        #print(f"Results are: {result}")

    
    #change the file from numbers to strings
    IntToStringArray(result)

if __name__ == '__main__':
    main()