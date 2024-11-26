import sys
import numpy as np
import time

if(sys.argv[1] != '-i' or sys.argv[3] != '-o'):
    print("Example calling: main.py -i input.dat -o output.dat")
    sys.exit(1)

#Command line arguments
cmdline = sys.argv[2]
outputFile = sys.argv[4]
inputFile = open(cmdline, "r")

#Do these in batches
lowerBound = 0
upperBound = 3


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

def getAdjectCells(matrix, x_cord, y_cord):
    row_len = len(matrix)
    col_len = len(matrix[0])
    outerloop_1 = x_cord - 1
    outerloop_2 = x_cord + 2
    innerloop_1 = y_cord - 1
    innerloop_2 = y_cord + 2
    result = []

    #check the first level case
    if x_cord - 1 < 0:
        outerloop_1 = 0

    #check the last level case
    if x_cord + 2 > row_len:
        outerloop_2 = row_len

    #check the first level case
    if y_cord - 1 < 0:
        innerloop_1 = 0

    #check the last level case
    if y_cord + 2 > col_len:
        innerloop_2 = col_len


    for i in range(outerloop_1, outerloop_2, 1):
        for j in range(innerloop_1, innerloop_2, 1):
            # print(f"i: {i} j: {j}\n")
            # print(f"x: {x_cord} y: {y_cord}\n")
            if (i != x_cord or j != y_cord):
                result.append(matrix[i][j])

    return result
    


#Do the transforming
def Compute(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #print(i, j)
            neighbors = getAdjectCells(matrix, i, j)
            print(neighbors)
            #matrix[i][j] = Rules(matrix[i][j], neighbors)
            print(matrix[i][j])
            
        sys.exit(1)    

def Rules(value, neighbors):
    return 0


#Convert String to Integer
def IntToStringArray(matrix):
    fileOutput = open(outputFile, "w")
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
    for line in lines:
        fileOutput.write(line)




def main():
    result = StringToIntArray(inputFile)
    matrix = Compute(result)
    print(matrix)   

    IntToStringArray(matrix)
    




main()