# this console only exists to 

import os
import subprocess

# title variables
app = 'Portfolio Console'
version = 'v0.0.1'
name = app + ' ' + version

# get terminal length and width
length, width = os.get_terminal_size()

# clear console
# move cursor to first line
def clear():
  print("\033c", end='')

# seperator function
def sep(s):
  print( s * width)

# call external script
def call(proj):
  # open subprocess
  subprocess.call(["python", proj + "/main.py"])

def select():
  print('What project would you like to run?')
  proj = input()
  match (proj):
    # Run game
    case 'game':
      # open subprocess
      call('game')
    # if project not found
    case _:
      print(f"Hmm I couldn't find {proj}")

def title():
  clear()
  sep('=')
  print(name.center(width))
  sep('=')
  print()

if __name__ == "__main__":
  title()
  select()