# # SOURCE: https://abndistro.com/post/2019/07/07/detecting-image-differences-using-python-and-opencv/#compute-structural-similarity-index-between-images-and-obtain-difference-image

# from skimage.metrics import structural_similarity
# import cv2
# import numpy as np

# def artScoring():
#     image_orig = cv2.imread("images/heart.png")
#     image_mod = cv2.imread("result.jpg")

#     # resize for faster processing
#     resized_orig = cv2.resize(image_orig, (200, 200))    
#     resized_mod = cv2.resize(image_mod, (200, 200))

#     gray_orig = cv2.cvtColor(resized_orig, cv2.COLOR_BGR2GRAY)
#     gray_mod = cv2.cvtColor(resized_mod, cv2.COLOR_BGR2GRAY)

#     (score, diff) = structural_similarity(gray_orig, gray_mod, full=True)
#     # diff = (diff * 255).astype("uint8")
#     formatted = "{:.2f}".format(score)
#     return float(formatted)

# print(artScoring())

from cmu_112_graphics_openCV import *

def appStarted(app):
    app.username = app.getUserInput("Hello there! What's your name?").lower()

    # SOURCE: https://www.guru99.com/reading-and-writing-files-in-python.html
    f = open("users.txt", "r+")
    contents = f.readlines()
    isIn = False
    for line in contents:
        if app.username in line:
            app.day = line[-3]
            isIn = True
            print(app.day)
            break
    if isIn == False:
        f.write(f"{app.username} 1 \n")
    f.close()

    # # SOURCE: https://www.kite.com/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python
    # f = open("users.txt", "r")
    # lines = f.readlines()
    # print(lines)
    # for i in range(len(lines)):
    #     if app.username in lines[i]:
    #         lines[i] = f"{app.username} {app.day + 1} \n"
    #         print(lines[i])

    # f = open("users.txt", "w")
    # f.writelines(lines)
    # f.close()
    
   
    
    




runApp(width=500, height=300)