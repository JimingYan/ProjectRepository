#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Int64
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64
global a
global pub

def callback(data):           ## callback triggered whenever a message from a subscribed topic is received
    global pub
    a = data.axes[5]*0.1      ## mapped data to send to the VESC
    rospy.loginfo(a)          ## print this data in terminal
    pub.publish(a)            ## publish this data
    
     
def JoyControl():
    global pub
    rospy.init_node("JoyControl", anonymous=True)    ## initilize node
    rospy.Subscriber("/joy", Joy, callback)          ## create subscriber, listen to /joy topic 
    pub = rospy.Publisher('/commands/motor/duty_cycle', Float64, queue_size=10)   ## create publisher, publishes to teh VESC
    rospy.spin()  

if __name__ == '__main__':
    JoyControl()
 
