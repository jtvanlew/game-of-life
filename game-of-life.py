import numpy as np
import matplotlib.pyplot as plt
import time

A = np.ones([50,50])
A[25,25], A[26,26], A[25,26], A[26,25] = 0, 0, 0, 0
#A = A.astype(int)
m = len(A)
plt.pcolor(A, cmap='gray')
plt.ion()
plt.show()
A1 = A
for k in np.arange(0,100):
	for i in np.arange(0,m):# arange is non-inclusive on last value
		for j in np.arange(0,m):# arange is non-inclusive on last value
			count = 0
			if i == 0:
				if j == 0:
					count = count + A[i,j+1] + A[i+1,j] + A[i+1,j+1]
				elif j == m-1:
					count = count + A[i,j-1] + A[i+1,j-1] + A[i+1,j]
				else:
					count = count + (A[i,j-1] + A[i,j+1] + A[i+1,j-1] +
								A[i+1,j] + A[i+1,j+1])
			if i == m-1:
				if j == 1:
					count = count + A[i-1,j] + A[i-1,j+1] + A[i,j+1]
				elif j == m-1:
					count = count + A[i-1,j-1] + A[i-1,j] + A[i,j-1]
				else:
					count = count + (A[i-1,j-1] + A[i-1,j] + A[i-1,j+1] +
								A[i,j-1] + A[i,j+1])
			if (j == 0 and i > 0 and i < m-1):
				count = count + (A[i-1,j] + A[i-1,j+1] + A[i,j+1] +
							A[i+1,j] + A[i+1,j+1])
			if (j == m-1 and i > 0 and i < m-1):
				count = count + (A[i-1,j-1] + A[i-1,j] + A[i,j-1] +
							A[i+1,j-1] + A[i+1,j])
			if (i > 0 and j > 0 and i < m-1 and j < m-1):
				count = count + (A[i-1,j-1] + A[i-1,j] + A[i-1,j+1] +
							A[i,j-1] + A[i,j+1] + A[i+1,j-1] +
							A[i+1,j] + A[i+1,j+1])
			if A1[i,j]:
				if not (count == 2 or count == 3):
					A1[i,j]=0
			else:
				if count == 3:
					A1[i,j]=1
	A = A1
	plt.pcolor(A, cmap='gray')
	plt.draw()
	time.sleep(0.01)