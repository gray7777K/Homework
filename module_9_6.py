def all_variants(text):
    for i in range (len(text)):
        for j in range(i + 1, len(text) + 1):
            yield text[i:j]

substrings = all_variants('гелиотроп')

for value in substrings:
    print(f'{value} ', end = '')
