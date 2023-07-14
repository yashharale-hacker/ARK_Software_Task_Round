# # import the cv2 package
# import cv2
#
# # read the image
# img = cv2.imread('download.jpeg')
# for i, row in enumerate(img):
#     # get the pixel values by iterating
#     for j, pixel in enumerate(img):
#         if (i == j or i + j == img.shape[0]):
#             # update the pixel value to black
#             img[i][j] = [0, 0, 0]
#
# # display image
# cv2.imshow("output", img)
# cv2.imwrite("output.png", img)
# print(54//5)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import mpmath

# Set the precision to 5000 digits
mpmath.mp.dps = 20

# Calculate pi with the desired precision
pi = mpmath.pi
print(pi, type(pi))
pi = float(pi)
print(pi, type(pi))

# Convert pi to a string
# pi_str1 = str(pi)
# pi_value = pi_str1[:12]
# pi_str = "3" + pi_str1[2:]

choices = [0, 200, 400, 600, 800, 1000, 300, 500, 700, 900, 1100]
pwd = []

for choice in choices:
    c = pi * choice
    pwd.append(int(c))
    print(int(c))

# 0
# 628 - Password
# 1256
# 1884
# 2513
# 3141
# 942
# 1570
# 2199
# 2827
# 3455