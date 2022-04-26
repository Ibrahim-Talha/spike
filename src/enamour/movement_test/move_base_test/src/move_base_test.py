#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
import numpy as np
import math
from tf.transformations import quaternion_from_euler
from tf.transformations import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



def movebase_client():

    rospy.loginfo("Starting client")
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    rospy.loginfo("Setting parameters")
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "base_link"
    goal.target_pose.header.stamp = rospy.Time.now()
    x_input = float(input("Input meters to move forwards/backwards: "))
    y_input = float(input("Input meters to move left/right: "))
    degree = float(input("how much degree: "))

    q_rot = quaternion_from_euler( 0, 0, np.radians(degree) ) # wandelt den float in radianten und bildet daraus von euler winkel in quationen um

    goal.target_pose.pose.position.x = x_input
    goal.target_pose.pose.position.y = y_input
    
    goal.target_pose.pose.orientation.x = q_rot[0] # setzt qx-quaternion Wert ein
    goal.target_pose.pose.orientation.y = q_rot[1] # setzt qy-quaternion Wert ein
    goal.target_pose.pose.orientation.z = q_rot[2] # setzt qz-quaternion Wert ein
    goal.target_pose.pose.orientation.w = q_rot[3] # setzt qw-quaternion Wert ein


  

    print("Sending command to action server")
    client.send_goal(goal)
    wait = client.wait_for_result()
    print("Action server received result")
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()





if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
