import numpy as np
import inspect

matr = np.matrix([[7, 0, 4], [8, 3, 9]])

def introspection_info(obj):
    obj_info = {}

    obj_type = type(obj)

    obj_parameters = inspect.getmembers(obj)
    obj_attributes = []
    obj_methods = []
    for i in obj_parameters:
        if 'method' in str(i[1]):
            obj_methods.append(i[0])
        else:
            obj_attributes.append(i[0])

    obj_dimensions_number = obj.ndim

    obj_sizes = list(obj.shape)

    obj_module = inspect.getmodule(obj)

    obj_info['type'] = obj_type
    obj_info['attributes'] = obj_attributes
    obj_info['methods'] = obj_methods
    obj_info['dimensions_number'] = obj_dimensions_number
    obj_info['sizes'] = obj_sizes
    obj_info['module'] = obj_module

    return obj_info

matrix_info = introspection_info(matr)
print(matrix_info)

# Доброго времени суток! В настоящей работе задача получения раздельных списков атрибутов и методов объекта решена
# нестандартным путем, без применения метода ismethod. Дело в том, что по причине, в которой я так и не смог
# разобраться, использование этого метода в моей программе даёт некорректные результаты. Ниже я привожу два
# написанных мной варианта решения, из которых оба приводят к получению некорректных результатов. Буду очень
# признателен, если Вы объясните мне, в чём заключается проблема, в чём я ошибся.

# matr_all = inspect.getmembers(matr)
# methods = [i for i in inspect.getmembers(matr, predicate = inspect.ismethod)]
# methods_0 = [i[0] for i in methods]
# all_parameters = [i[0] for i in matr_all]
# attributes_0 = [i for i in all_parameters if i not in methods_0]

# matr_all = inspect.getmembers(matr)
# methods = inspect.getmembers(matr, lambda attr: not(inspect.ismethod(attr)))
# methods_0 = [i[0] for i in methods]
# all_parameters = [i[0] for i in matr_all]
# attributes_0 = [i for i in all_parameters if i not in methods_0]
