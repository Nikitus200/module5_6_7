class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            list_ = []
            with open(name, encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line_ = ""
                    for char in line:
                        if char not in [',', '.', '=', '!', '?', ';', ':', '-']:
                            line_ = line_ + char
                    line_ = line_.split()
                    list_ = list_ + line_
                dict_ = {name: list_}
                all_words.update(dict_)
        return all_words

    def find(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            c = 1
            for i in words:
                if i  == word:
                    dict_ = {name: c}
                    return dict_
                c += 1

    def count(self, word):
        dict_ = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if i == word:
                    count += 1
            dict_2 = {name: count}
            dict_.update(dict_2)
        return dict_

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))




