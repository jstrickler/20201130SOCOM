

value = 43.45 / 7.6

print(value)

print("{:.2f}".format(value))
# OR
print(f"{value:.2f}")

human = "man"
animal = "dog"

print("{} bites {}".format(human, animal))
print("{} bites {}".format(animal, human))

print(f"{human} bites {animal}")
print(f"{animal} bites {human}")

number = 1234
print(f"{number:d} {number:x} {number:b}")
