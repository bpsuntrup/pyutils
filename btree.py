''' unfinished implementation of binary sorting tree '''

class Node(object):
    """private class for ContestTree"""
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.judged = False

    def judged(self):
        self.judged = True

class ContestTree(object):
    """ used for contests """

    def __init__(self):
        self.root = None
        self.next = None
        self.depth = 0
        self.inserting = True

    def find_next_node(self):
        """ sets self.next_node to next available node in tree """

    def insert(self, val):
        """ insert value into the tree """
        if not self.inserting:
            raise InsertionError('The tree has already been read, and is ' \
                + 'immutible')

        # check for first insertion
        if self.depth == 0:
            self.next = Node(val)
            self.root = self.next
        elif self.next.left is None:
            self.next.left = Node(val, parent=self.node)
        elif self.next.right is None:
            self.next.right = Node(val, parent=self.node)
        elif self.next.parent is not None:
            # check if we're at the top of the tree

    def __call__(self, lhs, rhs):
        pass
