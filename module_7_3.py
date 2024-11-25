class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r+', encoding = 'utf-8') as file:
                string = file.read().lower()
                for p in punct:
                    if p in string:
                        string = string.replace(p, '')
                    else:
                        continue
                words = string.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        search_word_position = {}
        counter = 0
        for file_name, words in self.get_all_words().items():
            with (open(file_name, 'r', encoding = 'utf-8') as file):
                if word.lower() in words:
                    search_word_position[file_name] = words.index(word.lower()) +1
                    counter += 1
                else:
                    pass
        if counter > 0:
            return search_word_position
        else:
            return 'Заданное слово не найдено'

    def count(self, word):
        search_word_count = {}
        counter = 0
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                with (open(file_name, 'r', encoding = 'utf-8') as file):
                    counter1 = 0
                    for w in words:
                        if w == word.lower():
                            counter1 += 1
                        else:
                            continue
                search_word_count[file_name] = counter1
                counter += 1
            else:
                pass
        if counter > 0:
            return search_word_count
        else:
            return 'Заданное слово не найдено'

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))