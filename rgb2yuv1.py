import cv2
import numpy as np
import csv

img = cv2.imread('0.jpg')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(img_yuv)
print(y.shape)

yroi0 = y[1020:1470, 970:1420]
print(yroi0.shape)

cv2.imshow('Y channel', yroi0)
yroi1 = cv2.resize(yroi0, (int(yroi0.shape[1]/45),int(yroi0.shape[0]/45)))
print(yroi1.shape)

for byte in yroi1:
    print(byte)

cv2.imshow('Y channel', yroi1)
result = np.vstack([yroi1])
cv2.imwrite('1.jpg', result)

def print_and_save_raw_y_image(image_data, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in image_data:
            for byte in row:
                writer.writerow([byte])
                print(byte)

file = yroi1
output = "1.csv"
print_and_save_raw_y_image(file, output)

#wait

yroi0 = y[1490:1940, 980:1430]
print(yroi0.shape)

cv2.imshow('Y channel', yroi0)
yroi1 = cv2.resize(yroi0, (int(yroi0.shape[1]/45),int(yroi0.shape[0]/45)))
print(yroi1.shape)

for byte in yroi1:
    print(byte)

cv2.imshow('Y channel', yroi1)
result = np.vstack([yroi1])
cv2.imwrite('2.jpg', result)

file = yroi1
output = "2.csv"
print_and_save_raw_y_image(file, output)

#wait

yroi0 = y[1990:2440, 1000:1450]
print(yroi0.shape)

cv2.imshow('Y channel', yroi0)
yroi1 = cv2.resize(yroi0, (int(yroi0.shape[1]/45),int(yroi0.shape[0]/45)))
print(yroi1.shape)

for byte in yroi1:
    print(byte)

cv2.imshow('Y channel', yroi1)
result = np.vstack([yroi1])
cv2.imwrite('3.jpg', result)

file = yroi1
output = "3.csv"
print_and_save_raw_y_image(file, output)

#wait

yroi0 = y[2510:2960, 1000:1450]
print(yroi0.shape)

cv2.imshow('Y channel', yroi0)
yroi1 = cv2.resize(yroi0, (int(yroi0.shape[1]/45),int(yroi0.shape[0]/45)))
print(yroi1.shape)

for byte in yroi1:
    print(byte)

cv2.imshow('Y channel', yroi1)
result = np.vstack([yroi1])
cv2.imwrite('4.jpg', result)

file = yroi1
output = "4.csv"
print_and_save_raw_y_image(file, output)

#wait

yroi0 = y[2990:3440, 1020:1470]
print(yroi0.shape)

cv2.imshow('Y channel', yroi0)
yroi1 = cv2.resize(yroi0, (int(yroi0.shape[1]/45),int(yroi0.shape[0]/45)))
print(yroi1.shape)

for byte in yroi1:
    print(byte)

cv2.imshow('Y channel', yroi1)
result = np.vstack([yroi1])
cv2.imwrite('5.jpg', result)

file = yroi1
output = "5.csv"
print_and_save_raw_y_image(file, output)
