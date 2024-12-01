
def getAdjectCells(matrix, i , j):

    neighbors = []

    rowLimit = len(matrix)
    columnLimit = len(matrix[i])

    def checkNeighbor(x, y):
        return (0 <= x < rowLimit) and (0 <= y < columnLimit) and (matrix[x][y] != matrix[i][j])
           
    
    for x in range (max(0, i-1), min(rowLimit, i+2)):
        for y in range (max(0, j-1), min(columnLimit, j+2)):
            if checkNeighbor(x, y):
                neighbors.append(matrix[x][y])

    return neighbors


    # rowLimit = len(matrix)
    # columnLimit = len(matrix[i]) 

    # def is_neighbor(r,c):
    #     return (
    #         0 <= r < rowLimit and
    #         0 <= c < columnLimit and
    #         (r,c) != (i,j)
    #     )

    # return [
    #     matrix[r][c]
    #     for r in range (max(0, i-1), min(rowLimit, i+2))
    #     for c in range (max(0, j-1), min(columnLimit, j+2))
    #     if is_neighbor(r,c)
    # ]

def main():
    myMatrix = [[1,2,3],
                [4,5,6],
                [7,8,9],]
    for i in range(len(myMatrix)):
        for j in range(len(myMatrix[0])):
            print (i, j)
            print(getAdjectCells(myMatrix, i, j))



main()