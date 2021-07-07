#!/usr/bin/env python
# BEGIN ALL
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge


def callback(data):
    bridge = cv_bridge.CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    # cv2.resize(cv_image, (500, 500))
    cv2.imshow("Received!!", cv_image)
    cv2.waitKey(0)


def showImage():
    rospy.init_node('catchCam', anonymous=True)
    rospy.Subscriber('camera/rgb/image_raw', Image, callback)
    rospy.spin()


if __name__ == '__main__':
    showImage()
