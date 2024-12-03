from operator import index
from os.path import split



class WordsFinder:
    file_names = []

    def __init__(self, *list_files):

        # Для имён файлов переданных в list_files
        for file_name in list_files:

            # проверяем наличие в списке WordsFinder.file_names. Если отсутствует, то добавляем в список
            if file_name not in WordsFinder.file_names:
                WordsFinder.file_names.append(file_name)

    # Функция получения всех слов.
    # get_all_words - подготовительный метод, который возвращает словарь следующего вида:
    # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    # Где:
    # 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    # ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
    def get_all_words(self):

        # Создаём пустой словарь.
        all_words = {}

        # список символов не относящихся к словам
        delete_symbol = [',', '.', '=', '!', '?', ';', ':']

        # для всех файлов из списка
        for file_name in WordsFinder.file_names:
            # открываем файл
            with open(file_name, encoding='utf-8') as file:

                # создаём пустой список слов из файла
                result_list = []

                # создаём пустую строку
                clean_string = ''

                # перебираем строки из файла
                for line in file:

                    # переводим строку в нижний регистр
                    line = line.lower()

                    # ищем дефисы в строке и заменяем их на пробелы
                    while line.find(' — ') != -1:
                        line = line.replace(' — ', " ")  # (тире обособлено пробелами, это не дефис в слове)
                        continue

                    # ищем двойные пробелы в строке и заменяем их на одинарные
                    while line.find('  ') != -1:
                        line = line.replace('  ', " ")
                        continue

                    # перебираем символы строки
                    for char in line:

                        # заносим только те, которые не относятся к знакам пунктуации
                        if char not in delete_symbol:
                            clean_string += char

                # В список заносим слова из получившейся строки
                result_list = clean_string.split()

            # В словарь заносим ключом имя файла, значениями список из слов
            all_words[file_name] = result_list

        return all_words

    # find(self, word) - метод, где word - искомое слово.
    # Возвращает словарь, где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.

    def find(self, word):

        # переводим искомое слово в нижний регистр
        word = word.lower()

        # создаём пустой результирующий словарь
        result = {}

        # получаем словарь для работы
        work_slovar = self.get_all_words()

        # для имён файлов и слов из них
        for names, words in work_slovar.items():

            # Если искомое слово обнаружено, то получаем его индекс, так как отсчёт идёт о 0, то добавляем 1
            if word in words:
                place = words.index(word) + 1

                # Заносим в словарь имя файла и позицию слова
                result[names] = place

        # Если словарь пустой, то искомого слова не найдено
        if result == {}:
            return 'Искомое слово не обнаружено ни в одном файле'

        return result

    # count(self, word) - метод, где word - искомое слово.
    # Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла.

    def count(self, word):
        # переводим искомое слово в нижний регистр
        word = word.lower()

        # создаём пустой результирующий словарь
        result = {}

        # получаем словарь для работы
        work_slovar = self.get_all_words()

        # для имён файлов и слов из них
        for names, words in work_slovar.items():

            # счётчик
            # counter = 0

            if word in words:

                counter = words.count(word)

                # Заносим в словарь имя файла и сколько раз встречается слово в этом файле
                result[names] = counter

        # Если словарь пустой, то искомого слова не найдено
        if result == {}:
            return 'Искомое слово не обнаружено ни в одном файле'

        return result


# -------------------------------------------------------------------------------
# Основное тело программы.

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))
#
# finder3 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder3.get_all_words())
# print(finder3.find('if'))
# print(finder3.count('if'))