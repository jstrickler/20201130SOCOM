import os

def spam(a, b):
    print(a, b)


spam(1, 2)
spam("hey", "there")

def square_root(x=1):
    return x ** .5


print(square_root(2))
print(square_root(100))

def powers(x):
    return x ** 0, x ** 1, x ** 2, x ** 3

print(powers(5))

print(square_root())

def config(**kwargs):
    print(kwargs)

config(filename="wombats.txt", city="Atlanta", animal="pine marten")

def join(*, folder, filename):
    return folder + os.path.sep + filename

print(join(folder="DATA", filename="mary.txt"))
print(join(filename="mary.txt", folder="DATA"))

#        pos        named
#        req   opt  req   opt
def wacky(a, b, *c, d, e, **f):
    print(a, b)
    print(c)
    print(d, e)
    print(f)
    print()

wacky(1, 2, 3, 4, 5, d=6, e=7, animal="wombat", country="Estonia")

wacky(1, 2, e=7, d=6)

