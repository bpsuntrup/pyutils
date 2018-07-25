import itertools

def big_bite(i, n=2):
    ''' Takes iterator i and bite size (defaults to 2), and returns iterator
    returning "bite"-sized tuples of items from iterator. Iterator i can be
    infinite. Returns tuple stuffed with Nones if iterator size is not divisible
    by n.'''
    while True:
        items = []
        for _ in range(n):
            try:
                items.append(next(i))
            except StopIteration:
                if len(items) == 0:
                    raise StopIteration
                else:
                    number_of_Nones = n = len(items)
                    for _ in range( number_of_Nones ):
                        items.append(None)
                    break
        yield tuple(items)

def test_big_bite():
    i = big_bite(iter([1,2]))
    print("Does it chunk?")
    assert(next(i) == (1,2))
    throws = False
    try:
        next(i)
    except StopIteration:
        throws = True
    print("Does it throw?")
    assert(throws)

if __name__ == '__main__':
    test_big_bite()
