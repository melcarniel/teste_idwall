import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path")
args = vars(ap.parse_args())

img = cv2.imread("circles.png")
saida = img.copy()
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circulo = cv2.HoughCircles(cinza, cv2.HOUGH_GRADIENT, 1.2, 10)

if circulo is not None:
    circulo = np.round(circulo[0,:]).astype("int")

    for(x, y, r) in circulo:
        cv2.circle(saida, (x, y), r, (0, 255, 0), 4)

    cv2.imshow("saida", np.hstack([img, saida]))
    cv2.waitKey(0)

print(circulo)

