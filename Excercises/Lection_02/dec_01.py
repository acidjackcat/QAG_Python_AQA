def monster_decorator(func):
    def wrapper():
        return func() * 5
    return wrapper


@monster_decorator
def func1():
    return 'aaa'


@monster_decorator
def func2():
    return 'baba'

print(func1())
print(func2())