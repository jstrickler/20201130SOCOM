import sys

x = 5
y = 10
m = "wombat"

print(x, y, m)

print(str(x), str(y), str(m))

print(x, y, m, sep="/")

print(x, y, m, sep=" => ")

print(x)
print(y)
print(m)
print()

print(x, end=".")
print(y, end=".")
print(m)

print(x, end=' ')
if len(m) > 10:
    print(m, end=' ')
print(y)

print("Houston, we have a problem", file=sys.stderr)

print("Hello", flush=True)

def printx(*args, file=sys.stdout, end='\n', sep=' ', flush=False):
    for i, x in enumerate(args):
        if i > len(args):
            file.write(str(x) + sep)
        else:
            file.write(str(x) + end)
    if flush:
        file.flush()

printx(x, y, m, "Uhoh", file=sys.stderr)

