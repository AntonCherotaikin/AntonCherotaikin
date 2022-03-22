# Задание 5


price_list = [21.2, 123.3, 451.55, 4.75, 90.6, 11.9, 66.6, 26.4, 757.4, 5.2, 940.5]

prices = []
for el in price_list:
    kk = round(el % 1 * 100)
    rub = int(el)
    price = f"{rub} rub {kk:02d} kk "
    prices.append(price)

print(f"Отредактированная строка: {','.join(prices)}")

# Вывести цены, отсортированные по возрастанию, не создавая новый список.
# Доказать, что объект списка после сортировки остался тот же.

first_id = id(price_list)
print(f"Первый id: {first_id}")
price_list.sort()
second_id = id(price_list)
print(f"Отсортированный по возрастанию список: {price_list}")
print(f"Второй id (после сортировки): {second_id}")
print(first_id == second_id)

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.

reversed_price_list = sorted(price_list, reverse=True)
print(f"Отсортированный по убыванию список: {reversed_price_list}")

# Вывести цены пяти самых дорогих товаров.
print("5 самых дорогих товаров: ")
for price in reversed(reversed_price_list[:5]):
    print(price)