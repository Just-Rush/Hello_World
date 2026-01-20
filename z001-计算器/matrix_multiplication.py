import numpy as np

def matrix_multiplication():
    matrix_a_data = np.loadtxt('matrix_a.txt')
    row_number_a = matrix_a_data.shape[0] // 3
    matrix_a = matrix_a_data.reshape((row_number_a, 3, 3))
    matrix_b_data = np.loadtxt('matrix_b.txt')
    row_number_b = matrix_b_data.shape[0] // 3
    matrix_b = matrix_b_data.reshape((row_number_b, 3, 3))
    matrix_a2_data = np.loadtxt('matrix_a2.txt')
    row_number_a2 = matrix_a2_data.shape[0] // 3
    matrix_a2 = matrix_a2_data.reshape((row_number_a2, 3, 3))
    for i in range(row_number_a):
        inverse_a = np.linalg.inv(matrix_a[i])
        inverse_a2 = np.linalg.inv(matrix_a2[i])
    matrix_c = matrix_a @ matrix_b @ inverse_a
    matrix_c2 = inverse_a @ matrix_b @ matrix_a
    matrix_d =  inverse_a2 @ matrix_b @ matrix_a2
    print(matrix_c,'\n\n', matrix_c2, '\n\n', matrix_d)


if __name__ == "__main__":
    matrix_multiplication()
    