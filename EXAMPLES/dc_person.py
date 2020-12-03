#!/usr/bin/env python
"""
dataclass_person
================

Module to provide Person class
"""
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Person:
    """
    Represent personal data for one person
    """
    first_name: str #: first name
    last_name: str  #: last name
    full_name: str = field(init=False)  #: full name (created from first and last names)
    dob: date = field(repr=False)  #: date of birth

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

if __name__ == '__main__':
    p = Person("John", "Smith", date(1972, 4, 22))

    print(p)
    print(p.full_name)
