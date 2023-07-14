import cv2
import numpy as np


img = cv2.imread("devImg3.jpg", cv2.IMREAD_COLOR)
img1 = cv2.imread("lsdkfsdl.png", cv2.IMREAD_COLOR)

height, width = img.shape[:2]
# print(img)

b_value = img[:, :, 0]
g_value = img[:, :, 1]
r_value = img[:, :, 2]

# for i, value in enumerate(b_value):
#     print(i, value)

# print(b_value[0][0])
# print(g_value[0][0])
# print(r_value[0][0])
#
# print(b_value-g_value)
#
# print(height, width)

# cv2.imwrite("lsdkfsdl.png", img)
row = 2
col = 4

l1 = [[[[0, 127, 255]] * 3] * col] * row

# print(type(l1), len(l1))
# print(l1)
# print(l1[0])
# print(l1[0][0])
# print(l1[0][0][1])

# guess_img = np.zeros(shape=(row, col, 3), dtype=int)
# print(guess_img)

# a = 4
# b = a
# a = 8
# print(a, b)

# pixel = l1[0][0]
# pixel_value = pixel[1]
# pixel_value[1] = 8349
#
# print(l1)
# print(pixel)
# print(pixel_value)

a = 3
b = 334
c = 234
d = 9

a = b = c
print(a, b, c)

