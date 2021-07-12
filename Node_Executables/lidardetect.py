#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float64
from vesc_msgs.msg import VescStateStamped
from sensor_msgs.msg import LaserScan

global pub1
global pub3
global pub2

def callback(data):
    global pub1
    global pub2
    global pub3
    front_left =(data.ranges[0:10])
    front_right=(data.ranges[-10:])
    front = front_right+front_left
    Min=min(front)
    if(Min>1.5):
        verd="far"
#        print front[10]
        pub1.publish(0.125)
        pub3.publish(0.48)
    else:
        verd="near"
        brake()

def brake():
    rospy.Subscriber("/sensors/core",VescStateStamped ,getspeed)
    rospy.spin() 

def getspeed(data):
   global pub2
   global pub1
#   rospy.loginfo(data.state.current_motor)
   pub2.publish(70.0)

def lidardetect():
    global pub1
    global pub2
    global pub3
    rospy.init_node("LidarDetect", anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback)
    pub1 = rospy.Publisher("commands/motor/duty_cycle", Float64, queue_size=10)
    pub2 = rospy.Publisher("commands/motor/brake", Float64, queue_size=10)
    pub3 = rospy.Publisher("commands/servo/position",Float64, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    lidardetect()
