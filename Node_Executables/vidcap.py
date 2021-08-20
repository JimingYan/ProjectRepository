#!/usr/bin/env python

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def callback(data):
    global vid
    global convert
    cv_image = convert.imgmsg_to_cv2(data, "bgr8")
    vid.write(cv_image)
    cv2.waitKey(1)
  
def vidcap():
    global vid
    global convert
    convert = CvBridge()
    print "okay"
    vid = cv2.VideoWriter("a.mp4",cv2.VideoWriter_fourcc(*'mp4v'), 15, (640,480),True)
    rospy.init_node("vidcap",anonymous=True)
    rospy.Subscriber("/camera/color/image_raw",Image,callback)
    rospy.spin()
    vid.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    vidcap()
