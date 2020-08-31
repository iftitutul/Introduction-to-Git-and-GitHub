# !/usr/bin/env python3.6

import os
import sys
import shutil
import socket
import psutil

def check_reboot():
   ## Returns True if the computer has a pending reboot
   return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_gb, min_percent):
   # Returns True if there is enough free disk space, false otherwise
   du = shutil.disk_usage(disk)
   # calculate the percent of disk space
   percent_free = 100 * du.free / du.total
   # calculate how many free gigabytes
   gigabytes_free = du.free / 2**30
   if percent_free < min_gb or gigabytes_free < min_percent:
      return True
   return False

def check_root_full():
   """Returns True if the root partition is full, False otherwise."""
   return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_no_network():
   """Returns True if it fails to resolve Google's URL,Flase otherwise."""
   try: 
      socket.gethostbyname("www.google.com")
      return False
   except:
      return True

def check_cpu_contrained():
   """Returns True if cpu load is having too much usage, Flase otherwise."""
   return psutil.cpu_percent(1) > 75

def main():
   checks = [
      (check_reboot, "Pending reboot"),
      (check_reboot, "Root partition full"),
      (check_no_network, "No working network"),
      (check_cpu_contrained,"CPU load is too high"),
   ]
   everything_ok = True
   for check, msg in checks:
      if check():
         print(msg)
         everything_ok= False
   
   if not everything_ok:
      sys.exit(1)

   print ("Everything ok")
   sys.exit(0)

main()
