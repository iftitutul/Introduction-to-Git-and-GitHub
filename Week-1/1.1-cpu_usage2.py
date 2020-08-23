#!/usr/bin/env python3.6

import psutil

def check_cpu_usage(percent):
   usage = psutil.cpu_percent()
   print ("DEBUG: usage: {}".format(usage))
   return usage < percent

if not check_cpu_usage(75):
   print("ERROR! CPU is overloaded")
else:
   print("Everything ok")