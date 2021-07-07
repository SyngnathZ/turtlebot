#!/usr/bin/env python
# BEGIN ALL
import rospy
from sensor_msgs.msg import CompressedImage
import cv2, cv_bridge
import numpy as np


def callback(data):
    # bridge = cv_bridge.CvBridge()
    np_arr = np.fromstring(data.data, np.uint8)      #Loading Compressed Image
    cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    # cv_image = cv2.imdecode(data, 1)
    # cv2.resize(cv_image, (500, 500))
    cv2.imshow("Received!!", cv_image)
    cv2.waitKey(0)


def showImage():
    rospy.init_node('catchCam', anonymous=True)
    rospy.Subscriber('camera/image/compressed', CompressedImage, callback)
    rospy.spin()


if __name__ == '__main__':
    showImage()
