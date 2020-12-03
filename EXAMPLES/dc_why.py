#!/usr/bin/env python
from dataclasses import dataclass
from collections import namedtuple

# list
person = ['Joe', 'Schmoe', 'Schenectady', 'NY']
print("list:", person[0], person[1], "repr:", repr(person))
person[1] = 'Smith'

# tuple
person = 'Joe', 'Schmoe', 'Schenectady', 'NY'
print("tuple:", person[0], person[1], "repr:", repr(person))
# can't modify tuple

# dictionary
person = {'first_name': 'Joe', 'last_name': 'Schmoe', 'city': 'Schenectady', 'state': 'NY'}
print("dict:", person['first_name'], person['last_name'], "repr:", repr(person))
person['last_name'] = 'Smith'

# named tuple
Person = namedtuple('Person', 'first_name last_name city state')
person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')
print("named tuple:", person.first_name, person.last_name, "repr:", repr(person))
# can't modify named tuple

# class
class Person:
    def __init__(self, first_name, last_name, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state

    def __repr__(self):
        return f"Person(first_name='{self.first_name}', last_name='{self.last_name}', city='{self.city}', state='{self.state})"

person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')
print("class:", person.first_name, person.last_name, "repr:", repr(person))
person.last_name = 'Smith'

# dataclass
@dataclass
class Person:
    first_name: str
    last_name: str
    city: str
    state: str

person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')
print("dataclass:", person.first_name, person.last_name, "repr:", repr(person))
person.last_name = 'Smith'
