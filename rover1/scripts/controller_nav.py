#!/usr/bin/env python

import threading
import rospy
import time
from rospy.timer import Rate
from std_msgs.msg import Float64

def steer1():
    pub = rospy.Publisher('/rover2/steersxfront/command', Float64, queue_size=10)
    #rospy.init_node('controller_nav', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = (-0.785)
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

def steer2():
    pub = rospy.Publisher('/rover2/steerdxfront/command', Float64, queue_size=10)
    #rospy.init_node('controller_nav', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = (0.785)
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

def steer3():
    pub = rospy.Publisher('/rover2/steersxrear/command', Float64, queue_size=10)
    #rospy.init_node('controller_nav', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = (0.785)
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

def steer4():
    pub = rospy.Publisher('/rover2/steerdxrear/command', Float64, queue_size=10)
    #rospy.init_node('controller_nav', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = (-0.785)
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('controller_nav', anonymous=True)
        thread1=threading.Thread(target=steer1)
        thread2=threading.Thread(target=steer2)
        thread3=threading.Thread(target=steer3)
        thread4=threading.Thread(target=steer4)
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        time.sleep(3)
        thread1.stop()
        thread2.stop()
        thread3.stop()
        thread4.stop()
    except rospy.ROSInterruptException:
        pass