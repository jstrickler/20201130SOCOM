from dataclasses import dataclass

#  __init__()  __eq__() __repr__()
@dataclass()
class Point:
    x: int = 0.0  # <.>
    y: int = 0.0

    def __post_init__(self):
        print("Doing something fun!!")

p1 = Point()  # <.>
p2 = Point(3.4, 5.8)  # <.>

print(p1, p2)
