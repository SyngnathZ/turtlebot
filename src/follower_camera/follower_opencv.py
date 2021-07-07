#!/usr/bin/env python
# BEGIN ALL
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw',
                                          Image, self.image_callback)

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("window", image)
        cv2.imwrite("windows.png", image)
        cv2.waitKey(3)


rospy.init_node('follower')
follower = Follower()
rospy.spin()
# END ALL
