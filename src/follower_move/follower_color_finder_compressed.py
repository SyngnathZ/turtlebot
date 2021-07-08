#!/usr/bin/env python
# BEGIN ALL
import rospy, cv2, cv_bridge
from sensor_msgs.msg import CompressedImage
import numpy as np


def callback(data):
    # bridge = cv_bridge.CvBridge()
    np_arr = np.fromstring(data.data, np.uint8)  # Loading Compressed Image
    cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    # END HSV
    # BEGIN FILTER
    lower_yellow = np.array([10, 10, 150])
    upper_yellow = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # END FILTER
    # masked = cv2.bitwise_and(cv_image, cv_image, mask=mask)

    # BEGIN CROP
    h, w, d = cv_image.shape
    search_top = 3 * h / 4
    search_bot = search_top + 20
    mask[0:search_top, 0:w] = 0
    mask[search_bot:h, 0:w] = 0
    # END CROP
    # BEGIN FINDER
    M = cv2.moments(mask)
    if M['m00'] > 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        # END FINDER
        # BEGIN CIRCLE
        cv2.circle(cv_image, (cx, cy), 20, (0, 0, 255), -1)
    # END CIRCLE

    # OPTIMZE THE SIZE OF WINDOW
    cv2.namedWindow("window", 0);
    width = 1200
    height = 800
    cv2.resizeWindow("window", int(width * (height - 80) / height), height - 80);
    cv2.imshow("window", cv_image)
    cv2.waitKey(3)


def showImage():
    rospy.init_node('catchCam', anonymous=True)
    rospy.Subscriber('camera/rgb/image_raw/compressed', CompressedImage, callback)
    rospy.spin()


if __name__ == '__main__':
    showImage()
