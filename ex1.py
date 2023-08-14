import atexit
import time
import bisect
import sys
import random
import os

#logger.error='Test message 1!'
from . import log
log.as1="as1log"

class MyEnvironment(Model):
    pass
log.as1="as1"
#####
# create an act-r agent

class MyAgent(ACTR):
    
    focus=Buffer()
    focus.set('sandwich bread')
    log.as1="aso111"
    #log.as2="aaa"
    def bread_bottom(focus='sandwich bread'):     # if focus buffer has this chunk then....
        print("I have a piece of bread")           # print
        log.as1='goal1'
        focus.set('sandwich cheese')              # change chunk in focus buffer

    def cheese(focus='sandwich cheese'):          # the rest of the productions are the same
        print ("ended")    # but carry out different actions
        log.as2='goal2'
        focus.set('stop')
    def stop_production(focus='stop'):
        self.stop()                        # stop the agent
##
##    def ham(focus='sandwich ham'):
##        print "I have put  ham on the cheese"
##        focus.set('sandwich bread_top')
##
##    def bread_top(focus='sandwich bread_top'):
##        print "I have put bread on the ham"
##        print "I have made a ham and cheese sandwich"
##        focus.set('stop')   
##
