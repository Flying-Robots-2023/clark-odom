#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped

def callback(data):
    pose_stamped = PoseStamped()
    pose_stamped.header = data.header
    pose_stamped.pose = data.pose.pose
    pub.publish(pose_stamped)

rospy.init_node('convert_pose_node')
pub = rospy.Publisher('/converted_pose', PoseStamped, queue_size=10)
rospy.Subscriber('/rtabmap/localization_pose', PoseWithCovarianceStamped, callback)
rospy.spin()
