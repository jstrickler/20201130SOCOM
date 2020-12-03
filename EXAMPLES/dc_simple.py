#!/usr/bin/env python
from dataclasses import dataclass
from typing import List

class Dog:
    pass


@dataclass   # <1>
class Person:  # <2>
    first_name: str  # <3>
    last_name: str
    city: str
    state: str
    dog: List[Dog]

    def bark(self):
        print("Woof! Woof!")


if __name__ == '__main__':
    person = Person('Joe', 'Schmoe', 'Schenectady', 'NY', [])  # <4>
    print("using fields:", person.first_name, person.last_name)
    print("repr:", repr(person))  # <5>
    print("str:", person)
    person.last_name = 'Smith' # <6>
    print("after changing last name:", person)
    person.bark()


