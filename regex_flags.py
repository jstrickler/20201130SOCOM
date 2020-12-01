import re


rx_name = re.compile(r"foobar", re.I | re.M | re.X)

all_flags = re.I, re.M | re.X

for flag in re.I, re.M, re.X, all_flags:
    print(f"{flag:8d} {flag:08b}")
print()

print(f"{all_flags & re.I:08b}")


