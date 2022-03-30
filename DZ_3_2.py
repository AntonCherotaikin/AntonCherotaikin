#    Задание 2 к уроку 3

def num_translate_adv(num):
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
    if num.istitle():
        result = tr_dict.get(num.lower(), 'there is no such a word').title()
    else:
        result = tr_dict.get(num, 'there is no such a word')

    print(result)


num_translate_adv('Two') # перевод работает

num_translate_adv('Twelve') # перевод сделать невозможно