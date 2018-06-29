class Borg(object):
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

class ExampleBorg(Borg):
    def __init__(self):
        super(ExampleBorg, self).__init__()
        self.shared_property = None

'''
a = ExampleBorg()
b = ExampleBorg()
a.shared_property = 1
assert(b.shared_property == 1)
'''




