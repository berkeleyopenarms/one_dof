#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float64

pub = rospy.Publisher('/motor_controller/command', Float64, queue_size=1)
rospy.init_node('move_motor')
r = rospy.Rate(20)

while not rospy.is_shutdown():
   rospy.loginfo("Publishing motor command")
   pub.publish(math.pi)
   r.sleep()
