from datetime import datetime
from functools import wraps

def void(old_function):
    def _(*args, **kwargs):
        pass

    return _

def timestamp(old_function):

    @wraps(old_function)
    def _(*args, **kwargs):
        print(datetime.now().ctime())  # added code

        result = old_function(*args, **kwargs)

        return result

    return _


@timestamp
def ham():
    print("Hello from ham()")

@timestamp
def spam():
    print("Hello from spam()")

def eggs():
    print("Hello from eggs()")

eggs = timestamp(eggs)

@void
def toast():
    print("HELLO FROM TOAST!!!!")

ham()
spam()
eggs()
toast()

print(ham.__name__, spam.__name__)
