from code1 import *
import sys
# sys.path.insert(0, '../')
print("-----------\n")
print(sys.path)
print("-----------\n")

def test1():
    assert(func1(5) == 6)

def test2():
    assert(func1(3) == 4)


