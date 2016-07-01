#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess
"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def printDirContents(path):
  string=subprocess.Popen(["dir", path],stdout=subprocess.PIPE,shell=True)
  (out,err)=string.communicate()
  temp=out.split('\n')
  listOfFiles=[]
  for l in temp:
    if(re.search(r'__\w*__', l) != None):
      temp2=l.split()
      x=os.path.abspath(temp2[4])
      listOfFiles.append(x)
  return listOfFiles

def copyFiles(path,todir):
  list=printDirContents(path)
  p=os.path.exists(todir)
  if(p!=True):
    os.makedirs(todir)
  for l in list:
    try:
      shutil.copy(l,todir)
    except shutil.Error as e:
      print 'Error: %s' % e
    except IOError as e:
      print 'Error: %s' % e.strerror

def zipFiles(path,tozip):
  list=printDirContents(path)
  str1=""
  for l in list:
    l=l+" , "
    str1+=l
  str1=str1[:-2]
  try:
    string=subprocess.Popen(["7z", "a", "-tzip", tozip, str1],stdout=subprocess.PIPE,shell=True)
  except IOError as e:
    print '7z Error: %s' % e.strerror
    
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] != '':
    list=printDirContents(args[0])
    for l in list:
      print l
    
  if args[0] == '--todir':
    todir = args[1]
    path=args[2]
    copyFiles(path,todir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    path=args[2]
    zipFiles(path,tozip)
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
