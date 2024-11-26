import sys
import time

n = len(sys.argv)

cmdline = sys.argv[1]
outputFile = sys.argv[2]

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
    #Do the calculation
    #Mathing()
    return matrix

#do the math 
def Mathing():
    return 0












result = StringToIntArray(inputFile)
print(result)

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

IntToStringArray(result)