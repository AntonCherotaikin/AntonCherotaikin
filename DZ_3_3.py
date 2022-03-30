#    Задание 3 к уроку 3


def thesaurus(*args):
    initials = (el[0] for el in args)
    res_dict = {}
    for i in initials:
        res_dict[i] = [name for name in args if name[0] == i]
    return res_dict


a = thesaurus('Ilyas', 'Dimas', 'Mityas', 'Semen', 'Egor', 'Anton')
print(a)

a_list = list(a.keys())
a_list.sort()
for j in a_list:
    print(f'{j} -- {a[j]}')
