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
        pub1.publish(5000)
        pub3.publish(0.48)
    if(Min<1.5):
        verd="near"
        brake()
    print verd
def brake():
    rospy.Subscriber("/sensors/core",VescStateStamped ,applybrake)
    rospy.spin() 

def applybrake(data):
    global pub2
    global pub1
    if(data.state.speed>500):
        pub2.publish(-0.006*data.state.speed)
    else:
        pub2.publish(0.0)
def lidardetect():
    global pub1
    global pub2
    global pub3
    rospy.init_node("LidarDetect", anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback)
    pub1 = rospy.Publisher("commands/motor/speed", Float64, queue_size=10)
    pub2 = rospy.Publisher("commands/motor/current", Float64, queue_size=10)
    pub3 = rospy.Publisher("commands/servo/position",Float64, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    lidardetect()
