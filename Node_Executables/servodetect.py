#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64
from vesc_msgs.msg import VescStateStamped 

global thresh
global turn_div
global bub
thresh = 2.75  #edit this number for the threshold distance
turn_div = 120.0  #edit this number for the servo command divisor (larger number means milder turns)
bub = 26  #edit this number for the forbidden bubble (larger number will mandate a larger gap)

def bubble(data):
    global counter
    global direc
    global prev
    if(counter == 0): #find out what the minimum distance is located
        data = list(data.ranges)
        cone = data[-45:]+data[0:45]
        mincone = min(cone)
        Min=(cone.index(mincone))
    if(counter == 0):
        count = 0
        direc = float("inf")  #divide data into two chunks
        right = cone[0:Min]
        left = cone[Min+1:]
        for i in range(len(right)): #find gap using for loop
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
            tar = left[i]
            if(tar>thresh):
                 count+=1
            if(tar<=thresh):
                 count =0
            if(count == bub):
                 direc = i-bub/2+Min+1
                 count = 0
        if(direc != float("inf")):  #if no gap is found, use the previous servo command
            prev = direc
            pub.publish((direc-45)/turn_div+0.5)  #new servo command, proportional to the angle of the gap center
        pub2.publish(0.09)  #constant duty cycle
    counter =0


def servodetect():
    global counter
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

