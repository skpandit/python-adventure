#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import urllib
import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  string="file:///C:\Python27\google-python-exercises\babynames" + filename
  f=urllib.urlopen(filename).read()
  match=re.search(r'Popularity in (\d\d\d\d)' ,f)
  opfileName=filename+".summary"
  target=open(opfileName,'w')
  newMatch=re.findall(r'<td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', f)
  dicts={}
  mylist=[]
  mylist.append(match.group(1))
  for l in newMatch:
    rank=l[0]
    name1=l[1]
    name2=l[2]
    if (name1 in dicts):
      if(dicts[name1]>rank):
        dicts[name1]=rank
    else:
      dicts[name1]=rank
    if(name2 in dicts):
      if(dicts[name2]>rank):
        dicts[name2]=rank
    else:
      dicts[name2]=rank
  for key in sorted(dicts.keys()):
    item = key + " " + dicts[key]
    mylist.append(item)
  text='\n'.join(mylist)+'\n'
  target.write(text)
  target.close()
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)
  
  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  i=0
  while(i<len(args)):
    extract_names(args[i])
    i+=1
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
    
if __name__ == '__main__':
  main()