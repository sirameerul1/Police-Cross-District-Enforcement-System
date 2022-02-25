# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.models import load_model

from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
# from picamera import PiCamera
# import picamera
from time import sleep
import time

from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from .models import *
from django.views import *
import io
from threading import Condition

module_dir = os.path.dirname(__file__) 

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
# face_detection_webcam = cv2.CascadeClassifier(os.path.join(
# 			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
# # load our serialized face detector model from disk
# prototxtPath = os.path.sep.join([settings.BASE_DIR, "face_detector/deploy.prototxt"])
# weightsPath = os.path.sep.join([settings.BASE_DIR,"face_detector/res10_300x300_ssd_iter_140000.caffemodel"])
# faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
# maskNet = load_model(os.path.join(settings.BASE_DIR,'face_detector/mask_detector.model'))




class VideoCamera2(object):						#Face Detection Camera 2
	def __init__(self):


		self.video2 = cv2.VideoCapture(1, cv2.CAP_V4L) #tukar raspi cam web2
		self.video2.set(3,426)
		self.video2.set(4,240)


	def __del__(self):
		self.video2.release()

	def get_frame(self):
		success, image2 = self.video2.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image2, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		frame_flip2 = cv2.flip(image2,1)
		ret, jpeg2 = cv2.imencode('.jpg', frame_flip2)
		return jpeg2.tobytes()

class VideoCamera1(object):		 #tukar raspi cam web				#Face Detection Camera 1
	def __init__(self):
		self.video = cv2.VideoCapture(3, cv2.CAP_V4L)
		self.video.set(3,426)
		self.video.set(4,240)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()



from picamera.array import PiRGBArray
from picamera import PiCamera

class PiCamera(object):							#Camera 1
	def __init__(self):
		self.camera = cv2.VideoCapture(0, cv2.CAP_V4L) #tukar raspi cam pi
		# self.camera.set(3,1280)
		# self.camera.set(4,720)

		time.sleep(0.1)
		
	
	def __del__(self):
		self.camera.release()
	
	def get_frame(self):
		success, image2 = self.camera.read()
		# frame_flip2 = cv2.flip(image2,1)
		ret, jpeg2 = cv2.imencode('.jpg', image2)
		return jpeg2.tobytes()



		# rawCapture = PiRGBArray(self.video1)
		# time.sleep(0.1)
		# self.video1.capture(rawCapture, format="bgr")
		# image1 = rawCapture.array
		# frame_flip1 = cv2.flip(image1,1)
		# ret, jpeg1 = cv2.imencode('.jpg', frame_flip1)
		# return jpeg1.tobytes()




	# def __del__(self):
	# 	self.video3.stop_preview()
	# 	self.video3.close()

	# def get_frame(self):
	# 	success, image3 = self.video3.read()
	# 	frame_flip3 = cv2.flip(image3,1)
	# 	ret, jpeg3 = cv2.imencode('.jpg', frame_flip3)
	# 	return jpeg3.tobytes()



# class MaskDetect(object):
	
# 	def __init__(self):
# 		# self.vs = VideoStream(src=0).start()
# 		#
# 		self.video = cv2.VideoCapture(0, cv2.CAP_V4L)
# 		self.video.set(3,426)
# 		self.video.set(4,240)
# 		#

# 	def __del__(self):
# 		# cv2.destroyAllWindows()
# 		#
# 		self.video.release()
# 		#

# 	def detect_and_predict_mask(self,frame, faceNet, maskNet):
# 		# grab the dimensions of the frame and then construct a blob
# 		# from it
# 		(h, w) = frame.shape[:2]
# 		blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
# 									 (104.0, 177.0, 123.0))

# 		# pass the blob through the network and obtain the face detections
# 		faceNet.setInput(blob)
# 		detections = faceNet.forward()

# 		# initialize our list of faces, their corresponding locations,
# 		# and the list of predictions from our face mask network
# 		faces = []
# 		locs = []
# 		preds = []

# 		# loop over the detections
# 		for i in range(0, detections.shape[2]):
# 			# extract the confidence (i.e., probability) associated with
# 			# the detection
# 			confidence = detections[0, 0, i, 2]

# 			# filter out weak detections by ensuring the confidence is
# 			# greater than the minimum confidence
# 			if confidence > 0.5:
# 				# compute the (x, y)-coordinates of the bounding box for
# 				# the object
# 				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
# 				(startX, startY, endX, endY) = box.astype("int")

# 				# ensure the bounding boxes fall within the dimensions of
# 				# the frame
# 				(startX, startY) = (max(0, startX), max(0, startY))
# 				(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

# 				# extract the face ROI, convert it from BGR to RGB channel
# 				# ordering, resize it to 224x224, and preprocess it
# 				face = frame[startY:endY, startX:endX]
# 				face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
# 				face = cv2.resize(face, (224, 224))
# 				face = img_to_array(face)
# 				face = preprocess_input(face)

# 				# add the face and bounding boxes to their respective
# 				# lists
# 				faces.append(face)
# 				locs.append((startX, startY, endX, endY))

# 		# only make a predictions if at least one face was detected
# 		if len(faces) > 0:
# 			# for faster inference we'll make batch predictions on *all*
# 			# faces at the same time rather than one-by-one predictions
# 			# in the above `for` loop
# 			faces = np.array(faces, dtype="float32")
# 			preds = maskNet.predict(faces, batch_size=32)
# 			# preds = maskNet.predict(faces, batch_size=2)

# 		# return a 2-tuple of the face locations and their corresponding
# 		# locations
# 		return (locs, preds)

# 	# def get_frame(self):
# 	# 	success, image2 = self.video2.read()
# 	# 	frame_flip2 = cv2.flip(image2,1)
# 	# 	ret, jpeg2 = cv2.imencode('.jpg', frame_flip2)
# 	# 	return jpeg2.tobytes()

# 	def get_frame(self):
# 		# frame = self.vs.read()
# 		success, frame = self.video.read()
# 		# frame = imutils.resize(frame, width=650)
# 		frame = cv2.flip(frame, 1)
# 		# detect faces in the frame and determine if they are wearing a
# 		# face mask or not
# 		(locs, preds) = self.detect_and_predict_mask(frame, faceNet, maskNet)

# 		# loop over the detected face locations and their corresponding
# 		# locations
# 		for (box, pred) in zip(locs, preds):
# 			# unpack the bounding box and predictions
# 			(startX, startY, endX, endY) = box
# 			(mask, withoutMask) = pred

# 			# determine the class label and color we'll use to draw
# 			# the bounding box and text
# 			label = "Mask" if mask > withoutMask else "No Mask"
# 			color = (0, 255, 0) if label == "Mask" else (0, 0, 255) #BRG

# 			# include the probability in the label
# 			label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

# 			# display the label and bounding box rectangle on the output
# 			# frame
# 			cv2.putText(frame, label, (startX, startY - 10),
# 						cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
# 			cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
# 		ret, jpeg = cv2.imencode('.jpg', frame)
# 		return jpeg.tobytes()
