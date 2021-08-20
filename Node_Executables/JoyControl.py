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
    a = data.axes[5]*0.08
    rospy.loginfo(a)
    pub.publish(a)
    
     
def JoyControl():
    global a
    global pub
    a=0
    rospy.init_node("JoyControl", anonymous=True)
    rospy.Subscriber("/joy_orig", Joy, callback)
    pub = rospy.Publisher('/commands/motor/duty_cycle', Float64, queue_size=10)
    rospy.spin()  

if __name__ == '__main__':
    JoyControl()
 
