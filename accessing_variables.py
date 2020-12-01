
spam = 42

actor = "Chris Hemsworth"


def ham():
    pass

g = globals()

print(g, '\n')

print(g['spam'])

g['color'] = 'pink'

print(color)

g['bark'] = lambda : print("Woof! Woof!")


bark()
print()

variables = dict(g)

for name, value in variables.items():
    if name == 'g' or name.startswith('_'):
        continue
    print(name, value)

print()

globals()['bark']()
