#!/usr/bin/env python
import rospy

from std_msgs.msg import Int8
from std_msgs.msg import String

class computer:

    def __init__(self):
        # Subscriber
        self.sub = rospy.Subscriber("admin",
                                    String,
                                    self.callback_msg)
        self.key = 0
        rospy.spin()



# do not look further spoilers!!!!!!!!!!!!!!!!!!!!!!!!!!!














# i am siriusly
















# go back













# phhh....

    def callback_msg(self, msg):
        if self.key == 0:
            if msg.data == "passwod":
                print( " _________________________\n"+
                       "( ... you are welocme  ...)\n"+
                       " -------------------------\n"+
                       "        o   ^__^\n"+
                       "         o  (oo)\_______\n"+
                       "            (__)\       )\/\\\n"+
                       "                ||----w |\n"+
                       "                ||     ||\n")
                self.key = 1
            else:
                print("access denied")
        else:
            print( " _________________________\n"+
                   "( .. that's all go home ..)\n"+
                   " -------------------------\n"+
                   "        o   ^__^\n"+
                   "         o  (oo)\_______\n"+
                   "            (__)\       )\/\\\n"+
                   "                ||----w |\n"+
                   "                ||     ||\n")

if __name__ == '__main__':
    rospy.init_node('computer')
    try:
        t = computer()
    except rospy.ROSInterruptException:
        pass
