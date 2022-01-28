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
    front_left =(data.ranges[0:10])  ## create cone of detection infront of lidar 
    front_right=(data.ranges[-10:])
    front = front_right+front_left
    Min=min(front)
    if(Min>=0.5):         ## if no object for 0.5m in front of the car, run speed command to VESC for forward motion. 
        verd="far"
        pub1.publish(5000)      
        pub3.publish(0.48)
    if(Min<0.5):         ## if obstacle is detected, start brakes and print "near" on screen
        verd="near"
        brake()
    print verd
def brake():              ## create a subsriber that listens to /sensors/core
    rospy.Subscriber("/sensors/core",VescStateStamped ,applybrake)
    rospy.spin() 

def applybrake(data):
    global pub2
    global pub1
    if(data.state.speed>500): ## execute a braking command to stop the motor
        pub2.publish(15)
    else:
        pub2.publish(0.0)
def lidardetect():
    global pub1
    global pub2
    global pub3
    rospy.init_node("LidarDetect", anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback)
    pub1 = rospy.Publisher("commands/motor/speed", Float64, queue_size=10)
    pub2 = rospy.Publisher("commands/motor/brake", Float64, queue_size=10)
    pub3 = rospy.Publisher("commands/servo/position",Float64, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    lidardetect()
