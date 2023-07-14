import numpy as np
import cv2
from numpy import asarray


def bitwise_or(num1, num2):
    return num1 | num2


def bitwise_and(num1, num2):
    return num1 & num2


def bitwise_xor(num1, num2):
    return num1 ^ num2


def conv2d(input_mat, kernel_mat):
    # Ensure none of the inputs are empty.
    if input_mat.size == 0 or kernel_mat.size == 0:
        raise Exception("Error! Empty matrices found.")
        return [[]]

    # Ensure the input is a square matrix.
    if input_mat.shape[0] != input_mat.shape[1]:
        raise Exception("Error! The input is not a square matrix.")
        return [[]]

    # Ensure the kernel is a square matrix.
    if kernel_mat.shape[0] != kernel_mat.shape[1]:
        raise Exception("Error! The kernel is not a square matrix.")
        return [[]]

    # Get the size of the input and kernel matrices.
    (m, n) = input_mat.shape
    (x, y) = kernel_mat.shape

    # Ensure the kernel is not larger than the input matrix.
    if m < x:
        raise Exception("Error! The kernel is larger than the input.")
        return [[]]

    # Flip the kernel.
    # kernel_mat = np.flip(kernel_mat)

    # Set up the output matrix.
    # output_size = (m, n)
    output_mat = np.zeros(shape=(m, n), dtype=int)

    iterations_in_row = m // x
    iterations_in_column = n // y

    for i in range(iterations_in_column):
        row_no = i * y
        for j in range(iterations_in_row):
            column_no = j * x
            for k in range(x):
                for l in range(y):
                    output_mat[row_no + k][column_no + l] = bitwise_xor(input_mat[row_no + k][column_no + l],
                                                                        kernel_mat[k][l])
                    # if output_mat[row_no + k][column_no + l] > 255:
                    #     output_mat[row_no + k][column_no + l] -= 255

            # pixel11 = input_mat[row][column]
    return output_mat

    # Set up the output matrix.
    # output_size = (input_size - kernel_size) + 1
    # output_mat = np.zeros(shape=(output_size, output_size), dtype=int)
    #
    # row_offset = 0
    #
    # for output_row in range(output_size):
    #     col_offset = 0
    #
    #     for output_col in range(output_size):
    #         kernel_row = 0
    #
    #         for row in range(row_offset, row_offset + kernel_size):
    #             kernel_col = 0
    #
    #             for col in range(col_offset, col_offset + kernel_size):
    #                 # Perform the convolution computation.
    #                 output_mat[output_row, output_col] += (kernel_mat[kernel_row, kernel_col] * input_mat[row, col])
    #                 kernel_col += 1
    #
    #             kernel_row += 1
    #
    #         col_offset += 1
    #
    #     row_offset += 1
    #
    # return output_mat


if __name__ == '__main__':
    img = cv2.imread("artwork_picasso.png", cv2.IMREAD_COLOR)
    img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(img.shape)

    # cv2.imwrite("template.png", img)
    template_img = cv2.imread("template.png", cv2.IMREAD_COLOR)
    template_dim = template_img.shape
    print(template_dim)
    # (100, 100, 3)

    # print(img)
    # cv2.imshow("pi_noise_image", img)

    greyscale_dim = img_greyscale.shape
    print(greyscale_dim)
    # print(img_greyscale.shape)

    # print(img_greyscale)
    # print(type(img_greyscale))

    # cv2.imshow("Greyscale image", img_greyscale)

    """
    # This code showed that values of pixels on 3 scales are same, so we can handle corresponding greyscale image
    flag = 0
    for i in range(50):
        for j in range(50):
            c = img[i][j]
            print(c)
            if (c[0] != c[1] or c[1] != c[2]) or c[0] != c[2]:
                flag = 1
                # print(c[0])  
    print(flag)
    """

    filter_2x2 = [282, 251, 94, 0]
    # flag1 = 0
    # Either use numpy for element wise operation like convulation in general see on google
    # or use basic loop to do operation for row if it is even or odd etc.
    # for i, row in enumerate(img_greyscale):
    #     for j in range(greyscale_dim[1]):
    #         pixel = row[j]
    # pixel_value = img_greyscale[i][j]
    # print(pixel_value)
    # if i is
    # flag1 += 1
    # print(row)

    # print(flag1)

    kernal_mat = np.array([[282, 251], [94, 0]])

    input_mat = asarray(img_greyscale)
    # input_mat = asarray(img)
    # print(type(input_mat))
    # print(input_mat.shape)

    output_mat = conv2d(input_mat, kernal_mat)
    # print(output_mat)

    # output_mat = cv2.imread("template", )
    output_mat = output_mat.astype(np.uint8)

    cv2.imshow("output", output_mat)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

"""
number = 0
print(c, c[0], c[1], c[2])
_sum_ = c[0] + c[1] + c[2]
        print(_sum_ / 30)
print(c[0]/10)
number = number*10 + c[0]/10
flag += 1

print(number)
"""
