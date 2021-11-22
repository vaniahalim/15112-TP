# SOURCE: https://abndistro.com/post/2019/07/07/detecting-image-differences-using-python-and-opencv/#compute-structural-similarity-index-between-images-and-obtain-difference-image

from skimage.metrics import structural_similarity
import cv2
import numpy as np

def artScoring():
    image_orig = cv2.imread("images/heart.png")
    image_mod = cv2.imread("result.jpg")

    # resize for faster processing
    resized_orig = cv2.resize(image_orig, (200, 200))    
    resized_mod = cv2.resize(image_mod, (200, 200))

    gray_orig = cv2.cvtColor(resized_orig, cv2.COLOR_BGR2GRAY)
    gray_mod = cv2.cvtColor(resized_mod, cv2.COLOR_BGR2GRAY)

    (score, diff) = structural_similarity(gray_orig, gray_mod, full=True)
    # diff = (diff * 255).astype("uint8")
    formatted = "{:.2f}".format(score)
    return float(formatted)

print(artScoring())