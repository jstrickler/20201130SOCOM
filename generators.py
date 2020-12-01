
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

e = enumerate(fruits)
r = reversed(fruits)

print(e)
print(r)

for i, fruit in e:
    print(i, fruit)
print('-' * 60)

for fruit in r:
    print(fruit)
print('-' * 60)

print(type(e), type(r))

fgen = (f.upper() for f in fruits)
print(fgen)

fruits.append("boysenberry")
fruits.append("durian")

for fruit in fgen:
    print(fruit)

pfruits = (f for f in fruits if f.startwith('p'))

