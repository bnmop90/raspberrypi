import cv2
import os

def handle_video():
	os.system('sudo modprobe bcm2835-v4l2')
	cap = cv2.VideoCapture(0)
	cap.set(3, 260)
	cap.set(4, 240)

	while True:
		ret, frame = cap.read()
		if not ret:
			print('Not Found Devices')
			break

		cv2.imshow('frame', frame)
		if cv2.waitKey(1)&0xFF == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

handle_video()
