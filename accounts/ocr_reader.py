# Main.py

import cv2
import numpy as np
import os
from picamera import PiCamera
from time import sleep
import time

from .DetectChars import *
from .DetectPlates import *
from .PossiblePlate import *
module_dir = os.path.dirname(__file__) 

# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False

  


###################################################################################################
def ocr_reader(request):

    blnKNNTrainingSuccessful = loadKNNDataAndTrainKNN()         # attempt KNN training

    if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
        print("\nerror: KNN traning was not successful\n")  # show error message
        return                                                          # and exit program
    # end if
    
    # cam = cv2.VideoCapture(0)
    # # const char *pipeline = " tcambin serial=15810833 ! video/x-raw, format=BGRx, width=1280,height=960, framerate=25/1 ! videoconvert ! appsink"
    # # cv::VideoCapture *cap = new cv::VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    # ret, frame = cam.read()
    # firstimage = os.path.join(module_dir, '../static/images/LicPlateImages/imgOriginalSceneCapture.jpg')
    # img_name = firstimage
    # cv2.imwrite(img_name, frame)

    


    # camera = picamera.PiCamera()
    # camera.start_preview() 
    # sleep(5)
    # camera.capture('LicPlateImages/imgOriginalSceneCapture.jpg')
    # camera.stop_preview()
    # 
    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    firstimage = os.path.join(module_dir, '../static/images/LicPlateImages/capturedimage1.jpg')
    camera.capture(firstimage)
    camera.stop_preview()
    camera.close()


    

    # camera.capture('/LicPlateImages/imgOriginalSceneCapture.jpg')
    secondimage = os.path.join(module_dir, '../static/images/LicPlateImages/capturedimage.jpg')
    # secondimage = os.path.join(module_dir, 'LicPlateImages/2.jpeg')
    image = cv2.imread(secondimage)             #Modified Slightly 
    inverted = np.invert(image)

    thirdimage = os.path.join(module_dir, '../static/images/LicPlateImages/capturedimageinverted.jpg')                                        
    cv2.imwrite(thirdimage, inverted)    

    fourthimage = os.path.join(module_dir, '../static/images/LicPlateImages/capturedimageinverted.jpg') 
    imgOriginalScene = cv2.imread(fourthimage)     
   
    #imgOriginalScene = cv2.imread("LicPlateImages/16.png")               # open image

    if imgOriginalScene is None:                            # if image was not read successfully
        print("\nerror: image not read from file \n\n")  # print error message to std out
        os.system("pause")                                  # pause so user can see error message
        return                                              # and exit program
    # end if

    listOfPossiblePlates = detectPlatesInScene(imgOriginalScene)           # detect plates

    listOfPossiblePlates = detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates

    # cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image

    if len(listOfPossiblePlates) == 0:                          # if no plates were found
        print("\nno license plates were detected\n")  # inform user no plates were found
        error = "None"
        return error
    else:                                                       # else
                # if we get in here list of possible plates has at leat one plate

                # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]

        # cv2.imshow("imgPlate", licPlate.imgPlate)           # show crop of plate and threshold of plate
        # cv2.imshow("imgThresh", licPlate.imgThresh)

        if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
            print("\nno characters were detected\n\n")  # show message
            error = "None"
            return error                             # and exit program
        # end if

        drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             # draw red rectangle around plate

        print("\nlicense plate read from image = " + licPlate.strChars + "\n")  # write license plate text to std out
        print("----------------------------------------")

        writeLicensePlateCharsOnImage(imgOriginalScene, licPlate)           # write license plate text on the image

        # cv2.imshow("imgOriginalScene", imgOriginalScene)                # re-show scene image
        fifthimage = os.path.join(module_dir, '../static/images/LicPlateImages/capturedimageocr.jpg')
        cv2.imwrite(fifthimage, imgOriginalScene)           # write image out to file

    # end if else

    return licPlate.strChars

# end main

###################################################################################################
# def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

#     p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)            # get 4 vertices of rotated rect

#     cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)         # draw 4 red lines
#     cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
#     cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
#     cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)
# # end function

def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):
    # get 4 vertices of rotated rect
    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)
    # convert float arrays to int tuples for use with cv2.line()
    p0 = (int(p2fRectPoints[0][0]), int(p2fRectPoints[0][1]))
    p1 = (int(p2fRectPoints[1][0]), int(p2fRectPoints[1][1]))
    p2 = (int(p2fRectPoints[2][0]), int(p2fRectPoints[2][1]))
    p3 = (int(p2fRectPoints[3][0]), int(p2fRectPoints[3][1]))
    # draw 4 red lines
    cv2.line(imgOriginalScene, p0, p1, SCALAR_RED, 2)
    cv2.line(imgOriginalScene, p1, p2, SCALAR_RED, 2)
    cv2.line(imgOriginalScene, p2, p3, SCALAR_RED, 2)
    cv2.line(imgOriginalScene, p3, p0, SCALAR_RED, 2)

###################################################################################################
def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
    ptCenterOfTextAreaX = 0                             # this will be the center of the area the text will be written to
    ptCenterOfTextAreaY = 0

    ptLowerLeftTextOriginX = 0                          # this will be the bottom left of the area that the text will be written to
    ptLowerLeftTextOriginY = 0

    sceneHeight, sceneWidth, sceneNumChannels = imgOriginalScene.shape
    plateHeight, plateWidth, plateNumChannels = licPlate.imgPlate.shape

    intFontFace = cv2.FONT_HERSHEY_SIMPLEX                      # choose a plain jane font
    fltFontScale = float(plateHeight) / 30.0                    # base font scale on height of plate area
    intFontThickness = int(round(fltFontScale * 1.5))           # base font thickness on font scale

    textSize, baseline = cv2.getTextSize(licPlate.strChars, intFontFace, fltFontScale, intFontThickness)        # call getTextSize

            # unpack roatated rect into center point, width and height, and angle
    ( (intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg ) = licPlate.rrLocationOfPlateInScene

    intPlateCenterX = int(intPlateCenterX)              # make sure center is an integer
    intPlateCenterY = int(intPlateCenterY)

    ptCenterOfTextAreaX = int(intPlateCenterX)         # the horizontal location of the text area is the same as the plate

    if intPlateCenterY < (sceneHeight * 0.75):                                                  # if the license plate is in the upper 3/4 of the image
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) + int(round(plateHeight * 1.6))      # write the chars in below the plate
    else:                                                                                       # else if the license plate is in the lower 1/4 of the image
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) - int(round(plateHeight * 1.6))      # write the chars in above the plate
    # end if

    textSizeWidth, textSizeHeight = textSize                # unpack text size width and height

    ptLowerLeftTextOriginX = int(ptCenterOfTextAreaX - (textSizeWidth / 2))           # calculate the lower left origin of the text area
    ptLowerLeftTextOriginY = int(ptCenterOfTextAreaY + (textSizeHeight / 2))          # based on the text area center, width, and height

            # write the text on the image
    cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY), intFontFace, fltFontScale, SCALAR_YELLOW, intFontThickness)
# end function

###################################################################################################


# if __name__ == "__main__":
#     ocr_reader()


















