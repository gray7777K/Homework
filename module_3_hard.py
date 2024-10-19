def calculate_structure_sum(data_structure):
    def structure_recursion(data_structure):
        structure_list = []
        for i in range(0, len(data_structure)):
            if isinstance(data_structure[i], list) == True:
                structure_list.extend(data_structure[i])
            elif isinstance(data_structure[i], tuple) == True or isinstance(data_structure[i], set) == True:
                data_structure[i] = list(data_structure[i])
                structure_list.extend(data_structure[i])
            elif isinstance(data_structure[i], dict) == True:
                data_structure[i] = data_structure[i].items()
                for j in data_structure[i]:
                    for item in j:
                        structure_list.append(item)
            elif isinstance(data_structure[i], str) == True or isinstance(data_structure[i], int) == True or isinstance(data_structure[i], float) == True:
                structure_list.append(data_structure[i])
            else:
                continue
        structure_list_ = structure_list.copy()
        if all(isinstance(x, str) or isinstance(x, int) or isinstance(x, float) for x in structure_list) == True:
            return structure_list
        else:
            return structure_recursion(structure_list_)
    structure_sum = 0
    final_list = structure_recursion(data_structure)
    for k in range(0, len(final_list)):
        if isinstance(final_list[k], int) == True or isinstance(final_list[k], float) == True:
            structure_sum += final_list[k]
        elif isinstance(final_list[k], str) == True:
            structure_sum += len(final_list[k])
        else:
            continue
    return structure_sum

result = calculate_structure_sum([
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
])
print(result)
