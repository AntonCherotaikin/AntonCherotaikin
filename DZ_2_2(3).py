#    Задание 2 и 3 в одном, так как выполнены оба условия.


# Честно говоря, подглядел в интернете, не понятно было как +- вытащить)

def get_sign(x):
    if x[0] in '+-':
        return x[0]

list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while  i < len(list):
    sign = get_sign(list[i])
    if list[i].isdigit() or (sign and list[i][1:].isdigit()):
        if sign:
            list[i] = sign + list[i][1:].zfill(2)
        else:
            list[i] = list[i].zfill(2)

        list.insert(i, '"')
        list.insert(i + 2, '"')
        i += 2

    i += 1
print(list)