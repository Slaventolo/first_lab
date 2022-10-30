#!/usr/bin/env python
from random import randint
import rospy
import threading
import sys
from glassbridge.srv import myService, myServiceResponse

class service:
    
    def down(self):
        print('game over')
    def generateSequence(self):
        mask = {0:'l', 1:'r'}
        array = [mask[randint(0,1)] for i in range(18)]
        print(array)
        return ''.join(array)
    def __init__(self):
        self.sequence = self.generateSequence()
        self.s = rospy.Service('myService', myService, self.callback)
        rospy.init_node('service')
        self.r = rospy.Rate(10)
        rospy.on_shutdown(self.down)
        rospy.spin()
    def callback(self, req):

        position = len(req.sequence)
        if self.sequence[position] == req.nextLetter:
            return myServiceResponse('move next')
        else:
            
            return myServiceResponse('dead')
if __name__ == '__main__':
    service = service()