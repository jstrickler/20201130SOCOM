
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


target = 'z'
for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print(f"target {target} not found")

