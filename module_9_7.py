def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        counter = 0
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                counter += 1
            else:
                continue
        if counter == 0:
            print('Простое, ', end = '')
        else:
            print('Составное, ', end = '')
        return result
    return wrapper

@is_prime
def sum_three(x, y, z):
    return x + y + z

print(sum_three(2, 3, 7))
print(sum_three(7, 9, 1))
print(sum_three(4, 8, 2))
print(sum_three(5, 3, 7))
print(sum_three(2, 1, 2))