import numpy as np

'''
:param matrix: mat with 0,1,2 elements
 :return longest diagonal path: 1,2,0,2,0,2 ....(here max_path = 6)
'''
def max_path(matrix):
    max_seq = 0
    ones_idx = np.array(np.where(matrix==1)) # shape: 2 X num_idx
    for i in range(ones_idx.shape[1]):
        one_loc = ones_idx[:,i]
        upper_right_diag = np.diag(np.flip(matrix[:one_loc[0], one_loc[1]+1:], axis=0), k=0)#flip rows because diag takes only left-to-right diagon in the mat
        upper_left_diag = np.flip(np.diag(matrix[:one_loc[0], :one_loc[1]], k=0))  #flip diagon in order to begin sequence from 1
        down_right_diag = np.diag(matrix[one_loc[0]+1:, one_loc[1]+1:], k=0)
        down_left_diag = np.flip(np.diag(np.flip(matrix[one_loc[0]+1:, :one_loc[1]], axis=0), k=0))#flip diagon in order to begin sequence from 1

        diag_list = [upper_left_diag, upper_right_diag, down_left_diag, down_right_diag]
        for diag in diag_list:
            if diag.shape[0] == 0:
                continue
            if(np.where(diag[::2] != 2)[0] != None):
                twos = np.where(diag[::2] != 2)[0][0]
            elif  np.where(diag[::2] == 2)[0] != None:
                twos = np.where(diag[::2] == 2)[0][-1] + 1 ## 22222..
            else: twos = 0

            if (np.where(diag[1::2] != 0)[0] != None):
                zeros = np.where(diag[1::2] != 0)[0][0]
            elif np.where(diag[1::2] == 0)[0] != None:
                zeros = np.where(diag[1::2] == 0)[0][-1] + 1
            else: zeros = 0

            max_seq = max(1+zeros+twos, max_seq)

    return max_seq



rows = 3
cols = 4
matrix = np.random.choice([0,1,2], (rows,cols))
np.diag(np.flip(matrix[2:, :2+1], axis=0))
np.diag(matrix[2:, 2:], k=0)
np.array(np.where(matrix==1))[:,0]
upper_right = np.diag(matrix,k=-2)
arr = np.array([2,0,2,0,2,0,1,1,1])
np.where(arr[1::2] == 0)[0][-1]
upper_right
matrix = np.random.choice([0,1,2], (rows,cols))
# matrix = np.array([[2, 0, 2, 2],
#  [2, 0, 0, 0],
#  [1, 2, 1, 0]])
print("matrix is:\n", matrix)
print("max 1->2->0->2->0.. is", max_path(matrix))

