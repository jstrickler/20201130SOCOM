from collections import namedtuple


p = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(p[0], p[1])

pd = {
    'firstname': 'Bill',
    'lastname': 'Gates',
}

print(pd['firstname'], pd['lastname'])

Person = namedtuple('Person', 'firstname lastname product dob')

p1 = Person('Bill', 'Gates', 'Microsoft', '1955-10-24')

print(p1.firstname, p1.lastname)

print(p1)

print(p1[0], p1[1])
print(len(p1))

