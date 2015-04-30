#!/usr/local/bin/python3.4

def checkIfMatrixIsValid(array):
	#count = 0
	if type(array[0]) != list:
		return False
	prev = len(array[0])
	for i in list(array):
		if type(i) != list:
			return False
		if len(i) != prev:
			return False
		else:
			prev = len(i)
	return True

def getMatrixSize(array):
	valid = checkIfMatrixIsValid(array)
	c=0	
	if valid == True:
		for i in list(array):
			c = c + 1
		return [c,len(array[0])]
	else:
		return []

def getRow(array,num):
	valid = checkIfMatrixIsValid(array)	
	c = 0
	if valid == True:
		for i in list(array):
			c = c + 1
		if c < num:
			return []
		else:
			return array[num]
	else:
		return []

def getColumn(array,num):
	valid = checkIfMatrixIsValid(array)	
	c = 0
	new = []
	if valid == True:
		c = len(array[0]) - 1
		if c < num:
			return []
		else:
			for i in list(array):
				new.append(i[num])
		return new
	else:
		return []

def transposeMatrix(array):
	valid = checkIfMatrixIsValid(array)	
	c = 0
	new = []
	if valid == True:
		#c = len(array[0])
		#if c < num:
			#return []
		#else:
		for i in range(0,len(array[0])):
			new.append(getColumn(array,i))
			#num = num 
		return new
	else:
		return None

def dotProduct(row,col):
	if len(col) > 0 and len(row) > 0 and len(row) == len(col):
		su = 0		
		for i in range(0,len(col)):
			su = su + row[i] * col[i]
	else:
		return None
	return su

def multiplyMatrices(matrix1,matrix2):
	col = getMatrixSize(matrix1)
	row = getMatrixSize(matrix2) 	
	if checkIfMatrixIsValid(matrix1) == True and checkIfMatrixIsValid(matrix2) == True and col[1] == row[0]:
		su = 0
		foo = 0
		#print col[0] 
		C = [[0] * int(row[1]) for i in range(int(col[0]))]
                #print row[1] 	
		for i in range(0,col[0]):
        		for j in range(0,row[1]):
            			for k in range(0,row[0]):
                			su += matrix1[i][k] * matrix2[k][j]
				C[i][j] = su
				su = 0
    		return C
	else:
		return None
	#return su

if __name__ == "__main__":

    su = checkIfMatrixIsValid([[3],2])
    su2 = getMatrixSize([[3],[2]])
    freq = getRow([[6,2],[2,1]],1)
    su3 = getColumn([[3,2,1],[2,1,2]],1)
    di = transposeMatrix([[9,1],[1,3],[5,6]])
    cap = multiplyMatrices([[7,8,-2],[4,2,5]],[[9,0],[3,7],[-2,10]])

    print("addNumbers : {0} addMultiplesOf : {1} getNumberFrequency : {2} getDigitalSum : {3} getSequenceWithoutDigit : {4} capitalizeMe : {5}".format(su,su2,freq,su3,di,cap))
