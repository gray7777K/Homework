def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
        else:
            continue
    return same_words
result = single_root_words('Говор', 'отвертка', 'Договор', 'переполох', 'Вор', 'Говорильня', 'рог', 'разговор', 'Ор', 'перчатка', 'Переговоры')
print(result)

