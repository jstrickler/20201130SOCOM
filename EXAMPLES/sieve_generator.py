#!/usr/bin/env python

def next_prime(limit):
    flags = set()  # <1>

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit + 1, i):
            flags.add(j)  # <2>
        yield i  # <3>  #  next()....


np = next_prime(200)  # <4>
for prime in np:  # <5>
    # prime = next(np)
    print(prime, end=' ')
