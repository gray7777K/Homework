def add_everything_up(a, b):
    try:
        summ = a + b
        return summ
    except TypeError:
        if isinstance(a, int) or isinstance(a, float) and isinstance(b, str):
            return str(a) + b
        if isinstance(a, str) and isinstance(b, int) or isinstance(b, float):
            return a + str(b)

print(add_everything_up('гризли', 1987))
print(add_everything_up('сорока-', 'воровка'))
print(add_everything_up(4897.3561, 'паровоз'))
print(add_everything_up(913, 44.856))
