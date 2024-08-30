def bar():
    print('x bar')

bar()

from y import *

foo()
bar()

def foo():
    print('x foo')

foo()