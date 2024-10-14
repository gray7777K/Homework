def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    elif int(str_number[1:]) == 0:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
result = get_multiplied_digits(1350700981000)
print(result)
