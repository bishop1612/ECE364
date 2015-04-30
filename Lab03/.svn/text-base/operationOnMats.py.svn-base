def multiplyMatrices(matrix1, matrix2):
    if checkIfMatrixIsValid(matrix1) == False:
        return None
    if checkIfMatrixIsValid(matrix2) == False:
        return None
    ROW1,COL1 = getMatrixSize(matrix1);
    ROW2,COL2 = getMatrixSize(matrix2);
    if COL1 != ROW2:    # cannot multiply matrices that do not satisfy this condition
        return None
    # created resulting matrix below.
    myMatrix = [ [0] * COL2 for i in range(ROW1) ]
    # Below is code to populate the Matrix
    for i in range(ROW1):
        for j in range(COL2):
            myMatrix[i][j] = dotProduct( getRow(matrix1,i) , getColumn(matrix2, j) )

    return myMatrix

def dotProduct(row, column):
    if type(row) != list:
        return None
    if type(column) != list:
        return None
    if len(column) <= 0:
        return None
    if len(row) <= 0:
        return None
    if len(row) != len(column):
        return None
    sum = 0;
    for i in range(len(row)):
        sum += row[i] * column[i];
    return sum

def transposeMatrix(matrix):
    if checkIfMatrixIsValid(matrix) == False:
        return None
    ROW,COL = getMatrixSize(matrix);
    transMatrix = [];
    for i in range(COL):
        transMatrix.append( getColumn(matrix, i) )
    return transMatrix

def getColumn(matrix , columnIndex):
    if checkIfMatrixIsValid(matrix) == False:
        return []
    ROW,COL = getMatrixSize(matrix)
    if columnIndex >= COL:
        return []
    myCol = []
    for i in matrix:
        myCol.append(i[columnIndex])
    return myCol

def getRow(matrix, rowIndex):
    if checkIfMatrixIsValid(matrix) == False:
        return []
    ROW,COL = getMatrixSize(matrix)
    if rowIndex >= ROW:
        return []
    return matrix[rowIndex]

def getMatrixSize(matrix):
    if checkIfMatrixIsValid(matrix) == False:
        return []
    return [ len(matrix) , len(matrix[0]) ]

def checkIfMatrixIsValid(matrix):
    n_rows = len(matrix);
    for i in matrix:
        if type(i) != list:
            return False
    n_col1 = len(matrix[0])
    for i in range(n_rows):
        if len(matrix[i]) != n_col1:
            return False

    return True
