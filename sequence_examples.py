
stuff = ['spam', 'ham', 'eggs']

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

name = 'Chris Hemsworth'

my_data = b'stuffandnonsense'

for x in stuff, fruits, person, name, my_data:
    print(x)
    print(type(x), x[0], x[-1], len(x), x[:5])
    print()

f1 = []
for f in fruits:
    f1.append(f.upper())
print("f1:", f1)
