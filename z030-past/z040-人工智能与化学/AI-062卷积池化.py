import numpy as np


aaa = np.array([[0,1,0,1,1,0],
                [0,0,1,0,1,1],
                [1,0,0,1,0,0],
                [0,1,0,0,1,1],
                [1,0,1,1,0,1],
                [1,1,0,1,1,0]])

core_1 = np.array([[0,1,0],
                   [0,2,1],
                   [1,3,1]])

corr_2 =  np.array([[2, 1, 0],
                    [1, 0, 2],
                    [2, 0, 1]])

def convolve(image, core):
    core_h, core_w = core.shape
    i_h, i_w = image.shape

    output_h = i_h - core_h +1
    output_w = i_w - core_w +1

    output = np.zeros((output_w,output_w))

    for i in range(output_h):
        for j in range(output_w):
            region0 = image[i:i+core_h, j:j+core_w]
            output[i,j] = np.sum(region0 * core_1)
    return output

def max_pooling(image, pool_size=2):
    h, w = image.shape[:2]
    pool_h, pool_w = pool_size, pool_size

    out_height = h // pool_h
    out_width = w // pool_w

    output = np.zeros((out_height, out_width))

    for i in range(out_height):
        for j in range(out_width):
            region1 = image[i * pool_h:(i + 1) * pool_h, j * pool_w:(j + 1) * pool_w]
            output[i, j] = np.max(region1)
    return output

convolved_1 = convolve(aaa, core_1)
convolved_2 = convolve(aaa, corr_2)
pooled_1 = max_pooling(convolved_1)
pooled_2 = max_pooling(convolved_2)
print("Convolution I:\n", convolved_1)
print("Max Pooling I:\n", pooled_1)
print("Convolution I:\n", convolved_2)
print("Max Pooling I:\n", pooled_2)
