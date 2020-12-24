#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from roboclaw_driver.msg import Stats, SpeedCommand
from geometry_msgs.msg import Twist

pub = rospy.Publisher('roboclaw/speed_command', SpeedCommand, queue_size=10)

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo(data)
    pub.publish(data.linear.x*5000+data.angular.z*5000, data.linear.x*5000-data.angular.z*5000, 10000, 1)
    hello=0

def talker():
    #pub = rospy.Publisher('roboclaw/speed_command', SpeedCommand, queue_size=10)
    rospy.init_node('talker', anonymous=False)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #themsg = {SpeedCommand.m1_qpps: 10000, SpeedCommand.m2_qpps: -50000, SpeedCommand.accel: 10000, SpeedCommand.max_secs: 2}
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        #rospy.loginfo('10000', '-50000', '10000', '2')
        #pub.publish(1000, -1000, 10000, 1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
