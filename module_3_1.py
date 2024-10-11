calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    len_ = len(string)
    string_up = string.upper()
    string_lo = string.lower()
    result = (len_, string_up, string_lo)
    count_calls()
    return result
def is_contains(string, list_to_search):
    j = 0
    k = True
    for i in range(0, len(list_to_search)):
        if list_to_search[i] == string:
            j += 1
        else:
            continue
    if j == 0:
        k = False
    else:
        k = True
    count_calls()
    return k
print(string_info('Кербланкеттиблинк'))
print(string_info('Укрощение строптивого'))
print(is_contains('киви', ['апельсин', 'яблоко', 'лимон']))
print(is_contains('семёрка', ['тройка', 'семёрка', 'туз']))
print(calls)
