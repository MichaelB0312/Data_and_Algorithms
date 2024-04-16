import numpy as np


matrix = [[2,0,], [3,0,], [7,5], [4,5]]
matrix = np.array(matrix)
matrix = np.vstack((matrix[:,0], np.ones_like(matrix.shape[0]), matrix[:,1], np.zeros_like(matrix.shape[0])))
matrix
upper_right = np.diag(matrix,k=1)
upper_right

