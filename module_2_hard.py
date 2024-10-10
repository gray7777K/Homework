number = input("Введите число в первом поле ")
result_ = []
k = 1
for i in range(1, int(number)):
    for j in range(k, int(number)):
            if j != i and int(number) % (i + j) == 0:
                result_.append([i, j])
            else:
                continue
    k += 1
_result = []
for l in range(0, (len(result_))):
    _result.extend(result_[l])
for m in range (0, len(_result)):
    _result[m] = str(_result[m])
result = ''.join(_result)
print(result)