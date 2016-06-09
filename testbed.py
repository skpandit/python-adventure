#!/usr/bin/env/python
import subprocess
import time
from subprocess import Popen, PIPE
testbed = raw_input("Enter nsghw/dcdev/dchw/qa/vtb\n")
counter = raw_input("The program retries after every 10 seconds for 20 times if you want to modify the retry counter enter a value, if not just press enter\n")
if (counter == ""):
        retryCounter = 20
else:
        retryCounter = int(counter)
list=[]
count = 0
while (len(list) == 0 and count < retryCounter):
        if (count!=0):
                print "Retrying after 10 seconds of sleep"
                retriesLeft=retryCounter-count
                print str(retriesLeft) + " tries left"
                time.sleep(10)
        l = subprocess.Popen(['ls /usr/global/regression/idle'],stdout=subprocess.PIPE,shell=True)
        for x in l.stdout:
                if testbed in x:
                        x=x.strip('\n')
                        list.append(x)
        count+=1
if (len(list) == 0) :
        timePassed=10*retryCounter
        print "No Testbeds available after " + str(timePassed) + " seconds"
else:
        print "Testbed/s " + str(list) + " available"

