from typing import Union, List, Iterable, Optional

def triple(x: int=2) -> float:
    return x * 3

value: float

print(triple(5))
print(triple(109320932))
print(triple(2))

print(triple('abc'))

value = 12.3

value = "abc"

print(triple.__annotations__)

class Spam:
    def doit(self, driver: 'Ham'):  # "forward ref"
        print(driver)


class Ham:
    pass

h = Ham()


s = Spam()
s.doit(h)
s.doit('barf')

Numeric = Union[int, float]

def square_root(x: Numeric) -> float:
    return x ** .5

a = square_root(2)
b = square_root(2392039230)
try:
    c = square_root('abc')
except Exception as err:
    print(err)
d = square_root(5.93)

from datetime import date

calendar: List[date] = []


calendar.append(date.today())
calendar.append(date(2014, 8, 1))
calendar.append("2001-04-19")

print(calendar)

def process_items(items: Iterable) -> float:
    pass


def do_something() -> Optional[str]:
    pass
