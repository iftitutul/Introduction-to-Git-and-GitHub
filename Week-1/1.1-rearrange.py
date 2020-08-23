#!/usr/bin/env python3.6

import re

def rearrange_name():
   result = re.search(r"^([\w .]*), ([\w .]*)$", name)
   if result == None:
      return result
   return "{} {}".format(result[2], result[1])
