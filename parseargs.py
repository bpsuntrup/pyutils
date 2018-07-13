'''
pass a dictionary of single letter switches to multi-letter switch names.
This parses arguments
Right now it doesn't validate arguments belong to any specific set
right now it doesn't do anything
I'm just bored
'''

import sys

print(sys.argv)

class ArgError(Exception):
  pass

''' types of switches: 

on/off
-a

with parameter
-a hi

with several parameters
-a hi there

preceding args
blah 

trailing args

'''

switch_dict = {
  'a': 'apple',
  'g': 'great',
  'd': 'day',
}

def parseargs(switch_dict):
  pa = []
  ta = []
  preceding_args = True
  expect_trailing_arg = False
  expecting_parameter = False
  current_switch = None
  switches = {}
  for arg in sys.argv[1:]:
    if arg[0] == '-':
      expecting_parameter = False
      expecting_trailing_arg = False
      preceding_args = False
      if current_switch is not None:
        if current_switch not in switches.keys():
          switches[current_switch] = []
        current_switch = None
      if len(arg) == 1:
        raise ArgError('- is not a valid arg')
      elif arg[1] == '-':
        print 'longswitch: {}'.format(arg)
        expecting_parameter = True
        current_switch = arg[2:]
        expect_trailing_arg = False
      else:
        print 'switch: {}'.format(arg)
        if len(arg) == 2:
          expecting_parameter = True
          current_switch = switch_dict[arg[1]]
          expect_trailing_arg = False
        else:
          for char in arg[1:]:
            switches[switch_dict[char]] = []
          expect_trailing_arg = True
          current_switch = None
    else:
      if expecting_parameter:
        print 'parameter: {}'.format(arg)
        if current_switch in switches.keys():
          switches[current_switch].append(arg)
        else:
          switches[current_switch] = [arg,]
      elif preceding_args:
        print 'preceding arg: {}'.format(arg)
        pa.append(arg)
      else:
        print 'trailing arg: {}'.format(arg)
        ta.append(arg)
  return pa, switches, ta


if __name__ == '__main__':
  print parseargs(switch_dict)

# try python parseargs.py hi there i am -ag --day hi again and again -ag hi there

