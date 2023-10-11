#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import PositionTarget

class SetpointPublisher:
    def __init__(self):
        self.sub = rospy.Subscriber('/rtabmap/global_pose', PoseStamped, self.callback)
        self.pub = rospy.Publisher('/mavros/setpoint_raw/local', PositionTarget, queue_size=10)

    def callback(self, data):
        # Transform the PoseStamped data into PositionTarget format
        # This is a basic transformation; you might need to adjust based on your needs
        setpoint = PositionTarget()
        setpoint.header = data.header
        setpoint.coordinate_frame = PositionTarget.FRAME_LOCAL_NED
        setpoint.type_mask = PositionTarget.IGNORE_VX + PositionTarget.IGNORE_VY + PositionTarget.IGNORE_VZ + PositionTarget.IGNORE_AFX + PositionTarget.IGNORE_AFY + PositionTarget.IGNORE_AFZ + PositionTarget.IGNORE_YAW + PositionTarget.IGNORE_YAW_RATE
        setpoint.position = data.pose.position

        self.pub.publish(setpoint)

if __name__ == '__main__':
    rospy.init_node('setpoint_transformer')
    sp = SetpointPublisher()
    rospy.spin()
