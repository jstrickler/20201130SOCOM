

Animal = type('Animal', (), {'move': lambda self: print("moving...")})

def bark(self):
    print("Woof! Woof!")

Dog = type('Dog', (Animal,), {'bark': bark})

d = Dog()
d.bark()
d.move()

