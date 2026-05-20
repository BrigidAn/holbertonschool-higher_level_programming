#!/usr/bin/python3
from add_0 import add
add = __import__("add_0").add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
