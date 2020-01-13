def dec_2(f_param):
    def wrapper(*args, **kwargs):
        print(f'Calling function {f_param.__name__} with possitional '
              f'parameters {args} and named parameters {kwargs}')
        return f_param(*args, **kwargs)
    return wrapper


@dec_2
def mama():
    return 'mother'


@dec_2
def papa(a, b):
    return a * b


print(mama())
print(papa(5,  '- Meladze -'))