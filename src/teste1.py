import rospy
from geometry_msgs.msg import PoseStamped

def rtabmap_callback(data):
    setpoint = PoseStamped()
    setpoint.header = data.header
    setpoint.pose = data.pose.pose
    # Modify the setpoint if needed
    setpoint.pose.position.z += 2.0  # for example, to hover 2 meters above the current position
    setpoint_pub.publish(setpoint)

rospy.init_node('setpoint_node')
setpoint_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=10)
rospy.Subscriber('/rtabmap/localization_pose', PoseStamped, rtabmap_callback)
rospy.spin()
