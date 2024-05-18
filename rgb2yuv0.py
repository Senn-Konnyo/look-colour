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
yroi1 = cv2.resize(yroi0, (int(yroi0.shape[1]/25),int(yroi0.shape[0]/25)))
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
output = "0.csv"
print_and_save_raw_y_image(file, output)