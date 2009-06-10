#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2009 Daisuke Yabuki. All Rights Reserved.

"""Print local time and day for a given number of seconds since UNIX epoch.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import time
import sys
from optparse import OptionParser

def main():
  usage = "usage: $prog seconds_since_epoch"
  parser = OptionParser(usage=usage)
  (opsions, args) = parser.parse_args()

  if len(args) != 1:
    parser.error("one and only one argument expected")

  try:
    epoch = float(args[0])
  except ValueError:
    print "unable to parse the argument"
    sys.exit(1)

  (year, month, day,
   hour, minute, second,
   wday, yday, isdst) = time.localtime(epoch)

  print "%d/%d/%d %d:%d:%d" % (year, month, day, hour, minute, second)

if __name__ == '__main__':
  main()
