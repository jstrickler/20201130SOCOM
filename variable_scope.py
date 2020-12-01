
x = "Wolverine"

#  levels of scope, checked in this order:
#  local nonlocal global builtin

def spam():
    x = 100  # LOCAL variable
    print(x)


spam()

value = 22

if value > 10:
    y = 45


print("y is", y)

def ham():
    name = "Porky"   # local to ham()  nonlocal to eggs()

    def eggs():
        print(f"My name is {name}")

    return eggs


e = ham()
e()
