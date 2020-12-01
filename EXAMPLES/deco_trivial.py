#!/usr/bin/env python

def void(thing_being_decorated):
    return 42  # <1>

name = "Guido"
x = void(name)

def spam():
    print("Hello from spam()")

spam = void(spam)

def wombat(f):
    print(f)
    def color():
        return "blue"

    return color


def toast():
    print("HI from toast")

toast = wombat(toast)

@wombat
def eggs():
    print("Hello from eggs()")

# eggs = wombat(eggs)

print(toast)
print(toast())

print(eggs())
