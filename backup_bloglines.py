#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2008 Daisuke Yabuki All Rights Reserved.

"""Backup a list of feeds you subscribe at Bloglines in OPML."""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import datetime
import os
import shutil
import sys
import urllib2

username = 'dxy'
backup_dir = os.path.join(os.getenv('HOME'), 'var/bloglines/')
#backup_dir = '%s/var/bloglines/' % os.getenv('HOME')
#backup_dir = '/tmp/'

def BackupOpml():

  today = datetime.date.today()

  # create a daily backup
  opml_file_name = '%s.opml' % today.strftime("%a")    # e.g. Mon.opml
  opml_file_path = os.path.join(backup_dir, opml_file_name)
  export_url = 'http://www.bloglines.com/export?id=%s' % username

  req = urllib2.Request(export_url)
  try:
    response = urllib2.urlopen(req)
  except urllib2.HTTPError, e:
    print e.code, e.msg
    sys.exit(1)

  output = open(opml_file_path, 'w')
  for l in response:
    output.write(l)
  output.close()

  return opml_file_path

def MonthlyBackup(opml_file_path):

  today = datetime.date.today()

  # if today is 1st day of the month, make a separate backup
  if today.day != 1:
    return

  backup_file_path = '%s/%d-%d.opml' % (backup_dir, today.year, today.month)
  print opml_file_path
  if not os.path.exists(opml_file_path):
    print 'opml file doesn\'t exist'
    sys.exit(1)

  try:
    shutil.copyfile(opml_file_path, backup_file_path)
  except IOError, e:
    print 'failed to make a monthly backup %s' % e

def main():
  opml_file_path = BackupOpml()
  MonthlyBackup(opml_file_path)

if __name__ == '__main__':
  main()
