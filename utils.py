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

