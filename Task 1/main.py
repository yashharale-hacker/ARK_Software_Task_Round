import cv2
import mpmath

img = cv2.imread("pi_image.png", cv2.IMREAD_COLOR)
img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(img.shape)

# print(img)
# cv2.imshow("pi_noise_image", img)

greyscale_dim = img_greyscale.shape
# print(greyscale_dim)
# print(img_greyscale.shape)
# print(img_greyscale)

# cv2.imshow("Greyscale image", img_greyscale)

# Set the precision to 5000 digits
mpmath.mp.dps = 3000

# Calculate pi with the desired precision
pi = mpmath.pi

# Convert pi to a string
pi_str1 = str(pi)
pi_value = pi_str1[:12]
pi_str = "3" + pi_str1[2:]

# Print the first 100 characters of pi
# print(pi_str[:100], type(pi_str[:100]))

"""
# This code showed that values of pixels on 3 scales (R, G, B) are same, so we can handle corresponding greyscale image
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

distorted_digits = []
distorted_digits_index = []

flag1 = 0

for i in range(greyscale_dim[0]):
    for j in range(greyscale_dim[1]):
        pixel_value = img_greyscale[i][j]
        # print(pixel_value)
        pixel_digit = pixel_value / 10
        pi_digit = int(pi_str[0:1])
        if pixel_digit != pi_digit:
            distorted_digits_index.append([i, j, flag1])
            distorted_digits.append(pi_digit)

        pi_str = pi_str[1:]
        flag1 += 1

# print(distorted_digits_index) # [[7, 48, 398], [18, 31, 931], [35, 34, 1784], [42, 15, 2115]]
print(distorted_digits) # [0, 8, 3, 9]
# print(img_greyscale[7][48], img_greyscale[18][31], img_greyscale[35][34], img_greyscale[42][15]) # All are 255
# print(img_greyscale[7], img_greyscale[18], img_greyscale[35], img_greyscale[42])

# cv2.waitKey(0)
#
# cv2.destroyAllWindows()

filter_2x2 = []
pi_value = float(pi_value)

for i in range(4):
    digit = distorted_digits[i]
    number = digit * 10 * pi_value
    filter_2x2.append(int(number))

# Row major order is first filling rows a11, a12, a13, ..., a1n, a21, a22, a23, ..., a2n, ..., an1, an2, an3, ..., ann
filter_2x2.sort(reverse=True)

print(filter_2x2)
# [282, 251, 94, 0]














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
