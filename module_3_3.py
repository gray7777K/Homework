def print_params(a = False, b = 33, c = 'крыжовник'):
    print(a, b, c)

print_params()
print_params(c = 7, b = True, a = 'деятельность')
print_params('ура', True, 10)
print_params(7, 8)
print_params([1, 2, 3])
print_params([4, 5, 6], (7, 8, 9))
print_params(15)
print_params('шишка', 'дерево', 'хвоя')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [(True, 'termin', 95), [11, 12, 13], 'оливка']
values_dict = {'a': [78, 99, False], 'b': (-2, -3, -4), 'c': 85}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['киловатт', True]
print_params(*values_list_2, (8, 7, 6))
