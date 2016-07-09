#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys
import datetime

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = (s+' ')*3 # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result += '!!!'
    return result

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  # Get the second name from the command line, using '' as a fallback.
  if len(sys.argv) >= 3:
    name2 = sys.argv[2]
  else:
    name2 = ''

  #Print stuff
  print ('Hello', name, name2)
  if (name2 != ''):
    print (repeat(name2, True))
  print ('Today is ' + str(datetime.datetime.now().date().strftime("%A, %m/%d/%y")))
  print ('The time is a bitchin ' + str(datetime.datetime.now().time().strftime("%I:%M %p")) + '!!!')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
