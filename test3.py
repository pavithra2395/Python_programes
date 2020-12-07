#!/usr/bin/env python
import rospy

def start_node():
    rospy.init_node('image_pub')
    rospy.loginfo('image_pub node started')

if__name__ == '__main__':
    try:
        star_node()
    except rospy.ROSInterruptException:
         pass