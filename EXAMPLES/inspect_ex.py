#!/usr/bin/env python

import inspect


class Spam:  # <1>
    pass

def ham(p1, p2='a', *p3, p4, p5='b', **p6):  # <2>
    print(p1, p2, p3, p4, p5, p6)


for thing in (inspect, Spam, ham):
    print("{}: Module? {}. Function? {}. Class? {}".format(
        thing.__name__,
        inspect.ismodule(thing),  # <3>
        inspect.isfunction(thing),  # <4>
        inspect.isclass(thing),  # <5>
    ))

print()

print("Function spec for Ham:", inspect.getfullargspec(ham))  # <6>
print()

print("Current frame:", inspect.getframeinfo(inspect.currentframe()))  # <7>

class A:
    pass


class B(A):
    pass

class C(B):
    pass

class D(B):
    pass

d = D()

print(inspect.getclasstree([A,B,C,D]))
