#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absoulate, min_percent):
   # Returns True if there is enough free disk space, false otherwise
   du = shutil.disk_usage(disk)
   # calculate the percent of disk space
   percent_free = 100 - du.free / du.total
   # calculate how many free gigabytes
   gigabytes_free = du.free / 2**30
   if percent_free < min_percent or gigabytes_free < min_percent:
      return False
   return True

# check for at least 2 GB and 10% free
if not check_disk_usage("/", 2, 10):
   print("ERROR: Not Enough disk space")
   sys.exit (1)

print("Everything ok")
sys.exit(0)