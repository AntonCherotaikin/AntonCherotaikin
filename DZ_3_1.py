#    Задание 1 к уроку 3

def num_translate(num):
    """Function, that Translates numbers from 1 to 10 from English into Russian."""
    tr_dict = {'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}
    translation = tr_dict.get(num, 'there is no such a word in my dictionary.')
    print(translation)

num_translate('one') # перевод работает

num_translate('twelve') # перевод сделать невозможно