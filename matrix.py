
def matrixmult (A, B):

	rows_A = len(A)
	cols_A = len(A[0])
	rows_B = len(B)
	cols_B = len(B[0])
	if cols_A != rows_B:
		print("Cannot multiply the two matrices. Incorrect dimensions.")
		return

	# Create the result matrix
	# Dimensions would be rows_A x cols_B
	C = [[0 for row in range(cols_B)] for col in range(rows_A)]
	tarefa = 1
	for i in range(rows_A):
		for j in range(cols_B):
			for k in range(cols_A):
				print("tarefa " + str(tarefa) + " i: " + str(i) + " j: " + str(j) + " k: " + str(k) )
				C[i][j] += A[i][k] * B[k][j]
				tarefa = tarefa + 1

	return C

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[11,12,13],[14,15,16],[17,18,19]]

print(matrixmult(matrix1,matrix2))
