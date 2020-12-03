#!/usr/bin/env python

from collections import Counter

with open("../DATA/breakfast.txt") as breakfast_in:
    foods = [line.rstrip() for line in breakfast_in]  # <1>

counts = Counter(foods)  # <2>

for item, count in counts.items():  # <3>
    print(item, count)

with open("../DATA/words.txt") as words_in:
    words = [word[0] for word in words_in]

word_counts = Counter(words)

print(word_counts.most_common(5))
