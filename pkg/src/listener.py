#!/usr/bin/env python
import rospy

from std_msgs.msg import Int8
from std_msgs.msg import String

class users:

    def __init__(self):
        # Publisher
        self.pub = rospy.Publisher("users",
                                   String,
                                   queue_size=1)
        self.run()

    def run(self):
        while not rospy.is_shutdown():
            password = input("press passwod: ")
            self.pub.publish(password)


if __name__ == '__main__':
    rospy.init_node('users')
    try:
        t = users()
    except rospy.ROSInterruptException:
        pass
