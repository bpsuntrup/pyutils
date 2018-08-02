class Borg(object):
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

'''
class ExampleBorg(Borg):
    def __init__(self):
        super(ExampleBorg, self).__init__()
        self.shared_property = None

a = ExampleBorg()
b = ExampleBorg()
a.shared_property = 1
assert(b.shared_property == 1)
'''

def coroutine(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return wrapper

'''
def echo(line, target):
    target.send(line)

@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)

@coroutine
def writeln()
    while True:
        line = (yield)
        print(line)

echo('coroutines rock', grep('rock', writeln))

# output:
# coroutines rock
'''

class Switch(object):
    def __init__(self):
        self.cases = {}
    def case(self, name):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            self.cases[name] = func
        return decorator
    def print_dict(self):
        print self.cases
    def __call__(self, case, *args, **kwargs):
        return self.cases[case](*args, **kwargs)

'''
switch = Switch()

@switch.case('h')
def hello():
  print 'hello there'

@switch.case('b')
def byebye():
  print 'bye, now!'

switch('h')
switch('b')
'''

def apply(f, *args):
    return f(*args)

def index(a, i):
    return a[i]

def brackets(s,state=[[0]]):
    ''' Pass in a string containing ()s {}s {}s <>s etc. Returns 
    True if string is a valid nesting, False otherwise. The idea
    behind this algorithm is that each type of bracket ( { [ < etc is
    represented as a countable ordinal, 1, omega, omega^2, omega^3, etc, for
    as many types as are needed. A stack of ordinals is kept as the program's 
    state, represented as vectors over the basis [1, omega, omega^2, ... ]. 
    When an opening bracket is encountered, if its corresponding ordinal is
    less than or equal to the lowest order ordinal in the vector on the top
    of the stack, it is added to the top of the stack. Otherwise, a new 
    ordinal is pushed on top of the stack. When a closing bracket is encountered,
    it must be equal in order to the lowest order ordinal in the vector on the
    top of the stack, otherwise false is returned. In the case that it its order
    is equal, the top ordinal is decremented. If the top ordinal is decremented to
    0, it is popped off the stack. If the entire string is consumed and the stack
    is the same as it began, the string is valid. '''
    delimiters = '()[]{}<>/\^$+-'
    print(state)
    if state == []:
        return False
    elif state[-1][0] == -1:
        return False
    elif state == [[0]] and s == '':
        return True
    else:
        if s == '':
            return False
        try:
            order = state[-1].index(next(filter(lambda x: not x == 0, state[-1])))
        except StopIteration:
            order = 0
        closing = delimiters.index(s[0]) % 2 == 1
        next_order = delimiters.index(s[0]) // 2
        if not closing: # we have a (, {, [, etc
            if order >= next_order:
                state[-1][next_order] += 1
            else:
                state.append([0 for _ in range(next_order + 1)])
                state[-1][next_order] += 1
            return brackets(s[1:], state)
        else: # We have ), ], }, etc
            if order == next_order:
                state[-1][order] -= 1
                if all(v==0 for v in state[-1]) and len(state) > 1:
                    state.pop()
                return brackets(s[1:], state)
            else:
                return False
