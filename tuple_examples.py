
person = "Bill", "Gates", "Microsoft", "1955-10-28"

t = 5,   # tuple with single value
# t = (5)  # t is the integer 5

x = ()   # empty tuple
x = tuple()

print(person[0], len(person), person[:2], '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'NeXT', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

ipeople = iter(people)
for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = next(ipeople)
    print(first_name, last_name, product, dob)


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

colors = ['purple', 'green', 'ochre', 'mauve', 'ecru']
for i, color in enumerate(colors):
    print(i, color)


print(list(enumerate(colors)))



def spam(a, b):
    print(a, b)


spam(1, 2)
spam('hello', 'goodbye')

data = ['tot', 'waffle']
spam(*data)

def ham(**values):
    print(values)

ham(filename="wombat.txt", country="Burkina Faso")

data = {'filename': 'boomerang.txt', "country": "Australia"}

ham(**data)

args = {'end': 'WAHOO', 'sep': "ITSPAT"}

print(1, 2, 3, **args)








