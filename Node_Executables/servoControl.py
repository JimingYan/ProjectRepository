#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Int64
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64
global a
global pub

def callback(data):
    global a
    global pub
    a = data.axes[0]*0.5+0.5
    rospy.loginfo(a)
    pub.publish(a)
    
     
def servoControl():
    global a
    global pub
    rospy.init_node("Grid", anonymous=True)
    pub = rospy.Publisher('/commands/servo/position', Float64, queue_size=10)
    rospy.Subscriber("/joy", Joy, callback)
    rospy.spin()  

if __name__ == '__main__':
    servoControl()
 
