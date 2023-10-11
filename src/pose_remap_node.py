#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped

def callback(data):
    # Create a PoseStamped message
    pose_stamped = PoseStamped()

    # Copy the header
    pose_stamped.header = data.header

    # Copy the pose data
    pose_stamped.pose = data.pose.pose

    # Publish the PoseStamped message
    pub.publish(pose_stamped)

if __name__ == '__main__':
    # Initialize the node
    rospy.init_node('pose_remap_node')

    # Create a subscriber to the /rtabmap/localization_pose topic
    rospy.Subscriber('/rtabmap/localization_pose', PoseWithCovarianceStamped, callback)

    # Create a publisher for the /mavros/local_position/pose topic
    pub = rospy.Publisher('/mavros/local_position/pose', PoseStamped, queue_size=10)

    # Keep the node running
    rospy.spin()
