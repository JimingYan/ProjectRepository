#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64
from vesc_msgs.msg import VescStateStamped 

global rad
rad = 0.3

def bubble(data):
    global Min
    global counter
    global cone
    global direc
    global prev
    global bub
    if(counter == 0):
        data = list(data.ranges)
        cone = data[-45:]+data[0:45]
        mincone = min(cone)
        Min=(cone.index(mincone))
#        angle = math.atan(rad/(2*mincone))
        bub =24
    if(counter == 0):
        count = 0
        direc = float("inf")
        right = cone[0:Min-bub]
        left = cone[Min+bub+1:]
        thresh = 1.55
        for i in range(len(right)):
            tar =  right[i]
            if(tar>thresh):
                 count+=1
            if(tar<=thresh):
                 count =0
            if(count == bub):
                 direc = i-bub/2
                 count = 0
        count = 0
        for i in range(len(left)):
            if(left[i]>thresh):
                 count+=1
            if(left[i]<=thresh):
                 count =0
            if(count == bub):
                 direc = i-bub/2+Min+bub+1
                 count = 0
        if(direc != float("inf")):
            prev = direc
            pub.publish(direc/90.0)
            print direc, type(direc)
        pub2.publish(0.07)
    counter =0


def servodetect():
    global counter
    global angle
    global Min
    global pub
    global pub2
    counter = 0
    rospy.init_node("servodetect",anonymous = True)
    rospy.Subscriber("/scan", LaserScan, bubble)
    pub = rospy.Publisher("/commands/servo/position",Float64,queue_size=10)
    pub2 = rospy.Publisher("commands/motor/duty_cycle",Float64,queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    servodetect()

