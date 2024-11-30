from multiprocessing import *
import os
import math
import time





def matrixAddition(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = i*j + matrix[i][j]

    return matrix


def matrixSplit(matrix, processes):
    splitNums = len(matrix) / processes
    #EX: 2 processes matrix = [matrix[0:50], matrix[50:100]]
    splitMatrices = []

    splitNums = math.floor(splitNums)
    for i in range(0, processes, 1):
        start = splitNums * i
        if i < processes - 1:
            end = start + splitNums
        else:
            end = len(matrix) 
        print(start, end)
        splitMatrices.append(matrix[start:end])

    return splitMatrices


def main():
    num_of_processes = 6
    p = Pool(processes=num_of_processes)

    print(f"Number of processors used: {num_of_processes}")
    bigMatrix = [[0 for _ in range(100)] for _ in range(100)]

    print(f"First elements before addition: {bigMatrix[0][:5]}")

    start_time_mp = time.time()

    

    numberOfSplits = matrixSplit(bigMatrix, num_of_processes)
    result = p.map(matrixAddition, numberOfSplits)

    print(f"Number of splits: {numberOfSplits}")

    p.close()
    p.join()

    end_time_mp = time.time() - start_time_mp

    

    
    for i in range(len(result)):
        for j in range(len(result[0])):
            bigMatrix = result[i][j]


    # print(f"First few elements after addition: {bigMatrix[0:5]}")
    # print(f"%s seconds" %(end_time_mp))

    print(len(result), len(result[0]))

    # bigMatrix = [[0 for _ in range(10000)] for _ in range(10000)]

    # print(f"First elements before addition: {bigMatrix[0][:5]}")

    # start_time_sl = time.time()

    # bigMatrix = matrixAddition(bigMatrix)
    
    # end_time_sl = time.time() - start_time_sl

    # print(f"First few elements after addition: {bigMatrix[0]}")
    # print(f"%s seconds" %(end_time_sl))

if __name__ == '__main__':
    main()