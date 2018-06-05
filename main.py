import chardet
from operator import itemgetter

from chardet.universaldetector import UniversalDetector

def top_words(filename):

    detector = UniversalDetector()

    with open(filename, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        code_type = detector.result['encoding']
        print('\n Файл {} выполнен в кодировке {}' .format(filename, code_type))

    with open(filename, encoding = code_type) as f:

        content_read = f.read()
        print('\n', content_read, '\n')

        words = content_read.split()
        dictionary = {}
        dict_sort = {}

        for i in words:
            dictionary[i] = dictionary.get(i, 0) + 1

        for key in dictionary:
            if len(key) >= 6:
                print(key + ': %d' % dictionary[key])
                dict_sort = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
                print(dict_sort)




filename = input('\n Введите названиен файла в формате "name.txt": ')
c = top_words(filename)
print(c)
