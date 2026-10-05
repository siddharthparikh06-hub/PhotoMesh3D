import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.imwrite("output_test.jpg", image)

print("Image created successfully!")
print("OpenCV version:", cv2.__version__)
print("Image size:", image.shape)