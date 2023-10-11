#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

def callback(data):
    pose_stamped = PoseStamped()
    pose_stamped.header = data.header
    pose_stamped.pose = data.pose.pose

    pub.publish(pose_stamped)

rospy.init_node('odom_to_posestamped')
sub = rospy.Subscriber('/mavros/odometry/out', Odometry, callback)
pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=10)
rospy.spin()
