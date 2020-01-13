def monster_dec_1(func):
    def wrapper(*args, **kwargs):
        return sum(args) * len(kwargs.values()) / func(*args, **kwargs)
    return wrapper


@monster_dec_1
def sum3_1(a, b, c):
    return a + b + c

print(sum3_1(1, 2, c=3))
