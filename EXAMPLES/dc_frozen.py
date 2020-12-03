#!/usr/bin/env python
from dataclasses import dataclass, FrozenInstanceError
from datetime import date

@dataclass(frozen=True)
class President():

    first_name: str
    last_name: str
    birthdate: date


p = President(first_name='George', last_name='Washington', birthdate=date(1723, 2, 22))

print(p)

print(p.first_name)

try:
    p.first_name = 'Fred'
except FrozenInstanceError as err:
    print(err)


